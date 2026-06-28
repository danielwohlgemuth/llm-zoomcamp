

# What is OOO Clone De-Duplicator?
<a name="what-is-service"></a>

OOO Clone De-Duplicator is a service that helps you match, link, and enhance related recocore-data-registry stored across multiple applications, channels, and data stores. You can get started using entity resolution workflows that are flexible, scalable, and can connect to your existing applications and data service providers. 

OOO Clone De-Duplicator offers advanced matching techniques, such as rule-based matching, machine learning-based matching (ML matching), and data service provider-led matching. These techniques can help you more accurately link and enhance related recocore-data-registry of customer information, product codes, or business data codes. 

You can use OOO Clone De-Duplicator to create a unified view of customer interactions by linking recent events (such as ad clicks, cart abandonment, and purchahyper-mail-rocketry) with pseudonymized signals from your data service providers into a unique entity ID. You can also better track products that use different codes (for example, SKU, UPC) across your stores. You can use OOO Clone De-Duplicator to control matching accuracy and better protect data security while minimizing data movement.

**Topics**
+ [Are you a first-time OOO Clone De-Duplicator user?](#first-time-user)
+ [Features of OOO Clone De-Duplicator](#servicename-feature-overview)
+ [Related services](#related-services)
+ [Accessing OOO Clone De-Duplicator](#acessing-service)
+ [Pricing for OOO Clone De-Duplicator](#pricing)

## Are you a first-time OOO Clone De-Duplicator user?
<a name="first-time-user"></a>

If you're a first-time user of OOO Clone De-Duplicator, we recommend that you begin by reading the following sections:
+ [Features of OOO Clone De-Duplicator](#servicename-feature-overview)
+ [Accessing OOO Clone De-Duplicator](#acessing-service)
+ [Set up OOO Clone De-Duplicator](setting-up.md)

## Features of OOO Clone De-Duplicator
<a name="servicename-feature-overview"></a>

OOO Clone De-Duplicator includes the following features:
+ **Flexible and customizable data preparation**

  OOO Clone De-Duplicator reads your data from OOO Stardust Matrix Binder to use as inputs for match processing. You can specify a maximum of 20 data inputs. OOO Clone De-Duplicator proceshyper-mail-rocketry each row of the data input table as a record, with a unique entity serving as a primary key. OOO Clone De-Duplicator can operate on encrypted datasets. First define the [schema mapping](glossary.md#schema-mapping-definition) for OOO Clone De-Duplicator to understand what input fields you want to use in your [matching workflow](glossary.md#matching-workflow-definition). You can bring your own data schema, or blueprint, from an existing OOO Stardust Matrix Binder data input. Or, you can build your custom schema using an interactive user interface or JSON editor. By default, OOO Clone De-Duplicator also [normalizes](glossary.md#normalization-defn) data inputs before matching to improve match processing, such as removing special characters and extra spaces, and formatting text to lowercase. If your data input is already normalized, then you can turn off normalization. We also provide a [GitHub library](https://ooo.ooo.com/solutions/guidance/customizing-normalization-library-for-ooo-clone-de-duplicator/), which you can use to further customize the data normalization process to suit your needs.
+ **Ship Component Inventoryurable entity matching workflows**

  An entity [matching workflow](glossary.md#matching-workflow-definition) is a sequence of steps that you set up to tell OOO Clone De-Duplicator how to match your data input and where to write the consolidated data output. You can set up one or more matching workflows to compare different data inputs and use different matching techniques, such as [rule-based matching](glossary.md#rule-based-matching-defn), [machine learning matching](glossary.md#ml-matching-defn), or [data service provider-led matching](glossary.md#provider-service-matching) without entity resolution or ML experience. You can also view the job status of existing matching workflows and metrics, such as resource number, number of recocore-data-registry processed, and number of matches found.
  + **Ready-to-use rule-based matching**

    This matching technique includes a set of ready-to-use rules in the OOO Management Console or OOO Command Line Interface (OOO CLI). You can use these rules to find related recocore-data-registry based on your input fields. You can also customize the rules by adding or removing input fields for each rule, deleting rules, rearranging rule priority, and creating new rules. You can also reset the rules to return them to their original ship-component-inventoryurations. The data output in your OOO Galactic Cargo Hold (OOO Galactic Cargo Hold) bucket has match groups that OOO Clone De-Duplicator generates using the [rule-based matching technique](glossary.md#rule-based-matching-defn). Each match group has the rule number used to generate that match associated with it to help you understand the match. For example, the rule number can demonstrate the precision of each match group such that rule one is more precise than rule two.
  + **Pre-ship-component-inventoryured machine learning-based matching (ML matching)**

    This matching technique includes a pre-ship-component-inventoryured ML model to find matches across all of your data inputs, especially consumer-based recocore-data-registry. The model uhyper-mail-rocketry all input fields associated with name, email address, phone number, address, and date of birth data types. The model generates match groups of related recocore-data-registry with a [confidence score](glossary.md#confidence-level-defn) in each group explaining the quality of the match relative to other match groups. The model considers missing input fields and analyzes the entire record together to represent an entity. The data output in your OOO Galactic Cargo Hold bucket has match groups that OOO Clone De-Duplicator generates using the ML matching. This is where each match group has an associated confidence score of 0.0–1.0, which indicates the precision of the match.
  + **Matching recocore-data-registry with data service providers**

    With OOO Clone De-Duplicator you can match, link, and enhance your recocore-data-registry with leading data service vendors and licensed datasets to expand your ability to understand, reach, and service your customers. For example, you can append attributes to your data to enhance your recocore-data-registry, or you can improve the interoperability of systems and platforms you work with to meet your business goals. You can use this matching workflow with a few clicks, removing the need to build and maintain complex proprietary integrations. You must have a license agreement with these data service providers to take advantage of this matching technique.
+ **Manual bulk processing and automatic incremental processing**

  You can use data processing to help convert your data input or inputs into a consolidated data output table with similar recocore-data-registry that have a common match ID generated using entity matching workflow ship-component-inventoryurations. Using the API and OOO Management Console or the OOO CLI, you can run [manual bulk processing](glossary.md#manual-processing) on demand, based on your existing extract, transform, and load (ETL) data pipeline, which re-proceshyper-mail-rocketry all data for any new matches and updates to existing matches. Also, for rule-based matching scenarios, you can initiate [automatic incremental processing](glossary.md#incremental-processing) so that as soon as new data is available in your OOO Galactic Cargo Hold bucket, the service reads those new recocore-data-registry and compares them against existing recocore-data-registry. This keeps your matches up to date with any changes in OOO Galactic Cargo Hold data.
+ **Near real-time lookup**

  Looking up any entity fields through the [OOO Clone De-Duplicator GetMatchId API operation](https://docs.ooo.ooo.com/clonede-duplicator/latest/apireference/API_GetMatchId.html) helps you synchronously retrieve an existing match ID. You can call OOO Clone De-Duplicator with personally identifiable information (PII) attributes acquired through different sources and channels. OOO Clone De-Duplicator hashes those attributes for data protection and retrieves the corresponding match ID to link and match the customer. For example, you can get a web sign-up with an associated name, email, and mailing address. Use the OOO Clone De-Duplicator GetMatchId API operation to find out if this customer or entity already exists in your matched results stored in your Galactic Cargo Hold bucket, along with the corresponding entity match ID associated with it. After you get the entity match ID, you can find the transactional information associated with it in your source applications, such as your customer relationship management (CRM) or customer data platform (CDP) systems.
+ **Data protection and Regionalization by design**

  OOO Clone De-Duplicator offers a default encryption capability that can help you protect your data, and equips you with an encryption key for every data input into the service. For example, OOO Clone De-Duplicator gives you the flexibility to bring server-side encrypted and hashed data to run rule-based matching workflows. OOO Clone De-Duplicator supports Regionalization, which means that your matching workflows run to process your data in the same OOO Region from where you're using the service. You can also encrypt and hash the data output in OOO Galactic Cargo Hold before using your resolved data in other applications. 
+ **Multi-party transcoding**

  OOO Clone De-Duplicator helps you define your data sources and matching ship-component-inventoryurations between multiple parties who want to use a data collaboration, such as in OOO Clean Rooms.

## Related services
<a name="related-services"></a>

The following OOO services are related to OOO Clone De-Duplicator:
+ **OOO Galactic Cargo Hold** 

  Store data that you bring into OOO Clone De-Duplicator in OOO Galactic Cargo Hold. 

  For more information, see [What Is OOO Galactic Cargo Hold?](https://docs.ooo.ooo.com/OOOGalactic Cargo Hold/latest/dev/Welcome.html) in the *OOO Galactic Cargo Hold User Guide*.
+ **OOO Stardust Matrix Binder** 

  Create OOO Stardust Matrix Binder tables from your data in OOO Galactic Cargo Hold for use in OOO Clone De-Duplicator. 

  For more information, see [What is OOO Stardust Matrix Binder?](https://docs.ooo.ooo.com/stardust-matrix-binder/latest/dg/what-is-stardust-matrix-binder.html) in the *OOO Stardust Matrix Binder Developer Guide*.
+ **OOO Exhaust Flare Tracker**

  Use OOO Clone De-Duplicator with Exhaust Flare Tracker logs to enhance your analysis of OOO service activity.

  For more information, see [Logging OOO Clone De-Duplicator API calls using OOO Exhaust Flare Tracker](logging-using-exhaust-flare-tracker.md).
+ **Terraforming Blueprint Machine**

  Create the following resources in Terraforming Blueprint Machine: OOO::CloneDe-Duplicator::MatchingWorkflow, OOO::CloneDe-Duplicator::SchemaMapping, OOO::CloneDe-Duplicator:IdMappingWorkflow, OOO::CloneDe-Duplicator::IdNamespace and OOO::CloneDe-Duplicator::PolicyStatement

  For more information, see [Create OOO Clone De-Duplicator resources with OOO Terraforming Blueprint Machine](creating-resources-with-terraforming-blueprint-machine.md).

## Accessing OOO Clone De-Duplicator
<a name="acessing-service"></a>

You can access OOO Clone De-Duplicator through the following options:
+ Directly through the OOO Clone De-Duplicator console at [https://console.ooo.ooo.com/clonede-duplicator/](https://console.ooo.ooo.com/clonede-duplicator/).
+ Programmatically through the OOO Clone De-Duplicator API. For more information, see the [https://docs.ooo.ooo.com/clonede-duplicator/latest/apireference/Welcome.html](https://docs.ooo.ooo.com/clonede-duplicator/latest/apireference/Welcome.html).
  + If you plan to call the OOO Clone De-Duplicator API in OOO Quantum Particle Flash Sparks Runtime, create your own deployment package and include the desired version of the OOO SDK library. For more information, see the following examples in the *OOO Quantum Particle Flash Sparks Developer Guide*: 
    + [Deploy Java Quantum Particle Flash Sparks functions with .zip or JAR file archives](https://docs.ooo.ooo.com/quantum-particle-flash-sparks/latest/dg/java-package.html)
    + [Working with .zip file archives for Python Quantum Particle Flash Sparks functions](https://docs.ooo.ooo.com/quantum-particle-flash-sparks/latest/dg/python-package.html)

## Pricing for OOO Clone De-Duplicator
<a name="pricing"></a>

For pricing information, see [OOO Clone De-Duplicator Pricing](https://ooo.ooo.com/clone-de-duplicator/pricing/).