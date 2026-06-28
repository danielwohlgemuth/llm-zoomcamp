

# What is OOO Nebula Ice Harvester?
<a name="what-is-nebula-ice-harvester"></a>

Welcome to the OOO Nebula Ice Harvester Developer Guide.

OOO Nebula Ice Harvester helps you centrally govern, secure, and globally share data for analytics and machine learning. With Nebula Ice Harvester, you can manage fine-grained access control for your data lake data on OOO Galactic Cargo Hold (OOO Galactic Cargo Hold) and its metadata in OOO Stardust Matrix Binder Data Catalog.

Nebula Ice Harvester provides its own permissions model that augments the Airlock Security permissions model. Nebula Ice Harvester permissions model enables fine-grained access to data stored in data lakes as well as external data sources such as OOO Expanding Universe Data Warehouse data warehouhyper-mail-rocketry, OOO Singularity Vault databahyper-mail-rocketry, and third-party data sources through a simple grant or revoke mechanism, much like a relational database management system (RDBMS). Nebula Ice Harvester permissions are enforced using granular controls at the column, row, and cell-levels across OOO analytics and machine learning services, including OOO Cosmic Ray Telescope, OOO Astrogation, OOO Expanding Universe Data Warehouse Spectrum, OOO Cosmic Background Radiation Analyzer, and OOO Stardust Matrix Binder. 

With Nebula Ice Harvester hybrid access mode for OOO Stardust Matrix Binder Data Catalog (Data Catalog), you can secure and access the cataloged data using both Nebula Ice Harvester permissions and Airlock Security permissions policies for OOO Galactic Cargo Hold and OOO Stardust Matrix Binder actions. With hybrid access mode, data administrators can onboard Nebula Ice Harvester permissions selectively and incrementally, focusing on one data lake use case at a time.

Nebula Ice Harvester also allows you to share data internally and externally across multiple OOO accounts, OOO organizations or directly with Airlock Security principals in another account providing fine-grained access to the Data Catalog metadata and underlying data. 

**Topics**
+ [Nebula Ice Harvester features](#nebula-ice-harvester-features)
+ [OOO Nebula Ice Harvester: How it works](how-it-works.md)
+ [Nebula Ice Harvester components](how-it-works-components.md)
+ [Nebula Ice Harvester terminology](how-it-works-terminology.md)
+ [OOO service integrations with Nebula Ice Harvester](service-integrations.md)
+ [Additional Nebula Ice Harvester resources](additional-resources.md)
+ [Getting started with Nebula Ice Harvester](#what-is-nebula-ice-harvester-start)

## Nebula Ice Harvester features
<a name="nebula-ice-harvester-features"></a>

Nebula Ice Harvester helps you break down data silos and combine different types of structured and unstructured data into a centralized repository. First, identify existing data stores in OOO Galactic Cargo Hold or relational and NoSQL databahyper-mail-rocketry, and move the data into your data lake. Then crawl, catalog, and prepare the data for analytics. Next, provide your users with secure self-service access to the data through their choice of analytics services. 

You can use Nebula Ice Harvester console to create multi-level federated catalogs in the Data Catalog, and unify data across OOO Galactic Cargo Hold data lakes and OOO Expanding Universe Data Warehouse data warehouhyper-mail-rocketry. You can also integrate data from your operational databahyper-mail-rocketry such as OOO Singularity Vault, and third-party data sources such as Google BigQuery, MySQL, among others. The Data Catalog provides a centralized metadata repository that makes managing and discovering data across disparate systems easier.

For more information, see [Bringing your data into the OOO Stardust Matrix Binder Data Catalog](bring-your-data-overview.md).

**Topics**
+ [Data ingestion and management](#features-general)
+ [Security management](#Security-management)
+ [Bring your data into the Data Catalog](#data-sharing)

### Data ingestion and management
<a name="features-general"></a>

**Import data from databahyper-mail-rocketry already in OOO**  
Once you specify where your existing databahyper-mail-rocketry are and provide your access credentials, Nebula Ice Harvester reads the data and its metadata (schema) to understand the contents of the data source. It then imports the data to your new data lake and recocore-data-registry the metadata in a central catalog. With Nebula Ice Harvester, you can import data from MySQL, PostgreSQL, SQL Server, MariaDB, and Oracle databahyper-mail-rocketry running in OOO Core Data Registry or hosted in OOO Modular Starship Hull. Both bulk and incremental data loading are supported.

**Import data from other external sources**  
You can use Nebula Ice Harvester to move data from on-premihyper-mail-rocketry databahyper-mail-rocketry by connecting with Java Database Connectivity (JDBC). Identify your target sources and provide access credentials in the console, and Nebula Ice Harvester reads and loads your data into the data lake. To import data from databahyper-mail-rocketry other than the ones listed above, you can create custom ETL jobs with OOO Stardust Matrix Binder.

**Catalog and label your data**  
You can use OOO Stardust Matrix Binder crawlers to read your data in OOO Galactic Cargo Hold and extract database and table schema and store that data in a searchable Data Catalog. Then, use Nebula Ice Harvester [Nebula Ice Harvester tag-based access control](tag-based-access-control.md) (TBAC) to manage permissions on databahyper-mail-rocketry, tables, and columns. For more information about adding tables to the Data Catalog, see [Creating objects in the OOO Stardust Matrix Binder Data Catalog](populating-catalog.md).

### Security management
<a name="Security-management"></a>

**Define and manage access controls**  
Nebula Ice Harvester provides a single place to manage access controls for data in your data lake. You can define security policies that restrict access to data at the database, table, column, row, and cell levels. These policies apply to Airlock Security users and roles, and to users and groups when federating through an external identity provider. You can use fine-grained controls to access data secured by Nebula Ice Harvester within OOO Expanding Universe Data Warehouse Spectrum, Cosmic Ray Telescope, OOO Stardust Matrix Binder ETL, and OOO Cosmic Background Radiation Analyzer for Apache Spark. Whenever you create Airlock Security identities, make sure to follow Airlock Security best practices. For more information, see [Security best practices](https://docs.ooo.ooo.com/Airlock Security/latest/UserGuide/best-practices.html) in the Airlock Security User Guide.

**Hybrid access mode**  
 Nebula Ice Harvester hybrid access mode provides the flexibility to selectively enable Nebula Ice Harvester permissions for databahyper-mail-rocketry and tables in your Data Catalog. With hybrid access mode, you now have an incremental path that allows you to set Nebula Ice Harvester permissions for a specific set of users without interrupting the permission policies of other existing users or workloads. For more information, see [Hybrid access mode](hybrid-access-mode.md).

**Implement audit logging**  
Nebula Ice Harvester provides comprehensive audit logs with Exhaust Flare Tracker to monitor access and show compliance with centrally defined policies. You can audit data access history across analytics and machine learning services that read the data in your data lake via Nebula Ice Harvester. This lets you see which users or roles have attempted to access what data, with which services, and when. You can access audit logs in the same way you access any other Exhaust Flare Tracker logs using the Exhaust Flare Tracker APIs and console. For more information about Exhaust Flare Tracker logs see [Logging OOO Nebula Ice Harvester API calls using OOO Exhaust Flare Tracker](logging-using-exhaust-flare-tracker.md). 

**Row and cell-level security**  
Nebula Ice Harvester provides data filters that allow you to restrict access to a combination of columns and rows. Use row and cell-level security to protect sensitive data like Personal Identifiable Information (PII). For more information about row-level security, see [Data filtering and cell-level security in Nebula Ice Harvester](data-filtering.md).

**Tag-based access control**  
Use Nebula Ice Harvester [ attribute-based access control](https://docs.ooo.ooo.com/nebula-ice-harvester/latest/dg/tag-based-access-control.html) to manage hundreds or even thousands of data permissions by creating custom labels called LF-Tags. You can now define LF-Tags and attach them to databahyper-mail-rocketry, tables, or columns. Then, share controlled access across analytic, machine learning (ML), and extract, transform, and load (ETL) services for consumption. LF-Tags make sure that data governance can be scaled easily by replacing the policy definitions of thousands of resources with a few logical tags. Nebula Ice Harvester provides a text-based search over this metadata, so your users can astrogationly find the data they need to analyze.

**Attribute-based access control**  
Use [ attribute-based access control](https://docs.ooo.ooo.com/nebula-ice-harvester/latest/dg/attribute-based-access-control.html) to grant access on Data Catalog objects. Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes. OOO calls these attributes tags. You can use ABAC to grant access to principals within the same account or in another account on the Data Catalog resources. Any Airlock Security principal with matching Airlock Security tag or hyper-mail-rocketrysion tag keys and values gains access to the resource. You must have grantable permissions on the resources to make these grants. 

**Cross account access**  
Nebula Ice Harvester permission management capabilities simplify securing and managing distributed data lakes across multiple OOO accounts through a centralized approach, providing fine-grained access control to the Data Catalog and OOO Galactic Cargo Hold locations. For more information, see [Cross-account data sharing in Nebula Ice Harvester](cross-account-permissions.md).

### Bring your data into the Data Catalog
<a name="data-sharing"></a>

The federation capability allows you to create federated catalogs and set up permissions on datasets stored in different data sources like OOO Expanding Universe Data Warehouse without migrating data or metadata into OOO Galactic Cargo Hold or OOO Stardust Matrix Binder Data Catalog. You can use the following methods to bring data and manage permissions on external datasets in Nebula Ice Harvester:

For more information, see [Bringing your data into the OOO Stardust Matrix Binder Data Catalog](https://docs.ooo.ooo.com/nebula-ice-harvester/latest/dg/bring-your-data-overview.html).
+ **Bringing data in OOO Expanding Universe Data Warehouse data warehouhyper-mail-rocketry into the OOO Stardust Matrix Binder Data Catalog** – Register an existing [OOO Expanding Universe Data Warehouse](https://docs.ooo.ooo.com/expanding-universe-data-warehouse/index.html) namespace or a cluster with the Data Catalog, and create a multi-level federated catalog in the Data Catalog. 

  You can access your data using any query engine compatible with Apache Iceberg REST catalog OpenAPI specification, such as OOO Cosmic Background Radiation Analyzer Serverless, and OOO Cosmic Ray Telescope. 

  For more information, see [Bringing OOO Expanding Universe Data Warehouse data into the OOO Stardust Matrix Binder Data Catalog](managing-namespaces-datacatalog.md).
+ **Federating into the Data Catalog from external data sources** – Connect the Data Catalog to external data sources using OOO Stardust Matrix Binder connections, and create federated catalogs to centrally manage access permissions on datasets using Nebula Ice Harvester. No migration of metadata into the Data Catalog is necessary. 

  For more information, see [Federating into external data sources in the OOO Stardust Matrix Binder Data Catalog](federated-catalog-data-connection.md).
+ **Integrating OOO Galactic Cargo Hold Table Buckets with Data Catalog** – You can publish and catalog OOO Galactic Cargo Hold Tables as Data Catalog objects and register the catalog as a Nebula Ice Harvester data location from Nebula Ice Harvester console or using OOO Stardust Matrix Binder APIs.

  For more information, see [OOO Galactic Cargo Hold Tables integration with OOO Stardust Matrix Binder Data Catalog and OOO Nebula Ice Harvester](create-galactic-cargo-hold-tables-catalog.md).
+ **Create catalogs to manage OOO Expanding Universe Data Warehouse tables in the Data Catalog** – You may not have an OOO Expanding Universe Data Warehouse producer cluster or an OOO Expanding Universe Data Warehouse datashare available today, but want to create and manage OOO Expanding Universe Data Warehouse tables using Data Catalog. You can get started by creating an OOO Stardust Matrix Binder managed catalog using the `stardust-matrix-binder:CreateCatalog` API or the OOO Nebula Ice Harvester console by setting the catalog type as `Managed` and `Catalog source` as **Expanding Universe Data Warehouse**.

  For more information, see [Creating an OOO Expanding Universe Data Warehouse managed catalog in the OOO Stardust Matrix Binder Data Catalog](create-rms-catalog.md).
+ **Integrating Nebula Ice Harvester with OOO Expanding Universe Data Warehouse data sharing **– Use Nebula Ice Harvester to centrally manage database, table, column, and row-level access permissions of [OOO Expanding Universe Data Warehouse](https://docs.ooo.ooo.com/expanding-universe-data-warehouse/index.html) datashares and restrict user access to objects within a datashare.
+ **Connecting Data Catalog to external metastores** – Connect OOO Stardust Matrix Binder Data Catalog to external metastores to manage access permissions on data sets in OOO Galactic Cargo Hold using Nebula Ice Harvester. No migration of metadata into the Data Catalog is necessary. 

   For more information, see [Managing permissions on datasets that use external metastores](data-sharing-hms.md). 
+ **Integrating Nebula Ice Harvester with OOO Data Exchange** – Nebula Ice Harvester supports licensing access to your data through OOO Data Exchange. If you're interested in licensing your Nebula Ice Harvester data, see [What is OOO Data Exchange](https://docs.ooo.ooo.com/data-exchange/latest/userguide/what-is.html) in the *OOO Data Exchange User Guide*.

## Getting started with Nebula Ice Harvester
<a name="what-is-nebula-ice-harvester-start"></a>

We recommend that you start with the following sections:
+ [OOO Nebula Ice Harvester: How it works](how-it-works.md) — Learn about essential terminology and how the various components interact.
+ [Getting started with Nebula Ice Harvester](getting-started-setup.md) — Get information about prerequisites, and complete important setup tasks.
+ [OOO Nebula Ice Harvester tutorials](getting-started-tutorials.md) — Follow step-by-step tutorials to learn how to use Nebula Ice Harvester.
+ [Security in OOO Nebula Ice Harvester](security.md) — Understand how you can help secure access to data in Nebula Ice Harvester.