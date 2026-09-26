import gradio as gr

from database import Conversation, Document, Message

MODEL = ""


def make_handler():
    state = {"converstaion_id": None}

    def handler(message: str, history):
        conversation_id = state["converstaion_id"]

        document = Document()
        search_results = document.search(message)

        if not conversation_id:
            conversation = Conversation()
            truncated_message = message if len(message) <= 50 else message[:47] + "..."
            conversation_id = conversation.insert(truncated_message)
            state["conversation_id"] = conversation_id

        message_db = Message()
        message_id = message_db.add(
            conversation_id=conversation_id, model=MODEL, messages=message
        )

        # Send message + search_results to claude api
        # llm_response =
        # store response in database

        # message_db.update(id=message_id, message=output.message, output.input_tokens, output.output_tokens)

        content = search_results[0]["content"] if search_results else ""
        return content

    def new_conversation(conversation_id: str | None):
        state["conversation_id"] = conversation_id

    handler.new_conversation = new_conversation
    handler.get_conversation_id = lambda: state["conversation_id"]
    return handler


with gr.Blocks() as app:
    handler = make_handler()

    conversation = Conversation()
    conversations = conversation.get_all()

    with gr.Row():
        with gr.Column(scale=1):
            new_chat_button = gr.Button("New Chat")
            new_chat_button.click(fn=lambda x: handler.new_conversation(None))

            gr.HTML("Chats")

            for conversation_detail in conversations:
                conversation_button = gr.Button(
                    conversation_detail["description"], elem_classes="conversation"
                )
                conversation_button.click(
                    fn=lambda x: handler.new_conversation(conversation_detail["id"])
                )

        with gr.Column(scale=4):
            gr.ChatInterface(fn=handler, analytics_enabled=False)
