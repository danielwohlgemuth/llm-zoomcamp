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
