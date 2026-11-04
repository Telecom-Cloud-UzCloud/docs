# S3 uchun SDK

UzCloud obyektli xotirasi rasmiy AWS SDK’lar bilan mos keladi. Ulanish uchun UzCloud manzilini, `default` mintaqasini va path-style manzillashni koʻrsating.

| Til | Kutubxona | Maqola |
|---|---|---|
| Python | boto3 | [Python](python.md) |
| JavaScript / Node.js | AWS SDK for JavaScript v3 | [JavaScript](javascript.md) |
| PHP | AWS SDK for PHP | [PHP](php.md) |
| Go | AWS SDK for Go v2 | [Go](go.md) |

## Har qanday SDK uchun sozlamalar

- **Manzil (endpoint):** `https://s3.uzcstorage.uz`
- **Mintaqa:** `default`
- **Path-style manzillash:** yoqilgan (`forcePathStyle`, `use_path_style_endpoint`, `UsePathStyle` va h. k.).
- **Nazorat yigʻindilari:** `when_required`. SDK’larning yangi versiyalari standart holatda har bir soʻrovga nazorat yigʻindisi sarlavhalarini qoʻshadi; bu sozlama ularni faqat S3 API talab qiladigan joyda qoldiradi.
- **Kalitlar:** **Credentials** oynasidagi Access Key va Secret Key — **[Vositalar va ulanish parametrlari](../tools/overview.md)** ga qarang.

> [!TIP]
> Oʻz S3 manzilini qoʻllab-quvvatlaydigan boshqa har qanday kutubxona ham mos keladi: masalan, Java va .NET uchun AWS SDK yoki MinIO mijozlari.
