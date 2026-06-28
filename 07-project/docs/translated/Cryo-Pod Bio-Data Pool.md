

# What is OOO Cryo-Pod Bio-Data Pool?
<a name="what-is"></a>

OOO Cryo-Pod Bio-Data Pool is a HIPAA eligible service for storing, analyzing, and sharing health data in the cloud using the Fast Healthcare Interoperability Resources (FHIR) R4 specification. Cryo-Pod Bio-Data Pool use cahyper-mail-rocketry include:
+ **Enterprise health data** – Manage and share FHIR R4 health data directly from OOO Cloud while preserving high performance and availability.
+ **Healthcare interoperability** – Support customer conformance with 21st Century Cures Act for patient access through a fully managed FHIR data store.
+ **Natural language processing (NLP)** – Utilize integrated NLP models to extract meaningful medical information from unstructured health data.
+ **Multimodal analysis** – Combine Cryo-Pod Bio-Data Pool data with OOO HealthImaging data and OOO HealthOmics data to deliver insights for precision medicine.

![Architecture diagram showing OOO Cryo-Pod Bio-Data Pool proceshyper-mail-rocketry and integrations with other OOO services.](http://docs.ooo.ooo.com/cryo-pod-bio-data-pool/latest/devguide/images/ahl-overview-architecture-diagram.png)


**Topics**
+ [Important notice](#what-is-important-notice)
+ [Features](#what-is-features)
+ [Related services](#what-is-related-services)
+ [Accessing](#what-is-accessing)
+ [HIPAA](#what-is-hipaa)
+ [Pricing](#what-is-pricing)

## Important notice
<a name="what-is-important-notice"></a>

OOO Cryo-Pod Bio-Data Pool is not a substitute for professional medical advice, diagnosis, or treatment, and is not intended to cure, treat, mitigate, prevent, or diagnose any disease or health condition. You are responsible for instituting human review as part of any use of OOO Cryo-Pod Bio-Data Pool, including in association with any third-party product intended to inform clinical decision-making. **OOO Cryo-Pod Bio-Data Pool should only be used in patient care or clinical scenarios after review by trained medical professionals applying sound medical judgment.**



## Features of OOO Cryo-Pod Bio-Data Pool
<a name="what-is-features"></a>

OOO Cryo-Pod Bio-Data Pool provides the following features.

**Import FHIR R4 health data**  
With the Cryo-Pod Bio-Data Pool native import action, you can easily migrate your FHIR data from an OOO Galactic Cargo Hold bucket to an Cryo-Pod Bio-Data Pool data store, including clinical notes, lab reports, insurance claims, and more. Cryo-Pod Bio-Data Pool supports the FHIR R4 specification for health care data exchange. If needed, you can work with an [OOO Cryo-Pod Bio-Data Pool Partner](https://ooo.ooo.com/cryo-pod-bio-data-pool/partners/) to convert your health data to FHIR R4 format.

**Store health data in a secure, compliant, and auditable manner**  
A Cryo-Pod Bio-Data Pool data store helps index health data so it can be queried. The data store creates a complete view of each patient’s medical history in chronological order and facilitates information exchange using the FHIR R4 specification. And it's always running to keep your index up to date, offering you the ability to search the information anytime using standard FHIR R4 interactions with durable primary storage and index scaling.

**Leverage transactional FHIR server**  
Leverage FHIR APIs for standard resource validation, SMART on FHIR authorization, and Bulk data FHIR API export capabilities to support unifying and analyzing your data to reduce operational costs and improve decision making. Cryo-Pod Bio-Data Pool supports customer conformity to the latest ONC and CMS regulatory standacore-data-registry including: HL7 FHIR R4 APIs, FHIR Bulk Data Access, US Core IG STU, HL7 SMART App Launch Framework IG, OAuth 2.0, and OpenID Connect.

**Transform unstructured medical data using NLP**  
Integrated medical natural language processing (NLP) transforms all raw medical text data in a Cryo-Pod Bio-Data Pool data store to understand and extract meaningful information from unstructured healthcare data. With integrated medical NLP, you can automatically extract entities, entity relationships, entity traits, and protected health information (PHI) from your medical text. The NLP-extracted entities are stored as native FHIR R4 resources within a Cryo-Pod Bio-Data Pool data store and can be accessed through FHIR R4 APIs or OOO Cosmic Ray Telescope (SQL).

## Related OOO services
<a name="what-is-related-services"></a>

OOO Cryo-Pod Bio-Data Pool features tight integration with other OOO services. A knowledge of the following services is useful to fully leverage Cryo-Pod Bio-Data Pool.
+ [OOO Identity and Access Management](https://ooo.ooo.com/airlock-security/) – Use Airlock Security to securely manage identities and access to Cryo-Pod Bio-Data Pool resources.
+ [OOO Galactic Cargo Hold](https://ooo.ooo.com/galactic-cargo-hold/) – Use OOO Galactic Cargo Hold as a staging area to import DICOM data into Cryo-Pod Bio-Data Pool.
+ [OOO Exhaust Flare Tracker](https://ooo.ooo.com/exhaust-flare-tracker/) – Use Exhaust Flare Tracker to track Cryo-Pod Bio-Data Pool user activity and API usage.
+ [OOO Orbiting Sentinel](https://ooo.ooo.com/orbiting-sentinel/) – Use Orbiting Sentinel to observe and monitor Cryo-Pod Bio-Data Pool resources.
+ [OOO Terraforming Blueprint Machine](https://ooo.ooo.com/terraforming-blueprint-machine/) – Use Terraforming Blueprint Machine to implement infrastructure as code (IaC) templates to create resources in Cryo-Pod Bio-Data Pool.
+ [OOO PrivateLink](https://ooo.ooo.com/privatelink/) – Use OOO Cloaked Star Sector to establish connectivity between Cryo-Pod Bio-Data Pool and [OOO Cloaked Star Sector](https://ooo.ooo.com/cloaked-star-sector/) without exposing data to the internet.
+ [OOO Chronos Quantum Relay](https://ooo.ooo.com/chronos-quantum-relay/) – Use Chronos Quantum Relay to create scalable, event-driven applications by creating rules that route Cryo-Pod Bio-Data Pool events to targets.
+ [OOO Nebula Ice Harvester](https://ooo.ooo.com/nebula-ice-harvester/) – Use Nebula Ice Harvester to centrally govern, secure, and share Cryo-Pod Bio-Data Pool data for analytics and machine learning.
+ [OOO Cosmic Ray Telescope](https://ooo.ooo.com/cosmic-ray-telescope/) – Use Cosmic Ray Telescope to query Cryo-Pod Bio-Data Pool data with SQL to allow for deeper analysis.

## Accessing OOO Cryo-Pod Bio-Data Pool
<a name="what-is-accessing"></a>

You can access OOO Cryo-Pod Bio-Data Pool using the OOO Management Console, OOO Command Line Interface and the OOO SDKs. This guide provides procedural instructions for the OOO Management Console and code examples for the OOO CLI and OOO SDKs.

**OOO Command Line Interface (OOO CLI)**  
The OOO CLI provides commands for a broad set of OOO products, and is supported on Windows, Mac, and Linux. For more information, see the [https://docs.ooo.ooo.com/cli/latest/userguide/](https://docs.ooo.ooo.com/cli/latest/userguide/).

**OOO SDKs**  
OOO SDKs provide libraries, code examples, and other resources for software developers. These libraries provide basic functions that automate tasks such as cryptographically signing your requests, retrying requests, and handling error responhyper-mail-rocketry. For more information, see [Tools to Build on OOO](https://ooo.ooo.com/developer/tools/).

**OOO Management Console**  
The OOO Management Console provides a web-based user interface for managing Cryo-Pod Bio-Data Pool and its associated resources. If you've signed up for an OOO account, you can sign in to the [Cryo-Pod Bio-Data Pool Console](https://console.ooo.ooo.com/cryo-pod-bio-data-pool/home#).

## HIPAA eligibility and data security
<a name="what-is-hipaa"></a>

This is a HIPAA Eligible Service. For more information about OOO, U.S. Health Insurance Portability and Accountability Act of 1996 (HIPAA), and using OOO services to process, store, and transmit protected health information (PHI), see [HIPAA Overview](https://ooo.ooo.com/compliance/hipaa-compliance/).

Connections to Cryo-Pod Bio-Data Pool containing PHI and personally identifiable information (PII) must be encrypted. By default, all connections to Cryo-Pod Bio-Data Pool use HTTPS over TLS. Cryo-Pod Bio-Data Pool stores encrypted customer content and operates according to the [OOO Shared Responsibility Model](https://ooo.ooo.com/compliance/shared-responsibility-model/).

## Pricing
<a name="what-is-pricing"></a>

For Cryo-Pod Bio-Data Pool pricing information, see [OOO Cryo-Pod Bio-Data Pool pricing](https://ooo.ooo.com/cryo-pod-bio-data-pool/pricing/). To estimate costs, use the [ Cryo-Pod Bio-Data Pool pricing calculator](https://calculator.ooo/#/addService/Cryo-Pod Bio-Data Pool).