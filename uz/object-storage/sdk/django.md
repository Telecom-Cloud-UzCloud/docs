# Django

**django-storages** Django’ga yuklanadigan fayllarni (`FileField`, `ImageField`) va statik fayllarni obyektli xotirada saqlash imkonini beradi. Misollar Django 4.2 va undan yangi versiyalar uchun moʻljallangan.

## Oʻrnatish

```bash
pip install "django-storages[s3]>=1.14" "boto3>=1.36"
```

## Sozlash

Kalitlarni muhit oʻzgaruvchilari (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) orqali uzating va xotira sozlamalarini `settings.py` ga qoʻshing. Ushbu misolda foydalanuvchi fayllari yopiq, statik fayllar esa ommaviy kirishga ega `static/` papkasida:

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

`static/` papkasiga **[bucket siyosati](../buckets/bucket-policy.md)** yordamida oʻqish huquqini oching (misolda `public/*` ni `static/*` ga almashtiring) va statik fayllarni yuklang:

```bash
python manage.py collectstatic --noinput
```

## Modellar va fayllar

Model maydonlari odatdagidek ishlaydi — fayllar bucketga saqlanadi:

```python
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/%Y/%m/")

# In a view:
doc = Document.objects.create(title="Report", file=request.FILES["file"])
doc.file.url   # temporary link, valid for querystring_expire seconds
```

Xotira bilan bevosita ishlash:

```python
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

path = default_storage.save("exports/report.csv", ContentFile(b"id,name\n1,Demo\n"))
default_storage.exists(path)
with default_storage.open(path) as f:
    data = f.read()
default_storage.delete(path)
```

## Bir nechta xotira

Fayllarning bir qismini alohida bucketda saqlash uchun (masalan, ommaviy rasmlar) xotira sinfini yarating va uni maydonga uzating:

```python
from storages.backends.s3 import S3Storage

class PublicMediaStorage(S3Storage):
    bucket_name = "my-public-bucket"
    querystring_auth = False
    custom_domain = "s3.uzcstorage.uz/my-public-bucket"

class Product(models.Model):
    image = models.ImageField(upload_to="products/", storage=PublicMediaStorage())
```

Bunday sinf uchun ulanish parametrlari (`endpoint_url`, `region_name`, `client_config`) `settings.py` dagi `AWS_S3_ENDPOINT_URL`, `AWS_S3_REGION_NAME` va `AWS_S3_CLIENT_CONFIG` oʻzgaruvchilaridan olinadi.

> [!TIP]
> Python kodidan S3 bilan bevosita ishlash uchun (multipart yuklash, yuklash havolalari) **[Python (boto3)](python.md)** ga qarang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
