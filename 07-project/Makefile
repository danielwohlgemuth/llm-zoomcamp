.PHONY: download_documents download_model translate, translate_description fmt black isort

download_documents:
	uv run download_documents.py

download_model:
	uv run download_model.py

translate:
	uv run translate.py

translate_description:
	uv run translate_description.py

fmt: black isort

black:
	uv run black .

isort:
	uv run isort .