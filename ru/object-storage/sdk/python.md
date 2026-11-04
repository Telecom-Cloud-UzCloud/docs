# Python (boto3)

**boto3** — официальный AWS SDK для Python.

## Установка

```bash
pip install boto3
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Пример

```python
import boto3
from botocore.config import Config

s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.uzcstorage.uz",
    region_name="default",
    config=Config(
        signature_version="s3v4",
        s3={"addressing_style": "path"},
        request_checksum_calculation="when_required",
        response_checksum_validation="when_required",
    ),
)

BUCKET = "my-bucket"

# 1. Upload a file
s3.upload_file("report.pdf", BUCKET, "docs/report.pdf",
               ExtraArgs={"ContentType": "application/pdf"})

# 2. List objects
resp = s3.list_objects_v2(Bucket=BUCKET, Prefix="docs/")
for obj in resp.get("Contents", []):
    print(obj["Key"], obj["Size"])

# 3. Download a file
s3.download_file(BUCKET, "docs/report.pdf", "report-copy.pdf")

# 4. Temporary download link (1 hour)
url = s3.generate_presigned_url("get_object",
                                Params={"Bucket": BUCKET, "Key": "docs/report.pdf"},
                                ExpiresIn=3600)
print(url)

# 5. Delete an object
s3.delete_object(Bucket=BUCKET, Key="docs/report.pdf")
```

`upload_file` и `download_file` автоматически используют **[мультипарт-загрузку](../features/multipart-upload.md)** для больших файлов.

> [!NOTE]
> Параметры `request_checksum_calculation` и `response_checksum_validation` доступны в boto3 1.36 и новее. В более старых версиях удалите эти две строки.

> [!TIP]
> **См. также:**
>
> - **[SDK для S3](overview.md)**
