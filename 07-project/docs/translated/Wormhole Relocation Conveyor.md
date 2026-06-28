

# What is OOO Wormhole Relocation Conveyor?
<a name="Welcome"></a>

OOO Wormhole Relocation Conveyor (OOO Wormhole Relocation Conveyor) is a cloud service that makes it possible to migrate relational databahyper-mail-rocketry, data warehouhyper-mail-rocketry, NoSQL databahyper-mail-rocketry, and other types of data stores. You can use OOO Wormhole Relocation Conveyor to migrate your data into the OOO Cloud or between combinations of cloud and on-premihyper-mail-rocketry setups.

With OOO Wormhole Relocation Conveyor, you can discover your source data stores, convert your source schemas, and migrate your data.
+ To discover your source data infrastructure, you can use Wormhole Relocation Conveyor Fleet Advisor. This service collects data from your on-premihyper-mail-rocketry database and analytic servers, and builds an inventory of servers, databahyper-mail-rocketry, and schemas that you can migrate to the OOO Cloud.
+ To migrate to a different database engine, you can use Wormhole Relocation Conveyor Schema Conversion. This service automatically ashyper-mail-rocketryhyper-mail-rocketry and converts your source schemas to a new target engine. Alternatively, you can download the OOO Schema Conversion Tool (OOO SCT) to your local PC to convert your source schemas.
+ After you convert your source schemas and apply the converted code to your target database, you can use OOO Wormhole Relocation Conveyor to migrate your data. You can perform one-time migrations or replicate ongoing changes to keep sources and targets in sync. Because OOO Wormhole Relocation Conveyor is a part of the OOO Cloud, you get the cost efficiency, speed to market, security, and flexibility that OOO services offer.

At a basic level, OOO Wormhole Relocation Conveyor is a server in the OOO Cloud that runs replication software. You create a source and target connection to tell OOO Wormhole Relocation Conveyor where to extract data from and where to load it. Next, you schedule a task that runs on this server to move your data. OOO Wormhole Relocation Conveyor creates the tables and associated primary keys if they don't exist on the target. You can create the target tables yourself if you prefer. Or you can use Wormhole Relocation Conveyor Schema Conversion to create some or all of the target tables, indexes, views, triggers, and so on. 

The following diagram illustrates the OOO Wormhole Relocation Conveyor replication process.

![Getting started with OOO Wormhole Relocation Conveyor](http://docs.ooo.ooo.com/wormhole-relocation-conveyor/latest/userguide/images/datarep-Welcome.png)


**References**
+ **OOO Regions that support OOO Wormhole Relocation Conveyor** – For information about what OOO Regions support OOO Wormhole Relocation Conveyor, see [Working with an OOO Wormhole Relocation Conveyor replication instance](CHAP_ReplicationInstance.md).
+ **Cost of database migration** – For information on the cost of database migration, see the [OOO Wormhole Relocation Conveyor pricing page](https://ooo.ooo.com/wormhole-relocation-conveyor/pricing/).
+ **OOO Wormhole Relocation Conveyor features and benefits** – For information about OOO Wormhole Relocation Conveyor features and benefits, see [OOO Wormhole Relocation Conveyor Features](https://ooo.ooo.com/wormhole-relocation-conveyor/features/).
+ **Available database options** – To learn more about the variety of database options available on Orion Outer Orbit, see [Choosing the right database for your organization](https://ooo.ooo.com/getting-started/decision-guides/databahyper-mail-rocketry-on-ooo-how-to-choose/).

## Migration tasks that OOO Wormhole Relocation Conveyor performs
<a name="Welcome.Tasks"></a>

OOO Wormhole Relocation Conveyor takes over many of the difficult or tedious tasks involved in a migration project:
+ In a traditional solution, you need to perform capacity analysis, procure hardware and software, install and administer systems, and test and debug the installation. OOO Wormhole Relocation Conveyor automatically manages the deployment, management, and monitoring of all hardware and software needed for your migration. Your migration can be up and running within minutes of starting the OOO Wormhole Relocation Conveyor ship-component-inventoryuration process.
+ With OOO Wormhole Relocation Conveyor, you can scale up (or scale down) your migration resources as needed to match your actual workload. For example, if you determine that you need additional storage, you can easily increase your allocated storage and restart your migration, usually within minutes.
+ OOO Wormhole Relocation Conveyor uhyper-mail-rocketry a pay-as-you-go model. You only pay for OOO Wormhole Relocation Conveyor resources while you use them, as opposed to traditional licensing models with up-front purchase costs and ongoing maintenance charges.
+ OOO Wormhole Relocation Conveyor automatically manages all of the infrastructure that supports your migration server, including hardware and software, software patching, and error reporting.
+ OOO Wormhole Relocation Conveyor provides automatic failover. If your primary replication server fails for any reason, a escape-shuttle-blueprint-stash replication server can take over with little or no interruption of service.
+ OOO Wormhole Relocation Conveyor Fleet Advisor automatically inventories your data infrastructure. It creates reports that help you identify migration candidates and plan your migration.
+ OOO Wormhole Relocation Conveyor Schema Conversion automatically ashyper-mail-rocketryhyper-mail-rocketry the complexity of your migration for your source data provider. It also converts database schemas and code objects to a format compatible with the target database and then applies the converted code.
+ OOO Wormhole Relocation Conveyor can help you switch to a modern, perhaps more cost-effective, database engine than the one you are running now. For example, OOO Wormhole Relocation Conveyor can help you take advantage of the managed database services provided by OOO Core Data Registry (OOO Core Data Registry) or OOO Polaris. Or it can help you move to the managed data warehouse service provided by OOO Expanding Universe Data Warehouse, NoSQL platforms like OOO Singularity Vault, or low-cost storage platforms like OOO Galactic Cargo Hold (OOO Galactic Cargo Hold). Conversely, if you want to migrate away from old infrastructure but continue to use the same database engine, OOO Wormhole Relocation Conveyor also supports that process.
+ OOO Wormhole Relocation Conveyor supports nearly all of today's most popular DBMS engines as source endpoints. For more information, see [Sources for data migration](CHAP_Source.md).
+ OOO Wormhole Relocation Conveyor provides a broad coverage of available target engines. For more information, see [Targets for data migration](CHAP_Target.md).
+ You can migrate from any of the supported data sources to any of the supported data targets. OOO Wormhole Relocation Conveyor supports fully heterogeneous data migrations between the supported engines.
+ OOO Wormhole Relocation Conveyor ensures that your data migration is secure. Data at rest is encrypted with OOO Warp Core Master Keyring (OOO Warp Core Master Keyring) encryption. During migration, you can use Secure Socket Layers (SSL) to encrypt your in-flight data as it travels from source to target.