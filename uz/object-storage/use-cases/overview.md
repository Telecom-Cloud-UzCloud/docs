# Foydalanish stsenariylari

Obyektli xotira disklardan arzonroq va cheklovsiz kengayadi, shuning uchun saqlash zarur, lekin kamdan-kam oʻzgartiriladigan maʼlumotlar uchun juda mos.

| Stsenariy | Maqola |
|---|---|
| Shifrlash va deduplikatsiya bilan server fayllarining zaxira nusxalari | [restic bilan server zaxira nusxalari](server-backup-restic.md) |
| PostgreSQL va MySQL maʼlumotlar bazalarining kundalik damplari | [Maʼlumotlar bazalari zaxira nusxalari](database-backup.md) |
| Nextcloud uchun fayllar xotirasi | [S3 bilan Nextcloud](nextcloud.md) |
| Sayt rasmlari, videolari va boshqa statik fayllari | [S3’ni Nginx orqali proksilash](../features/nginx-proxy.md) |
| Statik sayt joylashtirish | [Statik sayt](../features/static-website.md) |

> [!TIP]
> Zaxira nusxalarni **[Object Lock](../features/object-lock.md)** va **[hayot sikli qoidalari](../features/lifecycle.md)** yoqilgan alohida bucketda saqlang: shunda nusxalar oʻchirishdan himoyalanadi, eskilari esa avtomatik oʻchiriladi.
