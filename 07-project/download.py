import json
import os
import requests
import time

from tqdm.auto import tqdm


WAIT_SECONDS_BETWEEN_REQUESTS = 1

SERVICES_TO_SKIP = [
    "Lookout for Vision",
    "Quantum Ledger Database",
    "IoT Analytics",
    "SimSpace Weaver",
]


with open("aws-intro-urls.json") as aws_intro_urls_file:
    aws_intro_urls = json.loads("".join(aws_intro_urls_file.readlines()))

docs_folder = "docs"
docs_original_folder = "original"
os.makedirs(os.path.join(docs_folder, docs_original_folder), exist_ok=True)

for item in tqdm(aws_intro_urls):
    service = item["long"]
    intro_url = item["intro_url"]
    intro_markdown_url = intro_url.removesuffix("html") + "md"

    if service in SERVICES_TO_SKIP:
        continue

    original_content_path = os.path.join(docs_folder, docs_original_folder, f"{service}.md")
    if os.path.exists(original_content_path):
        # print(f"\n{service}.md already exists. Skipping")
        continue

    response = requests.get(intro_markdown_url, allow_redirects=True)

    if response.status_code != 200:
        print(f"\nUnexpected response status code {response.status_code} for URL {intro_markdown_url} of service {service}")
        continue

    with open(original_content_path, "wb") as file:
        file.write(response.content)

    time.sleep(WAIT_SECONDS_BETWEEN_REQUESTS)
