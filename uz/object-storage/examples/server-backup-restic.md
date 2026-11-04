# restic bilan server zaxira nusxalari

**restic** — maʼlumotlarni shifrlaydigan, faqat oʻzgargan bloklarni saqlaydigan (deduplikatsiya) va nusxalar tarixini yuritadigan zaxira nusxalash vositasi. Linux, macOS va Windows’da ishlaydi.

## Oʻrnatish

```bash
sudo apt install restic        # Ubuntu, Debian
sudo dnf install restic        # Rocky Linux, AlmaLinux (EPEL)
```

## Sozlash

Ulanish parametrlari bilan fayl yarating, masalan `/root/.restic-env`:

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
export RESTIC_REPOSITORY=s3:https://s3.uzcstorage.uz/my-backups/server-1
export RESTIC_PASSWORD_FILE=/root/.restic-password
```

```bash
openssl rand -base64 32 > /root/.restic-password
chmod 600 /root/.restic-env /root/.restic-password
```

> [!WARNING]
> restic zaxira nusxalarni shu parol bilan shifrlaydi. **Parolsiz maʼlumotlarni tiklab boʻlmaydi.** Uning nusxasini serverdan tashqarida, masalan, parollar menejerida saqlang.

Repozitoriyni ishga tushiring:

```bash
source /root/.restic-env
restic -o s3.bucket-lookup=path -o s3.region=default init
```

## Zaxira nusxa yaratish

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R backup /etc /var/www /home --exclude-caches
$R snapshots
```

## Avtomatlashtirish va rotatsiya

`/usr/local/bin/restic-backup.sh` skriptini yarating: u zaxira nusxa yaratadi va 7 ta kundalik, 4 ta haftalik va 6 ta oylik nusxani saqlaydi:

```bash
#!/bin/bash
set -e
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"
$R backup /etc /var/www /home --exclude-caches --quiet
$R forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune --quiet
```

Uni bajariladigan qiling va cron orqali har kecha soat 03:00 da ishga tushiring:

```bash
sudo chmod 700 /usr/local/bin/restic-backup.sh
echo "0 3 * * * root /usr/local/bin/restic-backup.sh >> /var/log/restic.log 2>&1" | sudo tee /etc/cron.d/restic
```

## Tiklash

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R restore latest --target /restore                      # the whole latest backup
$R restore latest --target /restore --include /etc/nginx # one folder
$R check                                                 # verify the repository
```

Tiklashni muntazam tekshiring: hech qachon tiklanmagan zaxira nusxa kafolat emas.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
