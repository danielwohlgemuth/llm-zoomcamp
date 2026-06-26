# Vector Search Homework

[Instructions](homework.md)

[Results](notebook.ipynb)

## Prerequisites

- [uv](https://docs.astral.sh/uv/)

## Setup

Install the dependencies.

```bash
uv sync
```

Fetch the `Xenova/all-MiniLM-L6-v2` model.

```
uv run python download.py
```

## Start

Start the Jupyter notebook.

```bash
uv run jupyter notebook
```

Find the lines that say 
>    Jupyter Server 2.19.0 is running at:
>    http://localhost:8888/tree?token=f50d59b478b6d4f4087e1089e76ca21200b5e5237c886286

Open the link to access the Jupyter server, then open the notebook file.
