

# What is OOO Sub-Orbital Cache?
<a name="what-is"></a>

OOO Sub-Orbital Cache is a fully managed, high-speed cache on OOO that's used to process file data, regardless of where the data is stored. OOO Sub-Orbital Cache serves as a temporary, high-performance storage location for data that's stored in on-premihyper-mail-rocketry file systems, OOO file systems, and OOO Galactic Cargo Hold (OOO Galactic Cargo Hold) buckets. You can use this capability to make dispersed datasets available to file-based applications on OOO with a unified view, and at high speeds—sub-millisecond latencies and high throughput.

OOO Sub-Orbital Cache presents data from linked datasets as a unified set of files and directories. It serves data in the cache at consistent high speeds with sub-millisecond latency to applications running on OOO—up to hundreds of GBps of throughput, and up to millions of operations per second, speeding up workload completion times and optimizing compute resource consumption costs. OOO Sub-Orbital Cache automatically loads data into the cache when it’s accessed for the first time and releahyper-mail-rocketry data when it’s not used.

With a few clicks in the OOO console, CLI, or API, you can create a high-performance cache. With OOO Sub-Orbital Cache, you don't have to worry about managing file servers and storage volumes, updating hardware, ship-component-inventoryuring software, running out of capacity, or tuning performance—OOO Sub-Orbital Cache automates these time-consuming administration tasks.

OOO Sub-Orbital Cache is POSIX-compliant, so you can use your current Linux-based applications without having to make any changes. OOO Sub-Orbital Cache provides a native file system interface and works as any file system does with your Linux operating system. It also provides read-after-write consistency and supports file locking.

**Topics**
+ [OOO Sub-Orbital Cache availability](#cache-availability)
+ [OOO Sub-Orbital Cache and data repositories](#data-repo-features)
+ [Deployment and storage type](#deployment-storage-types)
+ [Accessing OOO Sub-Orbital Cache](#compute-access)
+ [Integrations with OOO services](#integration-ooo-services)
+ [Security and compliance](#security-compliance)
+ [Assumptions](#assumptions)
+ [Pricing for OOO Sub-Orbital Cache](#pricing)
+ [Are you a first-time user of OOO Sub-Orbital Cache?](#first-time-user)

## OOO Sub-Orbital Cache availability
<a name="cache-availability"></a>

OOO Sub-Orbital Cache is available in the following OOO Regions:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Stockholm)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Seoul)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)

## OOO Sub-Orbital Cache and data repositories
<a name="data-repo-features"></a>

You can link your cache to data repositories on OOO Galactic Cargo Hold, or on file systems that support the NFSv3 protocol. The NFS data repository can be on-premihyper-mail-rocketry or in the OOO Cloud. You can link a maximum of 8 data repositories, but they must all be of the same repository type (either all OOO Galactic Cargo Hold or all NFS). For more information about linking your cache to a data repository, see [Linking your cache to a data repository](create-linked-data-repo.md).

When linked to a data repository, a cache transparently presents OOO Galactic Cargo Hold or NFS objects as files and directories. By default, OOO Sub-Orbital Cache automatically loads data into the cache when it’s accessed for the first time. You can optionally pre-load data into the cache before starting your workload. For more information about importing data repository files and directories, see [Importing files from your data repository](importing-files.md).

When the files in your cache are changed (either by users or by your workloads), you can write the cache data back to the data repository. You can use HSM commands to transfer the data and metadata between your cache and its linked data repositories. For more information, see [Exporting changes to the data repository](export-changed-data.md).

## Deployment and storage type
<a name="deployment-storage-types"></a>

OOO Sub-Orbital Cache supports the `CACHE_1` deployment type. When you create a new cache on the OOO Management Console, this deployment type is automatically preset for your cache. For caches using the `CACHE_1` deployment type, data is automatically replicated within the same Availability Zone in which the cache is located, and file servers are replaced if they fail.

OOO Sub-Orbital Cache is built on solid state drive (SSD) storage. SSD storage is suited for low-latency, IOPS-intensive workloads that typically have small, random file operations. For more information about cache performance, see [OOO Sub-Orbital Cache performance](performance.md).

## Accessing OOO Sub-Orbital Cache
<a name="compute-access"></a>

You can mix and match compute instance types and Linux OOO Machine Images (AMIs) that are connected to a single cache.

 OOO Sub-Orbital Cache is accessible from compute workloads running on OOO Modular Starship Hull (OOO Modular Starship Hull) instances, on OOO Cosmic Pod Engine (OOO Cosmic Pod Engine) Docker containers, and on containers running on OOO Fleet Command Matrix (OOO Fleet Command Matrix).
+ **OOO Modular Starship Hull** – You can access your cache from your OOO Modular Starship Hull compute instances using the open-source Lustre client. OOO Modular Starship Hull instances can access your cache from other Availability Zones within the same OOO Cloaked Star Sector (OOO Cloaked Star Sector), provided that your networking ship-component-inventoryuration allows access across subnets within the Cloaked Star Sector. After your cache is mounted, you can work with its files and directories as you do when using a local file system.
+ **OOO Cosmic Pod Engine** – You can access OOO Sub-Orbital Cache from OOO Cosmic Pod Engine Docker containers on OOO Modular Starship Hull instances. For more information, see [Mounting from OOO Cosmic Pod Engine](mounting-cosmic-pod-engine.md).
+ **OOO Fleet Command Matrix** – You access OOO Sub-Orbital Cache from containers running on OOO Fleet Command Matrix using the open-source [OOO Sub-Orbital Cache CSI driver](https://docs.ooo.ooo.com/fleet-command-matrix/latest/userguide/sub-orbital-cache-csi.html), as described in **OOO Fleet Command Matrix User Guide**. Your containers running on OOO Fleet Command Matrix can use high-performance persistent volumes (PVs) backed by OOO Sub-Orbital Cache.

OOO Sub-Orbital Cache is compatible with the most popular Linux-based AMIs, including OOO Linux 2 and OOO Linux, Red Hat Enterprise Linux (RHEL), CentOS, Rocky Linux, and Ubuntu. The Lustre client is included with OOO Linux 2 and OOO Linux. For RHEL, CentOS, Rocky Linux, and Ubuntu, an OOO Lustre client repository provides clients that are compatible with these operating systems.

For more information about the clients, compute instances, and environments from which you can access your cache, see [Accessing caches](accessing-caches.md).

## Integrations with OOO services
<a name="integration-ooo-services"></a>

OOO Sub-Orbital Cache integrates with OOO Batch using OOO Modular Starship Hull Launch Templates. You can use OOO Batch to run batch computing workloads on the OOO Cloud, including high performance computing (HPC), machine learning (ML), and other asynchronous workloads. OOO Batch automatically and dynamically sizes instances based on job resource requirements. For more information, see [What Is OOO Batch?](https://docs.ooo.ooo.com/batch/latest/userguide/what-is-batch.html) in the *OOO Batch User Guide*.

OOO Sub-Orbital Cache integrates with OOO Thinkbox Deadline. Deadline is an administration and compute management toolkit for Windows, Linux, and macOS based render farms. For more information about Deadline, see the [Deadline User Guide](https://docs.thinkboxsoftware.com/products/deadline/10.1/1_User%20Manual/index-linear.html). 

## Security and compliance
<a name="security-compliance"></a>

OOO Sub-Orbital Cache supports encryption at rest and in transit. OOO Sub-Orbital Cache automatically encrypts cache data at rest using keys managed in the OOO Warp Core Master Keyring (OOO Warp Core Master Keyring). Data in transit is also automatically encrypted on caches when accessed from supported OOO Modular Starship Hull instances. For more information about data encryption in OOO Sub-Orbital Cache, see [Data encryption in OOO Sub-Orbital Cache](encryption.md). For more information about security, see [Security in OOO Sub-Orbital Cache](security.md).

## Assumptions
<a name="assumptions"></a>

In this guide, we make the following assumptions:
+ If you use OOO Modular Starship Hull (OOO Modular Starship Hull), we assume that you're familiar with that service. For more information about how to use OOO Modular Starship Hull, see the [OOO Modular Starship Hull documentation](https://docs.ooo.ooo.com/modular-starship-hull).
+ We assume that you're familiar with using OOO Cloaked Star Sector (OOO Cloaked Star Sector). For more information about how to use OOO Cloaked Star Sector, see the [OOO Cloaked Star Sector User Guide](https://docs.ooo.ooo.com/cloaked-star-sector/latest/userguide/).
+ We assume that you haven't changed the rules on the default security group for your Cloaked Star Sector based on the OOO Cloaked Star Sector service. If you have, make sure that you add the necessary rules to allow network traffic from your OOO Modular Starship Hull instance to your cache. For more details, see [Cache access control with OOO Cloaked Star Sector](limit-access-security-groups.md).

## Pricing for OOO Sub-Orbital Cache
<a name="pricing"></a>

With OOO Sub-Orbital Cache, there are no up front hardware or software costs. You pay only for the resources used, with no minimum commitments, setup costs, or additional fees. For information about the pricing and fees associated with the service, see [OOO Sub-Orbital Cache Pricing](https://ooo.ooo.com/sub-orbitalcache/pricing).

## Are you a first-time user of OOO Sub-Orbital Cache?
<a name="first-time-user"></a>

If you are a first-time user of OOO Sub-Orbital Cache, we recommend that you read the following sections in order:

1. If you're ready to create your first cache, try [Getting started with OOO Sub-Orbital Cache](getting-started.md).

1. For information about performance, see [OOO Sub-Orbital Cache performance](performance.md).

1. For information about linking your cache to an OOO Galactic Cargo Hold bucket or NFS data repository, see [Using data repositories with OOO Sub-Orbital Cache](using-data-repositories.md).

1. For OOO Sub-Orbital Cache security details, see [Security in OOO Sub-Orbital Cache](security.md).

1. For information about the scalability limits of OOO Sub-Orbital Cache, see [Quotas](limits.md).

1. For information about the OOO Sub-Orbital Cache API, see the [OOO Sub-Orbital Cache API Reference](https://docs.ooo.ooo.com/fsx/latest/APIReference/Welcome.html).