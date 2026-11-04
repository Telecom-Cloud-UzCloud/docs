# S3 bilan Nextcloud

**Nextcloud** — oʻz serveringizda joylashtirish mumkin boʻlgan fayllarni saqlash va hamkorlik platformasi. Obyektli xotira u uchun fayllar xotirasi boʻlib xizmat qilishi mumkin: shunda VM diskida faqat ilova va maʼlumotlar bazasi qoladi.

S3’ni ulashning ikki usuli bor:

- **asosiy xotira** — foydalanuvchilarning barcha fayllari bucketda saqlanadi;
- **tashqi xotira** — bucket alohida papka sifatida ulanadi.

## Asosiy xotira

> [!WARNING]
> Asosiy xotirani Nextcloud **birinchi marta ishga tushirilishidan oldin** sozlang. Mahalliy diskka allaqachon yuklangan fayllar S3’ga avtomatik koʻchirilmaydi.

`config/config.php` fayliga `objectstore` blokini qoʻshing:

```php
'objectstore' => [
    'class' => '\\OC\\Files\\ObjectStore\\S3',
    'arguments' => [
        'bucket' => 'my-nextcloud',
        'hostname' => 's3.uzcstorage.uz',
        'port' => 443,
        'use_ssl' => true,
        'region' => 'default',
        'key' => '<Access Key>',
        'secret' => '<Secret Key>',
        'use_path_style' => true,
        'autocreate' => false,
    ],
],
```

Nextcloud fayllarni bucketda `urn:oid:<id>` nomli obyektlar sifatida saqlaydi, shuning uchun fayllarni bevosita bucketda oʻqib boʻlmaydi. Nextcloud maʼlumotlar bazasining ham zaxira nusxasini yarating: usiz fayllarni foydalanuvchilarga moslashtirib boʻlmaydi.

## Tashqi xotira

1. **Apps** boʻlimida **External storage support** ilovasini yoqing.
2. **Administration settings → External storage** ni oching.
3. **Amazon S3** turidagi xotirani qoʻshing va toʻldiring: **Bucket** — bucket nomi, **Hostname** — `s3.uzcstorage.uz`, **Port** — `443`, **Region** — `default`, **Enable SSL** va **Enable Path Style** ni belgilang hamda **Access key** va **Secret key** ni kiriting.
4. Papkaga kirish huquqi boʻlgan foydalanuvchilar yoki guruhlarni tanlang. Xotira yonidagi yashil indikator ulanish ishlayotganini bildiradi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
