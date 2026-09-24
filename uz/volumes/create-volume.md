# Disk yaratish

## Blokli xotira disklari

**Blokli xotira disklari** (volume) — virtual mashinalarga ulanadigan va maʼlumotlar uchun qoʻshimcha joy beradigan NVMe SSD asosidagi masshtablanuvchi xotira. Ulangandan soʻng VM xotirasini kengaytirish uchun diskni qoʻlda formatlash va montaj qilish kerak.

**UzCloud** blokli xotirani joylashtirish va boshqarishni soddalashtiradi hamda infratuzilmani ehtiyojlarga muvofiq masshtablash imkonini beradi. Ushbu qoʻllanmada **UzCloud**’da blokli xotira diskini yaratish va ulash tushuntiriladi.

---

### UzCloud’da blokli xotira diskini yaratish

- Chap menyuda **Block Storages** yorligʻini oching.
- **Create Block Storage Volume** sahifasi ochiladi.

![Blokli xotira yaratish](../../images/create-block-storages.png)

- Disk yaratish uchun sahifaning oʻng tomonidagi **Create Block Storage** yoki **plyus (+)** belgisini bosing.

### Joylashuvni tanlash

- Resurs jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/create-block-storages-location.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun diskni loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/create-block-storages-select-project.png)

### Virtual mashinani tanlash

- Disk ulanadigan virtual mashinani tanlang.

![VM’ni tanlash](../../images/create-block-storages-select-instance.png)

### Disk hajmini tanlash

- Disk parametrlarini tanlang: **Storage Type** (xotira turi) va **Size** (hajm). Kerak boʻlsa, oʻzingizning hajmingizni belgilashingiz mumkin.
- Mavjud variantlar va rejalar:

![Disk hajmini tanlash](../../images/create-block-storages-select-volume-size.png)

### Disk nomi

- Diskni boshqaruv panelida oson topish uchun noyob **Volume Name** ni kiriting.

![Disk nomi](../../images/create-block-storages-name.png)

### Diskni yaratish

- Kerakli **Billing Cycle** (toʻlov davri) ni tanlang. Disklar uchun quyidagi davrlar qoʻllab-quvvatlanadi: soatlik, oylik, choraklik, yarim yillik, yillik, ikki yillik va uch yillik.
- Qoʻllab-quvvatlanadigan billing qoidalari: Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata va Unfixed Prorata.
- SSD hajmi va maʼlumotlar markazi joylashuviga qarab turli paketlar mavjud — bu unumdorlik va maʼlumotlarni saqlash hududini tanlashda moslashuvchanlik beradi.
- Barcha parametrlarni va umumiy narxni tekshiring. Diskni yaratish uchun **Create Volume** tugmasini bosing.

![Diskni yaratish](../../images/create-block-storages-deploy.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da blokli xotira disklarini osongina yaratishingiz va boshqarishingiz mumkin. Disklar virtual mashinalarga maʼlumotlarni saqlash vazifalarini samarali hal qilish uchun masshtablanuvchi va yuqori unumli xotira beradi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Disk snapshoti](../volume-snapshots/create-volume-snapshot.md)**
> - **[VM snapshoti](../vm-snapshots/create-instance-snapshot.md)**
> - **[Zaxira nusxalar yaratish](../backups/create-backups.md)**
