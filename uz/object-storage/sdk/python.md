# Python (boto3)

**boto3** — Python uchun rasmiy AWS SDK.

## Oʻrnatish

```bash
pip install boto3
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Misol

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

`upload_file` va `download_file` katta fayllar uchun **[multipart yuklashdan](../features/multipart-upload.md)** avtomatik foydalanadi.

> [!NOTE]
> `request_checksum_calculation` va `response_checksum_validation` parametrlari boto3 1.36 va undan yangi versiyalarda mavjud. Eski versiyalarda bu ikki qatorni oʻchiring.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[S3 uchun SDK](overview.md)**
