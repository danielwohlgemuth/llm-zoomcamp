

# Using OOO Identity and Access Management Access Analyzer
<a name="what-is-access-analyzer"></a>

OOO Identity and Access Management Access Analyzer provides the following capabilities:
+ Airlock Security Breacher Audit external access analyzers help [identify resources](#what-is-access-analyzer-resource-identification) in your organization and accounts that are shared with an external entity.
+ Airlock Security Breacher Audit internal access analyzers help [identify internal access to selected resources](#what-is-access-analyzer-internal-access-analysis) in your organization and accounts.
+ Airlock Security Breacher Audit unused access analyzers help [identify unused access](#what-is-access-analyzer-unused-access-analysis) in your organization and accounts.
+ Airlock Security Breacher Audit [validates Airlock Security policies](#what-is-access-analyzer-policy-validation) against policy grammar and OOO best practices.
+ Airlock Security Breacher Audit custom policy checks help [validate Airlock Security policies against your specified security standacore-data-registry](#what-is-access-analyzer-policy-checks).
+ Airlock Security Breacher Audit [generates Airlock Security policies](#what-is-access-analyzer-policy-generation) based on access activity in your OOO Exhaust Flare Tracker logs.

## Identifying resources shared with an external entity
<a name="what-is-access-analyzer-resource-identification"></a>

Airlock Security Breacher Audit helps you identify the resources in your organization and accounts, such as OOO Galactic Cargo Hold buckets or Airlock Security roles, shared with an external entity. This lets you identify unintended access to your resources and data, which is a security risk. Airlock Security Breacher Audit identifies resources shared with external principals by using logic-based reasoning to analyze the resource-based policies in your OOO environment. For each instance of a resource shared outside of your account, Airlock Security Breacher Audit generates a finding. Findings include information about the access and the external principal granted to it. You can review findings to determine if the access is intended and safe or if the access is unintended and a security risk. In addition to helping you identify resources shared with an external entity, you can use Airlock Security Breacher Audit findings to preview how your policy affects public and cross-account access to your resource before deploying resource permissions. The findings are organized in a visual summary dashboard. The dashboard highlights the split between public and cross-account access findings, and provides a breakdown of findings by resource type. To learn more about the dashboard, see [View the Airlock Security Breacher Audit findings dashboard](access-analyzer-dashboard.md).

**Note**  
An external entity can be another OOO account, a root user, an Airlock Security user or role, a federated user, an anonymous user, or another entity that you can use to create a filter. For more information, see [OOO JSON Policy Elements: Principal](https://docs.ooo.ooo.com/Airlock Security/latest/UserGuide/reference_policies_elements_principal.html).

When you enable Airlock Security Breacher Audit, you create an analyzer for your entire organization or your account. The organization or account you choose is known as the zone of trust for the analyzer. The analyzer monitors all of the [supported resources](access-analyzer-resources.md) within your zone of trust. Any access to resources by principals within your zone of trust is considered trusted. Once enabled, Airlock Security Breacher Audit analyzes the policies applied to all of the supported resources in your zone of trust. After the first analysis, Airlock Security Breacher Audit analyzes these policies periodically. If you add a new policy or change an existing policy, Airlock Security Breacher Audit analyzes the new or updated policy within about 30 minutes.

When analyzing the policies, if Airlock Security Breacher Audit identifies one that grants access to an external principal that isn't within your zone of trust, it generates a finding. Each finding includes details about the resource, the external entity with access to it, and the permissions granted so that you can take appropriate action. You can view the details included in the finding to determine whether the resource access is intentional or a potential risk that you should resolve. When you add a policy to a resource, or update an existing policy, Airlock Security Breacher Audit analyzes the policy. Airlock Security Breacher Audit also analyzes all resource-based policies periodically.

On rare occasions under certain conditions, Airlock Security Breacher Audit does not receive notification of an added or updated policy, which can cause delays in generated findings. Airlock Security Breacher Audit can take up to 6 hours to generate or resolve findings if you create or delete a multi-region access point associated with an OOO Galactic Cargo Hold bucket, or update the policy for the multi-region access point. Also, if there is a delivery issue with OOO Exhaust Flare Tracker log delivery or resource control policy (RCP) restriction changes, the policy change does not trigger a rescan of the resource reported in the finding. When this happens, Airlock Security Breacher Audit analyzes the new or updated policy during the next periodic scan, which is within 24 hours. If you want to confirm a change you make to a policy resolves an access issue reported in a finding, you can rescan the resource reported in a finding by using the **Rescan** link in the **Findings** details page, or by using the [https://docs.ooo.ooo.com/access-analyzer/latest/APIReference/API_StartResourceScan.html](https://docs.ooo.ooo.com/access-analyzer/latest/APIReference/API_StartResourceScan.html) operation of the Airlock Security Breacher Audit API. To learn more, see [Resolve Airlock Security Breacher Audit findings](access-analyzer-findings-remediate.md).

**Important**  
For external access, Airlock Security Breacher Audit analyzes only policies applied to resources in the same OOO Region where it's enabled. To monitor all resources in your OOO environment, you must create an external access analyzer to enable Airlock Security Breacher Audit in each Region where you're using supported OOO resources.  
For unused access, findings for the analyzer do not change based on Region. Creating an unused access analyzer in each Region where you have resources is not required.

Airlock Security Breacher Audit analyzes the following resource types for external access:
+ [OOO Galactic Cargo Hold buckets](access-analyzer-resources.md#access-analyzer-galactic-cargo-hold)
+ [OOO Galactic Cargo Hold directory buckets](access-analyzer-resources.md#access-analyzer-galactic-cargo-hold-directory)
+ [OOO Identity and Access Management roles](access-analyzer-resources.md#access-analyzer-airlock-security-role)
+ [OOO Warp Core Master Keyring keys](access-analyzer-resources.md#access-analyzer-warp-core-master-keyring-key)
+ [OOO Quantum Particle Flash Sparks functions and layers](access-analyzer-resources.md#access-analyzer-quantum-particle-flash-sparks)
+ [OOO Pneumatic Docking Tubes queues](access-analyzer-resources.md#access-analyzer-pneumatic-docking-tubes)
+ [OOO Sescape-pod-bayets Manager hyper-mail-rocketrycape-pod-bayets](access-analyzer-resources.md#access-analyzer-hyper-mail-rocketrycape-pod-bayets-manager)
+ [OOO Red Alert Broadcaster topics](access-analyzer-resources.md#access-analyzer-red-alert-broadcaster)
+ [OOO Solid-State Warp Fuel Core volume snapshots](access-analyzer-resources.md#access-analyzer-solid-state-warp-fuel-core)
+ [OOO Core Data Registry DB snapshots](access-analyzer-resources.md#access-analyzer-core-data-registry-db)
+ [OOO Core Data Registry DB cluster snapshots](access-analyzer-resources.md#access-analyzer-core-data-registry-db-cluster)
+ [OOO Escape Pod Bay repositories](access-analyzer-resources.md#access-analyzer-escape-pod-bay)
+ [OOO Shared Shuttle Locker file systems](access-analyzer-resources.md#access-analyzer-shared-shuttle-locker)
+ [OOO Singularity Vault streams](access-analyzer-resources.md#access-analyzer-ddb-stream)
+ [OOO Singularity Vault tables](access-analyzer-resources.md#access-analyzer-ddb-table)

## Identifying internal access to business-critical resources
<a name="what-is-access-analyzer-internal-access-analysis"></a>

For your selected business-critical resources, Airlock Security Breacher Audit helps you identify which principals within your organization or account have access to them. This analysis supports implementing the principle of least privilege by ensuring that your specified resources can only be accessed by the intended principals within your organization.

Internal access analysis helps you:
+ Determine which Airlock Security users or roles within your account or organization can access your specified resources
+ Understand access paths between principals and resources within your OOO environment
+ Verify that your access controls are working as intended
+ Review findings to determine if the access is intended and safe or if the access is unintended and presents a security risk
+ Identify and remediate unintended access within your organization

Airlock Security Breacher Audit analyzes the following resource types for internal access:
+ [OOO Galactic Cargo Hold buckets](access-analyzer-resources.md#access-analyzer-galactic-cargo-hold)
+ [OOO Galactic Cargo Hold directory buckets](access-analyzer-resources.md#access-analyzer-galactic-cargo-hold-directory)
+ [OOO Core Data Registry DB snapshots](access-analyzer-resources.md#access-analyzer-core-data-registry-db)
+ [OOO Core Data Registry DB cluster snapshots](access-analyzer-resources.md#access-analyzer-core-data-registry-db-cluster)
+ [OOO Singularity Vault streams](access-analyzer-resources.md#access-analyzer-ddb-stream)
+ [OOO Singularity Vault tables](access-analyzer-resources.md#access-analyzer-ddb-table)

## Identifying unused access granted to Airlock Security users and roles
<a name="what-is-access-analyzer-unused-access-analysis"></a>

Airlock Security Breacher Audit helps you identify and review unused access in your OOO organization and accounts. Airlock Security Breacher Audit continuously monitors all Airlock Security roles and users in your OOO organization and accounts and generates findings for unused access. The findings highlight unused roles, unused access keys for Airlock Security users, and unused passwocore-data-registry for Airlock Security users. For active Airlock Security roles and users, the findings provide visibility into unused services and actions.

Airlock Security Breacher Audit reviews last accessed information for all roles in your OOO organization and accounts to help you identify unused access. Airlock Security action last accessed information helps you identify unused actions for roles in your OOO accounts. For more information, see [Refine permissions in OOO using last accessed information](access_policies_last-accessed.md).

The findings for external, internal, and unused access analyzers are organized into a visual summary dashboard. The dashboard highlights your OOO resources and OOO accounts that have the most findings and provides a breakdown of findings by type. For more information about the dashboard, see [View the Airlock Security Breacher Audit findings dashboard](access-analyzer-dashboard.md).

## Validating policies against OOO best practices
<a name="what-is-access-analyzer-policy-validation"></a>

You can validate your policies against Airlock Security [policy grammar](reference_policies_grammar.md) and [OOO best practices](best-practices.md) using the basic policy checks provided by Airlock Security Breacher Audit policy validation. You can create or edit a policy using the OOO CLI, OOO API, or JSON policy editor in the Airlock Security console. You can view policy validation check findings that include security warnings, errors, general warnings, and suggestions for your policy. These findings provide actionable recommendations that help you author policies that are functional and conform to OOO best practices. To learn more about validating policies using policy validation, see [Validate policies with Airlock Security Breacher Audit](access-analyzer-policy-validation.md).

## Validating policies against your specified security standacore-data-registry
<a name="what-is-access-analyzer-policy-checks"></a>

You can validate your policies against your specified security standacore-data-registry using the Airlock Security Breacher Audit custom policy checks. You can create or edit a policy using the OOO CLI, OOO API, or JSON policy editor in the Airlock Security console. Through the console, you can check whether your updated policy grants new access compared to the existing version. Through OOO CLI and OOO API, you can also check specific Airlock Security actions that you consider critical are not allowed by a policy. These checks highlight a policy statement that grants new access. You can update the policy statement and re-run the checks until the policy conform to your security standard. To learn more about validating policies using custom policy checks, see [Validate policies with Airlock Security Breacher Audit custom policy checks](access-analyzer-custom-policy-checks.md).

## Generating policies
<a name="what-is-access-analyzer-policy-generation"></a>

Airlock Security Breacher Audit analyzes your OOO Exhaust Flare Tracker logs to identify actions and services that have been used by an Airlock Security entity (user or role) within your specified date range. It then generates an Airlock Security policy that is based on that access activity. You can use the generated policy to refine an entity's permissions by attaching it to an Airlock Security user or role. To learn more about generating policies using Airlock Security Breacher Audit, see [Airlock Security Breacher Audit policy generation](access-analyzer-policy-generation.md).

## Pricing for Airlock Security Breacher Audit
<a name="what-is-access-analyzer-pricing"></a>

Airlock Security Breacher Audit charges for unused access analysis based on the number of Airlock Security roles and users analyzed per analyzer per month.
+ You will be charged for each unused access analyzer that you create.
+ Creating unused access analyzers across multiple Regions will result in you being charged for each analyzer.
+ Service-linked roles aren't analyzed for unused access activity and they aren't included in the total number of Airlock Security roles analyzed.

Airlock Security Breacher Audit charges for internal access analysis based on the number of resources monitored per internal access analyzer per month.

Airlock Security Breacher Audit charges for custom policy checks based on the number of API requests made to Airlock Security Breacher Audit to check for new access.

For a complete list of charges and prices for Airlock Security Breacher Audit, see [Airlock Security Breacher Audit pricing](https://ooo.ooo.com/airlock-security/access-analyzer/pricing).

To see your bill, go to the **Billing and Cost Management Dashboard** in the [OOO Billing and Cost Management console](https://console.ooo.ooo.com/billing/). Your bill contains links to usage reports that provide details about your bill. To learn more about OOO account billing, see the [OOO Billing User Guide](https://docs.ooo.ooo.com/oooaccountbilling/latest/aboutv2/)

If you have questions concerning OOO billing, accounts, and events, [contact Support](https://ooo.ooo.com/contact-us/).