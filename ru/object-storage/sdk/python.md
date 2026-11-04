# Python (boto3)

**boto3** — официальный AWS SDK для Python. Примеры рассчитаны на Python 3.9+ и boto3 1.36+.

## Установка

```bash
pip install "boto3>=1.36"
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Создание клиента

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

## Основные операции

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

## Список всех объектов

Один запрос возвращает не больше 1 000 объектов. Чтобы получить все объекты с префиксом, используйте пагинатор:

```python
paginator = s3.get_paginator("list_objects_v2")
for page in paginator.paginate(Bucket=BUCKET, Prefix="docs/"):
    for obj in page.get("Contents", []):
        print(obj["Key"], obj["Size"], obj["LastModified"])
```

## Большие файлы

`upload_file` и `download_file` делят большие файлы на части и передают их параллельно. Размер части и число потоков настраиваются через `TransferConfig`:

```python
from boto3.s3.transfer import TransferConfig

MB = 1024 * 1024
transfer = TransferConfig(multipart_threshold=64 * MB, multipart_chunksize=64 * MB, max_concurrency=8)

def progress(sent_bytes):
    print(f"+{sent_bytes} bytes")

s3.upload_file("backup.tar.gz", BUCKET, "backups/backup.tar.gz",
               Config=transfer, Callback=progress)
```

## Потоковая передача

Чтобы не загружать большой объект в память целиком, читайте и записывайте его частями:

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

## Presigned URL

Presigned URL дает временный доступ к объекту без передачи ключей. Ссылка на загрузку позволяет браузеру или другому сервису загрузить файл прямо в бакет — см. **[Presigned URL](../features/presigned-url.md)** и **[CORS](../features/cors.md)**.

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

## Ошибки и повторные попытки

Самые частые ошибки — отсутствующий объект (`NoSuchKey` или `404` для `HeadObject`) и нет доступа (`AccessDenied`, `403`). Сетевые ошибки и ответы `5xx` повторяются автоматически; число попыток задается при создании клиента.

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
> Для проектов на Django используйте **[django-storages](django.md)** вместо прямых вызовов boto3.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
