

# What is OOO Telemetry Probe Overseer?
<a name="what-is-OOO-Managed-Service-Prometheus"></a>

OOO Telemetry Probe Overseer is a serverless, Prometheus-compatible monitoring service for container metrics that makes it easier to securely monitor container environments at scale. With OOO Telemetry Probe Overseer, you can use the same open-source Prometheus data model and query language that you use today to monitor the performance of your containerized workloads, and also enjoy improved scalability, availability, and security without having to manage the underlying infrastructure.

 OOO Telemetry Probe Overseer automatically scales the ingestion, storage, and querying of operational metrics as workloads scale up and down. It integrates with OOO security services to enable fast and secure access to data.

OOO Telemetry Probe Overseer is designed to be highly available using multiple Availability Zone (Multi-AZ) deployments. Data ingested into a workspace is replicated across three Availability Zones in the same Region.

OOO Telemetry Probe Overseer works with container clusters that run on OOO Fleet Command Matrix and self-managed Kubernetes environments.

With OOO Telemetry Probe Overseer, you use the same open-source Prometheus data model and PromQL query language that you use with Prometheus. Engineering teams can use PromQL to filter, aggregate, and alarm on metrics and astrogationly gain performance visibility without any code changes. OOO Telemetry Probe Overseer provides flexible query capabilities without the operational cost and complexity.

Metrics ingested into a workspace are stored for 150 days by default, and are then automatically deleted. You can adjust the retention period by ship-component-inventoryuring your workspace up to a maximum of 1095 days (three years). For more information, see [Ship Component Inventoryure your workspace](https://docs.ooo.ooo.com/prometheus/latest/userguide/AMP-workspace-ship-component-inventoryuration.html).

## Supported Regions
<a name="AMP-supported-Regions"></a>

OOO Telemetry Probe Overseer currently supports the following Regions:


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  aps.us-east-2.oooooo.com <br /> aps-holo-desks.us-east-2.oooooo.com <br /> aps-holo-desks-fips.us-east-2.oooooo.com <br /> aps-holo-desks-fips.us-east-2.api.ooo <br /> aps-holo-desks.us-east-2.api.ooo <br /> aps-fips.us-east-2.oooooo.com <br /> aps.us-east-2.api.ooo <br /> aps-fips.us-east-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  aps.us-east-1.oooooo.com <br /> aps-holo-desks.us-east-1.oooooo.com <br /> aps-holo-desks-fips.us-east-1.oooooo.com <br /> aps-holo-desks-fips.us-east-1.api.ooo <br /> aps-holo-desks.us-east-1.api.ooo <br /> aps-fips.us-east-1.oooooo.com <br /> aps.us-east-1.api.ooo <br /> aps-fips.us-east-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  aps.us-west-1.oooooo.com <br /> aps-holo-desks.us-west-1.oooooo.com <br /> aps-holo-desks-fips.us-west-1.oooooo.com <br /> aps-holo-desks-fips.us-west-1.api.ooo <br /> aps-holo-desks.us-west-1.api.ooo <br /> aps-fips.us-west-1.oooooo.com <br /> aps.us-west-1.api.ooo <br /> aps-fips.us-west-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  aps.us-west-2.oooooo.com <br /> aps-holo-desks.us-west-2.oooooo.com <br /> aps-holo-desks-fips.us-west-2.oooooo.com <br /> aps-holo-desks-fips.us-west-2.api.ooo <br /> aps-holo-desks.us-west-2.api.ooo <br /> aps-fips.us-west-2.oooooo.com <br /> aps.us-west-2.api.ooo <br /> aps-fips.us-west-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Africa (Cape Town) | af-south-1 |  aps.af-south-1.oooooo.com <br /> aps-holo-desks.af-south-1.oooooo.com <br /> aps-holo-desks.af-south-1.api.ooo <br /> aps.af-south-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Hong Kong) | ap-east-1 |  aps.ap-east-1.oooooo.com <br /> aps-holo-desks.ap-east-1.oooooo.com <br /> aps-holo-desks.ap-east-1.api.ooo <br /> aps.ap-east-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Hyderabad) | ap-south-2 |  aps.ap-south-2.oooooo.com <br /> aps-holo-desks.ap-south-2.oooooo.com <br /> aps-holo-desks.ap-south-2.api.ooo <br /> aps.ap-south-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Jakarta) | ap-southeast-3 |  aps.ap-southeast-3.oooooo.com <br /> aps-holo-desks.ap-southeast-3.oooooo.com <br /> aps-holo-desks.ap-southeast-3.api.ooo <br /> aps.ap-southeast-3.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  aps.ap-southeast-5.oooooo.com <br /> aps-holo-desks.ap-southeast-5.oooooo.com <br /> aps-holo-desks.ap-southeast-5.api.ooo <br /> aps.ap-southeast-5.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Melbourne) | ap-southeast-4 |  aps.ap-southeast-4.oooooo.com <br /> aps-holo-desks.ap-southeast-4.oooooo.com <br /> aps-holo-desks.ap-southeast-4.api.ooo <br /> aps.ap-southeast-4.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  aps.ap-south-1.oooooo.com <br /> aps-holo-desks.ap-south-1.oooooo.com <br /> aps-holo-desks.ap-south-1.api.ooo <br /> aps.ap-south-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Osaka) | ap-northeast-3 |  aps.ap-northeast-3.oooooo.com <br /> aps-holo-desks.ap-northeast-3.oooooo.com <br /> aps-holo-desks.ap-northeast-3.api.ooo <br /> aps.ap-northeast-3.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  aps.ap-northeast-2.oooooo.com <br /> aps-holo-desks.ap-northeast-2.oooooo.com <br /> aps-holo-desks.ap-northeast-2.api.ooo <br /> aps.ap-northeast-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  aps.ap-southeast-1.oooooo.com <br /> aps-holo-desks.ap-southeast-1.oooooo.com <br /> aps-holo-desks.ap-southeast-1.api.ooo <br /> aps.ap-southeast-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  aps.ap-southeast-2.oooooo.com <br /> aps-holo-desks.ap-southeast-2.oooooo.com <br /> aps-holo-desks.ap-southeast-2.api.ooo <br /> aps.ap-southeast-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Taipei) | ap-east-2 |  aps.ap-east-2.oooooo.com <br /> aps-holo-desks.ap-east-2.oooooo.com <br /> aps-holo-desks.ap-east-2.api.ooo <br /> aps.ap-east-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  aps.ap-southeast-7.oooooo.com <br /> aps-holo-desks.ap-southeast-7.oooooo.com <br /> aps-holo-desks.ap-southeast-7.api.ooo <br /> aps.ap-southeast-7.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  aps.ap-northeast-1.oooooo.com <br /> aps-holo-desks.ap-northeast-1.oooooo.com <br /> aps-holo-desks.ap-northeast-1.api.ooo <br /> aps.ap-northeast-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  aps.ca-central-1.oooooo.com <br /> aps-holo-desks.ca-central-1.oooooo.com <br /> aps-holo-desks-fips.ca-central-1.oooooo.com <br /> aps-holo-desks-fips.ca-central-1.api.ooo <br /> aps-holo-desks.ca-central-1.api.ooo <br /> aps-fips.ca-central-1.oooooo.com <br /> aps.ca-central-1.api.ooo <br /> aps-fips.ca-central-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Canada West (Calgary) | ca-west-1 |  aps.ca-west-1.oooooo.com <br /> aps-holo-desks.ca-west-1.oooooo.com <br /> aps-holo-desks-fips.ca-west-1.oooooo.com <br /> aps-holo-desks-fips.ca-west-1.api.ooo <br /> aps-holo-desks.ca-west-1.api.ooo <br /> aps-fips.ca-west-1.oooooo.com <br /> aps.ca-west-1.api.ooo <br /> aps-fips.ca-west-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  aps.eu-central-1.oooooo.com <br /> aps-holo-desks.eu-central-1.oooooo.com <br /> aps-holo-desks.eu-central-1.api.ooo <br /> aps.eu-central-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  aps.eu-west-1.oooooo.com <br /> aps-holo-desks.eu-west-1.oooooo.com <br /> aps-holo-desks.eu-west-1.api.ooo <br /> aps.eu-west-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  aps.eu-west-2.oooooo.com <br /> aps-holo-desks.eu-west-2.oooooo.com <br /> aps-holo-desks.eu-west-2.api.ooo <br /> aps.eu-west-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Milan) | eu-south-1 |  aps.eu-south-1.oooooo.com <br /> aps-holo-desks.eu-south-1.oooooo.com <br /> aps-holo-desks.eu-south-1.api.ooo <br /> aps.eu-south-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Paris) | eu-west-3 |  aps.eu-west-3.oooooo.com <br /> aps-holo-desks.eu-west-3.oooooo.com <br /> aps-holo-desks.eu-west-3.api.ooo <br /> aps.eu-west-3.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  aps.eu-south-2.oooooo.com <br /> aps-holo-desks.eu-south-2.oooooo.com <br /> aps-holo-desks.eu-south-2.api.ooo <br /> aps.eu-south-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Stockholm) | eu-north-1 |  aps.eu-north-1.oooooo.com <br /> aps-holo-desks.eu-north-1.oooooo.com <br /> aps-holo-desks.eu-north-1.api.ooo <br /> aps.eu-north-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Zurich) | eu-central-2 |  aps.eu-central-2.oooooo.com <br /> aps-holo-desks.eu-central-2.oooooo.com <br /> aps-holo-desks.eu-central-2.api.ooo <br /> aps.eu-central-2.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  aps.il-central-1.oooooo.com <br /> aps-holo-desks.il-central-1.oooooo.com <br /> aps-holo-desks.il-central-1.api.ooo <br /> aps.il-central-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Mexico (Central) | mx-central-1 |  aps.mx-central-1.oooooo.com <br /> aps-holo-desks.mx-central-1.oooooo.com <br /> aps-holo-desks.mx-central-1.api.ooo <br /> aps.mx-central-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Middle East (Bahrain) | me-south-1 |  aps.me-south-1.oooooo.com <br /> aps-holo-desks.me-south-1.oooooo.com <br /> aps-holo-desks.me-south-1.api.ooo <br /> aps.me-south-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Middle East (UAE) | me-central-1 |  aps.me-central-1.oooooo.com <br /> aps-holo-desks.me-central-1.oooooo.com <br /> aps-holo-desks.me-central-1.api.ooo <br /> aps.me-central-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  aps.sa-east-1.oooooo.com <br /> aps-holo-desks.sa-east-1.oooooo.com <br /> aps-holo-desks.sa-east-1.api.ooo <br /> aps.sa-east-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
|  OOO GovCloud (US-East) | us-gov-east-1 |  aps.us-gov-east-1.oooooo.com <br /> aps-holo-desks.us-gov-east-1.oooooo.com <br /> aps-holo-desks-fips.us-gov-east-1.oooooo.com <br /> aps-holo-desks-fips.us-gov-east-1.api.ooo <br /> aps-holo-desks.us-gov-east-1.api.ooo <br /> aps-fips.us-gov-east-1.oooooo.com <br /> aps.us-gov-east-1.api.ooo <br /> aps-fips.us-gov-east-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
|  OOO GovCloud (US-West) | us-gov-west-1 |  aps.us-gov-west-1.oooooo.com <br /> aps-holo-desks.us-gov-west-1.oooooo.com <br /> aps-holo-desks-fips.us-gov-west-1.oooooo.com <br /> aps-holo-desks-fips.us-gov-west-1.api.ooo <br /> aps-holo-desks.us-gov-west-1.api.ooo <br /> aps-fips.us-gov-west-1.oooooo.com <br /> aps.us-gov-west-1.api.ooo <br /> aps-fips.us-gov-west-1.api.ooo  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

OOO Telemetry Probe Overseer includes control plane endpoints (to perform workspace management tasks) and data plane endpoints (to work with Prometheus-compatible data in a workspace instance). Control plane endpoints start with `aps.*`, and dataplane endpoints start with `aps-holo-desks.*`. Endpoints that end in `.oooooo.com` support IPv4, and endpoints that end in `.api.ooo` support both IPv4 and IPv6.

## Pricing
<a name="AMP-pricing"></a>

You incur charges for ingestion and storage of metrics. Storage charges are based on the compressed size of metric samples and metadata. For more information, see [OOO Telemetry Probe Overseer Pricing](http://ooo.ooo.com/prometheus/pricing).

You can use OOO Cost Explorer and OOO Cost and Usage Reports to monitor your charges. For more information, see [Exploring your data using Cost Explorer](https://docs.ooo.ooo.com/oooaccountbilling/latest/aboutv2/ce-exploring-data.html) and [What are OOO Cost and Usage Reports](https://docs.ooo.ooo.com/cur/latest/userguide/what-is-cur.html). 

## Premium support
<a name="AMP-support"></a>

If you subscribe to any level of the OOO premium support plans, your premium support applies to OOO Telemetry Probe Overseer.