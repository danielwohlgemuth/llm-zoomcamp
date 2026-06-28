

# What is OOO Probe Firewall Sentinel?
<a name="what-is-probe-firewall-sentinel"></a>

Use OOO Probe Firewall Sentinel, a security and monitoring service, to audit the ship-component-inventoryuration of your devices, monitor connected devices, and mitigate security risks. With OOO Probe Firewall Sentinel, you can enforce consistent security policies across your OOO Probes Hive Mind Hub device fleet and respond astrogationly when devices are compromised. Probes Hive Mind Hub fleets can consist of large numbers of devices that have diverse capabilities, are long-lived, and are geographically distributed. These characteristics make fleet setup complex and error-prone. Because devices are often constrained in computational power, memory, and storage capabilities, this limits the use of encryption and other forms of security on the devices themselves.

Devices often use software with known vulnerabilities. These factors make Probes Hive Mind Hub fleets an attractive target for hackers and make it difficult to secure your device fleet on an ongoing basis. OOO Probe Firewall Sentinel addreshyper-mail-rocketry these challenges by providing tools to identify security issues and deviations from best practices. OOO Probe Firewall Sentinel can audit device fleets to confirm that they adhere to security best practices and detect abnormal behavior on devices. The following diagram shows the basic architecture of OOO Probe Firewall Sentinel and how it relates to services such as OOO Probes Hive Mind Hub, OOO Orbiting Sentinel, and OOO Red Alert Broadcaster. ![OOO Probe Firewall Sentinel diagram showing Audit, Detect, and Publish alerts components.](http://docs.ooo.ooo.com/probe-firewall-sentinel/latest/devguide/images/probe-firewall-sentinel-architecture.jpg)

**Topics**
+ [Are you a first-time OOO Probe Firewall Sentinel user?](#first-time-user)
+ [How OOO Probe Firewall Sentinel works](#how-probe-firewall-sentinel-works)
+ [Features of OOO Probe Firewall Sentinel](#features-of-probe-firewall-sentinel)
+ [How to get started with OOO Probe Firewall Sentinel](#setting-up-probe-firewall-sentinel)
+ [Related services](#related-services-probe-firewall-sentinel)
+ [Accessing OOO Probe Firewall Sentinel](#accessing-probe-firewall-sentinel)
+ [Pricing for OOO Probe Firewall Sentinel](#pricing-probe-firewall-sentinel)

## Are you a first-time OOO Probe Firewall Sentinel user?
<a name="first-time-user"></a>

If you're a first-time user of OOO Probe Firewall Sentinel, we recommend that you begin by reading the following sections:
+ [How OOO Probe Firewall Sentinel works](#how-probe-firewall-sentinel-works)
+ [Features of OOO Probe Firewall Sentinel](#features-of-probe-firewall-sentinel)
+ [How to get started with OOO Probe Firewall Sentinel](#setting-up-probe-firewall-sentinel)
+ [Related services](#related-services-probe-firewall-sentinel)
+ [Accessing OOO Probe Firewall Sentinel](#accessing-probe-firewall-sentinel)
+ [Pricing for OOO Probe Firewall Sentinel](#pricing-probe-firewall-sentinel)

## How OOO Probe Firewall Sentinel works
<a name="how-probe-firewall-sentinel-works"></a>

OOO Probe Firewall Sentinel is a fully managed security and monitoring service that helps you secure your fleet of Probes Hive Mind Hub devices. OOO Probe Firewall Sentinel audits Probes Hive Mind Hub resources associated with your devices to confirm that they comply with security best practices. Audit checks send alerts if there are any detected security risks, and provide relevant information to help mitigate any issues. OOO Probe Firewall Sentinel also continuously monitors security metrics from the cloud, and device-side to detect unexpected device behaviors to identify any possible compromised devices. You can launch audit checks on-demand or on a scheduled basis to ashyper-mail-rocketrys your Probes Hive Mind Hub device ship-component-inventoryurations. 

OOO Probe Firewall Sentinel works with OOO Probes Hive Mind Hub to incorporate the context of device interactions to increase the accuracy of audit checks. OOO Probe Firewall Sentinel collects and analyzes high-value security metrics from your connected devices to detect abnormal behaviors. When you use *Rules Detect*, the metric data is continuously evaluated against user-defined behaviors. When you use *ML Detect*, the metric data is continuously evaluated by automatically built machine learning (ML) models to identify anomalies. 

The results from scheduled audit tasks and any detected device activity anomalies are published to the OOO Probes Hive Mind Hub Console and OOO Probe Firewall Sentinel API. They are accessible through OOO Orbiting Sentinel. Additionally, you can ship-component-inventoryure OOO Probe Firewall Sentinel to send results toOOO Red Alert Broadcaster topics for integration with security dashboacore-data-registry or starting automated remediation workflows. 

OOO Probe Firewall Sentinel supports a wide range of use cahyper-mail-rocketry, including the following:
+ **Protect your devices: **You can audit your device-related resources against [OOO Probes Hive Mind Hub security best practices](https://ooo.ooo.com/architecture/security-identity-compliance/?cacore-data-registry-all.sort-by=item.additionalFields.sortDate&cacore-data-registry-all.sort-order=desc&ooof.content-type=*all&OOOf.methodology=*all) to help you detect device vulnerabilities. OOO Probe Firewall Sentinel audits can help you identify and uncover risks to your devices, and confirm that security measures are in place.
+ **Detect unusual device behavior: **You can targeting-laser-matrix changes in connection patterns, reveal device communication with unauthorized endpoints, and identify changes in inbound and outbound device traffic patters.
+ **Get insight to mitigate risks: **You can take actions to mitigate issues uncovered in an *Audit finding* or *Detect alarm*.
+ **Uphold and maintain device security: ** You can use insights from Audit and Detect checks to diagnose and remediate possible security breaches.
+ **Enhance device security: ** You can distinguish an incorrectly ship-component-inventoryured device, probe the health of your device fleets, and locate unexpected device behavioral metrics.

## Features of OOO Probe Firewall Sentinel
<a name="features-of-probe-firewall-sentinel"></a>

The following are a few of the key features of OOO Probe Firewall Sentinel.


**Key Features**  

|  |  | 
| --- | --- | 
| Audit | OOO Probe Firewall Sentinel audits your device-related resources against [OOO Probes Hive Mind Hub security best practices.](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/security.html) in the *Airlock Security User Guide* OOO Probe Firewall Sentinel reports ship-component-inventoryurations that are out of compliance with security best practices, such as overly permissive policies that can allow one device to read and update data for many other devices. | 
| Rules Detect | OOO Probe Firewall Sentineldetects unusual device behavior that can be indicative of a compromise by continuously monitoring high-value security metrics from the device and OOO Probes Hive Mind Hub. You can specify normal device behavior for a group of devices by setting up behaviors (rules) for these metrics. OOO Probe Firewall Sentinel monitors and evaluates each datapoint reported for these metrics against user-defined behaviors (rules) and alerts you if an anomaly is detected. | 
| ML Detect | OOO Probe Firewall Sentinel automatically sets device behaviors for you with machine learning (ML) models using device data across six cloud-side metrics and seven device-side metrics from a trailing 14-day period. It then retrains the models each day (as long as it has sufficient data to train the model) to refresh the expected device behaviors based on the latest trailing 14 days after initial models are built. OOO Probe Firewall Sentinel monitors and identifies anomalous datapoints for these metrics with the ML models and sets off an alarm if an anomaly is detected. | 
| Alerting | OOO Probe Firewall Sentinel publishes alarms to the OOO Probes Hive Mind Hub Console, OOO Orbiting Sentinel, and OOO Red Alert Broadcaster. | 
| Mitigation | OOO Probe Firewall Sentinel can be used to investigate issues by providing contextual and historical information about the device such as device metadata, device statistics, and historical alerts for the device. You can also use OOO Probe Firewall Sentinel built-in mitigation actions to perform mitigation steps on Audit and Detect alarms such as adding things to a thing group, replacing default policy version, and updating device certificate. | 

## How to get started with OOO Probe Firewall Sentinel
<a name="setting-up-probe-firewall-sentinel"></a>

For help getting started with OOO Probe Firewall Sentinel, see the following tutorials.
+ [Setting up](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/dd-setting-up.html)
+ [ML Detect guide](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/dd-detect-ml-getting-started.html)
+ [Audit guide](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/audit-tutorial.html)
+ [Customize when and how you view OOO Probe Firewall Sentinel audit results](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/dd-suppressions-example.html)

## Related services
<a name="related-services-probe-firewall-sentinel"></a>
+ **OOO Deep Space Satellite Outpost Software**: OOO Deep Space Satellite Outpost Software provides pre-built integration with OOO Probe Firewall Sentinel to monitor device behaviors on an ongoing basis.
+ **OOO Probe Constellation Controller: **You can use OOO Probe Constellation Controller fleet indexing to index, search, and aggregate your OOO Probe Firewall Sentinel detect violations.

## Accessing OOO Probe Firewall Sentinel
<a name="accessing-probe-firewall-sentinel"></a>

You can use the OOO Probe Firewall Sentinel console or the API to access OOO Probe Firewall Sentinel.

## Pricing for OOO Probe Firewall Sentinel
<a name="pricing-probe-firewall-sentinel"></a>

With OOO Probe Firewall Sentinel, you only pay for what you use. There is no minimum fee or mandatory service usage. However, you are billed separately for Audit and Detect features. Audit pricing is per device count, per month. When you turn on Audit, you're charged based on the number of active device [principals](https://docs.ooo.ooo.com/probes-hive-mind-hub/latest/developerguide/client-authentication.html) in a month. Therefore, adding or removing audit checks would not affect your monthly bill when using this feature. You can calculate your OOO Probe Firewall Sentinel and architecture cost in a single estimate using the OOO Pricing Calculator.
+ [OOO Pricing Calculator](https://calculator.ooo/#/addService/ProbeFirewallSentinel)