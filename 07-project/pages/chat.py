import json
from decimal import Decimal
from enum import Enum
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

from libs.database.connection import Database
from libs.database.repositories.conversation import Conversation
from libs.database.repositories.document import Document
from libs.database.repositories.example_question import ExampleQuestion
from libs.database.repositories.message import Message, MessageStatus
from libs.database.repositories.model import Model
from libs.database.repositories.setting import Setting
from libs.embedder import Embedder

MAX_TOKENS = 2048

SEARCH_DOCUMENTS_TOOL = ToolParam(
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


class ErrorCode(Enum):
    E1 = "Conversation input token limit reached"
    E2 = "Conversation output token limit reached"
    E3 = "Conversation cost limit reached"
    E4 = "Conversation turn limit reached"


class Chat:
    def __init__(
        self, db: Database, embedder: Embedder, setting: Setting, client: Anthropic
    ):
        self.db = db
        self.embedder = embedder
        self.setting = setting
        self.client = client

        self.conversation = Conversation(db)
        self.document = Document(db, embedder, setting)
        self.example_questions = ExampleQuestion(db)
        self.message = Message(db)
        self.model = Model(db)

    def load_conversation(self, conversation_id: str):
        history = []
        for row in self.message.get_all_by_conversation(conversation_id):
            for request_message in row["request"]:
                for content in request_message.get("content", []):
                    if content.get("type", "") == "text":
                        history.append({"role": "user", "content": content["text"]})
            if row["response"]:
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

        return conversation_id, history

    def load_raw_conversation(self, conversation_id: str):
        history = []
        for row in self.message.get_all_by_conversation(conversation_id):
            for request_message in row["request"]:
                history.append(
                    {
                        "role": request_message["role"],
                        "content": request_message.get("content", []),
                    }
                )
            if row["response"]:
                history.append(
                    {
                        "role": row["response"]["role"],
                        "content": row["response"]["content"],
                    }
                )

        return history

    def process_assistant_messages(self, content: list[dict]):
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

    def update_usage(
        self, usage: dict, model: str, input_tokens: int, output_tokens: int
    ):
        usage["input_tokens"] += input_tokens
        usage["output_tokens"] += output_tokens
        usage["cost"] += self.model.get_message_cost(model, input_tokens, output_tokens)
        usage["turns"] += 1

    def check_limits(self, usage: dict) -> str | None:
        if usage["input_tokens"] >= self.setting.get("conversation_max_input_tokens"):
            return "Chat limit reached. E1"
        if usage["output_tokens"] >= self.setting.get("conversation_max_output_tokens"):
            return "Chat limit reached. E2"
        if usage["cost"] >= Decimal(self.setting.get("conversation_max_cost")):
            return "Chat limit reached. E3"
        if usage["turns"] >= self.setting.get("conversation_max_turns"):
            return "Chat limit reached. E4"
        return None

    def tool_result(self, tool_use_id, content, is_error=False):
        return ToolResultBlockParam(
            type="tool_result",
            tool_use_id=tool_use_id,
            content=content,
            is_error=is_error,
        )

    def run_tool(self, content: list, tool_iterations: int) -> list:
        message_param_content = []

        for content_block in content:
            if content_block.type == "tool_use":
                if tool_iterations > self.setting.get(
                    "conversation_max_tool_iterations"
                ):
                    message_param_content.append(
                        self.tool_result(
                            content_block.id,
                            "Max tool iterations exceeded. Please provide an answer based on previous results.",
                            True,
                        )
                    )

                elif content_block.name == "search_documents":
                    try:
                        search_results = self.document.search(
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
                                    citations=CitationsConfigParam(enabled=True),
                                ),
                            )
                        if len(search_results) > 0:
                            message_param_content.append(
                                self.tool_result(content_block.id, search_result_blocks)
                            )
                        else:
                            message_param_content.append(
                                self.tool_result(content_block.id, "No search results")
                            )
                    except Exception as error:
                        message_param_content.append(
                            self.tool_result(
                                content_block.id,
                                f"Error while searching documents: {error}",
                                True,
                            )
                        )
                else:
                    message_param_content.append(
                        self.tool_result(
                            content_block.id,
                            f"Unknown tool name: {content_block.name}",
                            True,
                        )
                    )
        return message_param_content

    def handler(self, message: str, _, conversation_id: str, conversations):

        message_params = []
        messages = []
        conversation_usage = self.model.get_usage_by_conversation(conversation_id)
        if not conversation_id:
            raw_messages = []
            truncated_message = message if len(message) <= 50 else message[:47] + "..."
            conversation_id = self.conversation.insert(truncated_message)
            conversations = self.conversation.get_all()
        else:
            raw_messages = self.load_raw_conversation(conversation_id)

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
            check_limits_result = self.check_limits(conversation_usage)
            if check_limits_result:
                messages.append({"role": "assistant", "content": check_limits_result})
                break

            message_id = self.message.add(
                conversation_id=conversation_id,
                model=self.setting.get("default_model"),
                messages=json.dumps(message_params),
            )

            try:
                # Send request
                response = self.client.messages.create(
                    max_tokens=MAX_TOKENS,
                    messages=raw_messages + message_params,
                    thinking=ThinkingConfigAdaptiveParam(
                        type="adaptive", display="summarized"
                    ),
                    model=self.setting.get("default_model"),
                    system=self.setting.get("system_prompt"),
                    tools=[SEARCH_DOCUMENTS_TOOL],
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
                self.message.update(
                    id=message_id,
                    message=response_json,
                    status=MessageStatus.Completed.value,
                    input_tokens=response_obj["usage"]["input_tokens"],
                    output_tokens=response_obj["usage"]["output_tokens"],
                )

                # Handle tool call
                if response.stop_reason == "tool_use":
                    tool_iterations += 1

                    message_param_content = self.run_tool(response.content, tool_iterations)
                    if message_param_content:
                        message_params = [
                            MessageParam(
                                content=message_param_content,
                                role="user",
                            )
                        ]
                    else:
                        break
                else:
                    break

                self.update_usage(
                    conversation_usage,
                    response.model,
                    response.usage.input_tokens,
                    response.usage.output_tokens,
                )
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
            conversations = self.conversation.get_all()

        return messages, conversation_id, conversations

    def refresh_examples(self):
        questions = self.example_questions.get_questions()
        return gr.Chatbot(examples=[{"text": question} for question in questions])

    def render(self):
        with gr.Blocks() as app:
            conversation_id_state = gr.State(value=None)

            conversations_state = gr.State(value=self.conversation.get_all())

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
                                fn=lambda cid=detail["id"]: self.load_conversation(cid),
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
                            for question in self.example_questions.get_questions()
                        ],
                        analytics_enabled=False,
                    )

                new_chat_button.click(
                    lambda: (None, []),
                    outputs=[conversation_id_state, chat_interface.chatbot_value],
                )

            app.load(self.refresh_examples, outputs=chat_interface.chatbot)
