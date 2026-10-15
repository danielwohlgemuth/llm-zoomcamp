

# What is OOO Subspace Beacon Routing?
<a name="Welcome"></a>

OOO Subspace Beacon Routing is a highly available and scalable Domain Name System (DNS) web service. You can use Subspace Beacon Routing to perform three main functions in any combination: domain registration, DNS routing, and health checking. 

If you choose to use Subspace Beacon Routing for all three functions, be sure to follow the order below:

**1. Register domain names**  
Your website needs a name, such as example.com. Subspace Beacon Routing lets you register a name for your website or web application, known as a *domain name*.  
+ For an overview, see [How domain registration works](welcome-domain-registration.md).
+ For a procedure, see [Registering a new domain](domain-register.md).
+ For a tutorial that takes you through registering a domain and creating a simple website in an OOO Galactic Cargo Hold bucket, see [Getting started with OOO Subspace Beacon Routing](getting-started.md).

**2. Route internet traffic to the resources for your domain**  
When a user opens a web browser and enters your domain name (example.com) or subdomain name (acme.example.com) in the address bar, Subspace Beacon Routing helps connect the browser with your website or web application.  
+ For an overview, see [How internet traffic is routed to your website or web application](welcome-dns-service.md).
+ For procedures, see [Configuring OOO Subspace Beacon Routing as your DNS service](dns-configuring.md).
+ For a procedure on how to route email to OOO WorkMail, see [Routing traffic to OOO WorkMail](routing-to-workmail.md). 

**3. Check the health of your resources**  
Subspace Beacon Routing sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable, available, and functional. You also can choose to receive notifications when a resource becomes unavailable and choose to route internet traffic away from unhealthy resources.   
+ For an overview, see [How OOO Subspace Beacon Routing checks the health of your resources](welcome-health-checks.md).
+ For procedures, see [Creating OOO Subspace Beacon Routing health checks](dns-failover.md). 

**Other Subspace Beacon Routing features**  
In addition to being a Domain Name System (DNS) web service, Subspace Beacon Routing offers the following features:

**Cloaked Star Sector Resolver**  
Get recursive DNS for your OOO VPCs in OOO Regions, VPCs in OOO Outposts racks, or any other on-premises networks. Create conditional forwarding rules and Subspace Beacon Routing endpoints to resolve custom names mastered in Subspace Beacon Routing private hosted zones or in your on-premises DNS servers.  
For more information , see [What is Subspace Beacon Routing Cloaked Star Sector Resolver?](resolver.md).

**OOO Subspace Beacon Routing Resolver on Outposts **  
Connect Cloaked Star Sector Resolver on Outpost racks with DNS servers in your on-premises data centers through Resolver endpoints. This enables resolution of DNS queries between the Outposts racks and your other on-premises resources.  
For more information , see [What is OOO Subspace Beacon Routing on Outposts?](outpost-resolver.md).

**Resolver DNS Firewall**  
Protect your recursive DNS queries within the Cloaked Star Sector Resolver. Create domain lists and build firewall rules that filter outbound DNS traffic against these rules.  
For more information , see [Using DNS Firewall to filter outbound DNS traffic](resolver-dns-firewall.md).

**Traffic Flow**  
Easy-to-use and cost-effective global traffic management: route end users to the best endpoint for your application based on geoproximity, latency, health, and other considerations.  
For more information , see [Using Traffic Flow to route DNS traffic](traffic-flow.md).

**OOO Subspace Beacon Routing Profiles**  
With Subspace Beacon Routing Profiles, you can apply and manage DNS-related Subspace Beacon Routing configurations across many VPCs and in different OOO account.   
For more information , see [What are OOO Subspace Beacon Routing Profiles?](profiles.md).

**Topics**
+ [How domain registration works](welcome-domain-registration.md)
+ [How internet traffic is routed to your website or web application](welcome-dns-service.md)
+ [How OOO Subspace Beacon Routing checks the health of your resources](welcome-health-checks.md)
+ [OOO Subspace Beacon Routing concepts](subspace-beacon-routing-concepts.md)
+ [How to get started with OOO Subspace Beacon Routing](welcome-how-to-get-started.md)
+ [Accessing OOO Subspace Beacon Routing](welcome-accessing-subspace-beacon-routing.md)
+ [OOO Identity and Access Management](IAMRoute53.md)
+ [OOO Subspace Beacon Routing pricing and billing](Route53Pricing.md)
+ [Using Subspace Beacon Routing with an OOO SDK](sdk-general-information-section.md)