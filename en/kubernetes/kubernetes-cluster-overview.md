# Kubernetes Cluster Overview

## Kubernetes Cluster Overview for UzCloud

The **Kubernetes Overview** page provides a detailed summary of your cluster and quick actions to manage it: configuration, node plans, related virtual machines, load balancers and volumes.

---

### Action Buttons

- On the **Kubernetes** page, each cluster card has **Power Off** and **Delete** buttons. Click the cluster name to open the **Kubernetes Overview** page.
- The action buttons are on the right of the status bar.

![Action buttons](../../images/kb-m-1.png)

- **Refresh** — reloads the cluster status and data.
- **Upgrade Kubernetes Version** — updates the cluster to a newer Kubernetes release.
- **Download config file** — downloads the `kubeconfig` file for working with the cluster via `kubectl` and other CLI tools.
- **Scale Kubernetes Cluster** — changes the number of worker nodes.
- **Power Off** — shuts down the whole cluster.
- **Delete** — permanently deletes the cluster and all its resources.

The page has the following tabs:

- **Overview** — the cluster summary described below.
- **Access** — download the cluster config and instructions for connecting via the CLI and the Kubernetes Dashboard UI.
- **Settings** — **Change Plan** (change the master and worker node plans), **Upgrade Version**, **Firewall** and **Port Forwarding**.
- **Virtual Machines** — the cluster nodes.
- **Load Balancer** — the cluster load balancers (including the API load balancer).
- **Volumes** — the disks of the cluster nodes.

### Cluster Summary

![Cluster summary](../../images/kb-m-6.png)

- **Total CPU** — the total number of vCPUs across all cluster nodes.
- **Total RAM** — the total amount of memory allocated to the cluster.
- **Control nodes** — the number of nodes that manage the cluster state.
- **Worker Nodes** — the number of nodes that run your workloads.
- **Network** — the network in which the cluster is deployed.
- **Status** — the current state of the cluster (for example, Running).

### Cluster Information

![Cluster information](../../images/kb-m-2.png)

- **Project Name** — the project the cluster belongs to.
- **Created at** — the date and time the cluster was created.
- **IP Address** — the public IP address of the cluster.
- **End Point** — the Kubernetes API server endpoint. Click the copy icon to copy it.
- **User name** — the default user name on the cluster nodes.
- **Location** — the data center where the cluster runs.
- **Kubernetes Version** — the Kubernetes version running in the cluster.
- **Auto Scaling** — whether automatic scaling of nodes is enabled.
- **All Time Consumption** — the total cost of the cluster since it was created.
- **Network** — the name of the cluster network.
- **SSH key** — the SSH key used to access the cluster nodes.

### Node Config

![Node config](../../images/kb-m-3.png)

- **Master Node Config** and **Worker Node Config** — the plans of the control plane and worker nodes: **Current Plan**, **CPU** and **Memory**.

### Expose a Kubernetes Service

Your Kubernetes services are exposed on a port. To make a service available from the internet, open that port on the cluster's **Settings → Firewall** tab and create a rule on the **Settings → Port Forwarding** tab. Click **+ Add Port Forwarding Rule** and specify the public port, the private port, the protocol and the node.

![Port forwarding rules](../../images/kb-m-5.png)

---

### Conclusion

The **Kubernetes Overview** page gives a centralized view of your cluster's health, configuration, and resource usage. Action buttons simplify cluster maintenance, and detailed specs help with monitoring and planning.

> [!TIP]
> **See also:**
>
> - **[Create Kubernetes Cluster](create-kubernetes-cluster.md)**
> - **[Kubernetes Cluster CLI](kubernetes-cluster-via-cli.md)**
> - **[Kubernetes Cluster UI Access](kubernetes-dashboard-ui-access.md)**
