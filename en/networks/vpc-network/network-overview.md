# Network Overview

## VPC Network Overview

To open a VPC, click its name on the **VPC Network** tab of the **Networks** page. The VPC page shows its creation and renewal dates, project and location. The tabs on the left give access to the VPC settings.

![VPC page](../../../images/vpc-net-1.png)

### Action Buttons

The action buttons are in the upper-right corner of the VPC card:

- **Update vpc** — changes the VPC name and description.
- **Restart** — restarts the VPC network.
- **Refresh** — reloads the VPC data.
- **Delete** — deletes the VPC.

### Details

The **Details** tab shows the main VPC parameters.

![VPC details](../../../images/vpc-net-2.png)

- **ID** — the VPC identifier.
- **Location** — the data center of the VPC.
- **Description** — the VPC description.
- **Restart Network** — whether the network needs to be restarted to apply changes (true/false).
- **Account** and **Domain** — the account and domain that own the VPC.
- **Network Domain** — the DNS domain for internal communication within the VPC.
- **CIDR** — the VPC address space.

### VPC Tabs

- **[Network](add-network.md)** — the networks (tiers) created inside the VPC.
- **[Public IP Addresses](public-ip-address.md)** — the public IP addresses of the VPC.
- **[Network ACL List](network-acl-list.md)** — the access control lists for VPC networks.
- **[VPN Gateway](vpn-gateway.md)** — the site-to-site VPN gateway of the VPC.
- **[VPN Connections](vpn-connections.md)** — the site-to-site VPN connections.
- **[Associated VMs](associated-vms.md)** — the VMs connected to the VPC.
- **Static Routes** — the static routes of the VPC (see below).

### Static Routes

Static routes direct traffic for a given address range to a specified next hop.

![Static routes](../../../images/vpc-net-13.png)

- On the **Static Routes** tab, click **+ Add Static Route**.
- Enter the destination **CIDR** and the **Next Hop** address, then click **Add**.

![Add a static route](../../../images/vpc-net-14.png)

### Conclusion

The VPC page provides essential details about your virtual private cloud and access to all its settings: networks, IP addresses, ACLs, VPN and routes.

> [!TIP]
> **See also:**
>
> - **[Create VPC Network](create-vpc-network.md)**
> - **[VPN Gateway](vpn-gateway.md)**
> - **[VPN Connections](vpn-connections.md)**
