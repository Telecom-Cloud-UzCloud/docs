# Loyiha yaratish

## Loyihani yaratish va boshqarish

Ushbu qoʻllanmada UzCloud’da loyiha yaratish, unga foydalanuvchilarni qoʻshish hamda loyiha uchun akkaunt limitlari va kvotalarni sozlash bosqichma-bosqich tushuntiriladi.

### Yangi loyiha yaratish

- Chap menyuda **Projects** ni bosing.
- **Create a New Project** tugmasini bosing.

![Loyiha yaratish](../../images/create-project.png)

- Loyiha maʼlumotlarini kiriting: **Project Name** (nomi), **Project Description** (tavsifi) va **Project Purpose** (maqsadi).
- **Create Project** tugmasini bosing. Loyiha yaratiladi.

![Yangi loyiha maʼlumotlari](../../images/create-new-project.png)

### Loyiha resurslarini koʻrish

Loyiha yaratilgach, u bilan bogʻliq resurslarni koʻrishingiz mumkin.

![Loyiha resurslari](../../images/create-new-project-resources.png)

- **Virtual Machine** — ilovalarni ishga tushirish yoki veb-saytlarni joylashtirish uchun toʻliq sozlanadigan bulutli server.
- **VM Snapshot** — virtual mashina holati va maʼlumotlarining maʼlum bir vaqtdagi nusxasi.
- **Backup** — maʼlumotlarni himoya qilish va biznes uzluksizligini taʼminlash uchun boshqariladigan zaxira nusxalash.
- **Block Storage** — virtual mashinalarga ulanadigan qoʻshimcha xotira disklari.
- **Network** — bulutli resurslarni ulash va boshqarish uchun ommaviy va xususiy tarmoqlar.
- **Load Balancer** — yuqori mavjudlikni taʼminlash uchun trafikni bir nechta virtual mashinalar oʻrtasida taqsimlaydi.

### Loyihaga foydalanuvchilarni qoʻshish

- Loyihaga foydalanuvchilarni qoʻshish uchun **Add Users to the Project** tugmasini bosing.
- Qidiruv satri yordamida kerakli foydalanuvchini toping.
- Foydalanuvchini loyihaga qoʻshish uchun **Add** tugmasini bosing.

![Foydalanuvchi qoʻshish](../../images/create-new-project-add-user.png)

### Loyiha uchun akkaunt limitlarini sozlash

- Loyiha resurslari limitlari akkaunt limitlari orqali belgilanadi.
- **Project Account Limit** boʻlimiga oʻting. Bu yerda resurslar limitlari va joriy foydalanish koʻrsatiladi.
- Limit belgilanadigan **Zone** (zona) ni tanlang.

![Akkaunt limitlari](../../images/create-new-project-account-limit.png)

- **Edit Account Limit** tugmasini bosing. **Assign a Quota to the Project** sahifasi ochiladi.
- **Zone** va kvotasi oʻzgartiriladigan **Resource** (resurs) ni tanlang.
- Kerakli **Quota Limit** qiymatini kiriting. `-1` qiymati ushbu resurs uchun **cheklanmagan** kvotani bildiradi.
- **Submit** tugmasini bosing.

![Kvotani oshirish](../../images/create-new-project-account-limit-increase.png)

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da loyihalarni samarali yaratishingiz va boshqarishingiz, qulay hamkorlik va resurslarni optimal taqsimlashni taʼminlashingiz mumkin.
