# Yuklama muvozanatlagich

## Yuklama muvozanatlagich

**Yuklama muvozanatlagich** (Load Balancer) kiruvchi trafikni bir nechta serverlar oʻrtasida taqsimlab, yuqori mavjudlik, ishonchlilik va unumdorlikni taʼminlaydi. UzCloud’da muvozanatlagichni veb-ilovalar, maʼlumotlar bazalari va boshqa xizmatlar uchun sozlash mumkin. Ushbu qoʻllanmada UzCloud’da yuklama muvozanatlagichni sozlash bosqichma-bosqich tushuntiriladi.

---

### Yuklama muvozanatlagichni yaratish

- Chap menyuda **Load Balancer** yorligʻini oching.
- Muvozanatlagich yaratish uchun sahifaning oʻng tomonidagi **Load Balancer** yoki **plyus (+)** belgisini bosing. Yaratish menyusi ochiladi.

![Load Balancer sahifasi](../../images/ldb-1.png)

### Joylashuvni tanlash

- Muvozanatlagich jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/ldb-2.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun muvozanatlagichni loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/ldb-3.png)

### Tarmoqni tanlash

- Muvozanatlagich ishlaydigan tarmoqni tanlang. U trafik yoʻnalishi va serverlarga ulanishlarni belgilaydi.

![Tarmoqni tanlash](../../images/ldb-4.png)

### IP manzilni tanlash

- Muvozanatlagich IP manzilini tanlang: **Existing IP Address** (mavjud) yoki **Acquire New IP Address** (yangi).
- **Eslatma**: **Acquire New IP** tanlanganda tanlangan zonada standart izolyatsiya qilingan IP manzil yaratiladi.

![IP manzilni tanlash](../../images/ldb-5.png)

### Yoʻnaltirish qoidalari

- Trafik serverlar oʻrtasida qanday taqsimlanishini belgilovchi yoʻnaltirish qoidalarini sozlang.

- Noyob **Rule Name** (qoida nomi) ni kiriting. **Protocol** ni tanlang (masalan, TCP, UDP, HTTP, HTTPS). Kiruvchi trafik uchun portlar diapazonini belgilang.

- Soʻrovlarni VM’lar oʻrtasida taqsimlash algoritmini tanlang:

  - **Source** — mijozning IP manziliga qarab trafikni bitta VM’ga yoʻnaltiradi.
  - **Round Robin** — trafikni barcha mavjud VM’lar oʻrtasida teng taqsimlaydi.
  - **Least Connections** — trafikni faol ulanishlari eng kam boʻlgan VM’ga yoʻnaltiradi.

- Foydalanuvchi soʻrovlari har doim bitta VM’ga yoʻnaltirilishi uchun **Sticky sessions** (sessiyalarni bogʻlash) ni yoqish mumkin:

  - **LB Cookie** — muvozanatlagich yaratgan cookie yordamida sessiyani bogʻlash.
  - **App Cookie** — ilova cookie’si yordamida sessiyani bogʻlash.
  - **Source-Based** — sessiyani mijozning IP manziliga qarab VM’ga bogʻlash.
  - **None** — sessiyalar bogʻlanmaydi; soʻrovlar odatdagidek taqsimlanadi.

- Kiruvchi trafikni qayta ishlaydigan virtual mashinalarni tanlang.

![Yoʻnaltirish qoidalari](../../images/ldb-6.png)

### Muvozanatlagich nomi

- Muvozanatlagichning noyob nomini kiriting. Nom faqat harflar va raqamlar, defislar va nuqtalardan iborat boʻlishi mumkin.

![Muvozanatlagich nomi](../../images/ldb-7.png)

### Yuklama muvozanatlagichni yaratish

- Kerakli **Billing Cycle** ni tanlang. Muvozanatlagich uchun quyidagi davrlar qoʻllab-quvvatlanadi: soatlik, oylik, choraklik, yarim yillik, yillik, ikki yillik va uch yillik.
- Qoʻllab-quvvatlanadigan billing qoidalari: Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata va Unfixed Prorata.
- Har bir zonada faqat bitta muvozanatlagich paketi mavjud — bu sozlashni soddalashtiradi va zonada bir xil ishlashni taʼminlaydi.
- Barcha parametrlarni va umumiy narxni tekshiring. Tarmoq uchun muvozanatlagich yaratish maqsadida **Create Load Balancer** tugmasini bosing.

![Muvozanatlagichni yaratish](../../images/ldb-8.png)

### Muvozanatlagichni koʻrish

- Batafsil maʼlumot uchun muvozanatlagich ustiga bosing.

![Muvozanatlagichni koʻrish](../../images/ldb-9.png)

- Bu yerda muvozanatlagich bilan bogʻliq siyosatlar koʻrsatiladi.
- Muvozanatlagichga virtual mashina ulash uchun **Add VM** ni oching va kerakli VM’ni tanlang.

![VM ulash](../../images/ldb-10.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da yuklama muvozanatlagichni osongina sozlashingiz va boshqarishingiz mumkin. Muvozanatlagichlar kiruvchi trafikni bir nechta serverlar oʻrtasida taqsimlab, yuqori mavjudlik, ishonchlilik va unumdorlikni taʼminlaydi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ommaviy tarmoq](../networks/public-network/create-public-network.md)**
> - **[VPC tarmogʻi](../networks/vpc-network/create-vpc-network.md)**
> - **[Affinity guruhlari](../affinity-groups/create-affinity-groups.md)**
> - **[Ommaviy IP manzil](../networks/public-ip-address.md)**
> - **[Shablonlar yaratish](../templates/create-templates.md)**
