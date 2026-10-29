# Create VPC Networks

## Create VPC Networks

A **Virtual Private Cloud (VPC)** network in UzCloud gives you full control over your network. Along with firewall rules, port forwarding and remote access VPN, you can set up VPN gateways and site-to-site VPN connections, add several networks (tiers) and control traffic between them with ACLs.

- In the left-hand menu, under **NETWORKING**, click **Networks**. The **Your Networks** page opens on the **VPC Network** tab.
- Click **+ Create New** in the upper-right corner. The **Create VPC Network** page opens.

![Networks page](../../../images/vpc-networks-1.png)

### Choose a Project

- Assign the VPC to one of your projects to keep resources organized.

![Choose a project](../../../images/vpc-networks-3.png)

### Select a Location

- Select the data center where the VPC will be created: **TASHKENT** or **FERGANA**. A VPC can only contain resources from the same location.

![Select a location](../../../images/vpc-networks-2.png)

### Network Configuration

- **Network Address** — the base address of the VPC address space (for example, `10.10.0.0`).
- **Network Size** — the size of the address space, from **/16** (65,536 addresses) to **/30**. The default is **/24** (256 addresses).

![Network configuration](../../../images/vpc-networks-4.png)

### VPC Details

- Enter a unique **Network Name** and a **Network Description** that explains the purpose of the VPC.

![VPC details](../../../images/vpc-networks-5.png)

### Create the VPC

- At the bottom of the page, choose the **Billing Cycle**: **Monthly** or **Yearly**. **Price Summary** shows the cost.
- Check the configuration and click **Create VPC**.

![Create the VPC](../../../images/vpc-networks-6.png)

### Conclusion

A **VPC network** in UzCloud provides a secure, isolated and flexible environment for your cloud resources. After creating the VPC, add networks to it and configure ACLs and VPN as needed.

> [!TIP]
> **See also:**
>
> - **[VPC Network Overview](network-overview.md)**
> - **[Add Network](add-network.md)**
> - **[Network ACL List](network-acl-list.md)**
> - **[VPN Connections](vpn-connections.md)**
