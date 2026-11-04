# Python (boto3)

**boto3** is the official AWS SDK for Python. The examples require Python 3.9 or later and boto3 1.36 or later.

## Installation

```bash
pip install "boto3>=1.36"
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Create a Client

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
        retries={"max_attempts": 5, "mode": "standard"},
    ),
)
BUCKET = "my-bucket"
```

## Basic Operations

```python
# Upload a file
s3.upload_file("report.pdf", BUCKET, "docs/report.pdf",
               ExtraArgs={"ContentType": "application/pdf"})

# Upload bytes or a string
s3.put_object(Bucket=BUCKET, Key="docs/hello.txt", Body=b"Hello, UzCloud!")

# Download a file
s3.download_file(BUCKET, "docs/report.pdf", "report-copy.pdf")

# Read an object into memory (small objects only)
text = s3.get_object(Bucket=BUCKET, Key="docs/hello.txt")["Body"].read().decode()

# Copy and delete
s3.copy_object(Bucket=BUCKET, Key="archive/report.pdf",
               CopySource={"Bucket": BUCKET, "Key": "docs/report.pdf"})
s3.delete_object(Bucket=BUCKET, Key="docs/report.pdf")

# Delete up to 1,000 objects in one request
s3.delete_objects(Bucket=BUCKET, Delete={"Objects": [{"Key": "tmp/a.txt"}, {"Key": "tmp/b.txt"}]})
```

## List All Objects

One request returns at most 1,000 objects. To get all objects with a prefix, use a paginator:

```python
paginator = s3.get_paginator("list_objects_v2")
for page in paginator.paginate(Bucket=BUCKET, Prefix="docs/"):
    for obj in page.get("Contents", []):
        print(obj["Key"], obj["Size"], obj["LastModified"])
```

## Large Files

`upload_file` and `download_file` split large files into parts and transfer them in parallel. Tune the part size and the number of threads with `TransferConfig`:

```python
from boto3.s3.transfer import TransferConfig

MB = 1024 * 1024
transfer = TransferConfig(multipart_threshold=64 * MB, multipart_chunksize=64 * MB, max_concurrency=8)

def progress(sent_bytes):
    print(f"+{sent_bytes} bytes")

s3.upload_file("backup.tar.gz", BUCKET, "backups/backup.tar.gz",
               Config=transfer, Callback=progress)
```

## Streaming

To avoid loading a large object into memory, read and write it in chunks:

```python
# Upload from any file-like object (for example, an uploaded file in a web app)
with open("video.mp4", "rb") as f:
    s3.upload_fileobj(f, BUCKET, "media/video.mp4", Config=transfer)

# Download in 1 MB chunks
body = s3.get_object(Bucket=BUCKET, Key="media/video.mp4")["Body"]
with open("video-copy.mp4", "wb") as f:
    for chunk in body.iter_chunks(chunk_size=MB):
        f.write(chunk)
```

## Presigned URLs

A presigned URL gives temporary access to an object without sharing your keys. An upload link lets a browser or another service upload a file directly to the bucket — see **[Presigned URL](../features/presigned-url.md)** and **[CORS](../features/cors.md)**.

```python
# Download link, valid for 1 hour
url = s3.generate_presigned_url("get_object",
                                Params={"Bucket": BUCKET, "Key": "docs/report.pdf"},
                                ExpiresIn=3600)

# Upload link, valid for 10 minutes. The client must send the same Content-Type.
upload_url = s3.generate_presigned_url("put_object",
                                       Params={"Bucket": BUCKET, "Key": "uploads/photo.jpg",
                                               "ContentType": "image/jpeg"},
                                       ExpiresIn=600)
```

## Errors and Retries

The most common errors are a missing object (`NoSuchKey`, or `404` for `HeadObject`) and no access (`AccessDenied`, `403`). Network errors and `5xx` responses are retried automatically; the number of attempts is set when you create the client.

```python
from botocore.exceptions import ClientError

def object_exists(key: str) -> bool:
    try:
        s3.head_object(Bucket=BUCKET, Key=key)
        return True
    except ClientError as e:
        if e.response["Error"]["Code"] in ("404", "NoSuchKey"):
            return False
        raise

try:
    s3.get_object(Bucket=BUCKET, Key="missing.txt")
except ClientError as e:
    code = e.response["Error"]["Code"]
    if code == "NoSuchKey":
        print("Object not found")
    elif code == "AccessDenied":
        print("Check the keys and the bucket policy")
    else:
        raise
```

> [!TIP]
> For Django projects, use **[django-storages](django.md)** instead of calling boto3 directly.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
