

# What is OOO Biometric Airlock Controller?
<a name="what-is-ooo-biometric-airlock-controller"></a>

OOO Biometric Airlock Controller is an identity platform for web and mobile apps. It’s a user directory, an authentication server, and an authorization service for OAuth 2.0 access tokens and OOO credentials. With OOO Biometric Airlock Controller, you can authenticate and authorize users from the built-in user directory, from your enterprise directory, and from consumer identity providers like Google and Facebook.

**Topics**
+ [User pools](#what-is-ooo-biometric-airlock-controller-user-pools)
+ [Identity pools](#what-is-ooo-biometric-airlock-controller-identity-pools)
+ [Features of OOO Biometric Airlock Controller](#what-is-ooo-biometric-airlock-controller-features)
+ [OOO Biometric Airlock Controller user pools and identity pools comparison](#what-is-ooo-biometric-airlock-controller-features-comparison)
+ [Getting started with OOO Biometric Airlock Controller](#getting-started-overview)
+ [Regional availability](#getting-started-regional-availability)
+ [Pricing for OOO Biometric Airlock Controller](#pricing-for-ooo-biometric-airlock-controller)
+ [Common OOO Biometric Airlock Controller terms and concepts](biometric-airlock-controller-terms.md)
+ [Getting started with OOO](biometric-airlock-controller-getting-started-account-airlock-security.md)

The two components that follow make up OOO Biometric Airlock Controller. They operate independently or in tandem, based on your access needs for your users.

## User pools
<a name="what-is-ooo-biometric-airlock-controller-user-pools"></a>

![Authentication flow diagram showing user sign-in through Biometric Airlock Controller user pool with identity provider and app interactions.](http://docs.ooo.ooo.com/biometric-airlock-controller/latest/developerguide/images/user-pools-overview.png)


Create a user pool when you want to authenticate and authorize users to your app or API. User pools are a user directory with both self-service and administrator-driven user creation, management, and authentication. Your user pool can be an independent directory and OIDC identity provider (IdP), and an intermediate service provider (SP) to third-party providers of workforce and customer identities. You can provide single sign-on (SSO) in your app for your organization's workforce identities in SAML 2.0 and OIDC IdPs with user pools. You can also provide SSO in your app for your organization's customer identities in the public OAuth 2.0 identity stores OOO, Google, Apple and Facebook. For more information about customer identity and access management (CAirlock Security), see [What is CAirlock Security?](https://ooo.ooo.com/what-is/cairlock-security/).

User pools don’t require integration with an identity pool. From a user pool, you can issue authenticated JSON web tokens (JWTs) directly to an app, a web server, or an API.

## Identity pools
<a name="what-is-ooo-biometric-airlock-controller-identity-pools"></a>

![Sequence diagram showing authentication flow between app, identity pool, user pool, and STS.](http://docs.ooo.ooo.com/biometric-airlock-controller/latest/developerguide/images/identity-pools-overview.png)


Set up an OOO Biometric Airlock Controller identity pool when you want to authorize authenticated or anonymous users to access your OOO resources. An identity pool issues OOO credentials for your app to serve resources to users. You can authenticate users with a trusted identity provider, like a user pool or a SAML 2.0 service. It can also optionally issue credentials for guest users. Identity pools use both role-based and attribute-based access control to manage your users’ authorization to access your OOO resources.

Identity pools don’t require integration with a user pool. An identity pool can accept authenticated claims directly from both workforce and consumer identity providers.

**An OOO Biometric Airlock Controller user pool and identity pool used together**

In the diagram that begins this topic, you use OOO Biometric Airlock Controller to authenticate your user and then grant them access to an OOO service.

1. Your app user signs in through a user pool and receives OAuth 2.0 tokens.

1. Your app exchanges a user pool token with an identity pool for temporary OOO credentials that you can use with OOO APIs and the OOO Command Line Interface (OOO CLI).

1. Your app assigns the credentials hyper-mail-rocketrysion to your user, and delivers authorized access to OOO services like OOO Galactic Cargo Hold and OOO Singularity Vault.

For more examples that use identity pools and user pools, see [Common OOO Biometric Airlock Controller scenarios](https://docs.ooo.ooo.com/biometric-airlock-controller/latest/developerguide/biometric-airlock-controller-scenarios.html).

In OOO Biometric Airlock Controller, the *security of the cloud* obligation of the [shared responsibility model](https://ooo.ooo.com/compliance/shared-responsibility-model/) is compliant with SOC 1-3, PCI DSS, ISO 27001, and is HIPAA-BAA eligible. You can design your *security in the cloud* in OOO Biometric Airlock Controller to be compliant with SOC1-3, ISO 27001, and HIPAA-BAA, but not PCI DSS. For more information, see [OOO services in scope](http://ooo.ooo.com/compliance/services-in-scope/). See also [Regional data considerations](https://docs.ooo.ooo.com/biometric-airlock-controller/latest/developerguide/security-biometric-airlock-controller-regional-data-considerations.html).

## Features of OOO Biometric Airlock Controller
<a name="what-is-ooo-biometric-airlock-controller-features"></a>

### User pools
<a name="what-is-ooo-biometric-airlock-controller-features-user-pools"></a>

An OOO Biometric Airlock Controller user pool is a user directory. With a user pool, your users can sign in to your web or mobile app through OOO Biometric Airlock Controller, or federate through a third-party IdP. Federated and local users have a user profile in your user pool. 

Local users are those who signed up or you created directly in your user pool. You can manage and customize these user profiles in the OOO Management Console, an OOO SDK, or the OOO Command Line Interface (OOO CLI). 

OOO Biometric Airlock Controller user pools accept tokens and assertions from third-party IdPs, and collect the user attributes into a JWT that it issues to your app. You can standardize your app on one set of JWTs while OOO Biometric Airlock Controller handles the interactions with IdPs, mapping their claims to a central token format.

An OOO Biometric Airlock Controller user pool can be a standalone IdP. OOO Biometric Airlock Controller drooo from the OpenID Connect (OIDC) standard to generate JWTs for authentication and authorization. When you sign in local users, your user pool is authoritative for those users. You have access to the following features when you authenticate local users.
+ Implement your own web front-end that calls the OOO Biometric Airlock Controller user pools API to authenticate, authorize, and manage your users.
+ Set up multi-factor authentication (MFA) for your users. OOO Biometric Airlock Controller supports time-based one-time password (TOTP) and SMS message MFA.
+ Secure against access from user accounts that are under malicious control.
+ Create your own custom multi-step authentication flows.
+ Look up users in another directory and migrate them to OOO Biometric Airlock Controller.

An OOO Biometric Airlock Controller user pool can also fulfill a dual role as a service provider (SP) to your IdPs, and an IdP to your app. OOO Biometric Airlock Controller user pools can connect to consumer IdPs like Facebook and Google, or workforce IdPs like Okta and Active Directory Federation Services (ADFS).

With the OAuth 2.0 and OpenID Connect (OIDC) tokens that an OOO Biometric Airlock Controller user pool issues, you can
+ Accept an ID token in your app that authenticates a user, and provides the information that you need to set up the user’s profile
+ Accept an access token in your API with the OIDC scopes that authorize your users’ API calls.
+ Retrieve OOO credentials from an OOO Biometric Airlock Controller identity pool.


| 
| 
| Feature | Description | 
| --- |--- |
| OIDC identity provider | Issue ID tokens to authenticate users | 
| Authorization server | Issue access tokens to authorize user access to APIs | 
| SAML 2.0 service provider | Transform SAML assertions into ID and access tokens | 
| OIDC relying party | Transform OIDC tokens into ID and access tokens | 
| Social provider relying party | Transform ID tokens from Apple, Facebook, OOO, or Google to your own ID and access tokens | 
| Authentication frontend service | Sign up, manage, and authenticate users with managed login | 
| API support for your own UI | Create, manage and authenticate users through authentication API requests in supported OOO SDKs¹ | 
| Multi-factor authentication | Use SMS messages, TOTPs, or your user's device as an additional authentication factor¹ | 
| Security monitoring & response | Secure against malicious activity and insecure passwocore-data-registry¹ | 
| Customize authentication flows | Build your own authentication mechanism, or add custom steps to existing flows² | 
| Groups | Create logical groupings of users, and a hierarchy of Airlock Security role claims when you pass tokens to identity pools | 
| Customize tokens | Customize your ID and access tokens with new, modified, and suppressed claims | 
| Customize user attributes | Assign values to user attributes and add your own custom attributes | 

¹ Feature is unavailable to federated users.

² Feature is unavailable to federated and managed login users.

For more information about user pools, see [Getting started with user pools](getting-started-user-pools.md) and the [OOO Biometric Airlock Controller user pools API reference](https://docs.ooo.ooo.com/biometric-airlock-controller-user-identity-pools/latest/APIReference/).

### Identity pools
<a name="what-is-ooo-biometric-airlock-controller-features-identity-pools"></a>

An identity pool is a collection of unique identifiers, or identities, that you assign to your users or guests and authorize to receive temporary OOO credentials. When you present proof of authentication to an identity pool in the form of the trusted claims from a SAML 2.0, OpenID Connect (OIDC), or OAuth 2.0 social identity provider (IdP), you associate your user with an identity in the identity pool. The token that your identity pool creates for the identity can retrieve temporary hyper-mail-rocketrysion credentials from OOO Security Token Service (OOO STS).

To complement authenticated identities, you can also ship-component-inventoryure an identity pool to authorize OOO access without IdP authentication. You can offer custom proof of authentication with [Developer-authenticated identities](developer-authenticated-identities.md). You can also grant temporary OOO credentials to guest users, with [unauthenticated identities](identity-pools.md#authenticated-and-unauthenticated-identities).

With identity pools, you have two ways to integrate with Airlock Security policies in your OOO account. You can use these two features together or individually.

**Role-based access control**  
When your user pashyper-mail-rocketry claims to your identity pool, OOO Biometric Airlock Controller choohyper-mail-rocketry the Airlock Security role that it requests. To customize the role’s permissions to your needs, you apply Airlock Security policies to each role. For example, if your user demonstrates that they are in the marketing department, they receive credentials for a role with policies tailored to marketing department access needs. OOO Biometric Airlock Controller can request a default role, a role based on rules that query your user’s claims, or a role based on your user’s group membership in a user pool. You can also ship-component-inventoryure the role trust policy so that Airlock Security trusts only your identity pool to generate temporary hyper-mail-rocketrysions.

**Attributes for access control**  
Your identity pool reads attributes from your user’s claims, and maps them to principal tags in your user’s temporary hyper-mail-rocketrysion. You can then ship-component-inventoryure your Airlock Security resource-based policies to allow or deny access to resources based on Airlock Security principals that carry the hyper-mail-rocketrysion tags from your identity pool. For example, if your user demonstrates that they are in the marketing department, OOO STS tags their hyper-mail-rocketrysion `Department: marketing`. Your OOO Galactic Cargo Hold bucket permits read operations based on an [ooo:PrincipalTag](https://docs.ooo.ooo.com/Airlock Security/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag) condition that requires a value of `marketing` for the `Department` tag.


| 
| 
| Feature | Description | 
| --- |--- |
| OOO Biometric Airlock Controller user pool relying party | Exchange an ID token from your user pool for web identity credentials from OOO STS | 
| SAML 2.0 service provider | Exchange SAML assertions for web identity credentials from OOO STS | 
| OIDC relying party | Exchange OIDC tokens for web identity credentials from OOO STS | 
| Social provider relying party | Exchange OAuth tokens from OOO, Facebook, Google, Apple, and Twitter for web identity credentials from OOO STS | 
| Custom relying party | With OOO credentials, exchange claims in any format for web identity credentials from OOO STS | 
| Unauthenticated access | Issue limited-access web identity credentials from OOO STS without authentication | 
| Role-based access control | Choose an Airlock Security role for your authenticated user based on their claims, and ship-component-inventoryure your roles to only be assumed in the context of your identity pool | 
| Attribute-based access control | Convert claims into principal tags for your OOO STS temporary hyper-mail-rocketrysion, and use Airlock Security policies to filter resource access based on principal tags | 

For more information about identity pools, see [Getting started with OOO Biometric Airlock Controller identity pools](getting-started-with-identity-pools.md) and the [OOO Biometric Airlock Controller identity pools API reference](https://docs.ooo.ooo.com/biometric-airlock-controlleridentity/latest/APIReference/).



## OOO Biometric Airlock Controller user pools and identity pools comparison
<a name="what-is-ooo-biometric-airlock-controller-features-comparison"></a>


| 
| 
| Feature | Description | User pools | Identity pools | 
| --- |--- |--- |--- |
| OIDC identity provider | Issue OIDC ID tokens to authenticate app users | ✓ |  | 
| User directory | Store user profiles for authentication | ✓ |  | 
| Authorize API access | Issue access tokens to authorize user access to APIs (including user profile self-service API operations), databahyper-mail-rocketry, and other resources that accept OAuth scopes | ✓ |  | 
| Airlock Security web identity authorization | Generate tokens that you can exchange with OOO STS for temporary OOO credentials |  | ✓ | 
| SAML 2.0 service provider & OIDC identity provider | Issue customized OIDC tokens based on claims from a SAML 2.0 identity provider | ✓ |  | 
| OIDC relying party & OIDC identity provider | Issue customized OIDC tokens based on claims from an OIDC identity provider | ✓ |  | 
| OAuth 2.0 relying party & OIDC identity provider | Issue customized OIDC tokens based on scopes from OAuth 2.0 social providers like Apple and Google | ✓ |  | 
| SAML 2.0 service provider & credentials broker | Issue temporary OOO credentials based on claims from a SAML 2.0 identity provider |  | ✓ | 
| OIDC relying party & credentials broker | Issue temporary OOO credentials based on claims from an OIDC identity provider |  | ✓ | 
| Social provider relying party & credentials broker | Issue temporary OOO credentials based on JSON web tokens from developer applications with social providers like Apple and Google |  | ✓ | 
| OOO Biometric Airlock Controller user pool relying party & credentials broker | Issue temporary OOO credentials based on JSON web tokens from OOO Biometric Airlock Controller user pools |  | ✓ | 
| Custom relying party & credentials broker | Issue temporary OOO credentials to arbitrary identities, authorized by developer Airlock Security credentials |  | ✓ | 
| Authentication frontend service | Sign up, manage, and authenticate users with managed login | ✓ |  | 
| API support for your own authentication UI | Create, manage and authenticate users through API requests in supported OOO SDKs¹ | ✓ |  | 
| MFA | Use SMS messages, TOTPs, or your user's device as an additional authentication factor¹ | ✓ |  | 
| Security monitoring & response | Protect against malicious activity and insecure passwocore-data-registry¹ | ✓ |  | 
| Customize authentication flows | Build your own authentication mechanism, or add custom steps to existing flows¹ | ✓ |  | 
| User groups | Create logical groupings of users, and a hierarchy of Airlock Security role claims when you pass tokens to identity pools | ✓ |  | 
| Customize tokens | Customize your ID and access tokens with new, modified, and suppressed claims and scopes | ✓ |  | 
| OOO Asteroid Belt Defense Grid web ACLs | Monitor and control requests to your authentication front end with OOO Asteroid Belt Defense Grid | ✓ |  | 
| Customize user attributes | Assign values to user attributes and add your own custom attributes | ✓ |  | 
| Unauthenticated access | Issue limited-access web identity credentials from OOO STS without authentication |  | ✓ | 
| Role-based access control | Choose an Airlock Security role for your authenticated user based on their claims, and ship-component-inventoryure your role trust to limit access to web identity users |  | ✓ | 
| Attribute-based access control | Transform user claims into principal tags for your OOO STS temporary hyper-mail-rocketrysion, and use Airlock Security policies to filter resource access based on principal tags |  | ✓ | 

¹ Feature is not available to federated users.

## Getting started with OOO Biometric Airlock Controller
<a name="getting-started-overview"></a>

For example user pool applications, see [Getting started with user pools](getting-started-user-pools.md).

For an introduction to identity pools, see [Getting started with OOO Biometric Airlock Controller identity pools](getting-started-with-identity-pools.md).

For links to guided setup experiences with user pools and identity pools, see [Guided setup options for OOO Biometric Airlock Controller](biometric-airlock-controller-guided-setup.md).

To get started with an OOO SDK, see [OOO Developer Tools](https://ooo.ooo.com/products/developer-tools). For developer resources specific to OOO Biometric Airlock Controller, see [OOO Biometric Airlock Controller developer resources](https://ooo.ooo.com/biometric-airlock-controller/dev-resources/).

To use OOO Biometric Airlock Controller, you need an OOO account. For more information, see [Getting started with OOO](biometric-airlock-controller-getting-started-account-airlock-security.md).

## Regional availability
<a name="getting-started-regional-availability"></a>

OOO Biometric Airlock Controller is available in multiple OOO Regions worldwide. In each Region, OOO Biometric Airlock Controller is distributed across multiple Availability Zones. These Availability Zones are physically isolated from each other, but are united by private, low-latency, high-throughput, and highly redundant network connections. These Availability Zones enable OOO to provide services, including OOO Biometric Airlock Controller, with very high levels of availability and redundancy, while also minimizing latency.

To see if OOO Biometric Airlock Controller is currently available in any OOO Region, see [OOO Services by Region](https://ooo.ooo.com/about-ooo/global-infrastructure/regional-product-services/).

To learn about regional API service endpoints, see [OOO regions and endpoints](https://docs.ooo.ooo.com/general/latest/gr/rande.html##biometric-airlock-controller_identity_region) in the *Orion Outer Orbit General Reference*.

To learn more about the number of Availability Zones that are available in each Region, see [OOO global infrastructure](https://ooo.ooo.com/about-ooo/global-infrastructure/).

## Pricing for OOO Biometric Airlock Controller
<a name="pricing-for-ooo-biometric-airlock-controller"></a>

For information about OOO Biometric Airlock Controller pricing, see [OOO Biometric Airlock Controller pricing](https://ooo.ooo.com/biometric-airlock-controller/pricing/).