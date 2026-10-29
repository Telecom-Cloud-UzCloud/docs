# Blokli xotira

## Blokli xotira haqida umumiy maʼlumot

Blokli xotira virtual mashinaga qoʻshimcha disklarni (volume) ulash imkonini beradi. Disklar ilova maʼlumotlari, zaxira nusxalar va boshqa fayllar uchun mustaqil va masshtablanuvchi disklar sifatida ishlaydi; ularni maʼlumotlarni yoʻqotmasdan uzish va boshqa VM’larga ulash mumkin.

---

- **Virtual Machine Overview** sahifasida **VM Settings** yorligʻini oching va **Volumes** ni tanlang. Roʻyxatda VM disklari, xotira turi va hajmi koʻrsatiladi.
- Ushbu VM uchun yangi disk yaratish uchun **+ Create Volumes** ni yoki mavjud diskni ulash uchun **+ Attach Volumes** ni bosing.
- Disk kartochkasidagi belgilardan foydalaning:
  - strelka — disk snapshotlarini koʻrsatish;
  - **Create Template** — diskdan shablon yaratish;
  - **Resize Volumes** — disk hajmini oʻzgartirish;
  - **Create Snapshot** — diskning joriy holatidan snapshot olish.

![VM disklari](../../../images/vm-usage-volume.png)

---

### Xulosa

Blokli xotira maʼlumotlarni virtual mashinalardan mustaqil ravishda boshqarishning ishonchli va modulli usulidir. Muhim maʼlumotlarni himoya qilish uchun muntazam ravishda snapshot oling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Disk yaratish](../../volumes/create-volume.md)**
> - **[Disk snapshoti](../../volume-snapshots/create-volume-snapshot.md)**
> - **[VM snapshoti](../../vm-snapshots/create-instance-snapshot.md)**
