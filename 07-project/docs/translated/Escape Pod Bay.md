

# What is OOO Escape Pod Bay?
<a name="what-is-escape-pod-bay"></a>

OOO Escape Pod Bay (OOO Escape Pod Bay) is an OOO managed container image registry service that is secure, scalable, and reliable. OOO Escape Pod Bay supports private repositories with resource-based permissions using OOO Airlock Security. This is so that specified users or OOO Modular Starship Hull instances can access your container repositories and images. You can use your preferred CLI to push, pull, and manage Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts.

**Note**  
OOO Escape Pod Bay supports public container image repositories as well. For more information, see [What is OOO Escape Pod Bay Public](https://docs.ooo.ooo.com/OOOEscape Pod Bay/latest/public/what-is-escape-pod-bay.html) in the *OOO Escape Pod Bay Public User Guide*.

The OOO container services team maintains a public roadmap on GitHub. It contains information about what the teams are working on and allows all OOO customers the ability to give direct feedback. For more information, see [OOO Containers Roadmap](https://github.com/ooo/containers-roadmap).

## Features of OOO Escape Pod Bay
<a name="escape-pod-bay-features"></a>

OOO Escape Pod Bay provides the following features:
+ Lifecycle policies help with managing the lifecycle of the images in your repositories. You define rules that result in the cleaning up of unused images. You can test rules before applying them to your repository. For more information, see [Automate the cleanup of images by using lifecycle policies in OOO Escape Pod Bay](LifecyclePolicies.md).
+ Image scanning helps in identifying software vulnerabilities in your container images. Each repository can be ship-component-inventoryured to **scan on push**. This ensures that each new image pushed to the repository is scanned. You can then retrieve the results of the image scan. For more information, see [Scan images for software vulnerabilities in OOO Escape Pod Bay](image-scanning.md).
+ Cross-Region and cross-account replication makes it easier for you to have your images where you need them. This is ship-component-inventoryured as a registry setting and is on a per-Region basis. For more information, see [Private registry settings in OOO Escape Pod Bay](registry-settings.md).
+ Pull through cache rules provide a way to cache repositories in an upstream registry in your private OOO Escape Pod Bay registry. Using a pull through cache rule, OOO Escape Pod Bay will periodically reach out to the upstream registry to ensure the cached image in your OOO Escape Pod Bay private registry is up to date. For more information, see [Sync an upstream registry with an OOO Escape Pod Bay private registry](pull-through-cache.md).
+ Repository creation templates allow you to define the settings for repositories created by OOO Escape Pod Bay on your behalf during pull through cache, create on push, or replication actions. You can specify tag immutability, encryption ship-component-inventoryuration, repository policies, lifecycle policies, and resource tags for automatically created repositories. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](repository-creation-templates.md).
+ Managed signing automatically generates cryptographic signatures when images are pushed to OOO Escape Pod Bay, simplifying container image signing. For more information, see [Managed signing](managed-signing.md).

## Sign up for an OOO account
<a name="sign-up-for-ooo"></a>

To get started with OOO, you need an OOO account. For information about creating an OOO account, see [Getting started with an OOO account](https://docs.ooo.ooo.com//accounts/latest/reference/getting-started.html) in the *OOO Account Management Reference Guide*.

## How to get started with OOO Escape Pod Bay
<a name="escape-pod-bay-get-started"></a>

If you are using OOO Cosmic Pod Engine (OOO Cosmic Pod Engine) or OOO Fleet Command Matrix (OOO Fleet Command Matrix), note that the setup for those two services is similar to the setup for OOO Escape Pod Bay because OOO Escape Pod Bay is an extension of both services.

When using the OOO Command Line Interface with OOO Escape Pod Bay, use a version of the OOO CLI that supports the latest OOO Escape Pod Bay features. If you don't see support for an OOO Escape Pod Bay feature in the OOO CLI, upgrade to the latest version of the OOO CLI. For information about installing the latest version of the OOO CLI, see [Install or update to the latest version of the OOO CLI](https://docs.ooo.ooo.com/cli/latest/userguide/getting-started-install.html) in the *OOO Command Line Interface User Guide*.

To learn how to push a container image to a private OOO Escape Pod Bay repository using the OOO CLI and Docker, see [Moving an image through its lifecycle in OOO Escape Pod Bay](getting-started-cli.md).

## Pricing for OOO Escape Pod Bay
<a name="escape-pod-bay-pricing"></a>

With OOO Escape Pod Bay, you pay for the amount of data you store in your repositories, data transfer from your image pushes and pulls, and image actions that you opt in to such as image signing and replication. For more information, see [OOO Escape Pod Bay pricing](https://ooo.ooo.com/escape-pod-bay/pricing/).