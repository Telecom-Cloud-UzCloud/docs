# VM snapshotini yaratish

## Virtual mashina snapshoti

**VM snapshoti** virtual mashinaning maʼlum bir vaqtdagi holatini saqlaydi. Muvaffaqiyatsiz yangilanish yoki tasodifiy oʻzgarishlardan keyin unga qaytish mumkin.

> [!NOTE]
> Snapshotlar har bir GB uchun soatiga UZS 3,00 dan hisoblanadi. Snapshotni faqat hajmi teng yoki kattaroq diskka tiklash mumkin.

---

### VM snapshotini yaratish

- Chap menyuda **Snapshots** ni bosing va **Instances Snapshot** yorligʻini oching. Bu yerda barcha snapshotlar — qoʻlda va jadval boʻyicha yaratilganlari koʻrsatiladi.
- **+ Create New** tugmasini bosing. **Create Snapshot** sahifasi ochiladi. Snapshotni VM sahifasidagi **VM Snapshot** tugmasi bilan ham olish mumkin.

![Snapshotlar](../../images/create-snapshot-vm.png)

- VM joylashgan **loyiha** va **joylashuvni** tanlang.

![Loyihani tanlash](../../images/create-snapshot-project.png)

- **Choose Instance or Volumes** blokida **Instances** yorligʻini oching va virtual mashinani tanlang.

> [!IMPORTANT]
> Hozircha VM snapshoti faqat virtual mashinaning asosiy (root) diskini saqlaydi. Qoʻshimcha ulangan disklar unga kirmaydi — ular uchun disk snapshotlarini alohida oling.

![VM’ni tanlash](../../images/create-snapshot-vm-instance.png)

- Noyob **Snapshot Name** ni kiriting.
- **Price Summary** ni tekshiring va **Review And Create Snapshot** tugmasini bosing.

![Snapshot yaratish](../../images/create-snapshot-name.png)

### Xulosa

VM snapshotlari virtual mashinani tezda ishchi holatga qaytarish imkonini beradi. Snapshotlar avtomatik yaratilishi uchun **Schedules** dan foydalaning. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Disk snapshoti](../volume-snapshots/create-volume-snapshot.md)**
> - **[Virtual mashina](../compute/compute-instance.md)**
> - **[Zaxira nusxalar yaratish](../backups/create-backups.md)**
