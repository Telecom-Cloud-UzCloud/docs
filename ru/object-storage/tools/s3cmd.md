# s3cmd

**s3cmd** — легкий консольный S3-клиент для Linux и macOS. Он удобен для простой загрузки, скачивания и синхронизации файлов на серверах.

## Установка

```bash
sudo apt install s3cmd        # Ubuntu, Debian
sudo dnf install s3cmd        # Rocky Linux, AlmaLinux (EPEL)
pip install s3cmd             # any system with Python
```

## Настройка

Создайте файл `~/.s3cfg`:

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

Ограничьте доступ к файлу — в нем хранятся ключи:

```bash
chmod 600 ~/.s3cfg
```

> [!NOTE]
> `host_bucket = s3.uzcstorage.uz` (без `%(bucket)s`) включает адресацию path-style.

## Работа с файлами

```bash
s3cmd ls                                   # list buckets
s3cmd ls s3://my-bucket/                   # list objects
s3cmd put report.pdf s3://my-bucket/docs/  # upload
s3cmd get s3://my-bucket/docs/report.pdf   # download
s3cmd sync ./backups/ s3://my-bucket/backups/   # sync a folder
s3cmd del s3://my-bucket/docs/report.pdf   # delete
s3cmd du -H s3://my-bucket                 # bucket size
```

Создайте временную ссылку на объект, действующую один час:

```bash
s3cmd signurl s3://my-bucket/docs/report.pdf +3600
```

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
