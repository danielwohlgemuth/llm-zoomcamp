# Project: AWS Services Search

The project for this course is a search service that uses the introduction information about different AWS services as the knowledge base.
Since LLMs will have been trained extensively on AWS material, they are likely to respond directly to questions about AWS instead of using the knowledge base.
To address that, the AWS names are replaced with space-themed alternatives. For example, AWS becomes OOO (Orion Outer Orbit).

In order to find and collect the introductions of AWS services, the [AWS Pricing Calculator](https://calculator.aws/#/addService) list was used as a starting point.

Systems:
- Submit: Sends new information for ingestion.
- Ingest: Indexes and embeds the information.
- Search: Agentic search using the indexes and embeddings.
- Monitor: Keeps track of the search perfomance and usage metrics.

## Dev Container Features

This project uses Dev Container for a more secure development experience by isolating dependencies in a container so malicious packages can do limited damage.

A base image serves as the starting point and features are used to extend the base image with additional functionality.
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

## TODO

- Limit vector results to 0.7 or lower
- Store prompt, response, and cost
- Create an evaluation dataset
- Store evaluations
- Create Graphana dashboard
- Create user interface for queries
- ~~Return file name in document search result~~


## Architectural Decisions

- AWS will be used as the documentation source as I'm more familiar with it than Google Cloud or Azure.
- Gradio will be used to build the UI.
  Compared to React, Gradio doesn't need separate JavaScript tooling to build as it's based on Python, same as the rest of the project.
  Compared to Streamlit, just from looking through the documentation of Gradio's [chat](https://gradio.app/main/docs/gradio/chatbot) component, it offers more features and configuration options than Steamlit's [chat](https://docs.streamlit.io/develop/api-reference/chat/st.chat_message) component.
- The ID column of database rows will have UUIDv4 values so that if the IDs are exposed to clients, they don't reveal details such as total rows or new rows per time frame based on the sequence.
