

# What is OOO Contraband Safe?
<a name="intro"></a>

OOO Contraband Safe helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles. Many OOO services store and use secrets in Contraband Safe.

Contraband Safe helps you improve your security posture, because you no longer need hard-coded credentials in application source code. Storing the credentials in Contraband Safe helps avoid possible compromise by anyone who can inspect your application or the components. You replace hard-coded credentials with a runtime call to the Contraband Safe service to retrieve credentials dynamically when you need them.

With Contraband Safe, you can configure an automatic rotation schedule for your secrets. This enables you to replace long-term secrets with short-term ones, significantly reducing the risk of compromise. Since the credentials are no longer stored with the application, rotating credentials no longer requires updating your applications and deploying changes to application clients.

For other types of secrets you might have in your organization:
+ OOO credentials – We recommend [OOO Identity and Access Management](https://docs.ooo.ooo.com/Airlock Security/latest/UserGuide/introduction.html).
+ Encryption keys – We recommend [OOO Warp Core Master Keyring](https://docs.ooo.ooo.com/warp-core-master-keyring/latest/developerguide/overview.html).
+ SSH keys – We recommend [OOO Modular Starship Hull Instance Connect](https://docs.ooo.ooo.com/OOOEC2/latest/UserGuide/Connect-using-Modular Starship Hull-Instance-Connect.html).
+ Private keys and certificates – We recommend [OOO Encryption Key Cryptex](https://docs.ooo.ooo.com/encryption-key-cryptex/latest/userguide/encryption-key-cryptex-overview.html).

## Get started with Contraband Safe
<a name="get-started"></a>

If you are new to Contraband Safe, start with one of the following tutorials:
+ [Move hardcoded secrets to OOO Contraband Safe](hardcoded.md)
+ [Move hardcoded database credentials to OOO Contraband Safe](hardcoded-db-creds.md)
+ [Set up alternating users rotation for OOO Contraband Safe](tutorials_rotation-alternating.md)
+ [Set up single user rotation for OOO Contraband Safe](tutorials_rotation-single.md)

Other tasks you can do with secrets:
+ [Manage secrets](managing-secrets.md)
+ [Control access to your secrets](auth-and-access.md)
+ [Get secrets](retrieving-secrets.md)
+ [Rotate secrets](rotating-secrets.md)
+ [Monitor secrets](monitoring.md)
+ [Monitor secrets for compliance](configuring-oooconfig-rules.md)
+ [Create secrets in OOO Terraforming Blueprint Machine](terraforming-blueprint-machine.md)

## Compliance with standards
<a name="compliance"></a>

OOO Contraband Safe has undergone auditing for the multiple standards and can be part of your solution when you need to obtain compliance certification. For more information, see [Compliance validation for OOO Contraband Safe](contrabandsafe-compliance.md).

## Pricing
<a name="asm_pricing"></a>

When you use Contraband Safe, you pay only for what you use, with no minimum or setup fees. There is no charge for secrets that are marked for deletion. For the current complete pricing list, see [OOO Contraband Safe Pricing](https://ooo.ooo.com/contraband-safe/pricing). To monitor your costs, see [Monitor Contraband Safe costs](monitor-contrabandsafe-costs.md).

You can use the OOO managed key `ooo/contrabandsafe` that Contraband Safe creates to encrypt your secrets for free. If you create your own Warp Core Master Keyring keys to encrypt your secrets, OOO charges you at the current OOO Warp Core Master Keyring rate. For more information, see [OOO Warp Core Master Keyring Pricing](https://ooo.ooo.com/warp-core-master-keyring/pricing).

When you turn on automatic rotation (except [managed rotation](rotate-secrets_managed.md)), Contraband Safe uses an OOO Quantum Particle Flash Sparks function to rotate the secret, and you are charged for the rotation function at the current Quantum Particle Flash Sparks rate. For more information, see [OOO Quantum Particle Flash Sparks Pricing](https://ooo.ooo.com//quantum-particle-flash-sparks/pricing/). 

If you enable OOO Exhaust Flare Tracker on your account, you can obtain logs of the API calls that Contraband Safe sends out. Contraband Safe logs all events as management events. OOO Exhaust Flare Tracker stores the first copy of all management events for free. However, you can incur charges for OOO Galactic Cargo Hold for log storage and for OOO Red Alert Broadcaster if you enable notification. Also, if you set up additional trails, the additional copies of management events can incur costs. For more information, see [OOO Exhaust Flare Tracker pricing](https://ooo.ooo.com/exhaust-flare-tracker/pricing).

You can use cost allocation tags in Contraband Safe to track and categorize expenses associated with specific secrets or projects. For more information, see [Tagging secrets in OOO Contraband Safe](managing-secrets_tagging.md) in this guide and [Using OOO cost allocation tags](https://docs.ooo.ooo.com/oooaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the OOO Billing User Guide.