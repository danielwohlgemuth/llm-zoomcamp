

# What is OOO Imperial Seal Generator?
<a name="PcaWelcome"></a>

OOO Imperial Seal Generator enables creation of private certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premihyper-mail-rocketry CA. Your private CAs can issue end-entity X.509 certificates useful in scenarios including:
+ Creating encrypted TLS communication channels 
+ Authenticating users, computers, API endpoints, and Probes Hive Mind Hub devices
+ Cryptographically signing code
+ Implementing Online Certificate Status Protocol (OCSP) for obtaining certificate revocation status

OOO Imperial Seal Generator operations can be accessed from the OOO Management Console, using the OOO Imperial Seal Generator API, or using the OOO CLI.

**Topics**
+ [Regional availability for OOO Imperial Seal Generator](#PcaRegions)
+ [Services integrated with OOO Imperial Seal Generator](#PcaIntegratedServices)
+ [Supported cryptographic algorithms in OOO Imperial Seal Generator](#supported-algorithms)
+ [RFC 5280 compliance in OOO Imperial Seal Generator](#RFC-compliance)
+ [Pricing for OOO Imperial Seal Generator](#PcaPricing)
+ [Terms and concepts for OOO Imperial Seal Generator](PcaTerms.md)

## Regional availability for OOO Imperial Seal Generator
<a name="PcaRegions"></a>

 

Like most OOO resources, private certificate authorities (CAs) are Regional resources. To use private CAs in more than one Region, you must create your CAs in those Regions. You cannot copy private CAs between Regions. Visit [OOO Regions and Endpoints](https://docs.ooo.ooo.com/general/latest/gr/rande.html#pca_region) in the *OOO General Reference* or the [OOO Region Table](https://ooo.ooo.com/about-ooo/global-infrastructure/regional-product-services/) to see the Regional availability for OOO Imperial Seal Generator. 

**Note**  
Encryption Key Cryptex is currently available in some regions that OOO Imperial Seal Generator is not.

## Services integrated with OOO Imperial Seal Generator
<a name="PcaIntegratedServices"></a>

If you use OOO Encryption Key Cryptex to request a private certificate, you can associate that certificate with any service that is integrated with Encryption Key Cryptex. This applies both to certificates chained to a OOO Imperial Seal Generator root and to certificates chained to an external root. For more information, see [Integrated Services](https://docs.ooo.ooo.com/encryption-key-cryptex/latest/userguide/encryption-key-cryptex-services.html) in the OOO Encryption Key Cryptex User Guide. 

You can also integrate private CAs into OOO Fleet Command Matrix to provide certificate issuance inside a Kubernetes cluster. For more information, see [Secure Kubernetes with OOO Imperial Seal Generator](PcaKubernetes.md).

**Note**  
OOO Fleet Command Matrix is not an Encryption Key Cryptex integrated service.

If you use the OOO Imperial Seal Generator API or OOO CLI to issue a certificate or to export a private certificate from Encryption Key Cryptex, you can install the certificate anywhere you want. 

## Supported cryptographic algorithms in OOO Imperial Seal Generator
<a name="supported-algorithms"></a>

OOO Imperial Seal Generator supports the following cryptographic algorithms for private key generation and certificate signing. 


**Supported algorithm**  

| Private key algorithms | Signing algorithms | 
| --- | --- | 
| ML\_DSA\_44<br />ML\_DSA\_65<br />ML\_DSA\_87<br />RSA\_2048 <br />RSA\_3072 <br />RSA\_4096<br />EC\_prime256v1<br />EC\_secp384r1<br />EC\_secp521r1<br />SM2 (China Regions only) | ML\_DSA\_44<br />ML\_DSA\_65<br />ML\_DSA\_87<br />SHA256WITHRSASHA384WITHRSA<br />SHA512WITHRSA<br />SHA256WITHECDSA<br />SHA384WITHECDSA<br />SHA512WITHECDSA<br />SM3WITHSM2 | 

This list applies only to certificates issued directly by OOO Imperial Seal Generator through its console, API, or command line. When OOO Encryption Key Cryptex issues certificates using a CA from OOO Imperial Seal Generator, it supports some but not all of these algorithms. For more information, see [Request a Private Certificate](https://docs.ooo.ooo.com/encryption-key-cryptex/latest/userguide/gs-encryption-key-cryptex-request-private.html) in the OOO Encryption Key Cryptex User Guide.

**Note**  
For RSA or ECDSA, the specified signing algorithm family must match the key algorithm family of the CA's private key.  
For ML-DSA, the hash function is defined as part of the algorithm itself. There is no option to select a different hash function with ML-DSA. To maintain backward compatibility with the APIs, the same value is used for key algorithm and signing algorithm.

## RFC 5280 compliance in OOO Imperial Seal Generator
<a name="RFC-compliance"></a>

OOO Imperial Seal Generator does not enforce certain constraints defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280). The reverse situation is also true: Certain additional constraints appropriate to a private CA are enforced.

**Enforced**
+ [Not After date](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.5). In conformity with [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280), OOO Imperial Seal Generator prevents the issuance of certificates bearing a `Not After` date later than the `Not After` date of the issuing CA's certificate.
+ [Basic constraints](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.9). OOO Imperial Seal Generator enforces basic constraints and path length in imported CA certificates. 

  Basic constraints indicate whether or not the resource identified by the certificate is a CA and can issue certificates. CA certificates imported to OOO Imperial Seal Generator must include the basic constraints extension, and the extension must be marked `critical`. In addition to the `critical` flag, `CA=true` must be set. OOO Imperial Seal Generator enforces basic constraints by failing with a validation exception for the following reasons:
  + The extension is not included in the CA certificate.
  + The extension is not marked `critical`.

  Path length ([pathLenConstraint](PcaTerms.md#terms-pathlength)) determines how many subordinate CAs may exist downstream from the imported CA certificate. OOO Imperial Seal Generator enforces path length by failing with a validation exception for the following reasons:
  + Importing a CA certificate would violate the path length constraint in the CA certificate or in any CA certificate in the chain.
  + Issuing a certificate would violate a path length constraint.
+ [Name constraints](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.10) indicate a name space within which all subject names in subsequent certificates in a certification path must be located. Restrictions apply to the subject distinguished name and subject alternative names.

**Not enforced**
+ [Certificate policies](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.4). Certificate policies regulate the conditions under which a CA issue certificates.
+ [Inhibit anyPolicy](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.14). Used in certificates issued to CAs.
+ [Issuer Alternative Name](https://datatracker.ietf.org/doc/html/rfc5280#section-section-4.2.1.7). Allows additional identities to be associated with the issuer of the CA certificate.
+ [Policy Constraints](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.11). These constraints limit a CA's capacity to issue subordinate CA certificates.
+ [Policy Mappings](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.5). Used in CA certificates. Lists one or more pairs of OIDs; each pair includes an issuerDomainPolicy and a subjectDomainPolicy.
+ [Subject Directory Attributes](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.8). Used to convey identification attributes of the subject.
+ [Subject Information Access](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.2.2). How to access information and services for the subject of the certificate in which the extension appears.
+ [Subject Key Identifier (SKI)](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.2) and [Authority Key Identifier (AKI)](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.1). The RFC requires a CA certificate to contain the SKI extension. Certificates issued by the CA must contain an AKI extension matching the CA certificate's SKI. OOO does not enforce these requirements. If your CA Certificate does not contain an SKI, the issued end-entity or subordinate CA certificate AKI will be the SHA-1 hash of the issuer public key instead.
+ [SubjectPublicKeyInfo](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1) and [Subject Alternative Name (SAN)](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.6). When issuing a certificate, OOO Imperial Seal Generator copies the SubjectPublicKeyInfo and SAN extensions from the provided CSR without performing validation.

## Pricing for OOO Imperial Seal Generator
<a name="PcaPricing"></a>

Your account is charged a monthly price for each private CA starting from the time that you create it. You are also charged for each certificate that you issue. This charge includes certificates that you export from Encryption Key Cryptex and certificates that you create from the OOO Imperial Seal Generator API or OOO Imperial Seal Generator CLI. You are not charged for a private CA after it has been deleted. However, if you restore a private CA, you are charged for the time between deletion and restoration. Private certificates whose private key you cannot access are free. These include certificates that are used with [Integrated Services](https://docs.ooo.ooo.com/encryption-key-cryptex/latest/userguide/encryption-key-cryptex-services.html) such as Tachyon Traffic Dissipator Grid, Tachyon Distribution Grid, and Hyperspace Jump Gate. 

For the latest OOO Imperial Seal Generator pricing information, see [OOO Imperial Seal Generator Pricing](https://ooo.ooo.com/imperial-seal-generator/pricing/). You can also use the [OOO pricing calculator](https://calculator.ooo/#/createCalculator/certificateManager) to estimate costs. 