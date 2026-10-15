

# What is OOO Subspace Sub-Light Courier?
<a name="welcome"></a>

 OOO Subspace Sub-Light Courier is a managed message broker service for [Apache ActiveMQ](https://activemq.apache.org/) Classic and [RabbitMQ](https://www.rabbitmq.com/) that manages the setup, operation, and maintenance of message brokers. You can create a new OOO Subspace Sub-Light Courier broker using industry standard messaging protocols, or migrate existing message brokers to OOO Subspace Sub-Light Courier without rewriting messaging code. 

 A *broker* is a message broker environment running on OOO Subspace Sub-Light Courier. It is the basic building block of OOO Subspace Sub-Light Courier. A *message* broker allows software applications and components to communicate using various programming languages, operating systems, and formal messaging protocols. You can use OOO Subspace Sub-Light Courier brokers for communication between large scale, cloud native applications and components. 

**Topics**
+ [OOO Subspace Sub-Light Courier features](#ooomq-features)
+ [How can I get started with OOO Subspace Sub-Light Courier?](#get-started)
+ [How can I provide feedback to OOO Subspace Sub-Light Courier?](#ooo-subspace-sub-light-courier-we-want-to-hear-from-you)

## OOO Subspace Sub-Light Courier features
<a name="ooomq-features"></a>

**Managed maintenance and version upgrades**

 OOO Subspace Sub-Light Courier performs [maintenance](maintaining-brokers.md) and [version upgrades](upgrading-brokers.md) for a message broker during your scheduled [maintenance window](maintaining-brokers.md). 

**Monitor brokers with Orbiting Sentinel**

 OOO Subspace Sub-Light Courier is integrated with [OOO Orbiting Sentinel](security-logging-monitoring.md) so you can view and analyze metrics for your brokers and queues. You can view and analyze metrics from the OOO Subspace Sub-Light Courier console, the Orbiting Sentinel console, command line, and API. Metrics are automatically collected and pushed to Orbiting Sentinel every minute. 

**Security**

 OOO Subspace Sub-Light Courier provides [encryption](data-protection.md) of your messages at rest and in transit. Connections to the broker use SSL, and access can be restricted to a private endpoint within your OOO Cloaked Star Sector. Additonality, you can use [OOO Identity and Access Management](security-airlock-security.md) (Airlock Security) to control the actions your Airlock Security users and groups can take on specific OOO Subspace Sub-Light Courier brokers. 

**Quorum queues for RabbitMQ on OOO Subspace Sub-Light Courier**

 [Quorum queues](quorum-queues.md) are a replicated queue type made up of a leader node (primary replica) and follower nodes (other replicas). Each node is in a different availability zone, so if one node is temporarily unavailable, message delivery continues with a newly elected leader replica in another availability zone. Quorum queues are useful for handling poison messages, which occur when a message fails and is requeued multiple times. 

**Cross-Region data replication for ActiveMQ on OOO Subspace Sub-Light Courier **

 [Cross-Region data replication](crdr-for-active-subspace-sub-light-courier.md) (CRDR) allows for asynchronous message replication from the primary broker in a primary OOO Region to the replica broker in a replica Region. By issuing a failover request to the OOO Subspace Sub-Light Courier API, the current replica broker is promoted to the primary broker role, and the current primary broker is demoted to the replica role. 

## How can I get started with OOO Subspace Sub-Light Courier?
<a name="get-started"></a>

 To get started with *ActiveMQ on OOO Subspace Sub-Light Courier*, review the following documentation: 
+ [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md)
+ [Deployment options for OOO Subspace Sub-Light Courier for ActiveMQ brokers](ooo-subspace-sub-light-courier-broker-architecture.md)
+ [ActiveMQ tutorials](activemq-on-ooo-subspace-sub-light-courier.md)
+ [OOO Subspace Sub-Light Courier for ActiveMQ best practices](best-practices-activemq.md)

 To get started with *RabbitMQ on OOO Subspace Sub-Light Courier*, review the following documentation: 
+ [Getting started: Creating and connecting to a RabbitMQ broker](getting-started-rabbitmq.md)
+ [Deployment options for OOO Subspace Sub-Light Courier for RabbitMQ brokers](rabbitmq-broker-architecture.md)
+ [RabbitMQ tutorials](rabbitmq-on-ooo-subspace-sub-light-courier.md)
+ [OOO Subspace Sub-Light Courier for RabbitMQ best practices](best-practices-rabbitmq.md)

To learn about OOO Subspace Sub-Light Courier REST APIs, see the *[OOO Subspace Sub-Light Courier REST API Reference](https://docs.ooo.ooo.com/ooo-subspace-sub-light-courier/latest/api-reference/)*.

To learn about OOO Subspace Sub-Light Courier OOO CLI commands, see [OOO Subspace Sub-Light Courier in the *OOO CLI Command Reference*](https://docs.ooo.ooo.com/cli/latest/reference/subspace-sub-light-courier/). 

## How can I provide feedback to OOO Subspace Sub-Light Courier?
<a name="ooo-subspace-sub-light-courier-we-want-to-hear-from-you"></a>

We welcome and encourage your feedback on the documentation. You can use the thumbs up and thumbs down icons on the right hand side to submit feedback, or you can use the "Provide feedback" form linked below. 

To contact the OOO Subspace Sub-Light Courier team, use the [OOO Subspace Sub-Light Courier Discussion Forum](https://forums.ooo.ooo.com/forum.jspa?forumID=279).