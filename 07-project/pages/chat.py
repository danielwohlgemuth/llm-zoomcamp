import json
import os
from urllib.parse import quote

import gradio as gr
from anthropic import Anthropic
from anthropic.types import (
    CitationsConfigParam,
    DocumentBlockParam,
    MessageParam,
    PlainTextSourceParam,
    TextBlockParam,
)

from libs.database import (
    Conversation,
    Database,
    Document,
    ExampleQuestion,
    Message,
    MessageStatus,
    Setting,
)
from libs.embedder import Embedder


class Chat:
    def __init__(self, db: Database, embedder: Embedder):
        self.db = db
        self.embedder = embedder
        self.setting = Setting(db)

    def load_conversation(self, conversation_id: str):
        history = []
        message = Message(self.db)
        for row in message.get_by_conversation(conversation_id):
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

    def process_assistant_messages(self, content: list[str]):
        long_message = ""
        citations = []

        for message in content:
            if message.get("type", "") == "text":
                long_message += message["text"]
                if "citations" in message:
                    for citation in message["citations"]:
                        citations.append(
                            {
                                "text": citation["cited_text"],
                                "title": citation["document_title"],
                            }
                        )
                        long_message += f" [{len(citations)}] "

        messages = [
            {
                "type": "text",
                "text": long_message,
            },
            {
                "type": "citation",
                "metadata": {"title": "Sources", "status": "done"},
                "content": "\n\n".join(
                    [
                        f"[{index+1}] {citation["text"]}\n\n[{citation["title"]}](/docs?file_name={quote(citation["title"], safe="")})"
                        for index, citation in enumerate(citations)
                    ]
                ),
            },
        ]
        return messages

    def handler(self, message: str, history, conversation_id: str, conversations):
        if not conversation_id:
            conversation = Conversation(self.db)
            truncated_message = message if len(message) <= 50 else message[:47] + "..."
            conversation_id = conversation.insert(truncated_message)
            conversations = conversation.get_all()

        document = Document(self.db, self.embedder)
        search_results = document.search(message)

        message_param_content = []
        for search_result in search_results:
            message_param_content.append(
                DocumentBlockParam(
                    source=PlainTextSourceParam(
                        data=search_result["content"],
                        type="text",
                        media_type="text/plain",
                    ),
                    citations=CitationsConfigParam(enabled=True),
                    title=search_result["file_name"],
                    type="document",
                ),
            )
        message_param_content.append(TextBlockParam(type="text", text=message))
        message_params = [
            MessageParam(
                content=message_param_content,
                role="user",
            )
        ]
        message_db = Message(self.db)
        message_id = message_db.add(
            conversation_id=conversation_id,
            model=self.setting.get("default_model"),
            messages=json.dumps(message_params),
        )

        # Send message + search_results to claude api
        client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            max_tokens=1024,
            messages=message_params,
            model=self.setting.get("default_model"),
            system=self.setting.get("system_prompt"),
        )

        response_json = response.to_json(indent=0)
        response_obj = json.loads(response_json)
        messages = self.process_assistant_messages(response_obj["content"])
        message_db.update(
            id=message_id,
            message=response_json,
            status=MessageStatus.Completed.value,
            input_tokens=response_obj["usage"]["input_tokens"],
            output_tokens=response_obj["usage"]["output_tokens"],
        )

        if (
            len(conversations) == 0
            or len(conversations) > 0
            and conversation_id != conversations[0]["id"]
        ):
            conversation = Conversation(self.db)
            conversations = conversation.get_all()

        return messages, conversation_id, conversations

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
                            for question in ExampleQuestion(self.db).get_questions()
                        ],
                        analytics_enabled=False,
                    )

                new_chat_button.click(
                    lambda: (None, []),
                    outputs=[conversation_id_state, chat_interface.chatbot_value],
                )
