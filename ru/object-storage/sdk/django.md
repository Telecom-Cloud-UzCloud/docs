# Django

**django-storages** позволяет Django хранить загружаемые файлы (`FileField`, `ImageField`) и статику в объектном хранилище. Примеры рассчитаны на Django 4.2 и новее.

## Установка

```bash
pip install "django-storages[s3]>=1.14" "boto3>=1.36"
```

## Настройка

Передайте ключи через переменные окружения (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`) и добавьте настройки хранилища в `settings.py`. В этом примере пользовательские файлы закрыты, а статика лежит в папке `static/` с публичным доступом:

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

Откройте доступ на чтение к папке `static/` **[политикой бакета](../buckets/bucket-policy.md)** (в примере замените `public/*` на `static/*`) и загрузите статику:

```bash
python manage.py collectstatic --noinput
```

## Модели и файлы

Поля моделей работают как обычно — файлы сохраняются в бакет:

```python
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/%Y/%m/")

# In a view:
doc = Document.objects.create(title="Report", file=request.FILES["file"])
doc.file.url   # temporary link, valid for querystring_expire seconds
```

Работа с хранилищем напрямую:

```python
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

path = default_storage.save("exports/report.csv", ContentFile(b"id,name\n1,Demo\n"))
default_storage.exists(path)
with default_storage.open(path) as f:
    data = f.read()
default_storage.delete(path)
```

## Несколько хранилищ

Чтобы хранить часть файлов в отдельном бакете (например, публичные изображения), создайте класс хранилища и передайте его полю:

```python
from storages.backends.s3 import S3Storage

class PublicMediaStorage(S3Storage):
    bucket_name = "my-public-bucket"
    querystring_auth = False
    custom_domain = "s3.uzcstorage.uz/my-public-bucket"

class Product(models.Model):
    image = models.ImageField(upload_to="products/", storage=PublicMediaStorage())
```

Параметры подключения (`endpoint_url`, `region_name`, `client_config`) для такого класса берутся из переменных `AWS_S3_ENDPOINT_URL`, `AWS_S3_REGION_NAME` и `AWS_S3_CLIENT_CONFIG` в `settings.py`.

> [!TIP]
> Для прямой работы с S3 из кода на Python (мультипарт-загрузка, ссылки на загрузку) см. **[Python (boto3)](python.md)**.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
