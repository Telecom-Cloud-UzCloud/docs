# VNF qurilmalari

## Virtual tarmoq funksiyalari (VNF) qurilmalari

**Virtual tarmoq funksiyalari (VNF)** — tarmoq xizmatlarini taqdim etuvchi dasturiy ilovalar: marshrutizatorlar, tarmoqlararo ekranlar, yuklama muvozanatlagichlar, WAN optimallashtiruvchilar. Anʼanaviy apparat tarmoq qurilmalaridan farqli oʻlaroq, VNF’lar virtuallashtirilgan infratuzilmada ishlaydi, bu esa moslashuvchanlik, masshtablanuvchanlik va iqtisodiy samaradorlikni taʼminlaydi.

**UzCloud** VNF qurilmalarini joylashtirish va boshqarishni soddalashtiradi hamda tarmoq infratuzilmasini ehtiyojlarga muvofiq masshtablash va moslash imkonini beradi. Ushbu qoʻllanmada **UzCloud**’da VNF qurilmasini yaratish tushuntiriladi.

---

### VNF qurilmasini yaratish

- Chap menyuda **VNF Appliances** yorligʻini oching.
- **VNF Appliances** sahifasi ochiladi.

![VNF Appliances sahifasi](../../images/create-vnf-app.png)

- VNF qurilmasini yaratish uchun sahifaning oʻng tomonidagi **Create VNF Appliances** yoki **plyus (+)** belgisini bosing. VNF qurilmasini yaratish sahifasi ochiladi.

### Joylashuvni tanlash

- Qurilma jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/create-instance-location.png)

### Obrazni tanlash

- Oʻrnatiladigan operatsion tizim yoki ilova shablonini tanlang.
- Mashhur OT obrazlari mavjud. Shuningdek, oʻzingizning ISO obrazingizni import qilishingiz mumkin.
- **Eslatma**: Microsoft Windows uchun faqat rasmiy sinov (evaluation) versiyalari mavjud.

![Obrazni tanlash](../../images/create-instance-choose-images.png)

### CPU ajratish turini tanlash

- Yuklamangizga mos protsessor resurslarini ajratish turini tanlang:

![CPU turini tanlash](../../images/create-instance-choose-type.png)

- **Shared CPU** — arzon variant, resurslar foydalanuvchilar oʻrtasida taqsimlanadi. Ishlab chiqish, testlash va kichik veb-saytlar kabi yengil yuklamalar uchun mos.
- **Dedicated CPU** — barqaror unumdorlik uchun ajratilgan resurslar. Ishlab chiqarish muhitlari, yuqori yuklamali ilovalar va maʼlumotlar bazalari uchun mos.
- **High-Frequency Compute** — modellashtirish, moliyaviy hisob-kitoblar va kechikishga sezgir ilovalar kabi murakkab hisoblashlar uchun yuqori takt chastotasi.
- **Cloud GPU** — mashinaviy oʻqitish, sunʼiy intellekt, video renderlash va ilmiy modellashtirish kabi talabchan vazifalar uchun GPU tezlatish.

### Tarif rejasini tanlash

- CPU, xotira, disk va oʻtkazish qobiliyatiga boʻlgan talablaringizga qarab reja tanlang. Kerak boʻlsa, oʻzingizning rejangizni yaratishingiz mumkin.

![Rejani tanlash](../../images/create-plan-vnf-app.png)

- **General Compute (GC)** — CPU, xotira, disk va oʻtkazish qobiliyati muvozanatlashgan yuklamalar uchun. Umumiy maqsadli ilovalar, veb-serverlar va test muhitlari uchun mos.

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun qurilmani loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/create-instance-choose-project.png)

### Tarmoqni tanlash

- Ulanish va xavfsizlik talablaringizga qarab tarmoqni tanlang. Mavjud tarmoq variantlari haqida batafsil maʼlumot tegishli qoʻllanmalarda keltirilgan.
- Qurilmani mavjud tarmoqqa ulash uchun uni mavjud tarmoqlar roʻyxatidan tanlang.

![Tarmoqni tanlash](../../images/create-networks-vnf-app.png)

- **Public Network** — tashqi ulanish uchun oldindan sozlangan oddiy tarmoq. Bulutli tarmoqlararo ekran, portlarni yoʻnaltirish va masofaviy kirish VPN’ini oʻz ichiga oladi. Ortiqcha sozlamalarsiz oddiy ulanish kerak boʻlganlar uchun mos.
- **VPC Network** — trafik marshrutlash ustidan toʻliq nazorat va yuqori xavfsizlikka ega ilgʻor tarmoq yechimi. VPN shlyuzi, site-to-site VPN ulanishlari va trafikni ajratishni qoʻllab-quvvatlaydi.

**Eslatma:** standart holatda VPC tasodifiy **CIDR** bloki va bitta tarmoq qatlami (tier) bilan yaratiladi.

- Qurilmaga internetdan kirish uchun ommaviy IPv4 manzilni yoqishingiz mumkin.

![Ommaviy IP’ni yoqish](../../images/create-instance-enable-public-ip.png)

### Affinity guruhini tanlash

- Affinity guruhini tanlang yoki **Create Affinity Groups** ni bosib yangisini yarating.

![Affinity guruhini tanlash](../../images/select-ag.png)

### Server sozlamalari

- Qoʻshimcha parametrlarni sozlang.
- Xavfsiz kirish uchun **SSH kalit qoʻshishingiz** mumkin. SSH kalit qoʻshish uchun **Add Now** tugmasini bosing.
- **Eslatma**: baʼzi OT obrazlari, masalan Arch Linux uchun SSH kalit majburiy, chunki parol orqali kirish qoʻllab-quvvatlanmaydi.

![SSH kalit qoʻshish](../../images/create-instance-add-ssh.png)

- SSH kalit nomi va qiymatini kiriting, soʻng **Add SSH Key** tugmasini bosing.

![SSH kalit maʼlumotlari](../../images/create-instance-add-ssh-kay.png)

- Ishga tushirishda amallarni avtomatlashtirish uchun ishga tushirish skriptini qoʻshing. Qurilma uchun skript qoʻshish maqsadida **Add Now** tugmasini bosing.

![Ishga tushirish skriptini qoʻshish](../../images/create-instance-add-startup-script.png)

### Kengaytirilgan sozlamalar (ixtiyoriy)

- Unumdorlik, xavfsizlik va moslashuvchanlikni optimallashtirish uchun VM’ning qoʻshimcha parametrlarini sozlash maqsadida **Advanced Mode** ni yoqing.

![Kengaytirilgan sozlamalar](../../images/create-instance-advance-mode.png)

- **Boot Mode** — yuklash jarayonini himoyalash uchun Legacy yoki Secure boot ni tanlang.
- **Boot Type** — UEFI (zamonaviy mikrodastur) yoki BIOS (anʼanaviy mikrodastur) ni tanlang.
- **Enable Dynamic Scaling** — yuklamaga qarab resurslarni avtomatik masshtablash imkonini beradi.

### Server nomi

- Qurilmani boshqaruv panelida oson topish uchun noyob **Server Name** va toʻgʻri **Server Hostname** ni kiriting.

![Server xost nomi](../../images/create-instance-server-hostname.png)

### Tekshirish va joylashtirish

- Kerakli **Billing Cycle** ni tanlang. VNF qurilmalari uchun quyidagi davrlar qoʻllab-quvvatlanadi: soatlik, oylik, choraklik, yarim yillik, yillik, ikki yillik va uch yillik.
- Barcha asosiy billing qoidalari qoʻllab-quvvatlanadi: Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata va Unfixed Prorata.
- SSD hajmi va maʼlumotlar markazi joylashuviga qarab turli paketlar mavjud — bu tarmoq funksiyalarini hudud va unumdorlik talablarini hisobga olgan holda joylashtirish imkonini beradi.
- Barcha parametrlarni va umumiy narxni tekshiring. Qurilmani yaratish uchun **Review & Deploy** tugmasini bosing.

![Tekshirish va joylashtirish](../../images/create-instance-depoly.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da VNF qurilmalarini osongina yaratishingiz va boshqarishingiz mumkin. VNF qurilmalari virtuallashtirilgan muhitda tarmoq xizmatlarini joylashtirish uchun moslashuvchan va masshtablanuvchi yechimdir. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ommaviy tarmoq](../networks/public-network/create-public-network.md)**
> - **[VPC tarmogʻi](../networks/vpc-network/create-vpc-network.md)**
> - **[Affinity guruhlari](../affinity-groups/create-affinity-groups.md)**
> - **[Ommaviy IP manzil](../networks/public-ip-address.md)**
> - **[Shablonlar yaratish](../templates/create-templates.md)**
