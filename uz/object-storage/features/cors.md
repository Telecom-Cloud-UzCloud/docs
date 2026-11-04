# CORS’ni sozlash

Brauzerlar, agar server aniq ruxsat bermasa, veb-sahifadan boshqa domenga soʻrovlarni bloklaydi. **CORS** (Cross-Origin Resource Sharing) qoidalari saytingizga bucketdan fayllarni yuklash yoki fayllarni bevosita brauzerdan bucketga yuborish imkonini beradi.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

## Qoidalarni yaratish

Qoidalarni `cors.json` faylida tavsiflang. Ushbu misol `https://example.com` saytiga obyektlarni oʻqish va ularni presigned URL orqali yuklash imkonini beradi:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://example.com"],
      "AllowedMethods": ["GET", "HEAD", "PUT"],
      "AllowedHeaders": ["*"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

- `AllowedOrigins` — saytingiz domenlari. Fayllar ommaviy boʻlmasa, `*` dan foydalanmang.
- `AllowedMethods` — ruxsat etilgan HTTP usullari.
- `MaxAgeSeconds` — brauzer dastlabki soʻrov natijasini qancha vaqt keshlaydi.

Qoidalarni qoʻllang va tekshiring:

```bash
aws s3api put-bucket-cors --bucket my-bucket --cors-configuration file://cors.json
aws s3api get-bucket-cors --bucket my-bucket
```

## Buyruqlar satridan tekshirish

Brauzer qilganidek dastlabki soʻrov yuboring. Javobda `Access-Control-Allow-Origin` sarlavhasi boʻlishi kerak:

```bash
curl -i -X OPTIONS "https://s3.uzcstorage.uz/my-bucket/image.png" \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: GET"
```

Qoidalarni oʻchirish uchun: `aws s3api delete-bucket-cors --bucket my-bucket`.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Qoʻllab-quvvatlanadigan imkoniyatlar](overview.md)**
