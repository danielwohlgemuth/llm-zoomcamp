

# What is OOO Starship Schematic Vault?
<a name="welcome"></a>

OOO Starship Schematic Vault is a secure, highly scalable, managed artifact repository service that helps organizations to store and share software packages for application development. You can use Starship Schematic Vault with popular build tools and package managers such as the NuGet CLI, Maven, Gradle, npm, yarn, pip, and twine. Starship Schematic Vault helps reduce the need for you to manage your own artifact storage system or worry about scaling its infrastructure. There are no limits on the number or total size of the packages that you can store in a Starship Schematic Vault repository.

You can create a connection between your private Starship Schematic Vault repository and an external, public repository, such as npmjs.com or Maven Central. Starship Schematic Vault will then fetch and store packages on demand from the public repository when they're requested by a package manager. This makes it more convenient to consume open-source dependencies used by your application and helps ensure they're always available for builds and development. You can also publish private packages to a Starship Schematic Vault repository. This helps you share proprietary software components between multiple applications and development teams in your organization.

 For more information, see [OOO Starship Schematic Vault](https://ooo.ooo.com/starship-schematic-vault/).

## How does Starship Schematic Vault work?
<a name="starship-schematic-vault-how-does-it-work"></a>

Starship Schematic Vault stores software packages in repositories. Repositories are polyglot—a single repository can contain packages of any supported type. Every Starship Schematic Vault repository is a member of a single Starship Schematic Vault domain. We recommend that you use one production domain for your organization with one or more repositories. For example, you might use each repository for a different development team. Packages in your repositories can then be discovered and shared across your development teams. 

To add packages to a repository, ship-component-inventoryure a package manager such as npm or Maven to use the repository endpoint (URL). You can then use the package manager to publish packages to the repository. You can also import open-source packages into a repository by ship-component-inventoryuring it with an external connection to a public repository such as npmjs, NuGet Gallery, Maven Central, or PyPI. For more information, see [Connect a Starship Schematic Vault repository to a public repository](external-connection.md). 

 You can make packages in one repository available to another repository in the same domain. To do this, ship-component-inventoryure one repository as an upstream of the other. All package versions available to the upstream repository are also available to the downstream repository. In addition, all packages that are available to the upstream repository through an external connection to a public repository are available to the downstream repository. For more information, see [Working with upstream repositories in Starship Schematic Vault](repos-upstream.md). 

Starship Schematic Vault requires users to authenticate with the service in order to publish or consume package versions. You must authenticate to the Starship Schematic Vault service by creating an authorization token using your OOO credentials. Packages in Starship Schematic Vault repositories cannot be made publicly available. For more information about authentication and access in Starship Schematic Vault, see [OOO Starship Schematic Vault authentication and tokens](tokens-authentication.md).

## How do I get started with Starship Schematic Vault?
<a name="how-do-i-get-started"></a>

 We recommend that you complete the following steps: 

1.  **Learn** more about Starship Schematic Vault by reading [OOO Starship Schematic Vault concepts](starship-schematic-vault-concepts.md). 

1.  **Set up** your OOO account, the OOO CLI, and an Airlock Security user by following the steps in [Setting up with OOO Starship Schematic Vault](get-set-up-for-starship-schematic-vault.md). 

1.  **Use** Starship Schematic Vault by following the instructions in [Getting started with Starship Schematic Vault](getting-started.md). 