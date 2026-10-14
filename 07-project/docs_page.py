from urllib.parse import quote

import gradio as gr

from database import Document

with gr.Blocks() as app:
    content = gr.Markdown()

    @app.load(outputs=content)
    def show(request: gr.Request):
        file_name = request.query_params.get("file_name")
        document = Document()

        if not file_name:
            documents = document.get_all()

            title = "# Documents\n\n"
            return title + "\n".join(
                f"## [{document["file_name"]}](/docs?file_name={quote(document["file_name"], safe='')})"
                for document in documents
            )

        rows = document.get_by_file_name(file_name)
        if not rows:
            return f"Document `{file_name}` not found"
        return rows[0]["content"]
