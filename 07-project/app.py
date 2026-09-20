import gradio as gr

import chat_page
import description_page

with gr.Blocks(title="Chat", analytics_enabled=False) as app:
    chat_page.app.render()
with app.route("Services"):
    description_page.app.render()

app.launch()
