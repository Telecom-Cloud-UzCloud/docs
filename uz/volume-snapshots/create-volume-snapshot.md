# Disk snapshotini yaratish

## Virtual mashina diskining snapshoti

**Disk snapshotlari** diskning maʼlum bir vaqtdagi holatini saqlaydi, maʼlumotlar yaxlitligini hamda ishonchli zaxiralash va tiklashni taʼminlaydi. Snapshot diskni u yaratilgan paytdagi aynan oʻsha holatga tezda qaytarish imkonini beradi — masalan, tasodifiy oʻchirish, maʼlumotlar shikastlanishi yoki tizim nosozligidan keyin.

**UzCloud**’da disk snapshotlarini tushunarli interfeys orqali oson yaratish va boshqarish mumkin. Ushbu qoʻllanmada disk snapshotini yaratish bosqichma-bosqich tushuntiriladi.

---

### Blokli xotira diskining snapshotini yaratish

- Chap menyuda **Snapshots** yorligʻini oching.
- **Snapshots** sahifasi ochiladi. **Volume Snapshot** yorligʻiga oʻting.

![Disk snapshotlari sahifasi](../../images/create-volume-snap.png)

- Snapshot yaratish uchun sahifaning oʻng tomonidagi **Take Snapshot** yoki **plyus (+)** belgisini bosing.

### Joylashuvni tanlash

- Resurs jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/create-snapshot-vm-instance-location.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun snapshotni loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/create-block-storages-select-project.png)

### Blokli xotirani tanlash

- **Volumes** roʻyxatidan snapshot yaratiladigan diskni tanlang.

![Blokli xotirani tanlash](../../images/create-volume-storage-snap.png)

### Snapshot nomi

- Snapshotni boshqaruv panelida oson topish uchun noyob **Snapshot Name** ni kiriting.

![Snapshot nomi](../../images/create-volume-snapshot-inline-70690b5b.png)

### Snapshotni yaratish

- Kerakli **Billing Cycle** ni tanlang. Snapshotlar va zaxira nusxalar uchun faqat soatlik toʻlov va yagona billing qoidasi — Fixed Prorata qoʻllab-quvvatlanadi.
- VM snapshotlari, blokli xotira snapshotlari va VM zaxira nusxalari uchun har bir zonada faqat bitta paket qoʻllab-quvvatlanadi. Avtomatik VM zaxira nusxalari administrator tomonidan yoqilgan boʻlsa, virtual mashina narxining 20% ini tashkil qiladi.
- Barcha parametrlarni va umumiy narxni tekshiring. Disk snapshotini yaratish uchun **Take Snapshot** tugmasini bosing.

![Snapshotni yaratish](../../images/create-snapshot-vm-instance-snapshot-takesnap.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da disk snapshotlarini osongina yaratishingiz va boshqarishingiz mumkin. Disk snapshotlari maʼlumotlar yaxlitligini hamda tasodifiy oʻchirish, maʼlumotlar shikastlanishi yoki tizim nosozliklaridan keyin tez tiklashni taʼminlaydigan ishonchli zaxiralash usulidir. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Disk yaratish](../volumes/create-volume.md)**
> - **[VM snapshoti](../vm-snapshots/create-instance-snapshot.md)**
> - **[Zaxira nusxalar yaratish](../backups/create-backups.md)**
