# S3 orqali ulanish

UzCloud obyektli xotirasi Amazon S3 API bilan mos keladi: u bilan konsoldan va istalgan S3 mijozi yoki SDK’dan ishlash mumkin. Ushbu maqolada har qanday mijozga kerak boʻlgan parametrlar jamlangan.

## Ulanish parametrlari

| Parametr | Qiymat |
|---|---|
| Manzil (endpoint) | `https://s3.uzcstorage.uz` |
| Mintaqa | `default` |
| Manzillash usuli | path-style: `https://s3.uzcstorage.uz/<bucket>/<obyekt>` |
| Access Key / Secret Key | obyektli xotirangiz kalitlari |

> [!IMPORTANT]
> Bucket nomini konsolda koʻrsatilganidek aniq kiriting, masalan `demo-store-001045`.

## Kirish kalitlari

1. Konsolda **Object Storage** ni oching va xotira nomini bosing.
2. **Credentials** ni bosing. Access Key **Access Keys** roʻyxatida koʻrsatiladi.
3. Secret Key **Create Key** bosilgandan keyin faqat 5 daqiqa davomida koʻrsatiladi. Uni darhol nusxalab, parollar menejerida saqlang. Agar maxfiy kalit yoʻqolgan boʻlsa, yangi kalit yarating va eskisini bekor qiling.

![S3 kirish maʼlumotlari](../../images/ob-17.png)

**[Obyektli xotirani boshqarish](manage-object-storage.md#kirish-maʼlumotlarini-koʻrish)** ga qarang.

## Mijoz sozlamalari

Manzil, mintaqa va kalitlardan tashqari, vositangiz yoki SDK’da ikkita sozlamani tekshiring:

- **Path-style manzillash** yoqilgan boʻlishi kerak. Turli mijozlarda parametr turlicha nomlanadi: `addressing_style = path`, `forcePathStyle`, `use_path_style_endpoint`, `UsePathStyle`, `force_path_style`.
- **Nazorat yigʻindilari** — `when_required`. AWS CLI va AWS SDK’larning yangi versiyalari standart holatda har bir soʻrovga nazorat yigʻindisi sarlavhalarini qoʻshadi; bu sozlama ularni faqat S3 API talab qiladigan joyda qoldiradi.

Mashhur mijozlar uchun tayyor sozlamalar:

- Buyruqlar satri: **[AWS CLI](tools/aws-cli.md)**, **[s3cmd](tools/s3cmd.md)**, **[rclone](tools/rclone.md)**, **[s3fs](tools/s3fs.md)**.
- Fayl menejerlari: **[Cyberduck](tools/cyberduck.md)**, **[S3 Browser](tools/s3-browser.md)**.
- Dasturlash tillari: **[Python](sdk/python.md)**, **[JavaScript](sdk/javascript.md)**, **[PHP](sdk/php.md)**, **[Go](sdk/go.md)**.

> [!TIP]
> Oʻz S3 manzilini qoʻllab-quvvatlaydigan boshqa har qanday kutubxona yoki dastur ham mos keladi: masalan, Java va .NET uchun AWS SDK, MinIO mijozlari yoki S3’ni qoʻllab-quvvatlaydigan zaxira nusxalash dasturlari.
