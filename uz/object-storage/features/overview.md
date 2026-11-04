# Qoʻllab-quvvatlanadigan imkoniyatlar

UzCloud obyektli xotirasi Ceph asosida qurilgan va Amazon S3 API’ning asosiy imkoniyatlarini qoʻllab-quvvatlaydi. Jadvalda imkoniyatlar va ular bilan ishlash usullari keltirilgan.

| Imkoniyat | Nima uchun | Konsol | S3 API |
|---|---|---|---|
| [Versiyalash](versioning.md) | Obyektlarning oldingi versiyalarini saqlash | ✓ | ✓ |
| [Object Lock](object-lock.md) | Obyektlarni oʻchirishdan himoya qilish (WORM) | ✓ | ✓ |
| [Hayot sikli](lifecycle.md) | Eski obyektlarni avtomatik oʻchirish | — | ✓ |
| [CORS](cors.md) | Boshqa domenlardagi veb-sahifalardan kirish | — | ✓ |
| [Bucket Policy](bucket-policy.md) | Bucketga kirish qoidalari | ✓ | ✓ |
| [Obyekt sarlavhalari](object-headers.md) | Content-Type, Cache-Control, metamaʼlumotlar | — | ✓ |
| [Multipart yuklash](multipart-upload.md) | Katta fayllarni qismlarga boʻlib yuklash | — | ✓ |
| [Presigned URL](presigned-url.md) | Yopiq obyektlarga vaqtinchalik havolalar | — | ✓ |
| [Statik sayt](static-website.md) | Bucketda statik sayt joylashtirish | — | ✓ |

Konsolda mavjud boʻlmagan imkoniyatlar uchun **[vositalar](../tools/overview.md)** yoki **[SDK](../sdk/overview.md)** dan foydalaning.
