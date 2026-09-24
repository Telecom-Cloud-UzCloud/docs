# Create Kubernetes Cluster

## Kubernetes Cluster

A **Kubernetes** cluster is a set of preconfigured machines (nodes) that work together to run containerized applications in an automated and scalable way. Kubernetes manages the deployment, scaling, and operation of application containers across multiple nodes.

In **UzCloud**, you can easily set up a Kubernetes cluster to manage your applications, scale resources, and maintain high availability.

---

### Creating a Kubernetes Cluster

- From the left-hand menu, click on the **Kubernetes** tab.
- You will be redirected to the **Kubernetes** page.

![Kubernetes Page](../../images/kb-1.png)

- To create a cluster, click on **Create Cluster** or the **Create New** icon located on the right side of the page.

### Choose a Location

- Select the data center location where your Kubernetes cluster will be deployed.
- Choose from the available locations listed.

![Choose Location](../../images/kb-7.png)

### Assign to a Project

- Assign the cluster server to one of your projects to organize and manage resources effectively.

![Assign to Project](../../images/kb-2.png)

### Choose Network

- Set up or choose a network for your server. This can be an isolated private network, or you can create an elastic network to connect multiple regions.
- Alternatively, you can also create or set up a new network by selecting **Create New Network**.

![Choose Network](../../images/kb-8.png)

### Choose Cluster Capacity

- You can select the predefined **Node Plan** with fixed configurations for CPU, memory, and storage.
- For a more tailored solution, you can create a **Custom Plan** by specifying CPU, memory, storage, and node count. More nodes improve scalability and distribute workloads efficiently.

![Choose Cluster Capacity](../../images/kb-3.png)

### Advanced Settings (Optional)

- You can **Enable High Availability** for better redundancy and add **Control Nodes** to ensure stability in case of failures.

![Advanced Settings](../../images/kb-4.png)

- Configure additional settings for your server:

  - **Add SSH Key** for secure access. Click on **Add Now** to add an SSH key.
  - **Note**: For some OS images, such as Arch Linux, an SSH key is required because password login is not supported.

![Add SSH Key](../../images/kb-9.png)

- Add the name of the SSH key with the key value and click **Add SSH Key**.

![Add SSH Key Details](../../images/kb-10.png)

### Choose Cluster Name

- Provide a unique **Cluster Name** for your Kubernetes cluster to identify it easily in your dashboard.

![Choose Cluster Name](../../images/create-kubernetes-cluster-inline-e0a45aae.png)

### Create Cluster

- Choose the desired **Billing Cycle** for your cluster. Kubernetes supports Hourly, Monthly, Quarterly, Semiannually, Yearly, Bi-annually, and Tri-annually billing cycles.
- Supported billing rules are Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata, and Unfixed Prorata.
- It supports multiple cluster packages based on resource needs such as nodes and disk size. This makes it suitable for a range of container-based application workloads.
- Verify all the configuration details and review the price summary. Click on **Create Cluster** to create the cluster.

![Create Cluster](../../images/kb-6.png)

### Conclusion

By following this guide, you can easily create and manage a Kubernetes cluster on UzCloud. Kubernetes clusters provide a powerful way to deploy, scale, and manage containerized applications with high availability and efficiency. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Manage Kubernetes Cluster](kubernetes-cluster-overview.md)**
> - **[Load Balancer](../load-balancer/load-balancer.md)**
> - **[Auto Scaling](../auto-scaling/create-auto-scaling.md)**
> - **[Affinity Group](../affinity-groups/create-affinity-groups.md)**
