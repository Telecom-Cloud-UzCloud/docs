# Obyektlarni versiyalash

Versiyalash yoqilgan boʻlsa, bucket obyektning barcha versiyalarini saqlaydi. Agar fayl xato bilan qayta yozilgan yoki oʻchirilgan boʻlsa, oldingi versiyani tiklash mumkin.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

## Versiyalashni yoqish

**Konsolda:** bucket yaratishda **Bucket Versioning** ni yoqing. **[Obyektli xotirani boshqarish](../../object-storage/manage-object-storage.md)** ga qarang.

**AWS CLI orqali:**

```bash
aws s3api put-bucket-versioning --bucket my-bucket \
  --versioning-configuration Status=Enabled

# check the status
aws s3api get-bucket-versioning --bucket my-bucket
```

Versiyalashni butunlay oʻchirib boʻlmaydi, faqat toʻxtatib turish mumkin (`Status=Suspended`). Mavjud versiyalar saqlanib qoladi.

## Versiyalarni koʻrish

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf
```

Har bir versiyaning `VersionId` si bor. Joriy versiyada `"IsLatest": true`.

## Versiyani tiklash

Kerakli versiyani yuklab oling:

```bash
aws s3api get-object --bucket my-bucket --key docs/report.pdf \
  --version-id <VersionId> report-old.pdf
```

Yoki uni obyekt ustiga nusxalab, yana joriy qiling:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source "my-bucket/docs/report.pdf?versionId=<VersionId>"
```

## Oʻchirilgan obyektni tiklash

Versiyalash yoqilgan bucketda obyektni oʻchirish faqat **oʻchirish belgisini** (delete marker) qoʻshadi. Obyektni tiklash uchun belgini oʻchiring:

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf \
  --query 'DeleteMarkers[?IsLatest].VersionId'

aws s3api delete-object --bucket my-bucket --key docs/report.pdf \
  --version-id <delete-marker-VersionId>
```

> [!NOTE]
> Barcha versiyalar joy egallaydi va toʻlanadi. Saqlanadigan versiyalar sonini cheklash uchun eski versiyalarni oʻchiradigan **[hayot sikli qoidasini](lifecycle.md)** sozlang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Qoʻllab-quvvatlanadigan imkoniyatlar](overview.md)**
