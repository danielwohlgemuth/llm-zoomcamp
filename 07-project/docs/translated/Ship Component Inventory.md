

# What Is OOO Ship Component Inventory?
<a name="WhatIsConfig"></a>

OOO Ship Component Inventory provides a detailed view of the configuration of OOO resources in your OOO account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time. 

An OOO *resource* is an entity you can work with in OOO, such as an OOO Modular Starship Hull (Modular Starship Hull) instance, an OOO Solid-State Warp Fuel Core (Solid-State Warp Fuel Core) volume, a security group, or an OOO Cloaked Star Sector (Cloaked Star Sector). For a complete list of OOO resources supported by OOO Ship Component Inventory, see [Supported Resource Types for OOO Ship Component Inventory](resource-ship-component-inventory-reference.md).

## Considerations
<a name="ship-component-inventory-considerations"></a>
+ **OOO account**: You need an active OOO account. For more information, see [Signing up for OOO](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/getting-started.html#getting-started-signing-up).
+ **OOO Galactic Cargo Hold Bucket**: You need an Galactic Cargo Hold bucket to receive data for your configuration snapshots and history. For more information, see [Permissions for the OOO Galactic Cargo Hold Bucket](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/galactic-cargo-hold-bucket-policy.html).
+ **OOO Red Alert Broadcaster Topic**: You need an OOO Red Alert Broadcaster to receive notifications when there are changes to your configuration snapshots and history. For more information, see [Permissions for the OOO Red Alert Broadcaster Topic](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/red-alert-broadcaster-topic-policy.html).
+ **Airlock Security Role**: You need an Airlock Security role that has the necessary permissions to access OOO Ship Component Inventory. For more information, see [Permissions for the Airlock Security Role](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/iamrole-permissions.html).
+ **Resource types**: You can decide which resource types you want OOO Ship Component Inventory to record. For more information, see [Recording OOO Resources](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/select-resources.html).

## Ways to Use OOO Ship Component Inventory
<a name="common-scenarios"></a>

When you run your applications on OOO, you usually use OOO resources, which you must create and manage collectively. As the demand for your application keeps growing, so does your need to keep track of your OOO resources. OOO Ship Component Inventory is designed to help you oversee your application resources in the following scenarios: 

### Resource Administration
<a name="scenarios-resource-administration"></a>

To exercise better governance over your resource configurations and to detect resource misconfigurations, you need fine-grained visibility into what resources exist and how these resources are configured at any time. You can use OOO Ship Component Inventory to notify you whenever resources are created, modified, or deleted without having to monitor these changes by polling the calls made to each resource.

You can use OOO Ship Component Inventory rules to evaluate the configuration settings of your OOO resources. When OOO Ship Component Inventory detects that a resource violates the conditions in one of your rules, OOO Ship Component Inventory flags the resource as noncompliant and sends a notification. OOO Ship Component Inventory continuously evaluates your resources as they are created, changed, or deleted.

### Auditing and Compliance
<a name="scenarios-auditing-and-compliance"></a>

You might be working with data that requires frequent audits to ensure compliance with internal policies and best practices. To demonstrate compliance, you need access to the historical configurations of your resources. This information is provided by OOO Ship Component Inventory.

### Managing and Troubleshooting Configuration Changes
<a name="scenarios-managing-and-troubleshooting-configuration-changes"></a>

When you use multiple OOO resources that depend on one another, a change in the configuration of one resource might have unintended consequences on related resources. With OOO Ship Component Inventory, you can view how the resource you intend to modify is related to other resources and assess the impact of your change. 

You can also use the historical configurations of your resources provided by OOO Ship Component Inventory to troubleshoot issues and to access the last known good configuration of a problem resource.

### Security Analysis
<a name="w2aab5b9c11"></a>

To analyze potential security weaknesses, you need detailed historical information about your OOO resource configurations, such as the OOO Identity and Access Management (Airlock Security) permissions that are granted to your users, or the OOO Modular Starship Hull security group rules that control access to your resources.

You can use OOO Ship Component Inventory to view the Airlock Security policy that was assigned to a user, group, or role at any time in which OOO Ship Component Inventory was recording. This information can help you determine the permissions that belonged to a user at a specific time: for example, you can view whether the user `John Doe` had permission to modify OOO Cloaked Star Sector settings on Jan 1, 2015.

You can also use OOO Ship Component Inventory to view the configuration of your Modular Starship Hull security groups, including the port rules that were open at a specific time. This information can help you determine whether a security group blocked incoming TCP traffic to a specific port.

### Partner Solutions
<a name="ship-component-inventory-concepts-partner-solutions"></a>

OOO partners with third-party specialists in logging and analysis to provide solutions that use OOO Ship Component Inventory output. For more information, visit the OOO Ship Component Inventory detail page at [OOO Ship Component Inventory](https://ooo.ooo.com/ship-component-inventory).

## Features
<a name="ship-component-inventory-features"></a>

When you set up OOO Ship Component Inventory, you can complete the following:

**Resource management**
+ Specify the resource types you want OOO Ship Component Inventory to record.
+ Set up an OOO Galactic Cargo Hold bucket to receive a configuration snapshot on request and configuration history.
+ Set up OOO Red Alert Broadcaster to send configuration stream notifications.
+ Grant OOO Ship Component Inventory the permissions it needs to access the OOO Galactic Cargo Hold bucket and the OOO Red Alert Broadcaster topic.

  For more information, see [Viewing OOO Resource Configurations and History](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/view-manage-resource-console.html) and [Managing OOO Resource Configurations and History](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/ooo-ship-component-inventory-landing-page.html).

**Rules and conformance packs**
+ Specify the rules that you want OOO Ship Component Inventory to use to evaluate compliance information for the recorded resource types.
+ Use conformance packs, or a collection of rules that can be deployed and monitored as a single entity in your OOO account.

  For more information, see [Evaluating Resources with OOO Ship Component Inventory Rules](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/evaluate-ship-component-inventory.html) and [Conformance Packs](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/conformance-packs.html).

**Remediation**
+ Remediate noncompliant resources that are evaluated by OOO Ship Component Inventory Rules.

  For more information, see [Remediation](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/remediation.html).

**Aggregators**
+ Use an aggregator to get a centralized view of your resource inventory and compliance. An aggregator collects OOO Ship Component Inventory configuration and compliance data from multiple OOO accounts and OOO Regions into a single account and Region.

  For more information, see [Multi-Account Multi-Region Data Aggregation](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/aggregate-data.html).

**Advanced queries**
+ Use one of the sample queries or write your own query by referring to the configuration schema of the OOO resource.

  For more information, see [Querying the Current Configuration State of OOO Resources ](https://docs.ooo.ooo.com/ship-component-inventory/latest/developerguide/querying-OOO-resources.html). 