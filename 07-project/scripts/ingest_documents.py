import os
from pathlib import Path

from langchain_text_splitters import MarkdownTextSplitter
from tqdm.auto import tqdm

from libs.database import Database, Document
from libs.embedder import Embedder

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 0


def ingest_document(
    document: Document,
    text_splitter: MarkdownTextSplitter,
    services_path: Path,
    file_name: str,
) -> None:
    file_path = Path(services_path, file_name)
    with open(file_path, "r") as file:
        content = file.read()
        # document.insert(file_name, 0, 0, content)
        content_chunks = text_splitter.split_text(content)
        for index, content_chunk in enumerate(content_chunks):
            document.insert(file_name, text_splitter._chunk_size, index, content_chunk)


def main():
    db = Database()
    embedder = Embedder()
    document = Document(db, embedder)
    text_splitter = MarkdownTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )

    services_path = Path("docs/translated")

    for entry in tqdm(os.scandir(services_path)):
        if entry.is_file() and entry.name.endswith(".md"):
            ingest_document(document, text_splitter, services_path, entry.name)


if __name__ == "__main__":
    main()
