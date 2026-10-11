import json

import gradio as gr

from database import Conversation, Document, Message, MessageStatus

MODEL = "claude-3-opus-20240229"


def load_conversation(conversation_id: str):
    history = []
    message = Message()
    for row in message.get_by_conversation(conversation_id):
        for request_message in row["request"]:
            if request_message["type"] == "text":
                history.append({"role": "user", "content": request_message["text"]})
        if row["result"]:
            for result_message in row["result"]["content"]:
                if result_message["type"] == "text":
                    history.append({"role": "assistant", "content": result_message["text"]})

    return conversation_id, history


def handler(message: str, history, conversation_id: str):
    conversations = gr.skip()
    if not conversation_id:
        conversation = Conversation()
        truncated_message = message if len(message) <= 50 else message[:47] + "..."
        conversation_id = conversation.insert(truncated_message)
        conversations = conversation.get_all()

    message_db = Message()
    message_id = message_db.add(
        conversation_id=conversation_id,
        model=MODEL,
        messages=json.dumps([{"type": "text", "text": message}]),
    )

    document = Document()
    search_results = document.search(message)
    content = search_results[0]["content"] if search_results else ""

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

    return content, conversation_id, conversations



with gr.Blocks() as app:
    conversation_id_state = gr.State(value=None)
    chatbot = gr.Chatbot()

    conversation = Conversation()
    conversations_state = gr.State(value=conversation.get_all())

    with gr.Row():
        with gr.Column(scale=1):
            new_chat_button = gr.Button("New Chat")
            new_chat_button.click(
                lambda: (None, []), outputs=[conversation_id_state, chatbot]
            )

            gr.HTML("Chats")

            @gr.render(inputs=[conversations_state])
            def render_conversations(conversations):
                for detail in conversations:
                    button = gr.Button(
                        detail["description"], elem_classes="conversation"
                    )
                    button.click(
                        fn=lambda cid=detail["id"]: load_conversation(cid),
                        outputs=[conversation_id_state, chatbot],
                    )

        with gr.Column(scale=4):
            gr.ChatInterface(
                fn=handler,
                additional_inputs=[conversation_id_state],
                additional_outputs=[conversation_id_state, conversations_state],
                chatbot=chatbot,
                analytics_enabled=False,
            )
