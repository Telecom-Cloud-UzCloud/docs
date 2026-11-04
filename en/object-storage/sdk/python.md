# Python (boto3)

**boto3** is the official AWS SDK for Python.

## Installation

```bash
pip install boto3
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Example

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

`upload_file` and `download_file` automatically use **[multipart upload](../features/multipart-upload.md)** for large files.

> [!NOTE]
> The `request_checksum_calculation` and `response_checksum_validation` options are available in boto3 1.36 and later. In older versions, remove these two lines.

> [!TIP]
> **See also:**
>
> - **[SDK for S3](overview.md)**
