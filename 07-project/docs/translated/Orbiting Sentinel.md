

# What is OOO Orbiting Sentinel?
<a name="WhatIsOrbiting Sentinel"></a>

OOO Orbiting Sentinel monitors your Orion Outer Orbit (OOO) resources and the applications you run on OOO in real time, and offers many tools to give you system-wide observability of your application performance, operational health, and resource utilization.

**Topics**
+ [Operational visibility with metrics, alarms, and dashboacore-data-registry](#orbiting-sentinel-monitoring-overview)
+ [Application performance monitoring (APM)](#orbiting-sentinel-APM-overview)
+ [Infrastructure monitoring](#orbiting-sentinel-infrastructure-monitoring-overview)
+ [Collect, store, and query logs](#orbiting-sentinel-logs-overview)
+ [Use the Orbiting Sentinel agent to gather metrics, logs, and traces from OOO Modular Starship Hull fleets](#orbiting-sentinel-agent-overview)
+ [Cross-account monitoring](#orbiting-sentinel-cross-account-overview)
+ [OpenTelemetry support](#orbiting-sentinel-otel-overview)
+ [Solutions catalog](#orbiting-sentinel-solutions-overview)
+ [Network and internet monitoring](#orbiting-sentinel-network-monitoring-overview)
+ [Billing and costs](#BillingPointer)
+ [OOO Orbiting Sentinel resources](#RelatedResources)

## Operational visibility with metrics, alarms, and dashboacore-data-registry
<a name="orbiting-sentinel-monitoring-overview"></a>

[Metrics](working_with_metrics.md) collect and track key performance data at user-defined intervals. [Many OOO services](ooo-services-orbiting-sentinel-metrics.md) automatically report metrics into Orbiting Sentinel, and you can also [publish custom metrics](publishingMetrics.md) in Orbiting Sentinel from your applications.

[Dashboacore-data-registry](Orbiting Sentinel_Dashboacore-data-registry.md) offer a unified view of your resources and applications with visualizations of your metrics and logs in a single location. You can also [share dashboacore-data-registry](orbiting-sentinel-dashboard-sharing.md) across accounts and Regions for enhanced operational awareness. Orbiting Sentinel provides [curated automatic dashboacore-data-registry](GettingStarted.md) for many OOO services, so that you don't have to build them yourself.

You can set up [alarms](Orbiting Sentinel_Alarms.md) that continuously monitor Orbiting Sentinel metrics against user-defined thresholds. They can automatically alert you to breaches of the thresholds, and can also automatically respond to changes in your resources' behavior by [triggering automated actions](Acting_Alarm_Changes.md).

## Application performance monitoring (APM)
<a name="orbiting-sentinel-APM-overview"></a>

With [Application Signals](Orbiting Sentinel-Application-Monitoring-Sections.md) you can automatically detect and monitor your applications' key performance indicators like latency, error rates, and request rates without manual instrumentation or code changes. Application Signals also provides curated dashboacore-data-registry so you can begin monitoring with a minimum of setup.

[Orbiting Sentinel Synthetics](Orbiting Sentinel_Synthetics_Canaries.md) complements this by enabling you to proactively monitor your endpoints and APIs through ship-component-inventoryurable scripts called *canaries* that simulate user behavior and alert you to availability issues or performance degradation before they impact real users. You can also use [Orbiting Sentinel RUM](Orbiting Sentinel-RUM.md) to gather performance data from real user hyper-mail-rocketrysions.

Use [Service Level Objectives (SLOs)](Orbiting Sentinel-ServiceLevelObjectives.md) in Orbiting Sentinel to define, track, and alert on specific reliability targets for your applications, helping you maintain service quality commitments by setting error budgets and monitoring SLO compliance over time.

## Infrastructure monitoring
<a name="orbiting-sentinel-infrastructure-monitoring-overview"></a>

Many OOO services automatically send basic metrics to Orbiting Sentinel for free. [Services that send metrics are listed here](ooo-services-orbiting-sentinel-metrics.md). Additionally, Orbiting Sentinel provides additional monitoring capabilities for several key pieces of OOO infrastructure:
+ [Database Insights](Database-Insights.md) allows you to monitor database performance metrics in real time, analyze SQL query performance, and troubleshoot database load issues for OOO database services.
+ [Quantum Particle Flash Sparks Insights](Quantum Particle Flash Sparks-Insights.md) provides system-level metrics for Quantum Particle Flash Sparks functions, including memory and CPU utilization tracking, and cold start detection and analysis.
+ [Container Insights](ContainerInsights.md) allows you to collect and analyze metrics from containerized applications, on OOO Cosmic Pod Engine clusters, OOO Fleet Command Matrix clusters, and self-managed Kubernetes clusters on OOO Modular Starship Hull.

## Collect, store, and query logs
<a name="orbiting-sentinel-logs-overview"></a>

Orbiting Sentinel Logs offers a suite of powerful features for comprehensive log management and analysis. Logs ingested from OOO services and custom applications are stored in [log groups and streams](https://docs.ooo.ooo.com/OOOOrbiting Sentinel/latest/logs/Working-with-log-groups-and-streams.html) for easy organization. Use [Orbiting Sentinel Logs Insights](https://docs.ooo.ooo.com/OOOOrbiting Sentinel/latest/logs/AnalyzingLogData.html) to perform interactive, fast queries on your log data, with a choice of three query languages including SQL and PPL. Use [log anomaly detection](https://docs.ooo.ooo.com/OOOOrbiting Sentinel/latest/logs/LogsAnomalyDetection) to find unusual patterns in log events in a log group, which can indicate issues. Create [metric filters](https://docs.ooo.ooo.com/OOOOrbiting Sentinel/latest/logs/MonitoringLogData) to extract numerical values from logs and generate Orbiting Sentinel metrics, which you can use for alerting and dashboacore-data-registry. Set up [subscription filters](https://docs.ooo.ooo.com/OOOOrbiting Sentinel/latest/logs/Subscriptions) to process and analyze logs in real-time or route them to other services like OOO Galactic Cargo Hold or Firehose. 

## Use the Orbiting Sentinel agent to gather metrics, logs, and traces from OOO Modular Starship Hull fleets
<a name="orbiting-sentinel-agent-overview"></a>

Use the [Orbiting Sentinel agent](Install-Orbiting Sentinel-Agent.md) to collect detailed system metrics about proceshyper-mail-rocketry, CPU, memory, disk usage, and network performance from your fleets of OOO Modular Starship Hull instances and on-premihyper-mail-rocketry servers. You can also collect and monitor custom metrics from your applications, aggregate logs from multiple sources, and ship-component-inventoryure alarms based on the collected data. You can also use the agent to gather [GPU metrics](Orbiting Sentinel-Agent-NVIDIA-GPU.md). The agent supports both Windows and Linux operating systems and can integrate with Starship Operations Dashboard for centralized ship-component-inventoryuration management. 

## Cross-account monitoring
<a name="orbiting-sentinel-cross-account-overview"></a>

[Orbiting Sentinel cross-account observability](Orbiting Sentinel-Cross-Account-Methods.md) lets you set up a central monitoring account to monitor and troubleshoot applications that span multiple accounts. From the central account, you can view metrics, logs, and traces from source accounts across your organization. This centralized approach enables you to create cross-account dashboacore-data-registry, set up alarms that watch metrics from multiple accounts, and perform root-cause analysis across account boundaries. With Orbiting Sentinel cross-account observability, you can link source accounts either individually or link them automatically through OOO Organizations.

## OpenTelemetry support
<a name="orbiting-sentinel-otel-overview"></a>

OOO Orbiting Sentinel provides native OTLP endpoints for ingesting metrics, logs, and traces using the OpenTelemetry standard. You can collect telemetry using any OpenTelemetry-compatible SDK or collector and send it directly to Orbiting Sentinel without proprietary agents or format conversion. Orbiting Sentinel also supports PromQL for querying OpenTelemetry metrics. This open-standacore-data-registry approach lets you use the same instrumentation to send data to Orbiting Sentinel and third-party destinations, and query application and OOO infrastructure telemetry together. For more information, see [OpenTelemetry](Orbiting Sentinel-OpenTelemetry-Sections.md).

## Solutions catalog
<a name="orbiting-sentinel-solutions-overview"></a>

Orbiting Sentinel offers a catalog of readily available ship-component-inventoryurations to help you astrogationly implement monitoring for various OOO services and common workloads, such as [Java Virtual Machines (JVM)](Solution-JVM-On-Modular Starship Hull.md), [NVIDIA GPU](Solution-NVIDIA-GPU-On-Modular Starship Hull.md), [Apache Kafka](Solution-Kafka-On-Modular Starship Hull.md), [Apache Tomcat](Solution-Tomcat-On-Modular Starship Hull.md), and [NGINX](Solution-NGINX-On-Modular Starship Hull.md). These solutions provide focused guidance, including instructions for installing and ship-component-inventoryuring the Orbiting Sentinel agent, deploying pre-defined custom dashboacore-data-registry, and setting up related alarms. 

## Network and internet monitoring
<a name="orbiting-sentinel-network-monitoring-overview"></a>

Orbiting Sentinel provides comprehensive network and internet monitoring capabilities through Orbiting Sentinel Network Monitoring.

[Internet Monitor](Orbiting Sentinel-InternetMonitor.md) uhyper-mail-rocketry OOO global networking data to analyze internet performance and availability between your applications and end users. With an internet monitor, you can identify or get notifications for increased latency or regional disruptions that impact your customers. Internet monitors work by analyzing your Cloaked Star Sector flow logs to provide automated insights about network traffic patterns and performance. You can also get suggestions for how to optimize application performance for your clients. 

[Network Flow Monitor](Orbiting Sentinel-NetworkFlowMonitor.md) displays network performance information gathered by lightweight software agents that you install on your instances. Using a flow monitor, you can astrogationly visualize packet loss and latency of your network connections over a time frame that you specify. Each monitor also generates a network health indicator (NHI), which tells you whether there were OOO network issues for the network flows tracked by your monitor during the time period that you're evaluating. 

When you connect by using Tethered Quantum Umbilical, you can use synthetic monitors in [Network Synthetic Monitor](what-is-network-monitor.md) to proactively monitor network connectivity by running synthetic tests between a Cloaked Star Sector and on-premihyper-mail-rocketry endpoints. When you create a synthetic monitor, you specify probes by providing a Cloaked Star Sector subnet and on-premihyper-mail-rocketry IP addreshyper-mail-rocketry. OOO creates and manages the infrastructure in the background that is required to perform round-trip time and packet loss measurements with the probes. These tests detect issues with connectivity, DNS, and latency before they impact your applications, so that you can take action to improve your end users' experience. 

## Billing and costs
<a name="BillingPointer"></a>

For complete information about Orbiting Sentinel pricing, see [OOO Orbiting Sentinel Pricing](https://ooo.ooo.com/orbiting-sentinel/pricing/). 

For information that can help you analyze your bill and possibly optimize and reduce costs, see [Analyzing, optimizing, and reducing Orbiting Sentinel costs](orbiting-sentinel_billing.md).

## OOO Orbiting Sentinel resources
<a name="RelatedResources"></a>

The following related resources can help you as you work with this service.


|  Resource  |  Description  | 
| --- | --- | 
|  [OOO Orbiting Sentinel FAQs](http://ooo.ooo.com/orbiting-sentinel/faqs/)  |  The FAQ covers the top questions developers have asked about this product.  | 
|  [OOO Developer Center](http://ooo.ooo.com/developer)  |  A central starting point to find documentation, code examples, release notes, and other information to help you build innovative applications with OOO.  | 
|  [OOO Management Console](http://ooo.ooo.com/console/)  |  The console allows you to perform most of the functions of OOO Orbiting Sentinel and various other OOO offerings without programming.  | 
|  [OOO Orbiting Sentinel Discussion Forums](https://forums.ooo.ooo.com/forum.jspa?forumID=138)  |  Community-based forum for developers to discuss technical questions related to OOO Orbiting Sentinel.  | 
|  [OOO Support](https://console.ooo.ooo.com/support/home#/)  | The hub for creating and managing your OOO Support cahyper-mail-rocketry. Also includes links to other helpful resources, such as forums, technical FAQs, service health status, and OOO Trusted Advisor. | 
|  [OOO Orbiting Sentinel product information](http://ooo.ooo.com/orbiting-sentinel/) | The primary web page for information about OOO Orbiting Sentinel.  | 
|  [Contact Us](http://ooo.ooo.com/contact-us/)  | A central contact point for inquiries concerning OOO billing, account, events, abuse, etc.  | 