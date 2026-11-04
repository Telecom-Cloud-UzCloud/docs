# Xavfsizlik boʻyicha nazorat roʻyxati

## Virtual mashinalarni qanday himoya qilish kerak

UzCloud’da platforma infratuzilmani himoya qiladi: maʼlumotlar markazlari, gipervizorlar va tarmoq. **VM ichida ishlaydigan narsalar uchun siz javobgarsiz**: operatsion tizim, ilovalar, hisob qaydnomalari va ochiq portlar. Bulutli serverlarga qilinadigan hujumlarning aksariyati hech qanday gʻayrioddiy usullardan foydalanmaydi — ular yangilanmagan tizimlar, zaif parollar va butun internet uchun ochiq portlardan foydalanadi.

Ushbu nazorat roʻyxatida har bir VM’da nima qilish kerakligi keltirilgan. Har bir bandda batafsil qoʻllanmaga havola bor.

---

### VM yaratilgandan keyin darhol

- **Faqat SSH kalitlar orqali kiring.** VM yaratishda SSH kalit qoʻshing, soʻng parol orqali kirishni va root sifatida bevosita kirishni oʻchiring. **[SSH himoyasi](ssh-hardening.md)** ga qarang.
- **Barcha yangilanishlarni oʻrnating va VM’ni qayta ishga tushiring.** Yangi VM bir necha hafta oldingi obrazdan yaratilgan boʻlishi mumkin. **[Operatsion tizimni yangilash](update-os.md)** ga qarang.
- **Faqat kerakli portlarni oching.** SSH (22) va RDP (3389) ga faqat oʻz IP manzillaringizdan ruxsat bering, hech qachon `0.0.0.0/0` uchun emas. **[Tarmoqqa kirish](network-access.md)** ga qarang.
- **Zaxira nusxalashni sozlang.** VM disklarini jadval boʻyicha zaxiralashni yoqing. **[Zaxira nusxalar](../backups/create-backups.md)** va **[Jadvallar](../schedules/schedules.md)** ga qarang.

### Har oy

- Xavfsizlik yangilanishlari oʻrnatilganini tekshiring va yadro yangilangan boʻlsa, VM’ni qayta ishga tushiring.
- Ochiq portlar va xavfsizlik devori qoidalari roʻyxatini koʻrib chiqing va keraksizlarini oʻchiring.
- Operatsion tizim hali ishlab chiqaruvchi tomonidan qoʻllab-quvvatlanishini tekshiring (end of life).
- UzCloud hisobingizning **Activity Logs** va **Login History** boʻlimlarini koʻrib chiqing.

### Har chorakda

- VM’ni zaxira nusxadan tiklashni sinab koʻring. Hech qachon tiklanmagan zaxira nusxa kafolat emas.
- UzCloud hisobi foydalanuvchilari va ularning rollarini koʻrib chiqing, kirish endi kerak boʻlmaganlarni oʻchiring.
- API tokenlari va S3 kirish kalitlarini almashtiring.

### UzCloud hisobini himoya qilish

- Ikki bosqichli autentifikatsiyani yoqing. **[Hisob xavfsizligi](account-security.md)** ga qarang.
- Bitta umumiy hisob oʻrniga har bir xodim uchun minimal zarur rolga ega alohida foydalanuvchi yarating.

---

### Dolzarb zaifliklar haqida ogohlantirishlar

Muhim zaiflik mijozlarimizning VM’lariga taʼsir qilganda, biz koʻrsatmalar bilan ogohlantirish eʼlon qilamiz:

- **[CVE-2026-98432: Linux yadrosidagi TCP zaifligi](vulnerabilities/cve-2026-98432.md)** — 2026-yil 4-noyabr

> [!TIP]
> Agar server muhim boʻlsa yoki biror narsa tushunarsiz boʻlsa, ishni boshlashdan oldin **[qoʻllab-quvvatlash xizmatiga](../support/support.md)** murojaat qiling — amallarni rejalashtirishga yordam beramiz.
