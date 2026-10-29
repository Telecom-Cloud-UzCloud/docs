# Profilni sozlash

## UzCloud’da foydalanuvchi profilini sozlash

**UzCloud** profili shaxsiy va kompaniya maʼlumotlarini, interfeys va xavfsizlik sozlamalarini, API’ga kirishni, foydalanuvchilar va rollarni, kvotalarni hamda akkauntdagi faoliyatni boshqarish imkonini beradi. Profilni ochish uchun konsolning yuqori oʻng burchagidagi ismingizni bosing.

![Profil sahifasi](../../images/profile-page.png)

### Shaxsiy maʼlumotlarni yangilash

Shaxsiy maʼlumotlaringizni dolzarb holatda saqlang.

- Profil menyusida **Personal Details** ni oching.
- Tahrirlash uchun qalam belgisini bosing.
- **Name** (ism), **Address Line 1** (manzil), **Country** (mamlakat), **State** (viloyat) va **City** (shahar) ni oʻzgartiring.
- Oʻzgarishlarni saqlash uchun **Submit** tugmasini bosing.

![Shaxsiy maʼlumotlar](../../images/profile-personal-details.png)

- Email yoki telefon raqamini oʻzgartirish uchun **Profile Details** blokidagi maydon yonida **Change** tugmasini bosing. Yangi qiymatni tasdiqlash kerak boʻladi.

### Kompaniya va toʻlov maʼlumotlari

Hisob-fakturalar va toʻlovlar uchun toʻgʻri toʻlov maʼlumotlari zarur.

- Profil menyusida **Company Details** ni oching.
- Tahrirlash uchun qalam belgisini bosing.
- **Organization Name** (tashkilot nomi) va **Billing Details** blokini toʻldiring: toʻlov manzili, veb-sayt, mamlakat, viloyat, shahar, INN (STIR), toʻlovchi nomi, toʻlov emaili va qoʻshimcha toʻlov emaili.
- Oʻzgarishlarni saqlang.

![Kompaniya va toʻlov maʼlumotlari](../../images/profile-billing-details.png)

### Akkaunt sozlamalari

- Profil menyusida **Account Preferences** ni oching.
- **Theme mode** blokida **Light Mode** (yorugʻ mavzu) yoki **Dark Mode** (qorongʻi mavzu) ni tanlang. Oʻzgarish darhol qoʻllaniladi.
- **App Language** blokida konsol tilini tanlang: **English**, **Russian** yoki **Uzbek**.

> [!NOTE]
> Ushbu hujjatlardagi skrinshotlar va interfeys elementlari nomlari konsolning inglizcha versiyasi uchun keltirilgan.

![Akkaunt sozlamalari](../../images/profile-account-preference.png)

### Sana va vaqt sozlamalari

- Profil menyusida **Date & Time** ni oching.
- **Preferred Time Zone** (vaqt mintaqasi) va **Preferred Date Time Format** (sana va vaqt formati) ni belgilang.
- Oʻzgarishlarni qoʻllash uchun **Submit** tugmasini bosing.

> [!NOTE]
> Tanlangan vaqt mintaqasi va format faqat koʻrsatish uchun ishlatiladi. Barcha amallar Asia/Samarkand vaqt mintaqasida qayta ishlanadi.

![Sana va vaqt sozlamalari](../../images/profile-date-and-time-settings.png)

### Ikki bosqichli autentifikatsiya

Xavfsizlikni oshirish uchun **ikki bosqichli autentifikatsiyani (2FA)** yoqing: har safar tizimga kirishda parol va emailga yuborilgan bir martalik kodni kiritish kerak boʻladi.

- Profil menyusida **Authentication** ni oching.
- **Email Authentication** blokida **SET UP** tugmasini bosing.
- Elektron pochta manzilingizni tasdiqlang va unga yuborilgan bir martalik kodni (OTP) kiriting.
- 2FA’ni akkauntning barcha foydalanuvchilari uchun majburiy qilish uchun **2FA Enforcement Status** blokidagi **Enable** oʻtkazgichini yoqing.

![Ikki bosqichli autentifikatsiyani sozlash](../../images/profile-auth-two-factor-auth.png)

### Parolni oʻzgartirish

- Profil menyusida **Authentication** ni oching va **Change Password** tugmasini bosing.
- **Current Password** (joriy parol) ni kiriting, soʻng **New Password** (yangi parol) ni kiriting va tasdiqlang.
- Oʻzgarishlarni saqlash uchun **Change Password** tugmasini bosing.

![Parolni oʻzgartirish](../../images/profile-change-password.png)

### API’ga kirish

**API** boʻlimi shaxsiy kirish tokeni yordamida UzCloud bilan API orqali ishlash imkonini beradi.

- Profil menyusida **API** ni oching.
- **Personal Access Token** yaratish uchun **Enable API** tugmasini bosing. Token ostida uning amal qilish muddati koʻrsatiladi; tokenni nusxalash belgisi yordamida nusxalash mumkin.
- API’ga kirishni oʻchirish uchun **Disable API** tugmasini bosing.
- API hujjatlariga havolalar sahifaning yuqori qismida keltirilgan.

> [!WARNING]
> Tokenni sir saqlang: unga ega boʻlgan har qanday kishi resurslaringizni boshqarishi mumkin.

![API’ga kirish](../../images/profile-api.png)

### Yangi foydalanuvchi qoʻshish

**Users** boʻlimi akkauntga foydalanuvchilarni qoʻshish va ularga rollar tayinlash imkonini beradi.

- Profil menyusida **Users** ni oching. Roʻyxatda har bir foydalanuvchining ismi, emaili, roli, yaratilgan sanasi, oxirgi kirishi va holati koʻrsatiladi.
- **+ Add New User** tugmasini bosing, foydalanuvchi maʼlumotlarini kiriting, rolni tanlang va saqlang.
- **Actions** menyusida foydalanuvchini tahrirlash yoki taklifnomani qayta yuborish mumkin.

![Foydalanuvchilar](../../images/user.png)

### Foydalanuvchi rollari va huquqlari

**Roles** boʻlimida mavjud rollar va ularning huquqlari koʻrsatiladi.

- Profil menyusida **Roles** ni oching.
- Rolning tavsifi va huquqlarini koʻrish uchun uni tanlang. Oldindan belgilangan rollar: **Owner**, **Service Administrator** va **Service Viewer**.
- Oʻz huquqlar toʻplamiga ega yangi rol yaratish uchun **+** tugmasini bosing.

![Rollar](../../images/roles.png)

### Kvotalar va ularni oshirish

**Account Limit** boʻlimi (**Quota** sahifasi) har bir zonadagi resurslar limitlari va ulardan foydalanishni koʻrsatadi.

- Profil menyusida **Account Limit** ni oching.
- **Quota Limits** yorligʻida har bir resursning limiti, foydalanilgan va mavjud hajmini koʻrish uchun zonani tanlang.
- Limitni oshirishni soʻrash uchun resurs yonidagi **Request To Increase** ni bosing. Soʻrov holati **Request Status** ustunida koʻrsatiladi.
- **Quota Usages Report** yorligʻida kvotalardan foydalanish hisoboti mavjud.

![Kvotalar](../../images/req.png)

### Faoliyat jurnali

**Activity Logs** boʻlimida akkauntdagi amallar yozuvlari saqlanadi: IP manzil, foydalanuvchi, loyiha, amal turi, tavsif, vaqt va holat.

- Profil menyusida **Activity Logs** ni oching.
- Yozuvlarni kalit soʻzlar boʻyicha filtrlash uchun qidiruv satridan foydalaning.

![Faoliyat jurnali](../../images/activity.png)

### Kirishlar tarixi

**Login History** boʻlimi akkauntga barcha kirishlarni, jumladan muvaffaqiyatsiz urinishlarni koʻrsatadi.

- Profil menyusida **Login History** ni oching.

![Kirishlar tarixi](../../images/loginhist.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud profilingizni boshqarishingiz, akkaunt xavfsizligini oshirishingiz va konsolni oʻz ehtiyojlaringizga moslashingiz mumkin.
