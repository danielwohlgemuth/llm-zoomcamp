from urllib.parse import quote

import gradio as gr

from libs.database import Database, Document, Setting
from libs.embedder import Embedder


class Docs:
    def __init__(self, db: Database, embedder: Embedder, setting: Setting):
        self.db = db
        self.embedder = embedder
        self.setting = setting

        self.document = Document(self.db, self.embedder, setting)

    def render(self):
        with gr.Blocks() as app:
            content = gr.Markdown()

            @app.load(outputs=content)
            def show(request: gr.Request):
                file_name = request.query_params.get("file_name")

                if not file_name:
                    documents = self.document.get_all()

                    title = "# Documents\n\n"
                    return title + "\n".join(
                        f"## [{document["file_name"]}](/docs?file_name={quote(document["file_name"], safe='')})"
                        for document in documents
                    )

                rows = self.document.get_by_file_name(file_name)
                if not rows:
                    return f"Document `{file_name}` not found"
                return rows[0]["content"]
