# Compute Instance

## Compute Instance for UzCloud

A **Compute Instance** is a virtual server in the cloud that functions similarly to a physical computer. It has its own CPU, memory, and storage, allowing you to install software, run applications, or host websites. With a Compute Instance, you have complete control over your server environment, and you can quickly launch and scale servers as needed.

---

### Creating a Compute Instance on UzCloud

- From the left-hand menu, click **Instances**. The page shows all your instances with their status, location, project, operating system, IP address and configuration.
- Click **+ Create New** in the top-right corner. The **Create a Server** page opens.

![Instances Page](../../images/select-instance.png)

### Choose a Project

- Assign the server to one of your projects to organize and manage resources effectively.

![Choose Project](../../images/create-instance-choose-project.png)

### Choose a Location

- Select the data center where your server will be hosted: **TASHKENT** or **FERGANA**.

![Choose Location](../../images/create-instance-location.png)

### Choose an Image

- Select the operating system or application to install on the server. Images are grouped into tabs:
  - **Linux** — Ubuntu, CentOS, Debian, Rocky Linux, AlmaLinux, SUSE and other distributions, as well as network and telephony images (for example, MikroTik CHR, OPNsense, FreePBX).
  - **Windows** — Windows Server 2019, 2022 and 2025.
  - **Marketplace Apps** — ready-made application stacks, for example WordPress, GitLab Runner, Zabbix, Prometheus-Grafana, n8n, Jitsi Meet.
- Select the version in the drop-down list on the image card.

![Choose Image](../../images/create-instance-choose-images.png)

### Choose a Plan

- In **Compute Offering**, choose a plan based on the required number of vCPUs and amount of memory. Plans are grouped into **General Compute** and **GPU Compute** tabs; the monthly and hourly prices are shown for each plan.
- To set your own configuration, enter the number of vCPUs and the amount of memory in the **Custom Plan** row.

![Choose Plan](../../images/create-instance-choose-plan.png)

### Choose the OS Disk

- In **OS Disk Offering**, select the disk type (**SSD**, **HDD** or **NVMe**) and the disk offering. You can choose a preset size or enter your own size in GB.

![OS Disk Offering](../../images/create-instance-os-disk.png)

### Choose a Network

- **Isolated Network** — creates a new isolated network for the server in the selected location.
- **VPC Network** — creates a new VPC with full control over traffic routing, VPN gateway and site-to-site VPN connections.
- To attach the server to an existing network, select it in the list below. Additional charges apply for IP addresses in shared networks (for example, **Internet**).

![Choose Network](../../images/create-instance-choose-network.png)

- In **Public IP Address**, choose whether the server needs a public IPv4 address for access from the internet (enabled by default).

![Enable Public IP](../../images/create-instance-enable-public-ip.png)

### Affinity Groups (Optional)

- Select an affinity group to control how instances are placed on hypervisor hosts, or create one with **+ Create Affinity Groups**.

![Affinity Groups](../../images/select-ag.png)

### Configure Server Settings

- To access the server with an SSH key, click **Add now** next to **Add SSH Key To Your Instance**.
- **Note**: for some OS images, such as Arch Linux, an SSH key is required because password login is not supported.

![Add SSH Key](../../images/create-instance-add-ssh.png)

- Select one of your existing keys, or enter a name and paste the public key (it starts with `ssh-rsa` or `ssh-ed25519`) and click **Add SSH Key**. Never upload your private key.

![Add SSH Key Details](../../images/kb-10.png)

- To run commands automatically when the server starts for the first time, click **Add now** next to **Add Startup Script to your instance**, enter the script and click **Add Startup Script**.

![Add Startup Script](../../images/create-instance-add-startup-script.png)

### Advanced Settings (Optional)

- Turn on **Advanced Mode** to configure additional settings:
  - **Boot Mode** — Legacy or Secure boot.
  - **Boot Type** — UEFI or BIOS.
  - **Dynamic Scaling Enable** — allows changing the server resources without stopping it.

![Advanced Mode](../../images/create-instance-advance-mode.png)

- In **Select Addons**, you can add extra services to the server, for example **Antivirus**.

![Select Addons](../../images/create-instance-addons.png)

### Server Hostname

- The **Server Name** and **Server Hostname** are generated automatically. Change them to make the server easy to identify in your dashboard.

![Server Hostname](../../images/create-instance-server-hostname.png)

### Review and Deploy

- At the bottom of the page, choose the **Billing Cycle**: **Monthly** or **Yearly**. The **Price Summary** shows the cost of the selected configuration.
- Check the configuration and click **Review & Deploy** to create the instance.

![Review and Deploy](../../images/create-instance-depoly.png)

---

### Conclusion

Creating a Compute Instance on UzCloud is a straightforward process that gives you the flexibility and scalability you need. Regularly review and optimize your instance settings to use resources efficiently. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Instance Overview](instance-overview.md)**
> - **[Instance Backups](instance-backups.md)**
> - **[VM Activity Logs](vm-activity-logs.md)**
