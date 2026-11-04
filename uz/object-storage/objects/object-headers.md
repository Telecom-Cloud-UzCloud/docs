# Obyekt sarlavhalari

Har bir obyekt yuklab olinganda qaytariladigan HTTP sarlavhalarni saqlaydi. Ular brauzerga faylni qanday koʻrsatish va uni qancha vaqt keshlashni bildiradi. Obyekt bilan oʻz metamaʼlumotlaringizni ham saqlash mumkin.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

| Sarlavha | Nima qiladi | Misol |
|---|---|---|
| `Content-Type` | Fayl turi | `image/png`, `text/html; charset=utf-8` |
| `Cache-Control` | Brauzer va CDN’da keshlash | `public, max-age=86400` |
| `Content-Disposition` | Ochish oʻrniga yuklab olish, fayl nomi | `attachment; filename="report.pdf"` |
| `Content-Encoding` | Siqilgan tarkib | `gzip` |
| `x-amz-meta-*` | Oʻz metamaʼlumotlaringiz | `x-amz-meta-author: Demo` |

## Yuklashda sarlavhalarni belgilash

```bash
aws s3 cp ./logo.png s3://my-bucket/img/logo.png \
  --content-type image/png \
  --cache-control "public, max-age=31536000" \
  --metadata author=Demo
```

Papka yuklanganda AWS CLI `Content-Type` ni fayl kengaytmasi boʻyicha avtomatik aniqlaydi. `Cache-Control` ni barcha fayllar uchun bir vaqtda belgilash mumkin:

```bash
aws s3 sync ./static s3://my-bucket/static/ --cache-control "public, max-age=86400"
```

## Sarlavhalarni koʻrish

```bash
aws s3api head-object --bucket my-bucket --key img/logo.png
```

## Mavjud obyekt sarlavhalarini oʻzgartirish

Sarlavhalarni joyida oʻzgartirib boʻlmaydi. Obyektni yangi sarlavhalar bilan oʻziga nusxalang:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source my-bucket/docs/report.pdf \
  --metadata-directive REPLACE \
  --content-type application/pdf \
  --content-disposition 'attachment; filename="report.pdf"'
```

> [!NOTE]
> `--metadata-directive REPLACE` bilan siz koʻrsatmagan barcha sarlavhalar va metamaʼlumotlar tiklanadi. Buyruqda barcha kerakli sarlavhalarni koʻrsating.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
