import gradio as gr

from database import Document


def process_request(message, history):
    doc = Document()
    results = doc.search(message)
    return results[0]["content"] if results else ""


with gr.Blocks() as app:
    with gr.Row():
        with gr.Column(scale=1):
            gr.Button("New Chat")
            for row in range(1):
                gr.Textbox("Hello", show_label=False)
        with gr.Column(scale=4):
            gr.ChatInterface(fn=process_request, analytics_enabled=False)
