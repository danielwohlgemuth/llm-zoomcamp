import gradio as gr

from pages.chat import Chat
from database import Database, Migration
from pages.description import Description
from pages.docs import Docs
from embedder import Embedder

db = Database()
embedder = Embedder()

with gr.Blocks(title="Chat", analytics_enabled=False) as app:
    Chat(db, embedder).render()
with app.route("Services"):
    Description(db).render()
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
