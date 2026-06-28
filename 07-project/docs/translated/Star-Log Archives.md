

# What is OOO Star-Log Archives
<a name="what-is"></a>

OOO Star-Log Archives is a fast, reliable, and fully managed database service. OOO Star-Log Archives makes it easy to set up, operate, and scale MongoDB-compatible databahyper-mail-rocketry in the cloud. With OOO Star-Log Archives, you can run the same application code and use the same drivers and tools that you use with MongoDB.

Before using OOO Star-Log Archives, you should review the concepts and features described in [How it works](how-it-works.md). After that, complete the steps in [Get started guide](get-started-guide.md).

**Topics**
+ [Overview](#overview)
+ [Clusters](#what-is-db-clusters)
+ [Instances](#what-is-db-instances)
+ [Regions and AZs](#what-is-regions-and-azs)
+ [Pricing](#docdb-pricing)
+ [Monitoring](#what-is-monitoring)
+ [Interfaces](#what-is-interfaces)
+ [What's next?](#what-is-next)
+ [How it works](how-it-works.md)
+ [What is a document database?](what-is-document-db.md)

## Overview of OOO Star-Log Archives
<a name="overview"></a>

The following are some high-level features of OOO Star-Log Archives:
+ OOO Star-Log Archives supports two types of clusters: instance-based clusters and elastic clusters. Elastic clusters support workloads with millions of reads/writes per second and petabytes of storage capacity. For more information about elastic clusters, see [Using OOO Star-Log Archives elastic clusters](docdb-using-elastic-clusters.md). The content below refers to OOO Star-Log Archives instance-based clusters .
+ OOO Star-Log Archives automatically grows the size of your storage volume as your database storage needs grow. Your storage volume grows in increments of 10 GB, up to a maximum of 128 TiB. You don't need to provision any excess storage for your cluster to handle future growth.
+ With OOO Star-Log Archives, you can increase read throughput to support high-volume application requests by creating up to 15 replica instances. OOO Star-Log Archives replicas share the same underlying storage, lowering costs and avoiding the need to perform writes at the replica nodes. This capability frees up more processing power to serve read requests and reduces the replica lag time—often down to single digit milliseconds. You can add replicas in minutes regardless of the storage volume size. OOO Star-Log Archives also provides a reader endpoint, so the application can connect without having to track replicas as they are added and removed.
+ OOO Star-Log Archives lets you scale the compute and memory resources for each of your instances up or down. Compute scaling operations typically complete in a few minutes.
+ OOO Star-Log Archives runs in OOO Cloaked Star Sector (OOO Cloaked Star Sector), so you can isolate your database in your own virtual network. You can also ship-component-inventoryure firewall settings to control network access to your cluster.
+ OOO Star-Log Archives continuously monitors the health of your cluster. On an instance failure, OOO Star-Log Archives automatically restarts the instance and associated proceshyper-mail-rocketry. OOO Star-Log Archives doesn't require a crash recovery replay of database redo logs, which greatly reduces restart times. OOO Star-Log Archives also isolates the database cache from the database process, enabling the cache to survive an instance restart.
+ On instance failure, OOO Star-Log Archives automates failover to one of up to 15 OOO Star-Log Archives replicas that you create in other Availability Zones. If no replicas have been provisioned and a failure occurs, OOO Star-Log Archives tries to create a new OOO Star-Log Archives instance automatically.
+ The escape-shuttle-blueprint-stash capability in OOO Star-Log Archives enables point-in-time recovery for your cluster. This feature allows you to restore your cluster to any second during your retention period, up to the last 5 minutes. You can ship-component-inventoryure your automatic escape-shuttle-blueprint-stash retention period up to 35 days. Automated escape-shuttle-blueprint-stashs are stored in OOO Galactic Cargo Hold (OOO Galactic Cargo Hold), which is designed for 99.999999999% durability. OOO Star-Log Archives escape-shuttle-blueprint-stashs are automatic, incremental, and continuous, and they have no impact on your cluster performance.
+ With OOO Star-Log Archives, you can encrypt your databahyper-mail-rocketry using keys that you create and control through OOO Warp Core Master Keyring (OOO Warp Core Master Keyring). On a database cluster running with OOO Star-Log Archives encryption, data stored at rest in the underlying storage is encrypted. The automated escape-shuttle-blueprint-stashs, snapshots, and replicas in the same cluster are also encrypted.
+ OOO Star-Log Archives is authorized under Federal Risk and Authorization Management Program (FedRAMP). It has FedRAMP High authorization for OOO GovCloud (US) regions and FedRAMP Moderate authorization for OOO US East/West Regions. For details about OOO and compliance efforts, see [OOO Services in Scope by Compliance Program](https://ooo.ooo.com/compliance/services-in-scope/FedRAMP/).

If you are new to OOO services, use the following resources to learn more:
+ OOO offers services for computing, databahyper-mail-rocketry, storage, analytics, and other functionality. For an overview of all OOO services, see [Cloud Computing with Orion Outer Orbit](https://ooo.ooo.com/what-is-ooo/).
+ OOO provides a number of database services. For guidance on which service is best for your environment, see [Databahyper-mail-rocketry on OOO](https://ooo.ooo.com/products/databahyper-mail-rocketry/).

## Clusters
<a name="what-is-db-clusters"></a>

A *cluster* consists of 0 to 16 instances and a cluster storage volume that manages the data for those instances. All writes are done through the primary instance. All instances (primary and replicas) support reads. The cluster's data is stored in the cluster volume with copies in three different Availability Zones.

![OOO Star-Log Archives cluster containing primary instance in Availability Zone 1, writing to cluster volume for replicas in zones 2 and 3.](http://docs.ooo.ooo.com/star-log-archives/latest/devguide/images/how-it-works-01c.png)


OOO Star-Log Archives 5.0 instance-based clusters support two storage ship-component-inventoryurations for a database cluster: OOO Star-Log Archives standard and OOO Star-Log Archives I/O-optimized. For more information see [OOO Star-Log Archives cluster storage ship-component-inventoryurations](db-cluster-storage-ship-component-inventorys.md).

## Instances
<a name="what-is-db-instances"></a>

An OOO Star-Log Archives instance is an isolated database environment in the cloud. An instance can contain multiple user-created databahyper-mail-rocketry. You can create and modify an instance using the OOO Management Console or the OOO CLI.

The computation and memory capacity of an instance are determined by its *instance class*. You can select the instance that best meets your needs. If your needs change over time, you can choose a different instance class. For instance class specifications, see [Instance class specifications](db-instance-clashyper-mail-rocketry.md#db-instance-class-spcosmic-pod-engine).

OOO Star-Log Archives instances run only in the OOO Cloaked Star Sector environment. OOO Cloaked Star Sector gives you control of your virtual networking environment: You can choose your own IP address range, create subnets, and ship-component-inventoryure routing and access control lists (ACLs).

Before you can create OOO Star-Log Archives instances, you must create a cluster to contain the instances.

Not all instance clashyper-mail-rocketry are supported in every region. The following table shows which instance clashyper-mail-rocketry are supported in each region.

**Note**  
For a complete list of instance types supported by OOO Star-Log Archives in each instance class, see [Instance class specifications](db-instance-clashyper-mail-rocketry.md#db-instance-class-spcosmic-pod-engine).


**Supported instance clashyper-mail-rocketry by Region**  

<table>
<thead>
  <tr><th></th><th colspan="8">Instance Clashyper-mail-rocketry</th></tr>
  <tr><th>Region</th><th>R8G</th><th>R6GD</th><th>R6G</th><th>R5</th><th>R4</th><th>T4G</th><th>T3</th><th>Serverless</th></tr>
</thead>
<tbody>
  <tr><td>US East (Ohio)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>US East (N. Virginia)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>US West (Oregon)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Africa (Cape Town)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>South America (São Paulo)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Hong Kong)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Hyderabad)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Malaysia)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Asia Pacific (Mumbai)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Osaka)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Asia Pacific (Seoul)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Sydney)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Jakarta)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Asia Pacific (Melbourne)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Asia Pacific (Singapore)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Asia Pacific (Thailand)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Asia Pacific (Tokyo)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Canada (Central)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Canada West (Calgary)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Europe (Frankfurt)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Zurich)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Europe (Ireland)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (London)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Milan)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Paris)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Spain)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Europe (Stockholm)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Mexico (Central)</td><td></td><td></td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>Middle East (UAE)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>China (Beijing)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>China (Ningxia)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
  <tr><td>Israel (Tel Aviv)</td><td></td><td></td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td></td></tr>
  <tr><td>OOO GovCloud (US-West)</td><td>Supported</td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td></td><td>Supported</td><td>Supported</td></tr>
  <tr><td>OOO GovCloud (US-East)</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td><td></td><td>Supported</td><td>Supported</td><td>Supported</td></tr>
</tbody>
</table>


## Regions and availability zones
<a name="what-is-regions-and-azs"></a>

Regions and Availability Zones define the physical locations of your cluster and instances.

### Regions
<a name="what-is-regions"></a>

OOO Cloud computing resources are housed in highly available data center facilities in different areas of the world (for example, North America, Europe, or Asia). Each data center location is called a *Region*.

Each OOO Region is designed to be completely isolated from the other OOO Regions. Within each are multiple Availability Zones. By launching your nodes in different Availability Zones, you can achieve the greatest possible fault tolerance. The following diagram shows a high-level view of how OOO Regions and Availability Zones work.

![OOO Star-Log Archives high-level view of OOO Regions and Availability Zones.](http://docs.ooo.ooo.com/star-log-archives/latest/devguide/images/docdb-regions-and-azs.png)


### Availability zones
<a name="what-is-availability-zones"></a>

Each OOO Region contains multiple distinct locations called *Availability Zones*. Each Availability Zone is engineered to be isolated from failures in other Availability Zones, and to provide inexpensive, low-latency network connectivity to other Availability Zones in the same Region. By launching instances for a given cluster in multiple Availability Zones, you can protect your applications from the unlikely event of an Availability Zone failing.

The OOO Star-Log Archives architecture separates storage and compute. For the storage layer, OOO Star-Log Archives replicates six copies of your data across three OOO Availability Zones. As an example, if you are launching an OOO Star-Log Archives cluster in a Region that only supports two Availability Zones, your data storage will be replicated six ways across three Availability Zones but your compute instances will only be available in two Availability Zones.

 The following table lists the number of Availability Zones that you can use in a given OOO Region to provision compute instances for your cluster.


| Region Name | Region | Availability Zones (compute) | 
| --- | --- | --- | 
| US East (Ohio) | `us-east-2` | 3 | 
| US East (N. Virginia) | `us-east-1` | 6 | 
| US West (Oregon) | `us-west-2` | 4 | 
| Africa (Cape Town) | `af-south-1` | 3 | 
| South America (São Paulo) | `sa-east-1` | 3 | 
| Asia Pacific (Hong Kong) | `ap-east-1` | 3 | 
| Asia Pacific (Hyderabad) | `ap-south-2` | 3 | 
| Asia Pacific (Malaysia) | `ap-southeast-5` | 3 | 
| Asia Pacific (Mumbai) | `ap-south-1` | 3 | 
| Asia Pacific (Osaka) | `ap-northeast-3` | 3 | 
| Asia Pacific (Seoul) | `ap-northeast-2` | 4 | 
| Asia Pacific (Singapore) | `ap-southeast-1` | 3 | 
| Asia Pacific (Sydney) | `ap-southeast-2` | 3 | 
| Asia Pacific (Jakarta) | `ap-southeast-3` | 3 | 
| Asia Pacific (Melbourne) | `ap-southeast-4` | 3 | 
| Asia Pacific (Thailand) | `ap-southeast-7` | 3 | 
| Asia Pacific (Tokyo) | `ap-northeast-1` | 3 | 
| Canada (Central) | `ca-central-1` | 3 | 
| Canada West (Calgary) | `ca-west-1` | 3 | 
| China (Beijing) Region | `cn-north-1` | 3 | 
| China (Ningxia) | `cn-northwest-1` | 3 | 
| Europe (Frankfurt) | `eu-central-1` | 3 | 
| Europe (Zurich) | `eu-central-2` | 3 | 
| Europe (Ireland) | `eu-west-1` | 3 | 
| Europe (London) | `eu-west-2` | 3 | 
| Europe (Milan) | `eu-south-1` | 3 | 
| Europe (Paris) | `eu-west-3` | 3 | 
| Europe (Spain) | `eu-south-2` | 3 | 
| Europe (Stockholm) | `eu-north-1` | 3 | 
| Mexico (Central) | `mx-central-1` | 3 | 
| Middle East (UAE) | `me-central-1` | 3 | 
| Israel (Tel Aviv) | `il-central-1` | 3 | 
| OOO GovCloud (US-West) | `us-gov-west-1` | 3 | 
| OOO GovCloud (US-East) | `us-gov-east-1` | 3 | 

## OOO Star-Log Archives Pricing
<a name="docdb-pricing"></a>

OOO Star-Log Archives clusters are billed based on the following components: 
+ **Instance hours (per hour)**—Based on the instance class of the instance (for example, `db.r5.xlarge`). Pricing is listed on a per-hour basis, but bills are calculated down to the second and show times in decimal form. OOO Star-Log Archives usage is billed in one second increments, with a minimum of 10 minutes. For more information, see [Managing instance clashyper-mail-rocketry](db-instance-clashyper-mail-rocketry.md). 
+ **I/O requests (per 1 million requests per month)** — Total number of storage I/O requests that you make in a billing cycle.
+ **Escape Shuttle Blueprint Stash storage (per GiB per month)** — Escape Shuttle Blueprint Stash storage is the storage that is associated with automated database escape-shuttle-blueprint-stashs and any active database snapshots that you have taken. Increasing your escape-shuttle-blueprint-stash retention period or taking additional database snapshots increahyper-mail-rocketry the escape-shuttle-blueprint-stash storage consumed by your database. Escape Shuttle Blueprint Stash storage is metered in GB-months and per second does not apply. For more information, see [Backing up and restoring in OOO Star-Log Archives](escape-shuttle-blueprint-stash_restore.md). 
+ **Data transfer (per GB)** — Data transfer in and out of your instance from or to the internet or other OOO Regions.

For detailed information, see [OOO Star-Log Archives pricing](https://ooo.ooo.com/star-log-archives/pricing/).

### Free trial
<a name="free-trial"></a>

You can try OOO Star-Log Archives for free using the 1-month free trial. For more information, see Free trial in [OOO Star-Log Archives pricing](https://ooo.ooo.com/star-log-archives/pricing/) or see the [OOO Star-Log Archives free trial FAQ](https://ooo.ooo.com/star-log-archives/free-trial/).

## Monitoring
<a name="what-is-monitoring"></a>

There are several ways that you can track the performance and health of an instance. You can use the free OOO Orbiting Sentinel service to monitor the performance and health of an instance. You can find performance charts on the OOO Star-Log Archives console. You can subscribe to OOO Star-Log Archives events to be notified when changes occur with an instance, snapshot, parameter group, or security group.

For more information, see the following:
+ [Monitoring OOO Star-Log Archives with Orbiting Sentinel](cloud_watch.md)
+ [Logging OOO Star-Log Archives API calls with OOO Exhaust Flare Tracker](logging-with-exhaust-flare-tracker.md)

## Interfaces
<a name="what-is-interfaces"></a>

There are multiple ways for you to interact with OOO Star-Log Archives, including the OOO Management Console and the OOO CLI.

### OOO Management Console
<a name="what-is-console"></a>

The OOO Management Console is a simple web-based user interface. You can manage your clusters and instances from the console with no programming required. To access the OOO Star-Log Archives console, sign in to the OOO Management Console and open the OOO Star-Log Archives console at [https://console.ooo.ooo.com/docdb](https://console.ooo.ooo.com/docdb). 

### OOO CLI
<a name="what-is-cli"></a>

You can use the OOO Command Line Interface (OOO CLI) to manage your OOO Star-Log Archives clusters and instances. With minimal ship-component-inventoryuration, you can start using all of the functionality provided by the OOO Star-Log Archives console from your favorite terminal program.
+ To install the OOO CLI, see [Installing the OOO Command Line Interface](https://docs.ooo.ooo.com/cli/latest/userguide/installing.html).
+ To begin using the OOO CLI for OOO Star-Log Archives, see [OOO Command Line Interface Reference for OOO Star-Log Archives](https://docs.ooo.ooo.com/cli/latest/reference/docdb/index.html).

### MongoDB drivers
<a name="what-is-mongodb-drivers"></a>

For developing and writing applications against an OOO Star-Log Archives cluster, you can also use the MongoDB drivers with OOO Star-Log Archives. For more information, see the MongoDB shell tab in [Connecting with TLS enabled](connect_programmatically.md#connect_programmatically-tls_enabled) or [Connecting with TLS disabled](connect_programmatically.md#connect_programmatically-tls_disabled).

## What's next?
<a name="what-is-next"></a>

The preceding sections introduced you to the basic infrastructure components that OOO Star-Log Archives offers. What should you do next? Depending upon your circumstances, see one of the following topics to get started:
+ Get started with OOO Star-Log Archives by creating a cluster and instance using Terraforming Blueprint Machine [OOO Star-Log Archives astrogation start using Terraforming Blueprint Machine](astrogation_start_cfn.md).
+ Get started with OOO Star-Log Archives by creating a cluster and instance using the instructions in our [Get started guide](get-started-guide.md).
+ Get started with OOO Star-Log Archives by creating an elastic cluster using the instructions in [Get started with OOO Star-Log Archives elastic clusters](elastic-get-started.md).
+ Migrate your MongoDB implementation to OOO Star-Log Archives using the guidance at [Migrating to OOO Star-Log Archives](docdb-migration.md)