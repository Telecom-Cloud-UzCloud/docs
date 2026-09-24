# Avtomatik masshtablashni yaratish

## Avtomatik masshtablash

**Avtomatik masshtablash** (auto-scaling) joriy yuklamaga qarab virtual mashinalar (VM) sonini avtomatik oʻzgartiradi. U ilovalarning mavjudligi va optimal unumdorligini taʼminlaydi hamda resurslarni kerak boʻlganda oshirib yoki kamaytirib, xarajatlarni qisqartiradi.

---

### Avtomatik masshtablash guruhini yaratish

- Chap menyuda **Auto-scaling** yorligʻini oching.
- Avtomatik masshtablash guruhini yaratish uchun sahifaning oʻng tomonidagi **Auto-scaling** yoki **Create New** tugmasini bosing. Yaratish menyusi ochiladi.

![Avtomatik masshtablash](../../images/as-1.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun avtomatik masshtablash guruhini loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/as-2.png)

### Joylashuvni tanlash

- Serverlar jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/as-3.png)

### Tarmoqni tanlash

- Serverlar uchun tarmoqni sozlang yoki tanlang. Bu izolyatsiya qilingan xususiy tarmoq boʻlishi mumkin; bir nechta hududlarni bogʻlash uchun elastik tarmoq ham yaratish mumkin.
- Yangi tarmoqni **Create New Network** ni tanlab yaratish mumkin.

![Tarmoqni tanlash](../../images/as-4.png)

### Yuklama muvozanatlagichni tanlash

- Yuklama muvozanatlagich kiruvchi trafikni bir nechta VM’lar oʻrtasida taqsimlaydi. Roʻyxatdan kerakli **Load Balancer** ni tanlang.

![Yuklama muvozanatlagichni tanlash](../../images/as-5.png)

### Yoʻnaltirish qoidalari

- Trafik serverlar oʻrtasida qanday taqsimlanishini belgilovchi yoʻnaltirish qoidalarini sozlang.
- Kiruvchi trafik uchun portlar diapazonini kiriting: **Public** (ommaviy) va **Private** (xususiy) portlar.

![Yoʻnaltirish qoidalari](../../images/as-6.png)

### Obrazni tanlash

- Serverlarga oʻrnatiladigan operatsion tizim yoki ilova shablonini tanlang. Koʻproq moslashuvchanlik uchun oʻzingizning ISO obrazingizni yuklashingiz mumkin.

![Obrazni tanlash](../../images/as-16.png)

### Tarif rejasini tanlash

- CPU, xotira, disk va oʻtkazish qobiliyatiga boʻlgan talablaringizga qarab reja tanlang. Kerak boʻlsa, oʻzingizning rejangizni yaratishingiz mumkin.
- Narx tanlangan resurslarga bogʻliq boʻladi.

![Rejani tanlash](../../images/as-7.png)

### Server sozlamalari

- Server sozlamalarida xavfsizlikni oshirish uchun parol oʻrnatish mumkin. **Set now** tugmasini bosing.
- **Username** va **Password** ni kiriting va parolni saqlash uchun **Confirm** tugmasini bosing.

![Server sozlamalari](../../images/as-17.png)

### Quvvatni rejalashtirish

- VM’larning minimal va maksimal sonini hamda kutish davrini (grace period) soniyalarda kiriting.

![Quvvatni rejalashtirish](../../images/as-8.png)

### Siyosatlarni sozlash

- **Scale Up** siyosati resurslardan foydalanish belgilangan chegaradan oshganda ishga tushadi va ortgan yuklamani qayta ishlash uchun VM’lar qoʻshadi.

![Scale Up siyosati](../../images/as-9.png)

- **Scale Down** siyosati yuklama kamayganda ishga tushadi va tejash uchun faol VM’lar sonini kamaytiradi.

![Scale Down siyosati](../../images/as-10.png)

- Scale Up va Scale Down siyosatlariga shart qoʻshish uchun **Expression** ni bosing. **Counter** (hisoblagich), **Operator** (operator) va **Threshold** (chegara) ni kiriting va **Submit** tugmasini bosing.

![Siyosat sharti](../../images/as-15.png)

- **Scheduled Policies** (jadval boʻyicha siyosatlar) joriy metrikalarga javoban emas, balki belgilangan vaqtda oldindan belgilangan masshtablash amallarini bajaradi.

![Jadval boʻyicha siyosatlar](../../images/as-11.png)

### Avtomatik masshtablash guruhi nomi

- Guruhni boshqaruv panelida oson topish uchun noyob **Auto-scaling Name** ni kiriting.

![Avtomatik masshtablash guruhi nomi](../../images/create-auto-scaling-inline-22660263.png)

### Avtomatik masshtablash guruhini yaratish

- Kerakli **Billing Cycle** ni tanlang. Avtomatik masshtablash uchun quyidagi davrlar qoʻllab-quvvatlanadi: oylik, choraklik, yarim yillik, yillik, ikki yillik va uch yillik.
- Qoʻllab-quvvatlanadigan billing qoidalari: Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata va Unfixed Prorata.
- Avtomatik masshtablash boshqa masshtablanuvchi xizmatlar bilan bir xil toʻlov modelidan foydalanadi va yuklamaga moslashadi.
- Barcha parametrlarni va umumiy narxni tekshiring. Avtomatik masshtablash guruhini yaratish uchun **Create** tugmasini bosing.

![Avtomatik masshtablash guruhini yaratish](../../images/as-14.png)

### Xulosa

Avtomatik masshtablash resurslarni yuklamaga avtomatik moslab, ilovalarning unumdorligi, mavjudligi va iqtisodiy samaradorligini saqlashga yordam beradi. Tarmoqlar, yuklama muvozanatlagichlar, server parametrlari va masshtablash siyosatlarini puxta sozlab, siz yuklamalarning trafik oʻzgarishlariga silliq moslashishini taʼminlaysiz.
