# Presigned URL

A **presigned URL** is a temporary link that gives access to a private object without sharing your keys. Use it to let a client download a file or to let a browser upload a file directly to the bucket.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

> [!NOTE]
> A presigned URL works until it expires, for anyone who has it. The maximum lifetime is 7 days (604,800 seconds). If you revoke the access key used to sign the link, the link stops working.

## Link for Downloading

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

The command prints a link that is valid for one hour. Graphical clients can also create such links: **Share** in Cyberduck, **Generate Web URL** in S3 Browser.

## Link for Uploading

AWS CLI creates only download links. Upload links are created with an SDK, for example in Python:

```python
import boto3
from botocore.config import Config

s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.uzcstorage.uz",
    region_name="default",
    config=Config(signature_version="s3v4", s3={"addressing_style": "path"}),
)

url = s3.generate_presigned_url(
    "put_object",
    Params={"Bucket": "my-bucket", "Key": "uploads/photo.jpg", "ContentType": "image/jpeg"},
    ExpiresIn=600,
)
print(url)
```

Upload a file using the link (the `Content-Type` must match the one used when signing):

```bash
curl -X PUT -H "Content-Type: image/jpeg" --upload-file photo.jpg "<presigned URL>"
```

To upload from a browser, also configure **[CORS](../buckets/cors.md)** for the bucket. Examples for other languages: **[JavaScript](../sdk/javascript.md)**, **[PHP](../sdk/php.md)**, **[Go](../sdk/go.md)**.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
