# VM snapshotini yaratish

## Virtual mashina snapshoti

**Virtual mashina snapshotlari** VM’ning joriy holatini, jumladan konfiguratsiya va maʼlumotlarni maʼlum bir vaqtda saqlaydi. Snapshotlar zaxiralash, avariyadan keyin tiklash va testlash uchun kuchli vosita. Ular VM’ni snapshot yaratilgan paytdagi aynan oʻsha holatga tezda qaytarish, maʼlumotlar muvofiqligini taʼminlash va nosozlik yoki tasodifiy oʻzgarishlarda ishlamay qolish vaqtini kamaytirish imkonini beradi.

**UzCloud** VM snapshotlarini yaratish va boshqarish uchun qulay interfeysni taqdim etadi, bu maʼlumotlarni himoya qilish va ish uzluksizligini saqlashga yordam beradi. Ushbu qoʻllanmada **UzCloud**’da VM snapshotini yaratish tushuntiriladi.

---

### Virtual mashina snapshotini yaratish

- Chap menyuda **Snapshots** yorligʻini oching.
- **Snapshots** sahifasi ochiladi. **Instances Snapshot** yorligʻiga oʻting.

![Snapshotlar sahifasi](../../images/create-snapshot-vm.png)

- Snapshot yaratish uchun sahifaning oʻng tomonidagi **Take Snapshot** yoki **plyus (+)** belgisini bosing.

### Joylashuvni tanlash

- Resurs jismoniy joylashadigan maʼlumotlar markazini tanlang.
- Mavjud joylashuvlardan birini tanlang.

![Joylashuvni tanlash](../../images/create-snapshot-vm-instance-location.png)

### Loyihaga biriktirish

- Resurslarni qulay tartibga solish va boshqarish uchun snapshotni loyihalaringizdan biriga biriktiring.

![Loyihaga biriktirish](../../images/create-block-storages-select-project.png)

### Virtual mashinani tanlash

- **Instances** roʻyxatidan snapshot yaratiladigan virtual mashinani tanlang.

![VM’ni tanlash](../../images/create-snapshot-vm-instance.png)

### Snapshot nomi

- Snapshotni boshqaruv panelida oson topish uchun noyob **Snapshot Name** ni kiriting.

![Snapshot nomi](../../images/create-volume-snapshot-inline-70690b5b.png)

### Snapshotni yaratish

- Kerakli **Billing Cycle** ni tanlang. Snapshotlar va zaxira nusxalar uchun faqat soatlik toʻlov va yagona billing qoidasi — Fixed Prorata qoʻllab-quvvatlanadi.
- VM snapshotlari, blokli xotira snapshotlari va VM zaxira nusxalari uchun har bir zonada faqat bitta paket qoʻllab-quvvatlanadi. Avtomatik VM zaxira nusxalari administrator tomonidan yoqilgan boʻlsa, virtual mashina narxining 20% ini tashkil qiladi.
- Barcha parametrlarni va umumiy narxni tekshiring. Virtual mashina snapshotini yaratish uchun **Take Snapshot** tugmasini bosing.

![Snapshotni yaratish](../../images/create-snapshot-vm-instance-snapshot-takesnap.png)

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da VM snapshotlarini osongina yaratishingiz va boshqarishingiz mumkin. Snapshotlar maʼlumotlar muvofiqligini hamda nosozlik yoki tasodifiy oʻzgarishlardan keyin tez tiklashni taʼminlaydigan ishonchli zaxiralash usulidir. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Disk snapshoti](../volume-snapshots/create-volume-snapshot.md)**
> - **[Virtual mashina](../compute/compute-instance.md)**
> - **[Zaxira nusxalar yaratish](../backups/create-backups.md)**
