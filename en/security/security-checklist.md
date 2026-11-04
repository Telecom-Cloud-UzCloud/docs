# Security Checklist

## Keep Your Virtual Machines Secure

In UzCloud, the platform protects the infrastructure: data centers, hypervisors and the network. **What runs inside your VM is your responsibility**: the operating system, applications, accounts and open ports. Most attacks on cloud servers do not use exotic techniques. They exploit missing updates, weak passwords and ports open to the whole internet.

This checklist lists what to do on every VM. Each item links to a detailed guide.

---

### Right After Creating a VM

- [ ] **Sign in with SSH keys only.** Add an SSH key when you create the VM, then disable password login and direct root login. See **[SSH Hardening](ssh-hardening.md)**.
- [ ] **Install all updates and reboot.** A new VM may be created from an image that is several weeks old. See **[Update the Operating System](update-os.md)**.
- [ ] **Open only the ports you need.** Allow SSH (22) or RDP (3389) only from your IP addresses, never from `0.0.0.0/0`. See **[Network Access](network-access.md)**.
- [ ] **Set up backups.** Configure scheduled backups of the VM disks. See **[Backups](../backups/create-backups.md)** and **[Schedules](../schedules/schedules.md)**.

### Every Month

- [ ] Check that security updates are installed, and reboot the VM if the kernel was updated.
- [ ] Review the list of open ports and firewall rules, and remove the ones you no longer need.
- [ ] Check that the operating system is still supported by its vendor (end of life).
- [ ] Review the **Activity Logs** and **Login History** of your UzCloud account.

### Every Quarter

- [ ] Test restoring a VM from a backup. A backup that has never been restored is not a guarantee.
- [ ] Review the users of your UzCloud account and their roles, and remove the ones who no longer need access.
- [ ] Rotate API tokens and S3 access keys.

### Protect Your UzCloud Account

- [ ] Enable two-factor authentication. See **[Account Security](account-security.md)**.
- [ ] Give each employee their own user with the minimum required role instead of sharing one account.

---

### Current Vulnerability Alerts

When a critical vulnerability affects VMs of our clients, we publish an alert with instructions:

- **[CVE-2026-98432: Linux kernel TCP vulnerability](vulnerabilities/cve-2026-98432.md)** — November 4, 2026

> [!TIP]
> If your server is critical or something is unclear, contact **[support](../support/support.md)** before you start: we will help you plan the work.
