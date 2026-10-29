# Loyiha yaratish

## Loyihani yaratish va boshqarish

Loyihalar resurslarni guruhlash va ularga kirishni boshqarishga yordam beradi. Ushbu qoʻllanmada UzCloud’da loyiha yaratish, unga foydalanuvchilarni qoʻshish va loyiha uchun kvotalarni belgilash tushuntiriladi.

### Yangi loyiha yaratish

- Chap menyuda **Projects** ni bosing. Sahifada barcha loyihalaringiz koʻrsatiladi.
- **+ Create New Project** tugmasini bosing.

![Loyihalar](../../images/create-project.png)

- **Project Name** (nomi) va **Project Description** (tavsifi, 250 belgigacha) ni kiriting hamda **Project Purpose** (maqsadi) ni tanlang. Xohlasangiz, rasmdagi qalamni bosib loyiha belgisini oʻzgartiring.
- **Create Project** tugmasini bosing.

![Loyiha yaratish](../../images/create-new-project.png)

### Loyiha resurslarini koʻrish

Loyihani ochish uchun uning kartochkasidagi **VIEW** tugmasini bosing. Loyiha sahifasida resurslar soni koʻrsatiladi: **Instances**, **Instances Snapshot**, **Backups**, **Network**, **Load Balancer** va **Kubernetes**. Loyiha nomi va tavsifini oʻzgartirish uchun yuqori oʻng burchakdagi qalam belgisini bosing.

![Loyiha resurslari](../../images/create-new-project-resources.png)

### Loyihaga foydalanuvchilarni qoʻshish

- **Users In Project** blokida **+ Add users to the project** tugmasini bosing.
- Qidiruv satri yordamida foydalanuvchilarni toping, ularni belgilang va **Assign** tugmasini bosing.
- Agar foydalanuvchi hali mavjud boʻlmasa, **+ Create new user** ni bosing.

![Loyihaga foydalanuvchilarni qoʻshish](../../images/create-new-project-add-user.png)

### Loyiha kvotalarini sozlash

**Project Quota Limit** blokida tanlangan zonadagi loyiha resurslarining limiti va ulardan foydalanish koʻrsatiladi.

- **Select Zone** maydonida zonani tanlang.

![Loyiha kvotalari](../../images/create-new-project-account-limit.png)

- **Edit Quota Limit** tugmasini bosing. **Assign a quota to the project** oynasi ochiladi.
- Zonani tanlang va cheklash kerak boʻlgan resurslar uchun **Quota Limit** ni kiriting. `-1` qiymati **cheklanmagan** kvotani bildiradi.
- **Submit** tugmasini bosing.

![Loyihaga kvota tayinlash](../../images/create-new-project-account-limit-increase.png)

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da loyihalarni yaratishingiz va boshqarishingiz, jamoa kirishini tashkil qilishingiz va resurslar isteʼmolini nazorat qilishingiz mumkin.
