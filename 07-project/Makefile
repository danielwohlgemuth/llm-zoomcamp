.PHONY: download_documents translate, translate_description fmt black isort

download_documents:
	uv run download_documents.py

translate:
	uv run translate.py

translate_description:
	uv run translate_description.py

fmt: black isort

black:
	uv run black .

isort:
	uv run isort .