# Presigned URL

**Presigned URL** — kalitlarni bermasdan yopiq obyektga kirish imkonini beradigan vaqtinchalik havola. Uning yordamida mijozga faylni yuklab olish yoki brauzerga faylni bevosita bucketga yuklash imkonini berish mumkin.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

> [!NOTE]
> Presigned URL muddati tugaguncha unga ega boʻlgan har kim uchun ishlaydi. Maksimal muddat — 7 kun (604 800 soniya). Agar havola imzolangan kirish kalitini bekor qilsangiz, havola ishlashdan toʻxtaydi.

## Yuklab olish uchun havola

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

Buyruq bir soat amal qiladigan havolani chiqaradi. Bunday havolalarni grafik mijozlar ham yarata oladi: Cyberduck’da **Share**, S3 Browser’da **Generate Web URL**.

## Yuklash uchun havola

AWS CLI faqat yuklab olish havolalarini yaratadi. Yuklash havolalari SDK orqali yaratiladi, masalan Python’da:

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

Faylni havola orqali yuklang (`Content-Type` imzolashda koʻrsatilgan bilan mos kelishi kerak):

```bash
curl -X PUT -H "Content-Type: image/jpeg" --upload-file photo.jpg "<presigned URL>"
```

Brauzerdan yuklash uchun bucket uchun **[CORS](../buckets/cors.md)** ni ham sozlang. Boshqa tillar uchun misollar: **[JavaScript](../sdk/javascript.md)**, **[PHP](../sdk/php.md)**, **[Go](../sdk/go.md)**.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
