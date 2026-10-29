# Public IP Address

## Public IP Address

Public IP addresses allow resources in the VPC to communicate with the internet.

- On the VPC page, open the **Public IP Addresses** tab. It lists the IP addresses of the VPC with their type, instances and VPC. The **SOURCE-NAT** address is assigned to the VPC automatically and is used for outgoing traffic.

![Public IP Addresses](../../../images/vpc-net-5.png)

- To get another address, click **+ Acquire New IP**.
- Choose the **Billing Cycle**, check the **Price Summary** and click **Buy IP**.

![Acquire a new public IP](../../../images/vpc-net-6.png)

- To configure firewall, port forwarding and VPN for an address, see **[Public IP Address](../public-ip-address.md)**.

### Conclusion

On the **Public IP Addresses** tab, you can view, acquire and manage the IP addresses of the VPC.

> [!TIP]
> **See also:**
>
> - **[VPC Network Overview](network-overview.md)**
> - **[Create VPC Network](create-vpc-network.md)**
> - **[VPN Gateway](vpn-gateway.md)**
> - **[VPN Connections](vpn-connections.md)**
