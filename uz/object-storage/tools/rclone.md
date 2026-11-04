# rclone

**rclone** — fayllarni bulutli xotiralar bilan sinxronlash vositasi. U zaxira nusxalash va maʼlumotlarni bulutlar oʻrtasida koʻchirish uchun juda mos, shuningdek bucketni papka sifatida ulay oladi.

## Oʻrnatish

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

Windows va macOS uchun rclone’ni [rclone.org/downloads](https://rclone.org/downloads/) dan yuklab oling.

## Sozlash

`~/.config/rclone/rclone.conf` fayliga ulanish qoʻshing:

```ini
[uzcloud]
type = s3
provider = Ceph
access_key_id = <Access Key>
secret_access_key = <Secret Key>
endpoint = https://s3.uzcstorage.uz
force_path_style = true
acl = private
```

Ulanishni `rclone config` buyrugʻi bilan interaktiv tarzda ham yaratish mumkin: **Amazon S3 Compliant Storage Providers** ni, soʻng **Ceph Object Storage** ni tanlang va kalitlar hamda manzilni kiriting.

## Fayllar bilan ishlash

```bash
rclone lsd uzcloud:                          # list buckets
rclone ls uzcloud:my-bucket                  # list objects
rclone copy ./report.pdf uzcloud:my-bucket/docs/
rclone copy uzcloud:my-bucket/docs/ ./docs/  # download
rclone sync ./site uzcloud:my-bucket/site --progress
rclone delete uzcloud:my-bucket/tmp/
```

> [!WARNING]
> `rclone sync` qabul qiluvchini manbaga aynan oʻxshash qiladi va qabul qiluvchida manbada yoʻq fayllarni **oʻchiradi**. Avval natijani `--dry-run` bilan tekshiring.

## Bucketni papka sifatida ulash

```bash
mkdir -p ~/s3
rclone mount uzcloud:my-bucket ~/s3 --vfs-cache-mode writes --daemon
```

Uzish uchun: `fusermount -u ~/s3` (Linux) yoki `umount ~/s3` (macOS).

## Boshqa bulutdan koʻchirish

Manba xotira uchun ikkinchi ulanishni qoʻshing va maʼlumotlarni bevosita nusxalang:

```bash
rclone copy old-cloud:source-bucket uzcloud:my-bucket --transfers 16 --progress
```

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Vositalar va ulanish parametrlari](overview.md)**
