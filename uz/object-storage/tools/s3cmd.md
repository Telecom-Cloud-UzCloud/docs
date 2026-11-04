# s3cmd

**s3cmd** — Linux va macOS uchun yengil konsol S3 mijozi. U serverlarda fayllarni oddiy yuklash, yuklab olish va sinxronlash uchun qulay.

## Oʻrnatish

```bash
sudo apt install s3cmd        # Ubuntu, Debian
sudo dnf install s3cmd        # Rocky Linux, AlmaLinux (EPEL)
pip install s3cmd             # any system with Python
```

## Sozlash

`~/.s3cfg` faylini yarating:

```ini
[default]
access_key = <Access Key>
secret_key = <Secret Key>
host_base = s3.uzcstorage.uz
host_bucket = s3.uzcstorage.uz
bucket_location = default
use_https = True
signature_v2 = False
```

Faylga kirishni cheklang — unda kalitlar saqlanadi:

```bash
chmod 600 ~/.s3cfg
```

> [!NOTE]
> `host_bucket = s3.uzcstorage.uz` (`%(bucket)s` siz) path-style manzillashni yoqadi.

## Fayllar bilan ishlash

```bash
s3cmd ls                                   # list buckets
s3cmd ls s3://my-bucket/                   # list objects
s3cmd put report.pdf s3://my-bucket/docs/  # upload
s3cmd get s3://my-bucket/docs/report.pdf   # download
s3cmd sync ./backups/ s3://my-bucket/backups/   # sync a folder
s3cmd del s3://my-bucket/docs/report.pdf   # delete
s3cmd du -H s3://my-bucket                 # bucket size
```

Bir soat amal qiladigan obyektga vaqtinchalik havola yarating:

```bash
s3cmd signurl s3://my-bucket/docs/report.pdf +3600
```

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
