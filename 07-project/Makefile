.PHONY: setup download_documents download_model translate_documents translate_descriptions fmt black isort notebook ingest_documents ingest_descriptions start_docker

setup:
	uv sync

download_documents: setup
	uv run download_documents.py

download_model: setup
	uv run download_model.py

translate_documents: setup
	uv run translate_documents.py

translate_descriptions: setup
	uv run translate_descriptions.py

fmt: black isort

black: setup
	uv run black .

isort: setup
	uv run isort .

notebook:
	uv run jupyter notebook

ingest_documents:
	uv run ingest_documents.py

ingest_descriptions:
	uv run ingest_descriptions.py

start_docker:
	docker compose up -d