import json

import gradio as gr
from anthropic.types import (CitationsConfigParam, DocumentBlockParam,
                             MessageParam, PlainTextSourceParam,
                             TextBlockParam)

from database import Conversation, Document, Message, MessageStatus

MODEL = "claude-haiku-5-5"
PROMPT = ""


def load_conversation(conversation_id: str):
    history = []
    message = Message()
    for row in message.get_by_conversation(conversation_id):
        for request_message in row["request"]:
            for content in request_message.get("content", []):
                if content.get("type", "") == "text":
                    history.append({"role": "user", "content": content["text"]})
        if row["response"]:
            for response_message in row["response"]["content"]:
                if response_message.get("type", "") == "text":
                    history.append(
                        {"role": "assistant", "content": response_message["text"]}
                    )

    return conversation_id, history


def handler(message: str, history, conversation_id: str, conversations):
    if not conversation_id:
        conversation = Conversation()
        truncated_message = message if len(message) <= 50 else message[:47] + "..."
        conversation_id = conversation.insert(truncated_message)
        conversations = conversation.get_all()

    document = Document()
    search_results = document.search(message)
    content = search_results[0]["content"] if search_results else ""

    message_param_content = []
    for search_result in search_results:
        message_param_content.append(
            DocumentBlockParam(
                source=PlainTextSourceParam(
                    data=search_result["content"], type="text", media_type="text/plain"
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
    message_db = Message()
    message_id = message_db.add(
        conversation_id=conversation_id,
        model=MODEL,
        messages=json.dumps(message_params),
    )

    # Send message + search_results to claude api

    response = f"""{{
        "id": "msg_01JHxbjBNcZG9hMDo4sqKHhn",
        "type": "message",
        "role": "assistant",
        "model": "claude-3-opus-20240229",
        "content": [
            {{
                "type": "text",
                "text": {json.dumps(content)}
            }}
        ],
        "stop_reason": "end_turn",
        "stop_sequence": null,
        "usage": {{
            "input_tokens": 10,
            "cache_creation_input_tokens": 0,
            "cache_read_input_tokens": 0,
            "output_tokens": 12
        }}
    }}"""
    response_obj = json.loads(response)
    message_db.update(
        id=message_id,
        message=response,
        status=MessageStatus.Completed.value,
        input_tokens=response_obj["usage"]["input_tokens"],
        output_tokens=response_obj["usage"]["output_tokens"],
    )

    if (
        len(conversations) == 0
        or len(conversations) > 0
        and conversation_id != conversations[0]["id"]
    ):
        conversation = Conversation()
        conversations = conversation.get_all()

    return content, conversation_id, conversations


with gr.Blocks() as app:
    conversation_id_state = gr.State(value=None)

    conversation = Conversation()
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
                        fn=lambda cid=detail["id"]: load_conversation(cid),
                        outputs=[conversation_id_state, chat_interface.chatbot_value],
                    )

        with gr.Column(scale=4):
            chat_interface = gr.ChatInterface(
                fn=handler,
                additional_inputs=[conversation_id_state, conversations_state],
                additional_outputs=[conversation_id_state, conversations_state],
                analytics_enabled=False,
            )

        new_chat_button.click(
            lambda: (None, []),
            outputs=[conversation_id_state, chat_interface.chatbot_value],
        )
