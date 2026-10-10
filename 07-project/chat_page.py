import gradio as gr
import json

from database import Conversation, Document, Message

MODEL = ""


def make_handler():
    conversation_id_state = gr.State(value=None)

    def handler(message: str, history):
        document = Document()
        search_results = document.search(message)

        if not conversation_id_state.value:
            conversation = Conversation()
            truncated_message = message if len(message) <= 50 else message[:47] + "..."
            conversation_id_state.value = conversation.insert(truncated_message)

        message_db = Message()
        message_id = message_db.add(
            conversation_id=conversation_id_state.value, model=MODEL, messages=json.dumps({"message": message})
        )

        # Send message + search_results to claude api
        llm_response = """{
            "id": "msg_01JHxbjBNcZG9hMDo4sqKHhn",
            "type": "message",
            "role": "assistant",
            "model": "claude-3-opus-20240229",
            "content": [
                {
                    "type": "text",
                    "text": "Hello! How can I assist you today?"
                }
            ],
            "stop_reason": "end_turn",
            "stop_sequence": null,
            "usage": {
                "input_tokens": 10,
                "cache_creation_input_tokens": 0,
                "cache_read_input_tokens": 0,
                "output_tokens": 12
            }
        }"""
        # store response in database

        # message_db.update(id=message_id, message=output.message, output.input_tokens, output.output_tokens)

        content = search_results[0]["content"] if search_results else ""
        return content

    def assign_conversation_id(conversation_id_state, conversation_id: str | None):
        conversation_id_state.value = conversation_id

    def new_conversation(conversation_id: str | None):
        return lambda: assign_conversation_id(conversation_id_state, conversation_id)

    handler.new_conversation = new_conversation
    handler.get_conversation_id = lambda: conversation_id_state.value
    return handler


with gr.Blocks() as app:
    handler = make_handler()

    conversation = Conversation()
    conversations = conversation.get_all()

    with gr.Row():
        with gr.Column(scale=1):
            new_chat_button = gr.Button("New Chat")
            new_chat_button.click(fn=handler.new_conversation(None))

            gr.HTML("Chats")

            for conversation_detail in conversations:
                conversation_button = gr.Button(
                    conversation_detail["description"], elem_classes="conversation"
                )
                # print("conversation_detail[id]", conversation_detail["id"])
                conversation_button.click(
                    fn=handler.new_conversation(conversation_detail["id"])
                )

        with gr.Column(scale=4):
            gr.ChatInterface(fn=handler, analytics_enabled=False)
