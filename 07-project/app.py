import os

import gradio as gr
from anthropic import Anthropic

from libs.database.connection import Database
from libs.database.repositories.setting import Setting
from libs.embedder import Embedder
from pages.chat import Chat
from pages.description import Description
from pages.docs import Docs

db = Database()
embedder = Embedder()
setting = Setting(db)
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


with gr.Blocks(title="Chat", analytics_enabled=False) as app:
    Chat(db, embedder, setting, client).render()
with app.route("Services"):
    Description(db).render()
with app.route("Docs"):
    Docs(db, embedder, setting).render()

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

app.launch(css=css)
