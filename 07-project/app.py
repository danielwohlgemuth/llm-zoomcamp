import gradio as gr

from libs.database import Database, Migration
from libs.embedder import Embedder
from pages.chat import Chat
from pages.description import Description
from pages.docs import Docs

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
