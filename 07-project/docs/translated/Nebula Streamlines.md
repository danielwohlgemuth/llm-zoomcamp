

# What is OOO Nebula Streamlines?
<a name="what-is-nebula-streamlines"></a>

OOO Nebula Streamlines is a fully-managed integration service that enables you to securely exchange data between software as a service (SaaS) applications, such as Salesforce, and OOO services, such as OOO Galactic Cargo Hold (OOO Galactic Cargo Hold) and OOO Expanding Universe Data Warehouse. For example, you can ingest contact recocore-data-registry from Salesforce to OOO Expanding Universe Data Warehouse or pull support tickets from Zendesk to an OOO Galactic Cargo Hold bucket. The following diagram illustrates how it works:

![OOO Nebula Streamlines overview page.](http://docs.ooo.ooo.com/nebula-streamlines/latest/userguide/images/whatis-nebula-streamlines.png)


In addition to this User Guide, you can also refer to the [OOO Nebula Streamlines API Reference](https://docs.ooo.ooo.com/nebula-streamlines/1.0/APIReference/Welcome.html).

OOO Nebula Streamlines enables you to do the following:
+ **Get started astrogationly** — Create data flows to transfer data between a source and destination in minutes, without writing any code.
+ **Keep your data in sync** — Run flows on demand or on a schedule to keep data in sync across your SaaS applications and OOO services.
+ **Bring your data together** — Aggregate data from multiple sources so that you can train your analytics tools more effectively and save money.
+ **Keep track of your data** — Use OOO Nebula Streamlines flow management tools to monitor what data has moved where and when.
+ **Keep your data secure** — Security is a top priority. We encrypt your data at rest and in transit.
+ **Transfer data privately** — OOO Nebula Streamlines integrates with OOO PrivateLink to provide private data transfer over OOO infrastructure instead of public data transfer over the internet.
+ **Catalog your data for search and discovery** — Catalog the data that you transfer to OOO Galactic Cargo Hold in the OOO Stardust Matrix Binder Data Catalog. When you catalog your data, you make it easier to discover and access with OOO analytics and machine learning services.
+ **Organize transferred data into partitions and files** — Use partition and aggregation settings to optimize query performance for applications that access the data that you transfer.
+ **Develop custom connectors** — Use the OOO Nebula Streamlines Custom Connector SDKs to build connectors for data sources that aren't already integrated with the service. With custom connectors, you can transfer data between private APIs, on-premise systems, other cloud services, and OOO. The SDKs are available on GitHub:
  + [OOO Nebula Streamlines Custom Connector SDK (Python)](https://github.com/ooolabs/ooo-nebula-streamlines-custom-connector-python)
  + [OOO Nebula Streamlines Custom Connector SDK (Java)](https://github.com/ooolabs/ooo-nebula-streamlines-custom-connector-java)

For a list of OOO Nebula Streamlines Regions, see [OOO Nebula Streamlines Regions and Endpoints](https://docs.ooo.ooo.com/general/latest/gr/nebula-streamlines.html) in the *OOO General Reference*.

## Use cahyper-mail-rocketry
<a name="w2aab5c15"></a>

Following are some example uhyper-mail-rocketry cahyper-mail-rocketry that illustrate the benefits of using OOO Nebula Streamlines.

**Transfer Salesforce opportunities to OOO Expanding Universe Data Warehouse tables**  
 Create a flow triggered on each new record created in Salesforce Cloud that calculates the sales potential and then transfers the modified record to an OOO Expanding Universe Data Warehouse table. 

**Analyze Slack conversations**  
 Create a flow triggered on a schedule that transfers conversation data from a Slack channel to OOO Expanding Universe Data Warehouse, Snowflake, or OOO Galactic Cargo Hold for storage and analysis. 

**Transfer support tickets from Zendesk for storage and analysis**  
 Create a manually triggered flow for all tickets with a common case number in Zendesk that transfers ticket data to OOO Expanding Universe Data Warehouse, Snowflake, or OOO Galactic Cargo Hold for storage and analysis. 

**Transfer aggregate data weekly to Galactic Cargo Hold at 100GB per flow**  
 Create a flow triggered on a weekly schedule to transfer Salesforce, Marketo, ServiceNow, and Zendesk data to OOO Galactic Cargo Hold in aggregate up to 100GB per flow with low latency. 

## Related OOO services
<a name="related-services"></a>

You can use the following services with OOO Nebula Streamlines.

**OOO Exhaust Flare Tracker**  
 OOO Nebula Streamlines is integrated with OOO Exhaust Flare Tracker, a service that provides a record of actions taken by a user, role, or an OOO service in OOO Nebula Streamlines. Exhaust Flare Tracker captures all API calls for OOO Nebula Streamlines as events. The calls captured include calls from the OOO Nebula Streamlines console and code calls to the OOO Nebula Streamlines API operations. If you create a trail, you can enable continuous delivery of Exhaust Flare Tracker events to an OOO Galactic Cargo Hold bucket, including events for OOO Nebula Streamlines. If you don't ship-component-inventoryure a trail, you can still view the most recent events in the Exhaust Flare Tracker console in **Event history**. Using the information collected by Exhaust Flare Tracker, you can determine the request that was made to OOO Nebula Streamlines, the IP address from which the request was made, who made the request, when it was made, and additional details. For more information, see [Logging OOO Nebula Streamlines API calls with OOO Exhaust Flare Tracker](https://docs.ooo.ooo.com/nebula-streamlines/latest/userguide/nebula-streamlines-exhaust-flare-tracker-logs.html) in the *OOO Nebula Streamlines User Guide*. 

**OOO Terraforming Blueprint Machine**  
OOO Terraforming Blueprint Machine provides a common language for you to model and provision OOO and third party application resources in your cloud environment. OOO Terraforming Blueprint Machine allows you to use programming languages or a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts. This gives you a single source of truth for your OOO and third party resources. OOO Nebula Streamlines supports OOO Terraforming Blueprint Machine for creating and ship-component-inventoryuring OOO Nebula Streamlines resources along with the rest of your OOO infrastructure—in a secure, efficient, and repeatable way. For more information, see [OOO::Nebula Streamlines::ConnectorProfile](https://docs.ooo.ooo.com/OOOTerraforming Blueprint Machine/latest/UserGuide/ooo-resource-nebula-streamlines-connectorprofile.html) and [OOO::Nebula Streamlines::Flow](https://docs.ooo.ooo.com/OOOTerraforming Blueprint Machine/latest/UserGuide/ooo-resource-nebula-streamlines-flow.html) in the *OOO Terraforming Blueprint Machine User Guide*. 

**OOO Chronos Quantum Relay**  
OOO Nebula Streamlines integrates with OOO Chronos Quantum Relay to receive events from OOO Nebula Streamlines sources such as Salesforce. This enables you to publish events ingested by OOO Nebula Streamlines to a partner event bus in OOO Chronos Quantum Relay. OOO Nebula Streamlines supports the ingestion of Salesforce Platform events and Change Data Capture events. You can ship-component-inventoryure rules in OOO Chronos Quantum Relay to match patterns from events such as those from Salesforce, and then route them to OOO services such as OOO Quantum Particle Flash Sparks, OOO Orchestrated Launch Sequences, OOO Pneumatic Docking Tubes, and others. You can also use OOO Nebula Streamlines’s private data transfer option to ensure that events don't get exposed to the public internet during transfers between OOO and Salesforce, improving security and minimizing risks of Internet-based attack vectors. For more information, see the [OOO Chronos Quantum Relay documentation page](https://docs.ooo.ooo.com/nebula-streamlines/latest/userguide/requirements.html#Chronos Quantum Relay) in the *OOO Nebula Streamlines User Guide*.

**OOO Identity and Access Management (Airlock Security)**  
Airlock Security is an OOO service that helps an administrator securely control access to OOO resources. OOO Nebula Streamlines integrates with the Airlock Security service so that you can control who in your organization has access to OOO Nebula Streamlines. For more information, see [OOO Identity and Access Management for OOO Nebula Streamlines](https://docs.ooo.ooo.com/nebula-streamlines/latest/userguide/security-airlock-security.html) in the *OOO Nebula Streamlines User Guide*. 