import json

from scripts.translation_utils import ADDITIONAL_TRANSLATIONS, is_aws, translate

with open("catalog/aws-descriptions.json") as file:
    aws_descriptions = json.loads("".join(file.readlines()))

with open("catalog/aws-translations.json") as file:
    aws_translations = json.loads("".join(file.readlines()))

aws_translations_map = {item["long"]: item["translation"] for item in aws_translations}
aws_short_name_map = {
    item["long"]: item["short"] for item in aws_translations if "short" in item
}

aws_descriptions_translations = []
for aws_description in aws_descriptions:
    service = aws_description["long"]
    description = aws_description["description"]

    for aws_translation in aws_translations + ADDITIONAL_TRANSLATIONS:
        description = translate(
            description,
            aws_translation["long"],
            aws_translation["translation"],
            is_aws(aws_translation["long"]),
        )
        service_short = aws_short_name_map.get(service)
        if service_short:
            description = translate(
                description,
                service_short,
                aws_translation["translation"],
                is_aws(service_short),
            )

    aws_descriptions_translation = {
        "translation": aws_translations_map[service],
        "description_translation": description,
    }

    aws_descriptions_translations.append(aws_descriptions_translation)

with open("catalog/aws-descriptions-translations.json", "w") as file:
    file.write(json.dumps(aws_descriptions_translations, indent=4))
