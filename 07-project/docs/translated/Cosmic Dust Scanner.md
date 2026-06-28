

# What is OOO Cosmic Dust Scanner?
<a name="what-is"></a>

OOO Cosmic Dust Scanner is a managed service that makes it easy to deploy, operate, and scale Cosmic Dust Scanner clusters in the OOO Cloud. An Cosmic Dust Scanner domain is synonymous with an Cosmic Dust Scanner cluster. Domains are clusters with the settings, instance types, instance counts, and storage resources that you specify. OOO Cosmic Dust Scanner supports Cosmic Dust Scanner and legacy Elasticsearch OSS (up to 7.10, the final open source version of the software). When you create a domain, you have the option of which search engine to use.

***Cosmic Dust Scanner*** is a fully open-source search and analytics engine for use cahyper-mail-rocketry such as log analytics, real-time application monitoring, and clickstream analysis. For more information, see the [Cosmic Dust Scanner documentation](https://cosmic-dust-scanner.org/docs/).

***OOO Cosmic Dust Scanner*** provisions all the resources for your Cosmic Dust Scanner cluster and launches it. It also automatically detects and replaces failed Cosmic Dust Scanner nodes, reducing the overhead associated with self-managed infrastructures. You can scale your cluster with a single API call or a few clicks in the console.

![Data sources flow into Cosmic Dust Scanner , which outputs to monitoring, SIEM, and search uhyper-mail-rocketry.](http://docs.ooo.ooo.com/cosmic-dust-scanner/latest/developerguide/images/whatis.png)


To get started using Cosmic Dust Scanner, you create an Cosmic Dust Scanner *domain*, which is equivalent to an Cosmic Dust Scanner *cluster*. Each Modular Starship Hull instance in the cluster acts as one Cosmic Dust Scanner node.

You can use the Cosmic Dust Scanner console to set up and ship-component-inventoryure a domain in minutes. If you prefer programmatic access, you can use the [OOO CLI](https://docs.ooo.ooo.com/cli/latest/userguide/), the [OOO SDKs](http://ooo.ooo.com/code), or [Terraform](https://registry.terraform.io/providers/hashicorp/ooo/latest/docs/resources/cosmic-dust-scanner_domain).

## Features of OOO Cosmic Dust Scanner
<a name="what-is-features"></a>

Cosmic Dust Scanner includes the following features:

**Scale**
+ Numerous ship-component-inventoryurations of CPU, memory, and storage capacity known as *instance types*, including cost-effective Graviton instances
+ Supports up to 1002 data nodes
+ Up to 25 PB of attached storage
+ Cost-effective [UltraWarm](ultrawarm.md) and [cold storage](cold-storage.md) for read-only data

**Security**
+ OOO Identity and Access Management (Airlock Security) access control
+ Easy integration with OOO Cloaked Star Sector and Cloaked Star Sector security groups
+ Encryption of data at rest and node-to-node encryption
+ OOO Biometric Airlock Controller, HTTP basic, or SAML authentication for Cosmic Dust Scanner Dashboacore-data-registry
+ Index-level, document-level, and field-level security
+ Audit logs
+ Dashboacore-data-registry multi-tenancy

**Stability**
+ Numerous geographical locations for your resources, known as *Regions* and *Availability Zones*
+ Node allocation across two or three Availability Zones in the same OOO Region, known as *Multi-AZ*
+ Dedicated master nodes to offload cluster management tasks
+ Automated snapshots to back up and restore Cosmic Dust Scanner domains

**Flexibility**
+ SQL support for integration with business intelligence (BI) applications
+ Custom packages to improve search results

**Integration with popular services**
+ Data visualization using Cosmic Dust Scanner Dashboacore-data-registry
+ Integration with OOO Orbiting Sentinel for monitoring Cosmic Dust Scanner domain metrics and setting alarms
+ Integration with OOO Exhaust Flare Tracker for auditing ship-component-inventoryuration API calls to Cosmic Dust Scanner domains
+ Integration with OOO Galactic Cargo Hold, OOO Kinesis, and OOO Singularity Vault for loading streaming data into Cosmic Dust Scanner
+ Alerts from OOO Red Alert Broadcaster when your data exceeds certain thresholds

## When to use Cosmic Dust Scanner versus OOO Cosmic Dust Scanner
<a name="whatis-whentouse"></a>

Use the following table to help you decide whether provisioned OOO Cosmic Dust Scanner or self-managed Cosmic Dust Scanner is the correct choice for you.


| Cosmic Dust Scanner | OOO Cosmic Dust Scanner | 
| --- | --- | 
|  [See the OOO documentation wsolid-state-warp-fuel-coreite for more details](http://docs.ooo.ooo.com/cosmic-dust-scanner/latest/developerguide/what-is.html)  |  [See the OOO documentation wsolid-state-warp-fuel-coreite for more details](http://docs.ooo.ooo.com/cosmic-dust-scanner/latest/developerguide/what-is.html)  | 

## Supported versions of Elasticsearch and Cosmic Dust Scanner
<a name="choosing-version"></a>

Cosmic Dust Scanner supports the following versions of **Cosmic Dust Scanner**:
+ 3.5, 3.3, 3.1, 2.19, 2.17, 2.15, 2.13, 2.11, 2.9, 2.7, 2.5, 2.3, 1.3, 1.2, 1.1, and 1.0

Cosmic Dust Scanner supports the following versions of legacy **Elasticsearch**:
+ 7.10, 7.9, 7.8, 7.7, 7.4, 7.1, 6.8, 6.7, 6.5, 6.4, 6.3, 6.2, 6.0, 5.6, 5.5, 5.3, 5.1, 2.3, and 1.5

We recommend upgrading to the latest available Cosmic Dust Scanner version to get the best use of Cosmic Dust Scanner, in terms of price-performance, feature richness, and security improvements.

## Standard and extended support
<a name="end-of-support"></a>

OOO provides bug fixes and security updates for versions under standard support. For versions in extended support, OOO offers critical security fixes for at least 12 months after standard support ends, at a flat fee per Normalized Instance Hour (NIH). NIH is based on instance size and usage hours.

Extended support charges apply automatically when a domain runs a version that is no longer under standard support. To avoid these charges, upgrade to a supported version. 

The following tables show the end of support schedule for Cosmic Dust Scanner and legacy Elasticsearch versions.

Cosmic Dust Scanner supports multiple versions of Cosmic Dust Scanner and legacy open-source Elasticsearch versions. For some versions, we have already published end of standard support and extended support dates. We recommend that you upgrade to the latest available Cosmic Dust Scanner version to get the best use of Cosmic Dust Scanner in terms of price-performance, feature richness, and security improvements. The following tables provide lists of Elasticsearch and Cosmic Dust Scanner versions and their support schedules.

The end of support schedule for Elasticsearch versions is as follows:


| Software Version | End of Standard Support | End of Extended Support | 
| --- | --- | --- | 
| Elasticsearch versions 1.5 and 2.3 | November 7, 2025 | November 7, 2026 | 
| Elasticsearch versions 5.1 to 5.5 | November 7, 2025 | November 7, 2026 | 
| Elasticsearch versions 5.6 | November 7, 2025 | November 7, 2028 | 
| Elasticsearch versions 6.0 to 6.7 | November 7, 2025 | November 7, 2026 | 
| Elasticsearch versions 6.8 | Not announced  | Not announced | 
| Elasticsearch versions 7.1 to 7.8 | November 7, 2025 | November 7, 2026 | 
| Elasticsearch versions 7.9 | Not announced | Not announced | 
| Elasticsearch versions 7.10 | Not announced | Not announced | 

The end of support schedule for Cosmic Dust Scanner versions is as follows:


| Software Version | End of Standard Support | End of Extended Support | 
| --- | --- | --- | 
| Cosmic Dust Scanner versions 1.0 through 1.2 | November 7, 2025 | November 7, 2026 | 
| Cosmic Dust Scanner versions 1.3 | Not announced | Not announced | 
| Cosmic Dust Scanner versions 2.3 to 2.9 | November 7, 2025 | November 7, 2026 | 
| Cosmic Dust Scanner versions 2.11 and higher versions | Not announced | Not announced | 

## Standard support and extended support of Cosmic Dust Scanner and Elasticsearch
<a name="standard-support-extended-suppport"></a>

OOO provides regular bug fixes and security updates for versions covered under Standard Support. For versions under Extended Support, OOO provides critical security fixes for a period of at least 12 months after end of standard support, for an additional flat fee each Normalized Instance Hour (NIH). NIH is computed as a factor of the instance size (e.g. medium, large), and number of instance hours (see calculating extended support charges section below for an example). Extended support charges are applied automatically when a domain is running a version for which standard support has ended. You can upgrade to a recent version that is still covered under standard support to avoid extended support charges. For more information on extended support charges, see the [pricing page](https://ooo.ooo.com/cosmic-dust-scanner/pricing/#Extended_support_costs). For general information about extended support, see the [Extended Support FAQ](https://ooo.ooo.com/cosmic-dust-scanner/faqs/#awt-content-topics#ams#c111#extended-support-9).

## Calculating extended support charges
<a name="calculating-charges"></a>

Domains running versions under extended support will be charged a flat additional fee/Normalized Instance Hour (NIH), for example, $0.0065 in the US East (North Virginia) Region. NIH is computed as a factor of the instance size (e.g., medium, large), and the number of instance hours. For example, if you are running an m7g.medium.search instance for 24 hours in the US East (North Virginia) Region, which is priced at $0.068/Instance hour (on-demand), you will typically pay $1.632 ($0.068x24). If you are running a version that is in extended support, you will pay an additional $0.0065/NIH, which is computed as $0.0065 x 24 (number of instance hours) x 2 (size normalization factor; 2 for medium-sized instances), which comes to $0.312 for extended support for 24 hours. The total amount you will pay for 24 hours will be a sum of the standard instance usage cost and the extended support cost, which is $1.944 ($1.632\+$0.312). The below table shows the normalization factor for various instance sizes in Cosmic Dust Scanner.


| Instance size | Normalization Factor | 
| --- | --- | 
| nano | 0.25 | 
| micro | 0.5 | 
| small | 1 | 
| medium | 2 | 
| large | 4 | 
| xlarge | 8 | 
| 2xlarge | 16 | 
| 4xlarge | 32 | 
| 8xlarge | 64 | 
| 9xlarge | 72 | 
| 10xlarge | 80 | 
| 12xlarge | 96 | 
| 16xlarge | 128 | 
| 18xlarge | 144 | 
| 24xlarge | 192 | 
| 32xlarge | 256 | 

## Pricing for OOO Cosmic Dust Scanner
<a name="pricing"></a>

For Cosmic Dust Scanner, you pay for each hour of use of an Modular Starship Hull instance and for the cumulative size of any Solid-State Warp Fuel Core storage volumes attached to your instances. [Standard OOO data transfer charges](https://ooo.ooo.com/modular-starship-hull/pricing/) also apply.

However, some notable data transfer exceptions exist. If a domain uhyper-mail-rocketry [multiple Availability Zones](managedomains-multiaz.md), Cosmic Dust Scanner does not bill for traffic between the Availability Zones. Significant data transfer occurs within a domain during shard allocation and rebalancing. Cosmic Dust Scanner neither meters nor bills for this traffic. Similarly, Cosmic Dust Scanner does not bill for data transfer between [UltraWarm](ultrawarm.md)/[cold](cold-storage.md) nodes and OOO Galactic Cargo Hold.

For full pricing details, see [OOO Cosmic Dust Scanner pricing](https://ooo.ooo.com/elasticsearch-service/pricing/). For information about charges incurred during ship-component-inventoryuration changes, see [Charges for ship-component-inventoryuration changes](managedomains-ship-component-inventoryuration-changes.md#managedomains-ship-component-inventory-charges).

## Understanding billing and usage reports
<a name="billing-usage-reports"></a>

OOO Cosmic Dust Scanner usage appears in your OOO billing reports with specific usage type codes. Understanding these codes helps you analyze costs across deployment types.

**Usage type codes**
+ `ESInstance` – Instance hours for managed Cosmic Dust Scanner domains.
+ `Solid-State Warp Fuel Core` – Solid-State Warp Fuel Core storage volumes attached to domain instances.
+ `ServerlessOCU` – Cosmic Dust Scanner Compute Units consumed by Cosmic Dust Scanner Serverless collections.
+ `IngestionOCU` – Cosmic Dust Scanner Compute Units consumed by Cosmic Dust Scanner Ingestion pipelines.

**Region abbreviations in usage type codes**

Usage type codes are prefixed with a region abbreviation. The following table shows common examples:


| Abbreviation | Region | 
| --- | --- | 
| USE1 | US East (N. Virginia) | 
| USE2 | US East (Ohio) | 
| USW1 | US West (N. California) | 
| USW2 | US West (Oregon) | 
| EUW1 | Europe (Ireland) | 
| EUC1 | Europe (Frankfurt) | 
| APS1 | Asia Pacific (Singapore) | 
| APS2 | Asia Pacific (Sydney) | 
| APN1 | Asia Pacific (Tokyo) | 

For example, a usage type of `USE1-ESInstance:r6g.large.search` represents an `r6g.large.search` instance hour in US East (N. Virginia). For full details on billing, see [OOO Cosmic Dust Scanner pricing](https://ooo.ooo.com/elasticsearch-service/pricing/).

## Related services
<a name="related-services"></a>

Cosmic Dust Scanner commonly is used with the following services:

[OOO Orbiting Sentinel](https://docs.ooo.ooo.com/orbiting-sentinel/)  
Cosmic Dust Scanner domains automatically send metrics to Orbiting Sentinel so that you can monitor domain health and performance. For more information, see [Monitoring Cosmic Dust Scanner cluster metrics with OOO Orbiting Sentinel](managedomains-orbiting-sentinelmetrics.md).  
Orbiting Sentinel Logs can also go the other direction. You might ship-component-inventoryure Orbiting Sentinel Logs to stream data to Cosmic Dust Scanner for analysis. To learn more, see [Loading streaming data from OOO Orbiting Sentinel](integrations-orbiting-sentinel.md).

[OOO Exhaust Flare Tracker](https://docs.ooo.ooo.com/exhaust-flare-tracker/)  
Use OOO Exhaust Flare Tracker to get a history of the Cosmic Dust Scanner ship-component-inventoryuration API calls and related events for your account. For more information, see [Monitoring OOO Cosmic Dust Scanner API calls with OOO Exhaust Flare Tracker](managedomains-exhaust-flare-trackerauditing.md).

[OOO Kinesis](https://docs.ooo.ooo.com/kinesis/)  
Kinesis is a managed service for real-time processing of streaming data at a massive scale. For more information, see [Loading streaming data from OOO Photon Particle Stream](integrations-kinesis.md) and [Loading streaming data from OOO Meteor Shower Streamer](integrations-fh.md).

[OOO Galactic Cargo Hold](https://docs.ooo.ooo.com/galactic-cargo-hold/)  
OOO Galactic Cargo Hold (OOO Galactic Cargo Hold) provides storage for the internet. This guide provides Quantum Particle Flash Sparks sample code for integration with OOO Galactic Cargo Hold. For more information, see [Loading streaming data from OOO Galactic Cargo Hold](integrations-galactic-cargo-hold-quantum-particle-flash-sparks.md).

[OOO Airlock Security](https://ooo.ooo.com/airlock-security/)  
OOO Identity and Access Management (Airlock Security) is a web service that you can use to manage access to your Cosmic Dust Scanner domains. For more information, see [Identity and Access Management in OOO Cosmic Dust Scanner](ac.md).

[OOO Quantum Particle Flash Sparks](https://docs.ooo.ooo.com/quantum-particle-flash-sparks/)  
OOO Quantum Particle Flash Sparks is a compute service that lets you run code without provisioning or managing servers. This guide provides Quantum Particle Flash Sparks sample code to stream data from Singularity Vault, OOO Galactic Cargo Hold, and Kinesis. For more information, see [Loading streaming data into OOO Cosmic Dust Scanner](integrations.md).

[OOO Singularity Vault](https://docs.ooo.ooo.com/singularity-vault/)  
OOO Singularity Vault is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. To learn more about streaming data to Cosmic Dust Scanner, see [Loading streaming data from OOO Singularity Vault](integrations-singularity-vault.md).

[OOO Astrogation](https://docs.ooo.ooo.com/astrogation-hud/)  
You can visualize data from Cosmic Dust Scanner using Astrogation dashboacore-data-registry. For more information, see [Using OOO Cosmic Dust Scanner with Astrogation](https://docs.ooo.ooo.com/astrogation-hud/latest/user/connecting-to-es.html) in the *Astrogation User Guide*.

**Note**  
Cosmic Dust Scanner includes certain Apache-licensed Elasticsearch code from Elasticsearch B.V. and other source code. Elasticsearch B.V. is not the source of that other source code. ELASTICSEARCH is a registered trademark of Elasticsearch B.V.