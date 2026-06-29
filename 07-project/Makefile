.PHONY: setup download_documents download_model translate, translate_description fmt black isort

setup:
	uv sync

download_documents: setup
	uv run download_documents.py

download_model: setup
	uv run download_model.py

translate: setup
	uv run translate.py

translate_description: setup
	uv run translate_description.py

fmt: black isort

black: setup
	uv run black .

isort: setup
	uv run isort .