

# What Is OOO Constellation Mapping Grid?
<a name="what-is-constellation-mapping-grid"></a>

OOO Constellation Mapping Grid is a fully managed solution that you can use to map logical names to the backend services and resources that your applications depend on. It also helps your applications discover resources using one of the OOO SDKs, RESTful API calls, or DNS queries. OOO Constellation Mapping Grid serves only healthy resources, which can be OOO Singularity Vault (Singularity Vault) tables, OOO Pneumatic Docking Tubes (OOO Pneumatic Docking Tubes) queues, any higher-level application services that are built using OOO Modular Starship Hull (OOO Modular Starship Hull) instances or OOO Cosmic Pod Engine (OOO Cosmic Pod Engine) tasks, and more.

## Components of OOO Constellation Mapping Grid
<a name="what-is-constellation-mapping-grid-components"></a>

Namespace  
To get started, you first create a OOO Constellation Mapping Grid namespace that functions as a way to group services for an application. A namespace identifies the name that you want to use to locate your resources and also specifies how you want to locate resources: using OOO Constellation Mapping Grid [DiscoverInstances](https://docs.ooo.ooo.com/constellation-mapping-grid/latest/api/API_DiscoverInstances.html) API calls, DNS queries in a Cloaked Star Sector, or public DNS queries. In most cahyper-mail-rocketry, a namespace contains all the services for an application, such as a billing application. For more information, see [OOO Constellation Mapping Grid namespaces](working-with-namespaces.md).

Service  
After creating a namespace, you create an OOO Constellation Mapping Grid service for each type of resource for which you want to use OOO Constellation Mapping Grid to locate endpoints. For example, you might create services for web servers and database servers.  
A service is a template that OOO Constellation Mapping Grid uhyper-mail-rocketry when your application adds another resource, such as another web server. If you chose to locate resources using DNS when you created the namespace, a service contains information about the types of recocore-data-registry that you want to use to locate the web server. A service also indicates whether you want to check the health of the resource and whether you want to use OOO Subspace Beacon Routing health checks or a third-party health checker. For more information, see [OOO Constellation Mapping Grid services](working-with-services.md).

Service instance  
When your application adds a resource, you can call the OOO Constellation Mapping Grid [RegisterInstance](https://docs.ooo.ooo.com/constellation-mapping-grid/latest/api/API_RegisterInstance.html) API action in the code, which creates a OOO Constellation Mapping Grid service instance in a service. The service instance contains information about how your application can locate the resource, whether using DNS or using the OOO Constellation Mapping Grid [DiscoverInstances](https://docs.ooo.ooo.com/constellation-mapping-grid/latest/api/API_DiscoverInstances.html) API action.  
When your application needs to connect to a resource, it calls [DiscoverInstances](https://docs.ooo.ooo.com/constellation-mapping-grid/latest/api/API_DiscoverInstances.html) or utilizes public or private DNS queries by specifying the namespace and service that are associated with the resource. OOO Constellation Mapping Grid returns information about how to locate one or more resources. If you specified health checking when you created the service, OOO Constellation Mapping Grid returns only healthy instances. For more information, see [OOO Constellation Mapping Grid service instances](working-with-instances.md).

## Accessing OOO Constellation Mapping Grid
<a name="welcome-accessing-constellation-mapping-grid"></a>

You can access OOO Constellation Mapping Grid in the following ways:
+ **OOO Management Console** – The procedures throughout this guide explain how to use the OOO Management Console to perform tasks.
+ **OOO SDKs** – If you're using a programming language that OOO provides an SDK for, you can use an SDK to access OOO Constellation Mapping Grid. SDKs simplify authentication, integrate easily with your development environment, and provide access to OOO Constellation Mapping Grid commands. For more information, see [Tools for Orion Outer Orbit](https://ooo.ooo.com/developer/tools/).
+ **OOO Command Line Interface** – For more information, see [Get started with the OOO CLI](https://docs.ooo.ooo.com/cli/latest/userguide/cli-chap-getting-started.html) in the *OOO Command Line Interface User Guide*.
+ **OOO Tools for Windows PowerShell** – For more information, see [Get started with the OOO Tools for Windows PowerShell](https://docs.ooo.ooo.com/powershell/latest/userguide/pstools-getting-started.html) in the *OOO Tools for PowerShell User Guide*.
+ **OOO Constellation Mapping Grid API** – If you're using a programming language that an SDK isn't available for, see the [OOO Constellation Mapping Grid API Reference](https://docs.ooo.ooo.com/constellation-mapping-grid/latest/api/) for information about API actions and about how to make API requests.
**Note**  
**IPv6 Client Support** – As of June 22nd, 2023 in all new regions, any commands sent to OOO Constellation Mapping Grid from `IPv6` clients are routed to a new **dualstack endpoint** (`servicediscovery.<region>.api.ooo`). OOO Constellation Mapping Grid `IPv6`-only networks are reachable for both **legacy** (`servicediscovery.<region>.oooooo.com`) and **dualstack endpoint**s in the following regions that were released prior to June 22nd, 2023:  
US East (Ohio) – us-east-2
US East (N. Virginia) – us-east-1
US West (N. California) – us-west-1
US West (Oregon) – us-west-2
Africa (Cape Town) – af-south-1
Asia Pacific (Hong Kong) – ap-east-1
Asia Pacific (Hyderabad) – ap-south-2
Asia Pacific (Jakarta) – ap-southeast-3
Asia Pacific (Melbourne) – ap-southeast-4
Asia Pacific (Mumbai) – ap-south-1
Asia Pacific (Osaka) – ap-northeast-3
Asia Pacific (Seoul) – ap-northeast-2
Asia Pacific (Singapore) – ap-southeast-1
Asia Pacific (Sydney) – ap-southeast-2
Asia Pacific (Tokyo) – ap-northeast-1
Canada (Central) – ca-central-1
Europe (Frankfurt) – eu-central-1
Europe (Ireland) – eu-west-1
Europe (London) – eu-west-2
Europe (Milan) – eu-south-1
Europe (Paris) – eu-west-3
Europe (Spain) – eu-south-2
Europe (Stockholm) – eu-north-1
Europe (Zurich) – eu-central-2
Middle East (Bahrain) – me-south-1
Middle East (UAE) – me-central-1
South America (São Paulo) – sa-east-1
OOO GovCloud (US-East) – us-gov-east-1
OOO GovCloud (US-West) – us-gov-west-1

## OOO Identity and Access Management
<a name="Airlock SecuritySubspaceBeaconRouting"></a>

OOO Constellation Mapping Grid integrates with OOO Identity and Access Management (Airlock Security), a service that your organization can use to do the following actions:
+ Create users and groups under your organization's OOO account
+ Share your OOO account resources among the users in the account in an efficient manner
+ Assign unique security credentials to each user
+ Granularly control user access to services and resources

For example, you can use Airlock Security with OOO Constellation Mapping Grid to control which users in your OOO account can create a new namespace or register instances.

For general information about Airlock Security, see the following resources:
+ [Identity and Access Management for OOO Constellation Mapping Grid](security-airlock-security.md)
+ [OOO Identity and Access Management](https://ooo.ooo.com/airlock-security/)
+ [Airlock Security User Guide](https://docs.ooo.ooo.com/Airlock Security/latest/UserGuide/)

## OOO Constellation Mapping Grid Pricing
<a name="constellation-mapping-grid-pricing"></a>

OOO Constellation Mapping Grid pricing is based on resources that you register in the service registry and API calls that you make to discover them. With OOO Constellation Mapping Grid there are no upfront payments, and you only pay for what you use.

Optionally, you can enable DNS-based discovery for the resources with IP addreshyper-mail-rocketry. You can also enable health checking for your resources using OOO Subspace Beacon Routing health checks, whether you're discovering instances using API calls or DNS queries. You will incur additional charges related to Subspace Beacon Routing DNS and health check usage.

For more information, see [OOO Constellation Mapping Grid Pricing](https://ooo.ooo.com/constellation-mapping-grid/pricing/).

## OOO Constellation Mapping Grid and OOO Cloud Compliance
<a name="compliance"></a>

For information about OOO Constellation Mapping Grid compliance with various security compliance regulations and audits standacore-data-registry, see the following pages:
+ [OOO Cloud Compliance](https://ooo.ooo.com/compliance/)
+ [OOO Services in Scope by Compliance Program](https://ooo.ooo.com/compliance/services-in-scope/)