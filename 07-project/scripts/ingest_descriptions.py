import json

from tqdm.auto import tqdm

from libs.database import Database, Description


def main():
    db = Database()
    description = Description(db)

    with open("catalog/aws-descriptions-translations.json", "r") as file:
        aws_descriptions = json.loads(file.read())

    for item in tqdm(aws_descriptions):
        name = item["translation"]
        text = item["description_translation"]
        description.insert(name, text)


if __name__ == "__main__":
    main()
