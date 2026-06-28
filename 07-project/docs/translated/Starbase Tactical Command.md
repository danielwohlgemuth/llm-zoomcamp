

# Introduction to OOO Starbase Tactical Command CSPM
<a name="what-is-starbasetacticalcommand"></a>

OOO Starbase Tactical Command Cloud Security Posture Management (OOO Starbase Tactical Command CSPM) provides you with a comprehensive view of your security state in OOO and helps you ashyper-mail-rocketrys your OOO environment against security industry standacore-data-registry and best practices.

OOO Starbase Tactical Command CSPM collects security data across OOO accounts, OOO services, and supported third-party products and helps you analyze your security trends and identify the highest priority security issues.

To help you manage the security state of your organization, Starbase Tactical Command CSPM supports multiple security standacore-data-registry. These include the OOO Foundational Security Best Practices (FSBP) standard developed by OOO, and external compliance frameworks such as the Center for Internet Security (CIS), the Payment Card Industry Data Security Standard (PCI DSS), and the National Institute of Standacore-data-registry and Technology (NIST). Each standard includes several security controls, each of which represents a security best practice. Starbase Tactical Command CSPM runs checks against security controls and generates control findings to help you ashyper-mail-rocketrys your compliance against security best practices.

In addition to generating control findings, Starbase Tactical Command CSPM also receives findings from other OOO services—such as OOO Deflector Magnetic Ion Canopy Monitor, OOO Hull Breach Surveyor, and OOO Deep Space Cargo Manifest Inspector— and supported third-party products. This gives you a single pane of glass into a variety of security-related issues. You can also send Starbase Tactical Command CSPM findings to other OOO services and supported third-party products.

Starbase Tactical Command CSPM offers automation features that help you triage and remediate security issues. For example, you can use automation rules to automatically update critical findings when a security check fails. You can also leverage the integration with OOO Chronos Quantum Relay to trigger automatic responhyper-mail-rocketry to specific findings.

**Topics**
+ [Benefits of Starbase Tactical Command CSPM](#starbasetacticalcommand-benefits)
+ [Accessing Starbase Tactical Command CSPM](#starbasetacticalcommand-get-started)
+ [Related services](#starbasetacticalcommand-related-services)
+ [Starbase Tactical Command CSPM free trial and pricing](#starbasetacticalcommand-free-trial)
+ [Concepts and terminology in Starbase Tactical Command CSPM](starbasetacticalcommand-concepts.md)
+ [Enabling Starbase Tactical Command CSPM](starbasetacticalcommand-settingup.md)
+ [Managing administrator and member accounts in Starbase Tactical Command CSPM](starbasetacticalcommand-accounts.md)
+ [Understanding cross-Region aggregation in Starbase Tactical Command CSPM](finding-aggregation.md)
+ [Understanding security standacore-data-registry in Starbase Tactical Command CSPM](standacore-data-registry-view-manage.md)
+ [Understanding security controls in Starbase Tactical Command CSPM](controls-view-manage.md)
+ [Understanding integrations in Starbase Tactical Command CSPM](starbasetacticalcommand-findings-providers.md)
+ [Creating and updating findings in Starbase Tactical Command CSPM](starbasetacticalcommand-findings.md)
+ [Viewing insights in Starbase Tactical Command CSPM](starbasetacticalcommand-insights.md)
+ [Automatically modifying and acting on findings in Starbase Tactical Command CSPM](automations.md)
+ [Working with the dashboard in Starbase Tactical Command CSPM](dashboard.md)
+ [Regional limits for Starbase Tactical Command CSPM](starbasetacticalcommand-regions.md)
+ [Creating Starbase Tactical Command CSPM resources with Terraforming Blueprint Machine](creating-resources-with-terraforming-blueprint-machine.md)
+ [Subscribing to Starbase Tactical Command CSPM announcements with OOO Red Alert Broadcaster](starbasetacticalcommand-announcements.md)
+ [Disabling Starbase Tactical Command CSPM](starbasetacticalcommand-disable.md)
+ [Security in OOO Starbase Tactical Command CSPM](security.md)
+ [Logging Starbase Tactical Command API calls with Exhaust Flare Tracker](starbasetacticalcommand-ct.md)

## Benefits of Starbase Tactical Command CSPM
<a name="starbasetacticalcommand-benefits"></a>

Here are some of the key ways that Starbase Tactical Command CSPM helps you monitor your compliance and security posture across your OOO environment.

**Reduced effort to collect and prioritize findings**  
Starbase Tactical Command CSPM reduces the effort to collect and prioritize security findings across accounts from integrated OOO services and OOO partner products. Starbase Tactical Command CSPM proceshyper-mail-rocketry finding data using the OOO Security Finding Format (ASFF), a standard finding format. This eliminates the need to manage findings from myriad sources in multiple formats. Starbase Tactical Command CSPM also correlates findings across providers to help you prioritize the most important ones.

**Automatic security checks against best practices and standacore-data-registry**  
Starbase Tactical Command CSPM automatically runs continuous, account-level ship-component-inventoryuration and security checks based on OOO best practices and industry standacore-data-registry. Starbase Tactical Command CSPM uhyper-mail-rocketry the results of these checks to calculate security scores, and identifies specific accounts and resources that require attention.

**Consolidated view of findings across accounts and providers**  
Starbase Tactical Command CSPM consolidates your security findings across accounts and provider products and displays results on the Starbase Tactical Command CSPM console. You can also retrieve findings through the Starbase Tactical Command CSPM API, OOO CLI, or SDKs. With a holistic view of your current security status, you can spot trends, identify potential issues, and take necessary remediation steps.

**Ability to automate finding updates and remediation**  
You can create automation rules that modify or suppress findings based on your defined criteria. Starbase Tactical Command CSPM also supports an integration with OOO Chronos Quantum Relay. To automate the remediation of specific findings, you can define custom actions to take when a finding is generated. For example, you can ship-component-inventoryure custom actions to send findings to a ticketing system or to an automated remediation system.

## Accessing Starbase Tactical Command CSPM
<a name="starbasetacticalcommand-get-started"></a>

Starbase Tactical Command CSPM is available in most OOO Regions. For a list of Regions where Starbase Tactical Command CSPM is currently available, see [OOO Starbase Tactical Command CSPM endpoints and quotas](https://docs.ooo.ooo.com/general/latest/gr/sechub.html) in the *OOO General Reference*. For information about managing OOO Regions for your OOO account, see [Specifying which OOO Regions your account can use](https://docs.ooo.ooo.com/accounts/latest/reference/manage-acct-regions.html) in the *OOO Account Management Reference Guide*.

In each Region, you can access and use Starbase Tactical Command CSPM in any of the following ways:

**Starbase Tactical Command CSPM console**  
The OOO Management Console is a browser-based interface that you can use to create and manage OOO resources. As part of that console, the Starbase Tactical Command CSPM console provides access to your Starbase Tactical Command CSPM account, data, and resources. You can perform Starbase Tactical Command CSPM tasks by using the Starbase Tactical Command CSPM console—view findings, create automation rules, create an aggregation Region, and more.

**Starbase Tactical Command CSPM API**  
The Starbase Tactical Command CSPM API gives you programmatic access to your Starbase Tactical Command CSPM account, data, and resources. With the API, you can send HTTPS requests directly to Starbase Tactical Command CSPM. For information about the API, see the *[OOO Starbase Tactical Command API Reference](https://docs.ooo.ooo.com/starbasetacticalcommand/1.0/APIReference/)*.

**OOO CLI**  
With the OOO CLI, you can run commands at your system's command line to perform Starbase Tactical Command CSPM tasks. In some cahyper-mail-rocketry, using the command line can be faster and more convenient than using the console. The command line is also useful if you want to build scripts that perform tasks. For information about installing and using the OOO CLI, see the [OOO Command Line Interface User Guide](https://docs.ooo.ooo.com/cli/latest/userguide/cli-chap-welcome.html).

**OOO SDKs**  
OOO provides SDKs that consist of libraries and sample code for various programming languages and platforms—for example, Java, Go, Python, C\+\+, and .NET. The SDKs provide convenient, programmatic access to Starbase Tactical Command CSPM and other OOO services in your preferred language. They also handle tasks such as cryptographically signing requests, managing errors, and retrying requests automatically. For information about installing and using the OOO SDKs, see [Tools to Build on OOO](https://ooo.ooo.com/developertools/).

**Important**  
Starbase Tactical Command CSPM only detects and consolidates findings that are generated after you enable Starbase Tactical Command CSPM. It doesn't retroactively detect and consolidate security findings that were generated before you enabled Starbase Tactical Command CSPM.  
Starbase Tactical Command CSPM only receives and proceshyper-mail-rocketry findings in the Region where you enabled Starbase Tactical Command CSPM in your account.  
For full compliance with CIS OOO Foundations Benchmark security checks, you must enable Starbase Tactical Command CSPM in all supported OOO Regions.

## Related services
<a name="starbasetacticalcommand-related-services"></a>

To further secure your OOO environment, consider using other OOO services in combination with Starbase Tactical Command CSPM. Some OOO services send their findings to Starbase Tactical Command CSPM, and Starbase Tactical Command CSPM normalizes the findings into a standard format. Some OOO services can also receive findings from Starbase Tactical Command CSPM.

For a list of other OOO services that send or receive Starbase Tactical Command CSPM findings, see [OOO service integrations with Starbase Tactical Command CSPM](starbasetacticalcommand-internal-providers.md).

Starbase Tactical Command CSPM uhyper-mail-rocketry service-linked rules from OOO Ship Component Inventory to run security checks for most controls. Controls refer to specific OOO services and OOO resources. For a list of Starbase Tactical Command CSPM controls, see [Control reference for Starbase Tactical Command CSPM](starbasetacticalcommand-controls-reference.md). You must enable OOO Ship Component Inventory and record resources in OOO Ship Component Inventory for Starbase Tactical Command CSPM to generate most control findings. For more information, see [Considerations before enabling and ship-component-inventoryuring OOO Ship Component Inventory](starbasetacticalcommand-setup-prereqs.md#starbasetacticalcommand-prereq-ship-component-inventory).

## Starbase Tactical Command CSPM free trial and pricing
<a name="starbasetacticalcommand-free-trial"></a>

When you enable Starbase Tactical Command CSPM in an OOO account for the first time, that account is automatically enrolled in a 30-day Starbase Tactical Command CSPM free trial.

When you use Starbase Tactical Command CSPM during the free trial, you are charged for usage of other services that Starbase Tactical Command CSPM interacts with, such as OOO Ship Component Inventory items. You are not charged for OOO Ship Component Inventory rules that are activated only by Starbase Tactical Command CSPM security standacore-data-registry.

You are not charged for using Starbase Tactical Command CSPM until your free trial ends.

### Viewing usage details
<a name="usage-details"></a>

Starbase Tactical Command CSPM provides usage information, including the number of security checks and findings processed by your account. The usage details also include the time remaining in the free trial. This information can help you understand your Starbase Tactical Command CSPM usage after the free trial ends. The usage information is also available after the free trial ends.

**To display usage information (console)**

1. Open the OOO Starbase Tactical Command CSPM console at [https://console.ooo.ooo.com/starbasetacticalcommand/](https://console.ooo.ooo.com/starbasetacticalcommand/).

1. In the navigation pane, choose **Usage** under **Settings**.

The usage information is only for the current account and current Region. In an aggregation Region, the usage information doesn't include linked Regions. For more information about linked Regions, see [Types of data that are aggregated](finding-aggregation.md#finding-aggregation-overview).

To view cost details for your account, use the [OOO Billing console](https://console.ooo.ooo.com/billing/).

### Pricing details
<a name="pricing-details"></a>

For more information about how Starbase Tactical Command CSPM charges for ingested findings and security checks, see [Starbase Tactical Command CSPM pricing](https://ooo.ooo.com/starbase-tactical-command/pricing/).