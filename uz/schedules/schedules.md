# Jadvallar

## Zaxiralash va snapshot jadvallari

**Jadvallar** (Schedules) virtual mashinalarning zaxira nusxalari va disk snapshotlarini belgilangan davriylik bilan avtomatik yaratadi hamda saqlash siyosatiga muvofiq eski nusxalarni oʻchiradi.

---

### Jadvallarni koʻrish

- Chap menyuda **Schedules** ni bosing.
- Sahifada ikkita yorliq bor: **Instances Backup Schedules** (VM zaxiralash) va **Block Storage Snapshot Schedules** (disk snapshotlari). Har biri uchun jadvallar soni, shuningdek ulardan qanchasi ishlayotgani va toʻxtatilgani koʻrsatiladi.
- Jadval yaratish uchun **+ Create New** tugmasini bosing.

![Jadvallar](../../images/schedules-1.png)

### Jadval yaratish

- Nusxalar yaratiladigan **loyiha**, **joylashuv** va **virtual mashinani** (yoki diskni) tanlang.

> [!NOTE]
> Hozircha VM zaxira nusxasi faqat virtual mashinaning asosiy (root) diskini saqlaydi. Qoʻshimcha ulangan disklar unga kirmaydi.

- **Schedule Configuration** blokida belgilang:
  - **Schedule Frequency** — nusxalar qanchalik tez-tez yaratilishi (masalan, har soatda, har kuni, har hafta yoki har oyda);
  - **Timezone** — jadval ishlaydigan vaqt mintaqasi (standart holatda Asia/Samarkand);
  - **Max. Snapshots/Backups to retain** — nechta nusxa saqlanishi; eskilari avtomatik oʻchiriladi.
- **Schedule Information** blokida **Policy Name** (siyosat nomi) va xohlasangiz **Description** (tavsif) ni kiriting.
- Birinchi nusxani darhol yaratish uchun **Take One Immediate** ni belgilang.
- **Price Summary** ni tekshiring va **Review & Create** tugmasini bosing.

![Jadvalni sozlash](../../images/schedules-2.png)

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Zaxira nusxalar yaratish](../backups/create-backups.md)**
> - **[Disk snapshoti](../volume-snapshots/create-volume-snapshot.md)**
