# Load Balancer

## Load Balancer

A **Load Balancer** helps distribute incoming traffic across multiple servers to ensure high availability, reliability, and improved performance. In UzCloud, you can set up a Load Balancer to handle web applications, databases, and other services efficiently. This guide will walk you through the steps to configure a Load Balancer in UzCloud.

---

### Creating a Load Balancer

- From the left-hand side menu, click on the **Load Balancer** tab.
- To create a load balancer, click the **Load Balancer** or **plus (+)** icon located on the right side of the page. This will open the load balancer creation menu.

![Load Balancer Page](../../images/ldb-1.png)

### Choose a Location

- Select the data center location where your server will be physically hosted.
- Choose from the available locations listed.

![Choose Location](../../images/ldb-2.png)

### Assign to a Project

- Assign the load balancer to one of your projects to organize and manage resources effectively.

![Assign to Project](../../images/ldb-3.png)

### Choose Network

- Select the network where your load balancer will operate. This will define the traffic flow and connections to your servers.

![Choose Network](../../images/ldb-4.png)

### Choose IP

- Choose the network IP for your load balancer by selecting from **Existing IP Address** or **Acquire New IP Address**.
- **Note**: By choosing **Acquire New IP**, it will create a default isolated IP under the selected zone.

![Choose IP](../../images/ldb-5.png)

### Set Forwarding Rules

- Configure forwarding rules to define how traffic should be distributed across your servers.

- Provide a unique **Rule Name** for the forwarding rule. Choose the appropriate **Protocol** (e.g., TCP, UDP, HTTP, HTTPS). Specify the port range for incoming traffic.

- Select an algorithm to distribute incoming requests among instances:

  - **Source** – Directs traffic to the same instance based on the client’s source IP.
  - **Round Robin** – Distributes traffic evenly across all available instances.
  - **Least Connections** – Sends traffic to the instance with the fewest active connections.

- You can enable **Sticky sessions** to ensure that a user’s requests are consistently routed to the same backend instance.

  - **LB Cookie** – Uses a load balancer-generated cookie to maintain session persistence.
  - **App Cookie** – Uses application-defined cookies for session persistence.
  - **Source-Based** – Binds sessions to a backend instance based on the client’s source IP.
  - **None** – No session persistence; requests are distributed normally.

- Choose the VM instances that will handle incoming traffic.

![Set Forwarding Rules](../../images/ldb-6.png)

### Name Load Balancer

- Provide a unique name for your load balancer to easily identify it. The name can only include alphanumeric characters, dashes, and periods.

![Name Load Balancer](../../images/ldb-7.png)

### Create Load Balancer

- Choose the desired **Billing Cycle** for your load balancer. Load Balancer supports Hourly, Monthly, Quarterly, Semiannually, Yearly, Bi-annually, and Tri-annually billing cycles.
- The billing rules it supports include Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata, and Unfixed Prorata.
- Only one load balancer package is available per zone. This simplifies configuration and ensures consistent behavior within each deployment zone.
- Verify all the configuration details and review the price summary. Click on **Create Load Balancer** to create the load balancer for your network.

![Create Load Balancer](../../images/ldb-8.png)

### View Load Balancer

- To view more about load balancer in detail, click on the Load Balancer.

![View Load Balancer](../../images/ldb-9.png)

- You can view the policies associated with this load balancer.
- If you want to attach a VM instance to your load balancer you can go to **Add VM** and select the VM instance to attach.

![View Load Balancer](../../images/ldb-10.png)

### Conclusion

By following this guide, you can easily configure and manage a Load Balancer on UzCloud. Load Balancers ensure high availability, reliability, and improved performance by distributing incoming traffic across multiple servers. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Public Network](../networks/public-network/create-public-network.md)**
> - **[VPC Network](../networks/vpc-network/create-vpc-network.md)**
> - **[Affinity Group](../affinity-groups/create-affinity-groups.md)**
> - **[Public IP Address](../networks/public-ip-address.md)**
> - **[Create Templates](../templates/create-templates.md)**
