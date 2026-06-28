import json
import os

ADDITIONAL_TRANSLATIONS = [
    { "long": "AWS", "translation": "OOO" },
    { "long": "Amazon Web Services", "translation": "Orion Outer Orbit" },
    { "long": "Amazon", "translation": "OOO" },
    { "long": "IAM", "translation": "Airlock Security" },
    { "long": "EVS", "translation": "Alien Atmosphere Simulator" },
    { "long": "Ground Truth", "translation": "Android Training Academy" },
    { "long": "Relational Database Service", "translation": "Core Data Registry" },
    { "long": "RDS", "translation": "Core Data Registry" },
    { "long": "Quick", "translation": "Astrogation" },
    { "long": "OpenSearch", "translation": "Cosmic Dust Scanner" },
    { "long": "Db2", "translation": "Deep Space Station Registry" },
    { "long": "Elastic Container Service", "translation": "Cosmic Pod Engine" },
    { "long": "ECS", "translation": "Cosmic Pod Engine" },
    { "long": "ACM", "translation": "Encryption Key Cryptex" },
    { "long": "FSx for ONTAP", "translation": "Federation Array (Omega)" },
    { "long": "MWAA", "translation": "Flight Plan Automator" },
    { "long": "FinSpace", "translation": "Galactic Credit Ledger Tracker" },
    { "long": "XRay", "translation": "Gamma-Ray Hull Scanner" },
    { "long": "Private CA", "translation": "Imperial Seal Generator" },
    { "long": "Transform MGN", "translation": "Interstellar Relocation Engine" },
    { "long": "MGN", "translation": "Interstellar Relocation Engine" },
    { "long": "MediaLive", "translation": "Live Galactic Broadcast Core" },
    { "long": "Aurora", "translation": "Polaris" },
    { "long": "Device Defender", "translation": "Probe Firewall Sentinel" },
    { "long": "IoT", "translation": "Probes Hive Mind Hub" },
    { "long": "AVP", "translation": "Security Clearance Matrix" },
    { "long": "GameLift", "translation": "Simulation Deck Thrusters" },
    { "long": "DocumentDB", "translation": "Star-Log Archives" },
    { "long": "Route 53", "translation": "Subspace Beacon Routing" },
    { "long": "MediaTailor", "translation": "Subspace Holo-Ad Injector" },
    { "long": "KMS", "translation": "Warp Core Master Keyring" },
    { "long": "DMS", "translation": "Wormhole Relocation Conveyor" },
]


def translate(content, original: str, translation: str) -> str:
    original_no_space = original.replace(" ", "")
    original_lowercase = original_no_space.lower()
    original_with_dash = original.replace(" ", "-").lower()

    translation_no_space = translation.replace(" ", "")
    translation_lowercase = translation_no_space.lower()
    translation_with_dash = translation.replace(" ", "-").lower()

    return content \
        .replace(original, translation) \
        .replace(original_no_space, translation_no_space) \
        .replace(original_with_dash, translation_with_dash) \
        .replace(original_lowercase, translation_lowercase)


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

    original_content_path = os.path.join(docs_folder, docs_original_folder, f"{service}.md")

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

    path = os.path.join(docs_folder, docs_translated_folder, f"{service_outer_translation}.md")
    with open(path, "w") as file:
        file.write(content)
