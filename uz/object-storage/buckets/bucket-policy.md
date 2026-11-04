# Bucket Policy

**Bucket Policy** — JSON formatidagi bucketga kirish qoidalari toʻplami. Uning yordamida obyektlarning bir qismini ommaviy qilish, kirishni IP manzil boʻyicha cheklash yoki obyektlarni oʻchirishni taqiqlash mumkin.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

**Konsolda** siyosatni bucket yaratishda **Bucket Policy** maydonida belgilash mumkin. **AWS CLI orqali** siyosatni faylga saqlang va uni qoʻllang:

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
aws s3api get-bucket-policy --bucket my-bucket
aws s3api delete-bucket-policy --bucket my-bucket   # remove the policy
```

## Papkaga ommaviy kirish

Har kim `public/` prefiksli obyektlarni yuklab olishi mumkin, bucketning qolgan obyektlari yopiq qoladi:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadForPublicFolder",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-bucket/public/*"]
    }
  ]
}
```

Shundan soʻng obyektlar `https://s3.uzcstorage.uz/my-bucket/public/<fayl>` manzilida mavjud boʻladi.

## Faqat oʻz IP manzillaringizdan kirish

Koʻrsatilgan manzillardan boshqa barcha soʻrovlarni taqiqlang:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOutsideOffice",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
      "Condition": {
        "NotIpAddress": { "aws:SourceIp": ["203.0.113.0/24"] }
      }
    }
  ]
}
```

> [!WARNING]
> Agar manzillar roʻyxatida xato qilsangiz, oʻz vositalaringizdan ham bucketga kirishni yoʻqotishingiz mumkin. Avval siyosatni test bucketida tekshiring. Siyosatni konsolda yoki ruxsat etilgan manzildan `delete-bucket-policy` buyrugʻi bilan oʻchirish mumkin.

## Obyektlarni oʻchirishni taqiqlash

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyDelete",
      "Effect": "Deny",
      "Principal": "*",
      "Action": ["s3:DeleteObject", "s3:DeleteObjectVersion"],
      "Resource": ["arn:aws:s3:::my-bucket/*"]
    }
  ]
}
```

Zaxira nusxalarni ishonchli himoya qilish uchun **[Object Lock](object-lock.md)** dan foydalaning: siyosatdan farqli oʻlaroq, uni kalitlaringizga ega boʻlgan kishi olib tashlay olmaydi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
