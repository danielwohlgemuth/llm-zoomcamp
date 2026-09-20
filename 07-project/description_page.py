import gradio as gr

from database import Description

css = """
.card-row {
    align-items: stretch !important;
}

.card {
    background: var(--block-background-fill);
    border: 1px solid var(--border-color-primary);
    border-radius: 12px;
    padding: 20px 24px;
    height: 100%;
    transition: border-color 0.25s ease-in-out;
}

.card h2 {
    margin: 0 0 12px 0;
    font-size: 1.5rem;
    font-weight: 600;
}

.card p {
    margin: 0;
    text-align: justify;
    hyphens: auto;
    line-height: 1.6;
    opacity: 0.85;
}

.card:hover {
    border-color: var(--color-accent);
}
"""

with gr.Blocks() as app:
    desc = Description()
    descriptions = desc.list()

    for row_index in range(0, len(descriptions), 3):
        with gr.Row(elem_classes="card-row", equal_height=True):
            for description in descriptions[row_index : row_index + 3]:
                with gr.Column():
                    gr.HTML(
                        f"""
                        <div class="card">
                            <h2>{description["name"]}</h2>
                            <p>{description["content"]}</p>
                        </div>
                        """,
                        css_template=css,
                    )
