import json
import os

from utils import ADDITIONAL_TRANSLATIONS, translate

docs_folder = "docs"
docs_original_folder = "original"
os.makedirs(os.path.join(docs_folder, docs_original_folder), exist_ok=True)

docs_translated_folder = "translated"
os.makedirs(os.path.join(docs_folder, docs_translated_folder), exist_ok=True)

with open("aws-translations.json") as file:
    aws_translations = json.loads("".join(file.readlines()))

for item in aws_translations:
    service = item["long"]
    service_outer_translation = item["translation"]

    original_content_path = os.path.join(
        docs_folder, docs_original_folder, f"{service}.md"
    )

    if not os.path.exists(original_content_path):
        continue

    with open(original_content_path, "r") as file:
        content = file.read()

    for translation in aws_translations + ADDITIONAL_TRANSLATIONS:
        service_long = translation["long"]
        service_short = translation.get("short")
        service_inner_translation = translation["translation"]

        content = translate(content, service_long, service_inner_translation)
        if service_short:
            content = translate(content, service_short, service_inner_translation)

    path = os.path.join(
        docs_folder, docs_translated_folder, f"{service_outer_translation}.md"
    )
    with open(path, "w") as file:
        file.write(content)
