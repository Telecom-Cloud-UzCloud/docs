# Load Balancer

## Load Balancer

A **Load Balancer** distributes incoming traffic across multiple servers to ensure high availability, reliability, and improved performance. In UzCloud, you can set up a load balancer for web applications, databases, and other services. This guide walks you through creating and managing a load balancer.

---

### Open the Load Balancer Page

- In the left-hand menu, under **NETWORKING**, click **Load Balancer**. The page lists your load balancers with their project, IP address, creation date, location and number of policies.
- Click **+ Create New** in the upper-right corner. The **Create Load Balancer** page opens.

![Load Balancer page](../../images/ldb-1.png)

### Choose a Project

- Assign the load balancer to one of your projects to keep resources organized.

![Choose a project](../../images/ldb-3.png)

### Select a Location

- Select the data center where the load balancer will be hosted: **TASHKENT** or **FERGANA**.

![Select a location](../../images/ldb-2.png)

### Select a Network

- Select the network where the load balancer will operate (a VPC or public network). The network defines which VM instances the load balancer can route traffic to.

![Select a network](../../images/ldb-4.png)

### Select an IP Address

- **Acquire New IP Address** — the console acquires a new public IP address for the load balancer (if needed, a default isolated network is created in the selected zone).
- **Choose IP Address** — select one of your existing IP addresses.

![Select an IP address](../../images/ldb-5.png)

### Set Forwarding Rules

Forwarding rules define how traffic is routed from the load balancer to your VM instances. At least one rule is required.

- Enter a **Rule Name** (at least 5 characters).
- Select the **Protocol**: **TCP** or **TCP Proxy**.
- Enter the **Public Port** (the port the load balancer listens on) and the **Private Port** (the port on the VM instances).
- Select the **Algorithm** for distributing requests:
  - **Source** — sends requests from the same client IP to the same instance.
  - **Roundrobin** — distributes requests evenly across all instances in turn.
  - **Least Connections** — sends requests to the instance with the fewest active connections.
- Select the **Sticky Session** method (for example, **SourceBased** — binds a client's session to one instance based on the client IP). Click **Compare** to compare the available methods.
- Under **Select Instances**, select the VM instances that will receive traffic.
- To add another rule, click **+ Add New Rule**.

![Set forwarding rules](../../images/ldb-6.png)

### Name the Load Balancer

- Enter a **Load Balancer Name**. The name must be unique and contain only alphanumeric characters, dashes and periods.

![Load balancer name](../../images/ldb-7.png)

### Create the Load Balancer

- At the bottom of the page, choose the **Billing Cycle**: **Monthly** or **Yearly**. **Price Summary** shows the cost of the load balancer.
- Check the configuration and click **Create Load Balancer**.

![Create the load balancer](../../images/ldb-8.png)

### View a Load Balancer

- Click a load balancer name to open its page. It shows the project, location, IP address, network and creation date. Click **Refresh** in the upper-right corner to reload the data.
- The **Policies** tab lists the forwarding rules: protocol, algorithm, sticky method, public and private ports, creation date and the number of attached instances. To add a rule, click **+ Add New Policies**; to delete one, click the delete icon on its card.
- The **Firewall Rules** tab lists the firewall rules for the load balancer IP address: source CIDR, protocol, ICMP type and code, and port range. To add a rule, click **+ Add A Firewall Rule**.

![Load balancer page](../../images/ldb-9.png)

- To see the instances attached to a policy, click the eye icon next to **Attached Instances**. To attach another VM, click **+ Add VM**; to detach a VM, click the unlink icon on its card.

![Attached instances](../../images/ldb-10.png)

### Conclusion

By following this guide, you can create and manage a load balancer on UzCloud. Load balancers ensure high availability, reliability, and improved performance by distributing incoming traffic across multiple servers. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Public Network](../networks/public-network/create-public-network.md)**
> - **[VPC Network](../networks/vpc-network/create-vpc-network.md)**
> - **[Affinity Group](../affinity-groups/create-affinity-groups.md)**
> - **[Public IP Address](../networks/public-ip-address.md)**
> - **[Create Templates](../templates/create-templates.md)**
