# Object Lock

**Object Lock** obyektlarni WORM rejimida (write once, read many — bir marta yozish, koʻp marta oʻqish) saqlaydi: bloklangan obyektni saqlash muddati tugaguncha oʻchirib yoki qayta yozib boʻlmaydi. Bu zaxira nusxalarni tasodifiy oʻchirishdan va shifrlovchi viruslardan himoya qiladi.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

> [!IMPORTANT]
> Object Lock’ni faqat bucket yaratilayotganda yoqish mumkin va keyin uni oʻchirib boʻlmaydi. U avtomatik ravishda **[versiyalashni](versioning.md)** yoqadi.

## Object Lock bilan bucket yaratish

**Konsolda:** bucket yaratishda **Bucket Versioning** va **Object Locking** ni yoqing.

**AWS CLI orqali:**

```bash
aws s3api create-bucket --bucket my-backups --object-lock-enabled-for-bucket
```

## Saqlash rejimlari

- **GOVERNANCE** — obyektlar himoyalangan, lekin maxsus huquqga ega foydalanuvchi `--bypass-governance-retention` bilan blokirovkani olib tashlashi mumkin. Aksariyat holatlar uchun mos.
- **COMPLIANCE** — muddat tugaguncha hech bir foydalanuvchi, shu jumladan hisob egasi ham, obyektni oʻchira yoki muddatni qisqartira olmaydi.

> [!WARNING]
> COMPLIANCE rejimida bloklangan obyektlar, hatto endi kerak boʻlmasa ham, muddat oxirigacha saqlanadi va toʻlanadi. GOVERNANCE va qisqa muddatlardan boshlang.

## Bucket uchun standart saqlash muddati

Bucketdagi barcha yangi obyektlar koʻrsatilgan muddatga bloklanadi:

```bash
aws s3api put-object-lock-configuration --bucket my-backups \
  --object-lock-configuration \
  'ObjectLockEnabled=Enabled,Rule={DefaultRetention={Mode=GOVERNANCE,Days=30}}'

aws s3api get-object-lock-configuration --bucket my-backups
```

## Alohida obyektni bloklash

```bash
aws s3api put-object-retention --bucket my-backups --key db/2026-11-01.sql.gz \
  --retention 'Mode=GOVERNANCE,RetainUntilDate=2026-12-31T00:00:00Z'

aws s3api get-object-retention --bucket my-backups --key db/2026-11-01.sql.gz
```

**Legal hold** obyektni muddatsiz — blokirovka olib tashlanmaguncha bloklaydi:

```bash
aws s3api put-object-legal-hold --bucket my-backups --key db/2026-11-01.sql.gz \
  --legal-hold Status=ON
```

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
