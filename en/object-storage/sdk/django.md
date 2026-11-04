# Django

**django-storages** lets Django store uploaded files (`FileField`, `ImageField`) and static files in object storage. The examples are for Django 4.2 or later.

## Installation

```bash
pip install "django-storages[s3]>=1.14" "boto3>=1.36"
```

## Configuration

Pass the keys through environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) and add the storage settings to `settings.py`. In this example, user files are private, and static files are in the `static/` folder with public access:

```python
from botocore.config import Config

S3_OPTIONS = {
    "bucket_name": "my-bucket",
    "endpoint_url": "https://s3.uzcstorage.uz",
    "region_name": "default",
    "client_config": Config(
        signature_version="s3v4",
        s3={"addressing_style": "path"},
        request_checksum_calculation="when_required",
        response_checksum_validation="when_required",
    ),
}

STORAGES = {
    # Uploaded files: private, accessed by temporary links
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            **S3_OPTIONS,
            "location": "media",
            "default_acl": None,
            "querystring_auth": True,
            "querystring_expire": 3600,
            "file_overwrite": False,
        },
    },
    # Static files: public, permanent links
    "staticfiles": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            **S3_OPTIONS,
            "location": "static",
            "default_acl": None,
            "querystring_auth": False,
            "custom_domain": "s3.uzcstorage.uz/my-bucket",
        },
    },
}
```

Open read access to the `static/` folder with a **[bucket policy](../features/bucket-policy.md)** (replace `public/*` with `static/*` in the example), then upload the static files:

```bash
python manage.py collectstatic --noinput
```

## Models and Files

Model fields work as usual — the files are saved to the bucket:

```python
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/%Y/%m/")

# In a view:
doc = Document.objects.create(title="Report", file=request.FILES["file"])
doc.file.url   # temporary link, valid for querystring_expire seconds
```

Working with storage directly:

```python
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

path = default_storage.save("exports/report.csv", ContentFile(b"id,name\n1,Demo\n"))
default_storage.exists(path)
with default_storage.open(path) as f:
    data = f.read()
default_storage.delete(path)
```

## Several Storages

To keep some files in a separate bucket (for example, public images), create a storage class and pass it to the field:

```python
from storages.backends.s3 import S3Storage

class PublicMediaStorage(S3Storage):
    bucket_name = "my-public-bucket"
    querystring_auth = False
    custom_domain = "s3.uzcstorage.uz/my-public-bucket"

class Product(models.Model):
    image = models.ImageField(upload_to="products/", storage=PublicMediaStorage())
```

Connection settings (`endpoint_url`, `region_name`, `client_config`) for such a class are taken from the `AWS_S3_ENDPOINT_URL`, `AWS_S3_REGION_NAME` and `AWS_S3_CLIENT_CONFIG` variables in `settings.py`.

> [!TIP]
> For direct work with S3 in Python code (multipart uploads, presigned upload links), see **[Python (boto3)](python.md)**.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
