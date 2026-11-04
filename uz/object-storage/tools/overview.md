# Obyektli xotira uchun vositalar

UzCloud obyektli xotirasi Amazon S3 API bilan mos keladi. U bilan konsoldan va istalgan S3 mijozidan ishlash mumkin: buyruqlar satri vositalari, fayl menejerlari va dasturlash tillari uchun SDK’lar.

## Ulanish parametrlari

Har qanday vosita bir xil parametrlarni talab qiladi:

| Parametr | Qiymat |
|---|---|
| Manzil (endpoint) | `https://s3.uzcstorage.uz` |
| Mintaqa | `default` |
| Manzillash usuli | path-style: `https://s3.uzcstorage.uz/<bucket>/<obyekt>` |
| Access Key / Secret Key | obyektli xotirangiz kalitlari |

### Kalitlarni qayerdan olish mumkin

1. Konsolda **Object Storage** ni oching va xotira nomini bosing.
2. **Credentials** ni bosing. Access Key **Access Keys** roʻyxatida koʻrsatiladi.
3. Secret Key **Create Key** bosilgandan keyin faqat 5 daqiqa davomida koʻrsatiladi. Uni darhol nusxalab, parollar menejerida saqlang. Agar maxfiy kalit yoʻqolgan boʻlsa, yangi kalit yarating va eskisini bekor qiling.

![S3 kirish maʼlumotlari](../../../images/ob-17.png)

**[Obyektli xotirani boshqarish](../../object-storage/manage-object-storage.md#kirish-maʼlumotlarini-koʻrish)** ga qarang.

> [!IMPORTANT]
> Bucket nomini konsolda koʻrsatilganidek aniq kiriting, masalan `demo-store-001045`.

## Vositani tanlash

| Vosita | Turi | Nima uchun qulay |
|---|---|---|
| [AWS CLI](aws-cli.md) | Buyruqlar satri | Skriptlar, avtomatlashtirish, S3’ning barcha imkoniyatlari |
| [s3cmd](s3cmd.md) | Buyruqlar satri | Linux serverlarda oddiy yuklash va sinxronlash |
| [rclone](rclone.md) | Buyruqlar satri | Sinxronlash, zaxira nusxalar, bulutlar oʻrtasida koʻchirish |
| [s3fs](s3fs.md) | Fayl tizimi | Bucketni Linux’da papka sifatida ulash |
| [Cyberduck](cyberduck.md) | Grafik | macOS va Windows’da fayllar bilan ishlash |
| [S3 Browser](s3-browser.md) | Grafik | Windows’da fayllar bilan ishlash |

Ilovalar uchun dasturlash tilingizga mos [SDK](../sdk/overview.md) dan foydalaning.
