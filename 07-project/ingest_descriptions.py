import json

from tqdm.auto import tqdm

from database import Description


def main():
    database = Description()

    with open("aws-descriptions-translations.json", "r") as file:
        aws_descriptions = json.loads(file.read())

    for item in tqdm(aws_descriptions):
        name = item["translation"]
        description = item["description_translation"]
        database.insert(name, description)


if __name__ == "__main__":
    main()
