from enum import Enum
import json
import os
from decimal import Decimal
from urllib.parse import quote

import gradio as gr
from anthropic import Anthropic
from anthropic.types import (
    CitationsConfigParam,
    MessageParam,
    SearchResultBlockParam,
    TextBlockParam,
    ThinkingConfigAdaptiveParam,
    ToolParam,
    ToolResultBlockParam,
)

from libs.database import (
    Conversation,
    Database,
    Document,
    ExampleQuestion,
    Message,
    MessageStatus,
    Model,
    Setting,
)
from libs.embedder import Embedder

MAX_TOKENS = 2048


class ErrorCode(Enum):
    E1 = "Conversation input token limit reached"
    E2 = "Conversation output token limit reached"
    E3 = "Conversation cost limit reached"
    E4 = "Conversation turn limit reached"

class Chat:
    def __init__(self, db: Database, embedder: Embedder):
        self.db = db
        self.embedder = embedder
        self.setting = Setting(db)

    def load_conversation(self, conversation_id: str):
        history = []
        raw_history = []
        message = Message(self.db)
        for row in message.get_all_by_conversation(conversation_id):
            for request_message in row["request"]:
                raw_history.append(
                    {
                        "role": request_message["role"],
                        "content": request_message.get("content", []),
                    }
                )
                for content in request_message.get("content", []):
                    if content.get("type", "") == "text":
                        history.append({"role": "user", "content": content["text"]})
            if row["response"]:
                raw_history.append(
                    {
                        "role": row["response"]["role"],
                        "content": row["response"]["content"],
                    }
                )
                for response_message in self.process_assistant_messages(
                    row["response"]["content"]
                ):
                    if response_message.get("type", "") == "text":
                        history.append(
                            {"role": "assistant", "content": response_message["text"]}
                        )
                    if response_message.get("type", "") == "citation":
                        history.append(
                            {
                                "role": "assistant",
                                "content": response_message["content"],
                                "metadata": response_message["metadata"],
                            }
                        )

        return conversation_id, history, raw_history

    def process_assistant_messages(self, content: list[str]):
        long_message = ""
        citations = []
        messages = []

        for message in content:
            if message.get("type", "") == "text":
                long_message += message["text"]
                if "citations" in message:
                    for citation in message.get("citations") or []:
                        citations.append(
                            {
                                "text": citation["cited_text"],
                                "title": citation.get("document_title", "")
                                or citation.get("title", ""),
                            }
                        )
                        long_message += f" [{len(citations)}] "

        if long_message:
            messages.append(
                {
                    "type": "text",
                    "text": long_message,
                },
            )
        if len(citations) > 0:
            messages.append(
                {
                    "type": "citation",
                    "metadata": {"title": "Sources", "status": "done"},
                    "content": "\n\n".join(
                        [
                            f"[{index+1}] {citation["text"]}\n\n[{citation["title"]}](/docs?file_name={quote(citation["title"], safe="")})"
                            for index, citation in enumerate(citations)
                        ]
                    ),
                }
            )
        return messages

    def handler(self, message: str, history, conversation_id: str, conversations):
        conversation = Conversation(self.db)
        message_db = Message(self.db)
        model = Model(self.db)
        model_price = model.get_price(self.setting.get("default_model"))
        conversation_limit = self.setting.get("conversation_limit")

        message_params = []
        messages = []
        if not conversation_id:
            raw_messages = []
            truncated_message = message if len(message) <= 50 else message[:47] + "..."
            conversation_id = conversation.insert(truncated_message)
            conversations = conversation.get_all()
            conversation_usage = {"cost": 0, "turns": 0, "input_tokens": 0, "output_tokens": 0}
        else:
            _, _, raw_messages = self.load_conversation(conversation_id)
            conversation_usage = message_db.get_usage_by_conversation(conversation_id)

        message_param_content = []
        message_param_content.append(TextBlockParam(type="text", text=message))
        message_params.append(
            MessageParam(
                content=message_param_content,
                role="user",
            )
        )

        tool_iterations = 0

        while True:
            if conversation_usage["input_tokens"] >= conversation_limit["max_input_tokens"]:
                messages.append({"role": "assistant", "content": "Chat limit reached. E1"})
                break
            if conversation_usage["output_tokens"] >= conversation_limit["max_output_tokens"]:
                messages.append({"role": "assistant", "content": "Chat limit reached. E2"})
                break
            if conversation_usage["cost"] >= Decimal(conversation_limit["max_cost"]):
                messages.append({"role": "assistant", "content": "Chat limit reached. E3"})
                break
            if conversation_usage["turns"] >= conversation_limit["max_turns"]:
                messages.append({"role": "assistant", "content": "Chat limit reached. E4"})
                break

            message_id = message_db.add(
                conversation_id=conversation_id,
                model=self.setting.get("default_model"),
                messages=json.dumps(message_params),
            )

            try:

                # Send request
                client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
                response = client.messages.create(
                    max_tokens=MAX_TOKENS,
                    messages=raw_messages + message_params,
                    thinking=ThinkingConfigAdaptiveParam(
                        type="adaptive", display="summarized"
                    ),
                    model=self.setting.get("default_model"),
                    system=self.setting.get("system_prompt"),
                    tools=[
                        ToolParam(
                            name="search_documents",
                            description="Execute a search against the document knowledge base. Returns a list of rows as JSON objects.",
                            input_schema={
                                "type": "object",
                                "properties": {
                                    "text": {
                                        "type": "string",
                                        "description": "Search query",
                                    }
                                },
                                "required": ["text"],
                            },
                        )
                    ],
                )
                raw_messages.extend(message_params)
                raw_messages.append(
                    {"role": response.role, "content": response.content}
                )

                # Store response
                response_json = response.to_json(indent=0)
                response_obj = json.loads(response_json)
                messages.extend(
                    self.process_assistant_messages(response_obj["content"])
                )
                message_db.update(
                    id=message_id,
                    message=response_json,
                    status=MessageStatus.Completed.value,
                    input_tokens=response_obj["usage"]["input_tokens"],
                    output_tokens=response_obj["usage"]["output_tokens"],
                )

                # Handle tool call
                if response.stop_reason == "tool_use":
                    tool_iterations += 1
                    document = Document(self.db, self.embedder)

                    message_param_content = []
                    for content_block in response.content:
                        if content_block.type == "tool_use":
                            if (
                                tool_iterations
                                > conversation_limit["max_tool_iterations"]
                            ):
                                message_param_content.append(
                                    ToolResultBlockParam(
                                        tool_use_id=content_block.id,
                                        type="tool_result",
                                        is_error=True,
                                        content="Max tool iterations exceeded. Please provide an answer based on previous results.",
                                    )
                                )
                            elif content_block.name == "search_documents":
                                try:
                                    search_results = document.search(
                                        content_block.input["text"]
                                    )
                                    search_result_blocks = []
                                    for search_result in search_results:
                                        search_result_blocks.append(
                                            SearchResultBlockParam(
                                                type="search_result",
                                                title=search_result["file_name"],
                                                source=search_result["file_name"],
                                                content=[
                                                    TextBlockParam(
                                                        type="text",
                                                        text=search_result["content"],
                                                    )
                                                ],
                                                citations=CitationsConfigParam(
                                                    enabled=True
                                                ),
                                            ),
                                        )
                                    if len(search_results) > 0:
                                        message_param_content.append(
                                            ToolResultBlockParam(
                                                tool_use_id=content_block.id,
                                                type="tool_result",
                                                content=search_result_blocks,
                                            )
                                        )
                                    else:
                                        message_param_content.append(
                                            ToolResultBlockParam(
                                                tool_use_id=content_block.id,
                                                type="tool_result",
                                                content="No search results",
                                            )
                                        )
                                except Exception as error:
                                    message_param_content.append(
                                        ToolResultBlockParam(
                                            tool_use_id=content_block.id,
                                            type="tool_result",
                                            is_error=True,
                                            content=f"Error while searching documents: {error}",
                                        )
                                    )
                            else:
                                message_param_content.append(
                                    ToolResultBlockParam(
                                        tool_use_id=content_block.id,
                                        type="tool_result",
                                        is_error=True,
                                        content=f"Unknown tool name: {content_block.name}",
                                    )
                                )
                    message_params = [
                        MessageParam(
                            content=message_param_content,
                            role="user",
                        )
                    ]
                else:
                    break

                conversation_usage["input_tokens"] += response.usage.input_tokens
                conversation_usage["output_tokens"] += response.usage.output_tokens
                conversation_usage["cost"] += (
                    model_price["input_price_per_million_tokens"]
                    / 1_000_000
                    * response.usage.input_tokens
                    + model_price["output_price_per_million_tokens"]
                    / 1_000_000
                    * response.usage.output_tokens
                )
                conversation_usage["turns"] += 1
            except Exception as error:
                error_message = {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Failed to process message: {error}",
                        }
                    ],
                }
                messages.append(error_message)
                break

        if len(conversations) > 1 and conversation_id != conversations[0]["id"]:
            conversation = Conversation(self.db)
            conversations = conversation.get_all()

        return messages, conversation_id, conversations

    def refresh_examples(self):
        questions = ExampleQuestion(self.db).get_questions()
        return gr.Chatbot(examples=[{"text": question} for question in questions])

    def render(self):
        with gr.Blocks() as app:
            conversation_id_state = gr.State(value=None)

            conversation = Conversation(self.db)
            conversations_state = gr.State(value=conversation.get_all())

            with gr.Row():
                with gr.Column(scale=1):
                    new_chat_button = gr.Button("New Chat")

                    gr.HTML("Chats")

                    @gr.render(inputs=[conversations_state, conversation_id_state])
                    def render_conversations(conversations, conversation_id):
                        for detail in conversations:
                            button = gr.Button(
                                detail["description"],
                                elem_classes="conversation",
                                variant=(
                                    "primary"
                                    if detail["id"] == conversation_id
                                    else "secondary"
                                ),
                            )
                            button.click(
                                fn=lambda cid=detail["id"]: self.load_conversation(cid)[
                                    :2
                                ],
                                outputs=[
                                    conversation_id_state,
                                    chat_interface.chatbot_value,
                                ],
                            )

                with gr.Column(scale=4):
                    chat_interface = gr.ChatInterface(
                        fn=self.handler,
                        additional_inputs=[conversation_id_state, conversations_state],
                        additional_outputs=[conversation_id_state, conversations_state],
                        examples=[
                            [{"text": question}]
                            for question in ExampleQuestion(self.db).get_questions()
                        ],
                        analytics_enabled=False,
                    )

                new_chat_button.click(
                    lambda: (None, []),
                    outputs=[conversation_id_state, chat_interface.chatbot_value],
                )

            app.load(self.refresh_examples, outputs=chat_interface.chatbot)

