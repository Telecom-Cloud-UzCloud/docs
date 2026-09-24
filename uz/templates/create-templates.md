# Shablonlar yaratish

## Virtual mashina shablonlari

**Shablon** — virtual mashinalar (VM) yoki konteynerlarni tez joylashtirish uchun oldindan sozlangan disk obrazi. Shablon oldindan belgilangan sozlamalar, dasturlar va parametrlarga ega oʻrnatilgan operatsion tizimni oʻz ichiga oladi, shuning uchun yangi VM’larni har safar OT’ni qoʻlda oʻrnatmasdan va sozlamasdan yaratish mumkin.

---

### Virtual mashina shablonini yaratish

- Chap menyuda **Templates** yorligʻini oching.
- Shablon yaratish uchun sahifaning oʻng tomonidagi **Templates** yoki **plyus (+)** belgisini bosing. Shablon yaratish menyusi ochiladi.

![Shablonlar sahifasi](../../images/create-temp.png)

### Joylashuvni tanlash

- Shablon saqlanadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/create-temp-location.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun shablonni loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/create-temp-projects.png)

### Shablon parametrlari

Shablon yaratishda bir nechta majburiy maydonlarni toʻldirish kerak:

- **Template Name** — shablonni aniqlash uchun nom.
- **Description** — shablonning maqsadi va tarkibi tavsifi.
- **URL** — shablon joylashgan manzilga havola (agar mavjud boʻlsa).
- **Format** — shablon formati, masalan RAW yoki boshqa qoʻllab-quvvatlanadigan format.
- **Root Disk Controller** — shablonni yuklash uchun ishlatiladigan asosiy disk kontrolleri (tizim arxitekturasiga bogʻliq).
- **Template Type** — shablon toifasi (masalan, VNF).
- **Image** — shablon bilan bogʻliq obraz fayli.
- **Operating System** — shablon OT’si (masalan, Linux, Windows).
- **OS Version** — OT’ning aniq versiyasi.

![Shablon parametrlari](../../images/create-temp-details.png)

### Qoʻshimcha parametrlar

Shablon uchun qoʻshimcha parametrlarni ham tanlash mumkin:

- **Password Enabled** — shablonga kirish yoki undan foydalanish uchun parol talab qilinadi, bu qoʻshimcha himoya qatlamini qoʻshadi.
- **Featured** — shablonni tavsiya etilgan sifatida belgilaydi, bu uni topishni osonlashtiradi.
- **Dynamically Scalable** — yuklamaga qarab resurslarni dinamik masshtablash imkonini beradi; bulutli joylashtirishlar uchun foydali.
- **Requires VM** — shablon jismoniy uskunada emas, balki virtual mashina muhitida ishlatilishi kerakligini bildiradi.

![Qoʻshimcha parametrlar](../../images/create-templates-inline-3ffaf779.png)

### Shablonni yaratish

- Kerakli **Billing Cycle** ni tanlang. Shablonlar uchun soatlik toʻlov qoʻllab-quvvatlanadi.
- Qoʻllab-quvvatlanadigan billing qoidalari: Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata va Unfixed Prorata.
- Shablonlar uchun har bir zonada faqat bitta paket qoʻllab-quvvatlanadi — bu turli muhitlarda joylashtirishlarni standartlashtirishga yordam beradi.
- Barcha parametrlarni va umumiy narxni tekshiring. Loyiha uchun shablon yaratish maqsadida **Create** tugmasini bosing.

![Shablonni yaratish](../../images/create-templates-inline-e20b927f.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da shablonlarni osongina yaratishingiz va boshqarishingiz mumkin. Shablonlar oldindan sozlangan parametrlarga ega virtual mashinalar yoki konteynerlarni tez joylashtirish, vaqtni tejash va bir xillikni taʼminlash imkonini beradi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VNF qurilmalari](../vnf-appliances/vnf-appliances.md)**
> - **[Virtual mashina](../compute/compute-instance.md)**
> - **[ISO obrazlar](../isos/import-iso.md)**
