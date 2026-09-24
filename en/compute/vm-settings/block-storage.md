# Block Storage

## Block Storage Overview

Block Storage allows you to attach additional storage volumes to your virtual machine. These volumes act as independent, scalable disks that can be used for storing application data, backups, or other files. They are highly flexible and can be detached or re-attached to different instances without data loss. This is ideal for separating your operating system from application data to maintain modularity.

---

- To view a volume instance, go to the **VM settings** and navigate to the **Volume** section, where you can view the instance volume and its size.
- If you want to see previously created snapshots for the volume, click the right arrow icon to expand the list.
- To create a new snapshot, simply click the camera icon on the rightmost side. This will capture the current state of the volume, allowing you to restore it if needed.

![View Volume Instance](../../../images/vm-usage-volume.png)

---

### Conclusion

Block Storage provides a reliable and modular way to manage your data independently of your virtual machines. With the ability to create snapshots, scale volumes, and attach them across different instances, it ensures both flexibility and data protection. Use snapshots regularly to safeguard critical data, and manage storage efficiently through the VM settings panel.

> [!TIP]
> **See also:**
>
> - **[Create Volume](../../volumes/create-volume.md)**
> - **[Volume Snapshot](../../volume-snapshots/create-volume-snapshot.md)**
> - **[VM Snapshot](../../vm-snapshots/create-instance-snapshot.md)**
