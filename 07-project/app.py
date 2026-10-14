import gradio as gr

import chat_page
import description_page
import docs_page
from database import Migration

with gr.Blocks(title="Chat", analytics_enabled=False) as app:
    chat_page.app.render()
with app.route("Services"):
    description_page.app.render()
with app.route("Docs"):
    docs_page.app.render()

css = """
.conversation {
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow: hidden;
    text-align: left;
    display: block;
    font-weight: 500;
}
"""

Migration.run()

app.launch(css=css)
