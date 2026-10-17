import gradio as gr

from chat_page import Chat
from database import Database, Migration
from description_page import DescriptionPage
from docs_page import Docs
from embedder import Embedder

db = Database()
embedder = Embedder()

with gr.Blocks(title="Chat", analytics_enabled=False) as app:
    Chat(db, embedder).render()
with app.route("Services"):
    DescriptionPage(db).render()
with app.route("Docs"):
    Docs(db, embedder).render()

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

Migration(db).run()

app.launch(css=css)
