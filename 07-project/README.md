# Project: AWS Services Search

My project idea for this course is a search service that uses the introduction information about different AWS services as the knowledge base.
Since LLMs will have been trained extensively on AWS material, they are likely to respond directly to questions about AWS instead of using the knowledge base.
To address that, the AWS names are replaced with space-themed alternatives. For example, AWS becomes OOO (Orion Outer Orbit).

In order to find and collect the introductions of AWS services, the [AWS Pricing Calculator](https://calculator.aws/#/addService) list was used as a starting point.

Systems:
- Submit: Sends new information for ingestion.
- Ingest: Indexes and embeds the information.
- Search: Agentic search using the indexes and embeddings.
- Monitor: Keeps track of the search perfomance and usage metrics.

## Dev Container Features

Features extend the base image with additional functionality.
- Main features: https://github.com/devcontainers/features/tree/main/src
- Extra features: https://github.com/devcontainers-extra/features/tree/main/src

To see how a dev container feature can be configured, inspect the devcontainer-feature.json file.

See docker-in-docker for an example: https://github.com/devcontainers/features/blob/main/src/docker-in-docker/devcontainer-feature.json

## Generate Database Password

```bash
tr -dc A-Za-z0-9 </dev/urandom | head -c 16; echo
```

## hybrid search / rrf

Initial code and query from
https://github.com/pgvector/pgvector-python/blob/master/examples/hybrid_search/rrf.py

<=> for Cosine distance, range of 0 to 2.

TODO: limit vector results to 0.7 or lower

TODO: build ingestor, consider inser duplicate insert detection

from langchain_text_splitters import MarkdownTextSplitter
splitter = MarkdownTextSplitter(
    chunk_overlap=0,
    chunk_size=512,
)
documents = splitter.split_text(readme)

