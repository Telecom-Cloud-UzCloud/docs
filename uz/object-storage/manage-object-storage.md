# Obyektli xotirani boshqarish

## Ceph obyektli xotirasini boshqarish

Ceph obyektli xotirasi faollashtirilgach, unumdorlik, bandlik va obyektlar sonini kuzatish uchun boshqaruv panelidan foydalaning.

![Ceph obyektli xotirasi paneli](../../images/ob-8.png)

### Amal tugmalari

- Amal tugmalari — xotira bilan bajariladigan odatiy amallarga tezkor kirish.
- Tezkor amallar uchun xotiraning oʻng tomonidagi tugmalardan foydalaning.

![Amal tugmalari](../../images/ob-9.png)

- **Refresh** — xotira holati va sahifadagi maʼlumotlarni yangilaydi.
- **Auto-scaling** — xotirani avtomatik masshtablashni yoqadi.
- **Credentials** — xotiraning hisob maʼlumotlarini koʻrsatadi.
- **Resize** — xotira hajmini oʻzgartiradi.
- **Delete** — xotirani butunlay oʻchirib tashlaydi.

### Xotirani avtomatik masshtablash

- Avtomatik masshtablashni yoqish uchun avtomatik masshtablash belgisini bosing. **Auto Scaling** oʻtkazgichini yoqing yoki oʻchiring va oʻzgarishlarni tasdiqlash uchun **Submit** tugmasini bosing.

![Avtomatik masshtablash](../../images/ob-19.png)

### Hisob maʼlumotlarini koʻrish

- Hisob maʼlumotlarini koʻrish uchun tegishli belgini bosing. **S3 Object Store Credentials** menyusi ochiladi, unda xotiraning **Secret Key** va **Password** koʻrsatiladi.

![Hisob maʼlumotlari](../../images/ob-17.png)

### Xotira hajmini oʻzgartirish

- Xotira hajmini oshirish yoki kamaytirish uchun hajmni oʻzgartirish belgisini bosing. **Resize Object Store** menyusi ochiladi, unda kerakli hajmni belgilash mumkin.
- Kerakli **Billing Cycle** ni tanlang: soatlik (Hourly) yoki oylik (Monthly).
- Barcha parametrlarni va umumiy narxni tekshiring. Hajmni oʻzgartirish uchun **Resize** tugmasini bosing.

![Xotira hajmini oʻzgartirish](../../images/ob-18.png)

### Bucket yaratish

- Yangi bucket yaratish uchun **Create Bucket** tugmasini bosing.

![Bucket yaratish](../../images/ob-10.png)

- **Bucket Name** ni kiriting va kerak boʻlsa **Bucket Versioning** ni yoqing. Versiyalash obyektlarning oldingi versiyalarini saqlash va tiklash imkonini beradi.

> [!NOTE]
> - Obyektlarni bloklash uchun bucket versiyalashini yoqish kerak.
> - Obyekt versiyalari maʼlumotlarni saqlashning umumiy narxiga qoʻshiladi.

- Kerak boʻlsa, obyektlarni belgilangan muddat davomida oʻchirish yoki qayta yozishdan himoya qilish uchun **Object Locking** ni yoqing.
- Obyektlar WORM (write-once-read-many — bir marta yozish, koʻp marta oʻqish) modeli boʻyicha saqlanadi: ularni belgilangan vaqt davomida yoki muddatsiz oʻchirib yoki qayta yozib boʻlmaydi.
- Bucket yaratishni yakunlash uchun **Create** tugmasini bosing.

> [!NOTE]
> - Obyektlarni bloklash faqat versiyalash yoqilgan bucketlarda ishlaydi.

![Bucket yaratish](../../images/ob-11.png)

### Bucket sharhi

- Bucket haqidagi maʼlumotlarni koʻrish uchun uning nomini bosing: fayllar soni, bucket URL manzili, foydalanish, yaratilgan sana va ommaviy kirish sozlamalari.

![Bucket sharhi](../../images/ob-12.png)

- Bucketni ulashish, oʻzgartirish yoki oʻchirish uchun tezkor amallardan foydalaning. Bucketni ulashish uchun ulashish belgisini bosing — ommaviy kirishni yoqish mumkin.

![Bucketni ulashish](../../images/ob-13.png)

- Ommaviy kirish yoqilganda obyekt havolasiga ega har qanday kishi uni maxsus huquqlarsiz ochishi mumkin. Sozlamani alohida fayllarga yoki butun bucketga qoʻllash mumkin; kirish oddiy HTTP yoki HTTPS soʻrovlari orqali amalga oshiriladi. Oʻzgarishlarni saqlash uchun **Update** tugmasini bosing.

![Ommaviy kirish](../../images/ob-14.png)

- Bucket ichida **Upload Files** yoki **Create Folder** belgilari yordamida papkalar yaratish yoki fayllarni yuklash mumkin.

![Fayllarni yuklash va papka yaratish](../../images/ob-15.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz Ceph obyektli xotirasini samarali boshqarishingiz mumkin: avtomatik masshtablashni sozlash, hajmni oʻzgartirish, bucketlar yaratish va foydalanishni kuzatish. Bu imkoniyatlar maʼlumotlarni saqlashda optimal unumdorlik, masshtablanuvchanlik va xavfsizlikni taʼminlaydi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.
