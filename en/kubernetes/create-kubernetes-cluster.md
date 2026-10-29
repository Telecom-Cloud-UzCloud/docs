# Create Kubernetes Cluster

## Kubernetes Cluster

A **Kubernetes** cluster is a set of preconfigured machines (nodes) that work together to run containerized applications in an automated and scalable way. Kubernetes manages the deployment, scaling, and operation of application containers across multiple nodes.

In **UzCloud**, you can set up a managed Kubernetes cluster in a few steps: the console creates the control plane and worker nodes, the cluster network and an API load balancer for you.

---

### Open the Kubernetes Page

- In the left-hand menu, under **CONTAINERS**, click **Kubernetes**. The page lists your clusters with their project, IP address, creation date, location, billing cycle and status.
- Click **+ Create New** in the upper-right corner. The **Create Kubernetes** page opens.

![Kubernetes page](../../images/kb-1.png)

### Choose a Project

- Assign the cluster to one of your projects to keep resources organized.

![Choose a project](../../images/kb-2.png)

### Select a Location and Version

- Select the data center where the cluster will be deployed: **TASHKENT** or **FERGANA**.
- Under **Select Version**, choose the Kubernetes version for the cluster.

![Location and version](../../images/kb-7.png)

### Configure Node Groups

- **Master Group** — select a **Node Plan** for the control plane nodes. Turn on **Enable High Availability** to run several control nodes instead of one (**Control Nodes: 1** by default).
- **Worker Group** — select a **Node Plan** for the worker nodes and set the number of nodes with **Node Count** (2 by default). Your workloads run on the worker nodes.

![Node groups](../../images/kb-3.png)

### Select a Disk Offering

- Under **Select Disk Offering**, choose the disk type (**SSD**, **HDD** or **NVMe**) and the disk for the nodes. The monthly and hourly prices are shown for each option.

![Disk offering](../../images/kb-4.png)

### SSH Key, Storage and Cluster Name

- An SSH key is required. Click **Add now** next to **Add SSH Key To Your Instance**, select an existing key or enter a name and paste the public key, then click **Add SSH Key**.

![SSH key details](../../images/kb-10.png)

- Turn on **Enable Cloud Storage Integration** to configure the CSI (Container Storage Interface) driver automatically. Kubernetes workloads can then dynamically provision and manage persistent volumes.
- Enter a unique **Cluster Name**.

### Create the Cluster

- At the bottom of the page, choose the **Billing Cycle**: **Monthly** or **Yearly**. **Price Summary** shows the cost of the selected configuration.
- Check the configuration and click **Review & Create Cluster**.

![Create the cluster](../../images/kb-6.png)

> [!NOTE]
> You don't need to choose a network: UzCloud creates a separate network for the cluster (for example, `k8s-test-network`) and a load balancer for the Kubernetes API.

### Conclusion

By following this guide, you can create a Kubernetes cluster on UzCloud in a few minutes. Kubernetes clusters provide a powerful way to deploy, scale, and manage containerized applications with high availability. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Manage Kubernetes Cluster](kubernetes-cluster-overview.md)**
> - **[Load Balancer](../load-balancer/load-balancer.md)**
> - **[Affinity Group](../affinity-groups/create-affinity-groups.md)**
