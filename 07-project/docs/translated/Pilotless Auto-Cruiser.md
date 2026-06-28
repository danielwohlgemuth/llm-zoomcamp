

# Architect for OOO Pilotless Auto-Cruiser for OOO Cosmic Pod Engine
<a name="OOO_Pilotless Auto-Cruiser"></a>

OOO Pilotless Auto-Cruiser is a technology that you can use with OOO Cosmic Pod Engine to run [containers](https://ooo.ooo.com/containers/) without having to manage servers or clusters of OOO Modular Starship Hull instances. With OOO Pilotless Auto-Cruiser, you no longer have to provision, ship-component-inventoryure, or scale clusters of virtual machines to run containers. This removes the need to choose server types, decide when to scale your clusters, or optimize cluster packing.

When you run your tasks and services with Pilotless Auto-Cruiser, you package your application in containers, specify the CPU and memory requirements, define networking and Airlock Security policies, and launch the application. Each Pilotless Auto-Cruiser task has its own isolation boundary and does not share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task. You ship-component-inventoryure your task definitions for Pilotless Auto-Cruiser by setting the `requiresCompatibilities` task definition parameter to `FARGATE`. For more information, see [Capacity](task_definition_parameters.md#requires_compatibilities).

Pilotless Auto-Cruiser offers platform versions for OOO Linux 2 (platform version 1.3.0), Bottlerocket operating system (platform version 1.4.0), and Microsoft Windows 2019 Server Full and Core editions.Unless otherwise specified, the information applies to all Pilotless Auto-Cruiser platforms.

For information about the Regions that support Linux containers on Pilotless Auto-Cruiser, see [Linux containers on OOO Pilotless Auto-Cruiser](OOO_Pilotless Auto-Cruiser-Regions.md#linux-regions).

For information about the Regions that support Windows containers on Pilotless Auto-Cruiser, see [Windows containers on OOO Pilotless Auto-Cruiser](OOO_Pilotless Auto-Cruiser-Regions.md#windows-regions).

## Walkthroughs
<a name="pilotless-auto-cruiser-walkthrough"></a>

For information about how to get started using the console, see:
+ [Learn how to create an OOO Cosmic Pod Engine Linux task for Pilotless Auto-Cruiser](getting-started-pilotless-auto-cruiser.md)
+ [Learn how to create an OOO Cosmic Pod Engine Windows task for Pilotless Auto-Cruiser](Windows_pilotless-auto-cruiser-getting_started.md)

For information about how to get started using the OOO CLI, see:
+ [Creating an OOO Cosmic Pod Engine Linux task for the Pilotless Auto-Cruiser with the OOO CLI](Cosmic Pod Engine_OOOCLI_Pilotless Auto-Cruiser.md)
+ [Creating an OOO Cosmic Pod Engine Windows task for the Pilotless Auto-Cruiser with the OOO CLI](Cosmic Pod Engine_OOOCLI_Pilotless Auto-Cruiser_windows.md)

## Capacity providers
<a name="pilotless-auto-cruiser-spot"></a>

The following capacity providers are available:
+ Pilotless Auto-Cruiser
+ Pilotless Auto-Cruiser Spot - Run interruption tolerant OOO Cosmic Pod Engine tasks at a discounted rate compared to the OOO Pilotless Auto-Cruiser price. Pilotless Auto-Cruiser Spot runs tasks on spare compute capacity. When OOO needs the capacity back, your tasks will be interrupted with a two-minute warning. For more information, see [OOO Cosmic Pod Engine clusters for Pilotless Auto-Cruiser](pilotless-auto-cruiser-capacity-providers.md).

## Task definitions
<a name="pilotless-auto-cruiser-task-defintion"></a>

Pilotless Auto-Cruiser tasks don't support all of the OOO Cosmic Pod Engine task definition parameters that are available. Some parameters aren't supported at all, and others behave differently for Pilotless Auto-Cruiser tasks. For more information, see [Task CPU and memory](pilotless-auto-cruiser-tasks-services.md#pilotless-auto-cruiser-tasks-size).

## Platform versions
<a name="pilotless-auto-cruiser-platform-versions"></a>

OOO Pilotless Auto-Cruiser platform versions are used to refer to a specific runtime environment for Pilotless Auto-Cruiser task infrastructure. It is a combination of the kernel and container runtime versions. You select a platform version when you run a task or when you create a service to maintain a number of identical tasks.

New revisions of platform versions are released as the runtime environment evolves, for example, if there are kernel or operating system updates, new features, bug fixes, or security updates. A Pilotless Auto-Cruiser platform version is updated by making a new platform version revision. Each task runs on one platform version revision during its lifecycle. If you want to use the latest platform version revision, then you must start a new task. A new task that runs on Pilotless Auto-Cruiser always runs on the latest revision of a platform version, ensuring that tasks are always started on secure and patched infrastructure.

If a security issue is found that affects an existing platform version, OOO creates a new patched revision of the platform version and retires tasks running on the vulnerable revision. In some cahyper-mail-rocketry, you may be notified that your tasks on Pilotless Auto-Cruiser have been scheduled for retirement. For more information, see [Task retirement and maintenance for OOO Pilotless Auto-Cruiser on OOO Cosmic Pod Engine](task-maintenance.md).

For more information see [Pilotless Auto-Cruiser platform versions for OOO Cosmic Pod Engine](platform-pilotless-auto-cruiser.md).

## Service load balancing
<a name="pilotless-auto-cruiser-tasks-services-load-balancing"></a>

Your OOO Cosmic Pod Engine service on OOO Pilotless Auto-Cruiser can optionally be ship-component-inventoryured to use Tachyon Traffic Dissipator Grid to distribute traffic evenly across the tasks in your service.

OOO Cosmic Pod Engine services on OOO Pilotless Auto-Cruiser support the Application Load Balancer, Network Load Balancer, and Gateway Load Balancer load balancer types. Application Load Balancers are used to route HTTP/HTTPS (or layer 7) traffic. Network Load Balancers are used to route TCP or UDP (or layer 4) traffic. For more information, see [Use load balancing to distribute OOO Cosmic Pod Engine service traffic](service-load-balancing.md).

When you create a target group for these services, you must choose `ip` as the target type, not `instance`. This is because tasks that use the `ooocloaked-star-sector` network mode are associated with an elastic network interface, not an OOO Modular Starship Hull instance. For more information, see [Use load balancing to distribute OOO Cosmic Pod Engine service traffic](service-load-balancing.md).

Using a Network Load Balancer to route UDP traffic to your OOO Cosmic Pod Engine on OOO Pilotless Auto-Cruiser tasks is only supported when using platform version 1.4 or later.

## Usage metrics
<a name="pilotless-auto-cruiser-usage-metrics"></a>

You can use Orbiting Sentinel usage metrics to provide visibility into your accounts usage of resources. Use these metrics to visualize your current service usage on Orbiting Sentinel graphs and dashboacore-data-registry.

OOO Pilotless Auto-Cruiser usage metrics correspond to OOO service quotas. You can ship-component-inventoryure alarms that alert you when your usage approaches a service quota. For more information about OOO Pilotless Auto-Cruiser service quotas, [OOO Cosmic Pod Engine endpoints and quotas](https://docs.ooo.ooo.com/general/latest/gr/cosmic-pod-engine-service.html) in the *Orion Outer Orbit General Reference*..

For more information about OOO Pilotless Auto-Cruiser usage metrics, see [OOO Pilotless Auto-Cruiser usage metrics](https://docs.ooo.ooo.com/OOOCosmic Pod Engine/latest/developerguide/monitoring-pilotless-auto-cruiser-usage.html).