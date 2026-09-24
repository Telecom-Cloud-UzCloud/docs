# Create Volume

## Block Storage Volumes

**Block storage volumes** provide scalable NVMe SSD storage that can be attached to virtual machines, offering additional capacity for your data. Once attached, you can manually format and mount the volume to extend your VM's storage.

**UzCloud** simplifies the deployment and management of Block Storage, enabling users to scale and adapt their infrastructure based on demand. This guide will walk you through the process of creating and attaching a block storage volume using **UzCloud**.

---

### Creating a Block Storage Volume on UzCloud

- From the left-hand menu, click on the **Block Storages** tab.
- You will be redirected to the **Create Block Storage Volume** page.

![Create Block Storage](../../images/create-block-storages.png)

- To create a volume, click on **Create Block Storage** or the **plus (+)** icon located on the right side of the Create Block Storage page.

### Choose a Location

- Select the data center location where your server will be physically hosted.
- Choose from the available locations listed.

![Choose Location](../../images/create-block-storages-location.png)

### Assign to a Project

- Assign the block storage volume to one of your projects to organize and manage resources effectively.

![Assign to Project](../../images/create-block-storages-select-project.png)

### Choose Instance

- Select the virtual machine instance to which you want this block storage volume to be attached.

![Choose Instance](../../images/create-block-storages-select-instance.png)

### Select Volume Size

- Select a volume size based on your requirements like **Storage Type** and **Size**. You can also create a custom volume if needed.
- These are some available options and their plans:

![Select Volume Size](../../images/create-block-storages-select-volume-size.png)

### Choose Volume Name

- Provide a unique **Volume Name** for your volume to identify it easily in your dashboard.

![Choose Volume Name](../../images/create-block-storages-name.png)

### Create Volume

- Choose the desired **Billing Cycle** for your volume. Volume supports Hourly, Monthly, Quarterly, Semiannually, Yearly, Bi-annually, and Tri-annually billing cycles.
- The supported billing rules are Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata, and Unfixed Prorata.
- It supports multiple packages based on SSD size and data center location. This ensures flexibility in performance and regional data preferences.
- Verify all the configuration details and review the price summary. Click on **Create Volume** to create the volume.

![Create Volume](../../images/create-block-storages-deploy.png)

### Conclusion

By following this guide, you can easily create and manage block storage volumes on UzCloud. These volumes provide scalable and high-performance storage solutions for your virtual machines, enabling you to meet your data storage needs efficiently. For further assistance, refer to the UzCloud documentation or reach out to support.

> [!TIP]
> **See also:**
>
> - **[Volume Snapshot](../volume-snapshots/create-volume-snapshot.md)**
> - **[VM Snapshot](../vm-snapshots/create-instance-snapshot.md)**
> - **[Create Backups](../backups/create-backups.md)**
