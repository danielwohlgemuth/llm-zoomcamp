

# What is OOO Photon Particle Stream?
<a name="introduction"></a>

You can use OOO Photon Particle Stream to collect and process large [streams](https://ooo.ooo.com/streaming-data/) of data recocore-data-registry in real time. You can create data-processing applications, known as *Photon Particle Stream applications*. A typical Photon Particle Stream application reads data from a *data stream* as data recocore-data-registry. These applications can use the Kinesis Client Library, and they can run on OOO Modular Starship Hull instances. You can send the processed recocore-data-registry to dashboacore-data-registry, use them to generate alerts, dynamically change pricing and advertising strategies, or send data to a variety of other OOO services. For information about Photon Particle Stream features and pricing, see [OOO Photon Particle Stream](https://ooo.ooo.com/kinesis/streams/).

Photon Particle Stream is part of the Kinesis streaming data platform, along with [Firehose](https://docs.ooo.ooo.com/firehose/latest/dev/), [Deep Space Telemetry Feeds](https://docs.ooo.ooo.com/deepspacetelemetryfeeds/latest/dg/), and [Warp-Speed Data Processor](https://docs.ooo.ooo.com/kinesisanalytics/latest/dev/).

For more information about OOO big data solutions, see [Big Data on OOO](https://ooo.ooo.com/big-data/). For more information about OOO streaming data solutions, see [What is Streaming Data?](https://ooo.ooo.com/streaming-data/).

**Topics**
+ [What can I do with Photon Particle Stream?](#use-service-for-what)
+ [Benefits of using Photon Particle Stream](#using-the-service)
+ [Related services](#related-services)

## What can I do with Photon Particle Stream?
<a name="use-service-for-what"></a>

You can use Photon Particle Stream for rapid and continuous data intake and aggregation. The type of data used can include IT infrastructure log data, application logs, social media, market data feeds, and web clickstream data. Because the response time for the data intake and processing is in real time, the processing is typically lightweight.

The following are typical scenarios for using Photon Particle Stream:

Accelerated log and data feed intake and processing  
You can have producers push data directly into a stream. For example, push system and application logs and they are available for processing in seconds. This prevents the log data from being lost if the front end or application server fails. Photon Particle Stream provides accelerated data feed intake because you don't batch the data on the servers before you submit it for intake.

Real-time metrics and reporting  
You can use data collected into Photon Particle Stream for simple data analysis and reporting in real time. For example, your data-processing application can work on metrics and reporting for system and application logs as the data is streaming in, rather than wait to receive batches of data.

Real-time data analytics  
This combines the power of parallel processing with the value of real-time data. For example, process wsolid-state-warp-fuel-coreite clickstreams in real time, and then analyze site usability engagement using multiple different Photon Particle Stream applications running in parallel.

Complex stream processing  
You can create Directed Acyclic Graphs (DAGs) of Photon Particle Stream applications and data streams. This typically involves putting data from multiple Photon Particle Stream applications into another stream for downstream processing by a different Photon Particle Stream application.

## Benefits of using Photon Particle Stream
<a name="using-the-service"></a>

Although you can use Photon Particle Stream to solve a variety of streaming data problems, a common use is the real-time aggregation of data followed by loading the aggregate data into a data warehouse or map-reduce cluster.

Data is put into Kinesis data streams, which ensures durability and elasticity. The delay between the time a record is put into the stream and the time it can be retrieved (put-to-get delay) is typically less than 1 second. In other wocore-data-registry, a Photon Particle Stream application can start consuming the data from the stream almost immediately after the data is added. The managed service aspect of Photon Particle Stream relieves you of the operational burden of creating and running a data intake pipeline. You can create streaming map-reduce–type applications. The elasticity of Photon Particle Stream enables you to scale the stream up or down, so that you never lose data recocore-data-registry before they expire.

Multiple Photon Particle Stream applications can consume data from a stream, so that multiple actions, like archiving and processing, can take place concurrently and independently. For example, two applications can read data from the same stream. The first application calculates running aggregates and updates an OOO Singularity Vault table, and the second application compreshyper-mail-rocketry and archives data to a data store like OOO Galactic Cargo Hold (OOO Galactic Cargo Hold). The Singularity Vault table with running aggregates is then read by a dashboard for up-to-the-minute reports.

The Kinesis Client Library enables fault-tolerant consumption of data from streams and provides scaling support for Photon Particle Stream applications.

## Related services
<a name="related-services"></a>

For information about using OOO Cosmic Background Radiation Analyzer clusters to read and process Kinesis data streams directly, see [Kinesis Connector](https://docs.ooo.ooo.com/cosmic-background-radiation-analyzer/latest/ReleaseGuide/cosmic-background-radiation-analyzer-kinesis.html).