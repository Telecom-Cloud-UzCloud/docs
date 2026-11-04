# Presigned URL

**Presigned URL** — временная ссылка, которая дает доступ к закрытому объекту без передачи ключей. С ее помощью можно дать клиенту скачать файл или позволить браузеру загрузить файл прямо в бакет.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

> [!NOTE]
> Presigned URL работает до истечения срока для любого, у кого она есть. Максимальный срок — 7 дней (604 800 секунд). Если отозвать ключ доступа, которым подписана ссылка, она перестанет работать.

## Ссылка на скачивание

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

Команда выводит ссылку, действующую один час. Такие ссылки умеют создавать и графические клиенты: **Share** в Cyberduck, **Generate Web URL** в S3 Browser.

## Ссылка на загрузку

AWS CLI создает только ссылки на скачивание. Ссылки на загрузку создаются через SDK, например на Python:

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

Загрузите файл по ссылке (`Content-Type` должен совпадать с указанным при подписи):

```bash
curl -X PUT -H "Content-Type: image/jpeg" --upload-file photo.jpg "<presigned URL>"
```

Для загрузки из браузера также настройте для бакета **[CORS](cors.md)**. Примеры для других языков — в разделе **[SDK](../sdk/overview.md)**.

> [!TIP]
> **См. также:**
>
> - **[Поддерживаемые возможности](overview.md)**
