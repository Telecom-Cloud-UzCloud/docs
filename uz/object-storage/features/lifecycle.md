# Obyektlarning hayot sikli

Hayot sikli qoidalari belgilangan muddat oʻtgach obyektlarni avtomatik oʻchiradi: eski zaxira nusxalar, jurnallar, vaqtinchalik fayllar, oldingi versiyalar va tugallanmagan yuklashlar. Bu xotirada tartibni saqlaydi va xarajatlarni kamaytiradi.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

## Qoidalarni yaratish

Qoidalarni `lifecycle.json` faylida tavsiflang. Ushbu misolda:

- `logs/` prefiksli obyektlar 30 kundan keyin oʻchiriladi;
- `tmp/` prefiksli obyektlar 1 kundan keyin oʻchiriladi;
- barcha obyektlarning oldingi versiyalari joriy boʻlmay qolganidan 14 kun oʻtgach oʻchiriladi;
- tugallanmagan multipart yuklashlar 3 kundan keyin tozalanadi.

```json
{
  "Rules": [
    {
      "ID": "expire-logs",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Expiration": { "Days": 30 }
    },
    {
      "ID": "expire-tmp",
      "Status": "Enabled",
      "Filter": { "Prefix": "tmp/" },
      "Expiration": { "Days": 1 }
    },
    {
      "ID": "old-versions-and-uploads",
      "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "NoncurrentVersionExpiration": { "NoncurrentDays": 14 },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 3 }
    }
  ]
}
```

Qoidalarni bucketga qoʻllang va tekshiring:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json

aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
```

Barcha qoidalarni oʻchirish uchun: `aws s3api delete-bucket-lifecycle --bucket my-bucket`.

> [!NOTE]
> Qoidalar fonda, odatda kuniga bir marta qoʻllanadi, shuning uchun obyektlar muddat tugaganidan keyin bir kungacha kechikish bilan oʻchirilishi mumkin. **[Object Lock](object-lock.md)** bilan himoyalangan obyektlar blokirovka tugaguncha oʻchirilmaydi.

> [!WARNING]
> Boʻsh prefiks va `Expiration` ga ega qoida muddat oʻtgach bucketdagi **barcha** obyektlarni oʻchiradi. Qoidalarni qoʻllashdan oldin filtrlarni diqqat bilan tekshiring.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
