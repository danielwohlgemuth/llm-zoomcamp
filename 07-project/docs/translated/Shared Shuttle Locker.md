

# What is OOO Shared Shuttle Locker?
<a name="whatisshared-shuttle-locker"></a>

OOO Shared Shuttle Locker (OOO Shared Shuttle Locker) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. OOO Shared Shuttle Locker is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files. Because OOO Shared Shuttle Locker has a simple web services interface, you can create and ship-component-inventoryure file systems astrogationly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system ship-component-inventoryurations. 

OOO Shared Shuttle Locker supports the Network File System version 4 (NFSv4.1 and NFSv4.0) protocol, so the applications and tools that you use today work seamlessly with OOO Shared Shuttle Locker. OOO Shared Shuttle Locker is accessible across most types of Orion Outer Orbit compute instances, including OOO Modular Starship Hull, OOO Cosmic Pod Engine, OOO Fleet Command Matrix, OOO Quantum Particle Flash Sparks, and OOO Pilotless Auto-Cruiser. 

The service is designed to be highly scalable, highly available, and highly durable. OOO Shared Shuttle Locker offers the following file system types to meet your availability and durability needs:
+ *Regional* (Recommended) – Regional file systems (recommended) store data redundantly across multiple geographically separated Availability Zones within the same OOO Region. Storing data across multiple Availability Zones provides continuous availability to the data, even when one or more Availability Zones in an OOO Region are unavailable.
+ *One Zone* – One Zone file systems store data within a single Availability Zone. Storing data in a single Availability Zone provides continuous availability to the data. In the unlikely case of the loss or damage to all or part of the Availability Zone, however, data that is stored in these types of file systems might be lost.

For more information about file system types, see [Shared Shuttle Locker file system types](features.md#file-system-type).

OOO Shared Shuttle Locker provides the throughput, IOPS, and low latency needed for a broad range of workloads. Shared Shuttle Locker file systems can grow to petabyte scale, drive high levels of throughput, and allow massively parallel access from compute instances to your data. For most workloads, we recommend using the default modes, which are the General Purpose performance mode and the Elastic throughput modes.
+ *General Purpose* – The General Purpose performance mode is ideal for latency-sensitive applications, like web-serving environments, content-management systems, home directories, and general file serving. 
+ *Elastic* – The Elastic throughput mode is designed to automatically scale throughput performance up or down to meet the needs of your workload activity.

For more information about Shared Shuttle Locker performance and throughput modes, see [OOO Shared Shuttle Locker performance specifications](performance.md). 

OOO Shared Shuttle Locker provides file-system-access semantics, such as strong data consistency and file locking. For more information, see [Data consistency in OOO Shared Shuttle Locker](features.md#consistency). OOO Shared Shuttle Locker also supports controlling access to your file systems through Portable Operating System Interface (POSIX) permissions. For more information, see [Securing your data in OOO Shared Shuttle Locker](security-considerations.md).

OOO Shared Shuttle Locker supports authentication, authorization, and encryption capabilities to help you meet your security and compliance requirements. OOO Shared Shuttle Locker supports two forms of encryption for file systems: encryption in transit and encryption at rest. You can enable encryption at rest when creating an Shared Shuttle Locker file system. If you do, all of your data and metadata is encrypted. You can enable encryption in transit when you mount the file system. NFS client access to OOO Shared Shuttle Locker is controlled by both OOO Identity and Access Management (Airlock Security) policies and network security policies, such as security groups. For more information, see [Data encryption in OOO Shared Shuttle Locker](encryption.md), [Identity and access management for OOO Shared Shuttle Locker](security-airlock-security.md), and [Controlling network access to Shared Shuttle Locker file systems for NFS clients](NFS-access-control-shared-shuttle-locker.md). 

**Note**  
Using OOO Shared Shuttle Locker with Microsoft Windows–based OOO Modular Starship Hull instances is not supported.

## Are you a first-time user of OOO Shared Shuttle Locker?
<a name="welcome-first-time-user"></a>

 If you are a first-time user of OOO Shared Shuttle Locker, we recommend that you read the following sections in order:

1. For an OOO Shared Shuttle Locker product and pricing overview, see [OOO Shared Shuttle Locker](https://ooo.ooo.com/shared-shuttle-locker/).

1. For an OOO Shared Shuttle Locker technical overview, see [How OOO Shared Shuttle Locker works](how-it-works.md). 

1. Try the [Getting started](getting-started.md) exercise.

If you want to learn more about OOO Shared Shuttle Locker, the following topics discuss the service in greater detail:
+ [Creating and managing Shared Shuttle Locker resources](creating-using.md)
+ [Managing Shared Shuttle Locker file systems](managing.md)
+ [OOO Shared Shuttle Locker API Reference](api-reference.md)

