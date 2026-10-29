# Obyektli xotirani boshqarish

## Obyektli xotirani boshqarish

Xotirani ochish uchun **Object Storage** sahifasida uning nomini bosing. **Object Storage Overview** sahifasida xotira haqidagi maʼlumotlar va uning bucketlari koʻrsatiladi.

![Object Storage Overview](../../images/ob-8.png)

### Amal tugmalari

Xotira kartochkasida loyiha, joylashuv, hajm, butun davrdagi isteʼmol, foydalanilgan hajm va yaratilgan sana koʻrsatiladi. Amal tugmalari oʻng tomonda joylashgan.

![Amal tugmalari](../../images/ob-9.png)

- **Refresh** — xotira holati va maʼlumotlarini yangilaydi.
- **Sync Buckets** — bucketlar roʻyxatini xotira bilan sinxronlaydi.
- **Credentials** — S3 manzili va kirish kalitlarini koʻrsatadi.
- **Upgrade/Downgrade Store** — xotira hajmini oʻzgartiradi.
- **Delete Object Storage** — xotirani butunlay oʻchirib tashlaydi.

### Kirish maʼlumotlarini koʻrish

- **Credentials** ni bosing. **S3 Object Storage Credentials** oynasida mintaqa (**Region**), S3 manzili (**URL**, `https://s3.uzcstorage.uz`) va kirish kalitlaringiz (**Access Keys**) koʻrsatiladi.

![Kirish maʼlumotlari](../../images/ob-17.png)

- Kirish kalitlari qoidalari:
  - 2 tagacha faol kalitga ega boʻlish mumkin. Rotatsiya uchun ikkinchi kalitni yarating; mavjudlaridan birini bekor qilmaguningizcha uchinchi kalitni yaratib boʻlmaydi.
  - Har doim kamida 1 ta faol kalit qolishi kerak. Oxirgi kalitni oʻchirib boʻlmaydi.
  - **Create Key** ni bosgandan soʻng maxfiy kalitni 5 daqiqa ichida nusxalab oling. Shundan keyin maxfiy kalit yashiriladi, kalitning oʻzi esa faol qoladi.
  - Kalitni bekor qilish uni foydalanishdan chiqaradi.
- Odatiy rotatsiya: 2-kalitni yarating → ilovalarni unga oʻtkazing → 1-kalitni bekor qiling.

### Xotira hajmini oʻzgartirish

- **Upgrade/Downgrade Store** ni bosing. **Resize Object Storage** oynasida yangi hajmni GB’da kiriting.
- **Billing Cycle** ni tanlang, toʻlanadigan summani (**Payable Amount**) tekshiring va **Resize** tugmasini bosing.

![Hajmni oʻzgartirish](../../images/ob-18.png)

### Bucket yaratish

- **Buckets** boʻlimida **+ Create Bucket** ni bosing.
- **Bucket Name** maydoniga bucket nomini kiriting.
- Kerak boʻlsa, **Bucket Versioning** ni yoqing: shunda bucketdagi obyektning istalgan oldingi versiyasini olish va tiklash mumkin boʻladi.
- Obyektlarni WORM (write-once-read-many — «bir marta yozish, koʻp marta oʻqish») modeli boʻyicha saqlash uchun **Object Locking** ni yoqing. Shunda obyektlarni belgilangan muddat davomida yoki muddatsiz oʻchirib yoki qayta yozib boʻlmaydi.
- Xohishga koʻra, **Bucket Policy** maydonida JSON formatidagi bucket siyosatini (**Policy Examples** va **Policy Generator** ga qarang) va **ACL** blokida ruxsatlarni belgilang.
- **Create** tugmasini bosing.

![Bucket yaratish](../../images/ob-11.png)

> [!NOTE]
> - Object Locking faqat versiyalash yoqilgan bucketlarda ishlaydi.
> - Object Lock — doimiy sozlama: bucket uchun yoqilgandan soʻng uni oʻchirib boʻlmaydi, versiyalashni ham endi oʻchirib boʻlmaydi.
> - Obyekt versiyalari maʼlumotlarni saqlashning umumiy qiymatiga qoʻshiladi.

### Bucketga ommaviy kirish

- Bucketlar jadvalida nom, bucket URL’i, fayllar soni, umumiy hajm, kirish turi (**Public** yoki **Private**) va yaratilgan sana koʻrsatiladi.
- Ommaviy kirishni oʻzgartirish uchun bucket qatoridagi ulashish belgisini (yoki bucket sahifasidagi **Share Bucket** ni) bosing, **Update Public Access** ni yoqing yoki oʻchiring va **Update** tugmasini bosing.

![Ommaviy kirishni oʻzgartirish](../../images/ob-14.png)

> [!WARNING]
> Ommaviy kirish yoqilganda obyekt havolasiga ega boʻlgan har kim unga hech qanday ruxsatsiz kira oladi. Ommaviy kirishni oʻzgartirish bucketning ACL sozlamalarini oʻzgartirishi mumkin.

### Bucket sharhi

- **Bucket Overview** sahifasini ochish uchun bucket nomini bosing. Unda fayllar soni, bucket URL’i, foydalanilgan hajm, yaratilgan sana va kirish turi koʻrsatiladi.
- Amal tugmalari yordamida maʼlumotlarni yangilash (**Refresh**), bucketni ulashish (**Share Bucket**), uni oʻzgartirish (**Update Bucket**) va oʻchirish mumkin.

![Bucket sharhi](../../images/ob-12.png)

- Fayl menejerida papkalarni koʻrish, fayllarni yuklash (**Upload Files**) va papka yaratish (**Create Folder**) mumkin. Fayl yonidagi menyu (uch nuqta) u bilan bajariladigan amallarni ochadi. Har bir fayl uchun yaratilgan sana, hajm va ommaviy kirish holati koʻrsatiladi.

![Fayl menejeri](../../images/ob-15.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz obyektli xotirani boshqarishingiz mumkin: kirish kalitlarini olish, xotira hajmini oʻzgartirish, bucketlar yaratish va ularga kirishni boshqarish. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.
