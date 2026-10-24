import os
from pathlib import Path

from tqdm.auto import tqdm

from libs.database import Database, Document
from libs.embedder import Embedder


def ingest_document(
    document: Document,
    services_path: Path,
    file_name: str,
) -> None:
    file_path = Path(services_path, file_name)
    with open(file_path, "r") as file:
        content = file.read()
        document.insert(file_name, 0, 0, content)


def main():
    db = Database()
    embedder = Embedder()
    document = Document(db, embedder)

    services_path = Path("docs/translated")

    for entry in tqdm(os.scandir(services_path)):
        if entry.is_file() and entry.name.endswith(".md"):
            ingest_document(document, services_path, entry.name)


if __name__ == "__main__":
    main()
