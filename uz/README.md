# UzCloud hujjatlari

UzCloud bulutni boshqarish konsoli boʻyicha foydalanuvchi qoʻllanmasi — **[console.uzcloud.uz](https://console.uzcloud.uz)**.

Boshqa tillar: [English](../en/README.md) · [Русский](../ru/README.md)

## Mundarija

### Ishni boshlash

- [Kirish](getting-started/introduction.md)
- [Profilni sozlash](getting-started/profile-setup.md)

### Xavfsizlik

- [Xavfsizlik boʻyicha nazorat roʻyxati](security/security-checklist.md)
- [Operatsion tizimni yangilash](security/update-os.md)
- [SSH himoyasi](security/ssh-hardening.md)
- [Tarmoqqa kirish](security/network-access.md)
- [Hisob xavfsizligi](security/account-security.md)
- [CVE-2026-98432: Linux yadrosidagi TCP zaifligi](security/vulnerabilities/cve-2026-98432.md)

### Loyihalar

- [Loyiha yaratish](projects/create-project.md)

### Hisoblash

- [Virtual mashina](compute/compute-instance.md)
- [Virtual mashina sharhi](compute/instance-overview.md)
- [Resurslar monitoringi](compute/monitoring-resources.md)
- **VM sozlamalari**
  - [Blokli xotira](compute/vm-settings/block-storage.md)
  - [Tarif rejasini oʻzgartirish](compute/vm-settings/change-plan.md)
  - [Xost nomini oʻzgartirish](compute/vm-settings/change-hostname.md)
  - [OT’ni oʻzgartirish](compute/vm-settings/change-os.md)
  - [Parolni tiklash](compute/vm-settings/reset-password.md)
  - [Ishga tushirish skriptini oʻzgartirish](compute/vm-settings/change-startup-script.md)
  - [Tarmoqlararo ekran](compute/vm-settings/firewall.md)
  - [Portlarni yoʻnaltirish](compute/vm-settings/port-forwarding.md)
  - [Tarmoqlar](compute/vm-settings/networks.md)
  - [SSH kalitlar](compute/vm-settings/ssh-keys.md)
  - [VM parametrlari](compute/vm-settings/settings.md)
- [Konsolga kirish](compute/console-access.md)
- [VM zaxira nusxalari](compute/instance-backups.md)
- [VM faoliyat jurnali](compute/vm-activity-logs.md)
- [SSH orqali ulanish](compute/connect-with-ssh.md)
- [RDP orqali ulanish](compute/connect-with-rdp.md)

### Disklar

- [Disk yaratish](volumes/create-volume.md)

### Disk snapshotlari

- [Disk snapshotini yaratish](volume-snapshots/create-volume-snapshot.md)

### VM snapshotlari

- [VM snapshotini yaratish](vm-snapshots/create-instance-snapshot.md)

### Zaxira nusxalar

- [Zaxira nusxalar yaratish](backups/create-backups.md)

### Jadvallar

- [Jadvallar](schedules/schedules.md)

### Shablonlar

- [Shablonlar yaratish](templates/create-templates.md)

### ISO obrazlar

- [ISO import qilish](iso/import-iso.md)

### Affinity guruhlari

- [Affinity guruhlarini yaratish](affinity-groups/create-affinity-groups.md)

### Kubernetes

- [Kubernetes klasterini yaratish](kubernetes/create-kubernetes-cluster.md)
- [Kubernetes klasteri sharhi](kubernetes/kubernetes-cluster-overview.md)
- [CLI orqali Kubernetes klasteri](kubernetes/kubernetes-cluster-via-cli.md)
- [Kubernetes Dashboard’ga kirish](kubernetes/kubernetes-dashboard-ui-access.md)

### Obyektli xotira (Ceph)

- [Obyektli xotira yaratish](object-storage/create-object-storage.md)
- [Obyektli xotirani boshqarish](object-storage/manage-object-storage.md)
- [S3 orqali ulanish](object-storage/connection.md)
- **Bucketlar bilan ishlash**
  - [Obyektlarni versiyalash](object-storage/buckets/versioning.md)
  - [Object Lock](object-storage/buckets/object-lock.md)
  - [Obyektlarning hayot sikli](object-storage/buckets/lifecycle.md)
  - [CORS’ni sozlash](object-storage/buckets/cors.md)
  - [Bucket Policy](object-storage/buckets/bucket-policy.md)
  - [Statik sayt](object-storage/buckets/static-website.md)
- **Obyektlar bilan ishlash**
  - [Obyekt sarlavhalari](object-storage/objects/object-headers.md)
  - [Multipart yuklash](object-storage/objects/multipart-upload.md)
  - [Presigned URL](object-storage/objects/presigned-url.md)
- **Vositalar**
  - [AWS CLI](object-storage/tools/aws-cli.md)
  - [s3cmd](object-storage/tools/s3cmd.md)
  - [rclone](object-storage/tools/rclone.md)
  - [s3fs](object-storage/tools/s3fs.md)
  - [Cyberduck](object-storage/tools/cyberduck.md)
  - [S3 Browser](object-storage/tools/s3-browser.md)
  - [S3 Explorer](object-storage/tools/s3-explorer.md)
- **Koddan ishlash**
  - [Python (boto3)](object-storage/sdk/python.md)
  - [JavaScript (Node.js)](object-storage/sdk/javascript.md)
  - [PHP](object-storage/sdk/php.md)
  - [Go](object-storage/sdk/go.md)
  - [Java](object-storage/sdk/java.md)
  - [C# / .NET](object-storage/sdk/dotnet.md)
  - [Laravel](object-storage/sdk/laravel.md)
  - [Django](object-storage/sdk/django.md)
- **Amaliy misollar**
  - [restic bilan server zaxira nusxalari](object-storage/examples/server-backup-restic.md)
  - [Maʼlumotlar bazalari zaxira nusxalari](object-storage/examples/database-backup.md)
  - [S3’ni Nginx orqali proksilash](object-storage/examples/nginx-proxy.md)

### Tarmoqlar

- **VPC tarmogʻi**
  - [VPC tarmoqlarini yaratish](networks/vpc-network/create-vpc-network.md)
  - [Tarmoq sharhi](networks/vpc-network/network-overview.md)
  - [Tarmoq qoʻshish](networks/vpc-network/add-network.md)
  - [Ommaviy IP manzil](networks/vpc-network/public-ip-address.md)
  - [Tarmoq ACL roʻyxati](networks/vpc-network/network-acl-list.md)
  - [VPN shlyuzi](networks/vpc-network/vpn-gateway.md)
  - [VPN ulanishlari](networks/vpc-network/vpn-connections.md)
  - [Bogʻlangan VM’lar](networks/vpc-network/associated-vms.md)
- **Ommaviy tarmoq**
  - [Ommaviy tarmoq yaratish](networks/public-network/create-public-network.md)
  - [Tarmoq sharhi](networks/public-network/network-overview.md)
  - [Chiquvchi trafik qoidalari](networks/public-network/egress-rules.md)
  - [Ommaviy IP manzillar](networks/public-network/public-ip-addresses.md)
  - [Bogʻlangan VM’lar](networks/public-network/associated-vms.md)
- [Ommaviy IP manzil](networks/public-ip-address.md)
- [VPN foydalanuvchilari](networks/vpn-users.md)
- [Mijoz VPN shlyuzi](networks/vpn-customer-gateway.md)

### Yuklama muvozanatlagich

- [Yuklama muvozanatlagich](load-balancer/load-balancer.md)

### Billing

- [Billing xulosasi](billing/billing-summary.md)
- [Obunalar](billing/subscriptions.md)
- [Tranzaksiyalar](billing/transactions.md)
- [Akkaunt boʻyicha koʻchirma](billing/account-statement.md)

### Qoʻllab-quvvatlash

- [Qoʻllab-quvvatlash](support/support.md)
