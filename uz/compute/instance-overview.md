# Virtual mashina sharhi

## UzCloud’da virtual mashina sharhi

**Virtual Machine Overview** sahifasida virtual mashina (VM) haqida batafsil maʼlumot va uni boshqarish uchun tezkor amallar jamlangan.

---

### VM’lar roʻyxatidagi tezkor amallar

- **Instances** sahifasida tezkor amallarni ochish uchun VM kartochkasidagi uch nuqtali tugmani bosing: konsolga kirish, toʻxtatish, qayta ishga tushirish va oʻchirish.

![Tezkor amallar](../../images/instance-cloudstack.png)

### Amal tugmalari

- **Virtual Machine Overview** sahifasini ochish uchun VM nomini bosing. Amal tugmalari holat satrining oʻng tomonida joylashgan.

![Amal tugmalari](../../images/instance-overview-action-buttons.png)

- **Refresh** — VM holati va sahifadagi maʼlumotlarni yangilaydi.
- **Console Access** — VM bilan bevosita ishlash uchun veb-konsolni ochadi.
- **VM Volumes Snapshots** — VM disklarining snapshotlarini koʻrsatadi va yangisini olish imkonini beradi.
- **VM Snapshot** — butun VM’ning snapshotini oladi.
- **Stop** — virtual mashinani oʻchiradi (VM toʻxtatilgan boʻlsa, tugma uni ishga tushiradi).
- **Reboot** — VM’ni qayta ishga tushiradi.
- **Attach ISO To This Virtual Machine** — tizimni oʻrnatish yoki tiklash uchun VM’ga ISO obrazni ulaydi.
- **Delete** — VM’ni butunlay oʻchirib tashlaydi.

Sahifada quyidagi yorliqlar ham bor: **Overview**, **Usage Graphics**, **VM Settings**, **VM Snapshot**, **Schedules**, **Backups**, **Addons** va **Activity logs**.

### Virtual mashina haqida maʼlumot

![VM haqida maʼlumot](../../images/instance-overview-info.png)

- **VM nomi** va **Created on** — virtual mashina nomi, yaratilgan sana va vaqt. Nom yonidagi strelka yordamida VM’lar oʻrtasida almashish mumkin.
- **Status** — VM’ning joriy holati (masalan, Running).

### Virtual mashina tafsilotlari

![VM tafsilotlari](../../images/instance-overview-details.png)

- **Joylashuv** — VM joylashgan maʼlumotlar markazi.
- **Operatsion tizim** — VM’ga oʻrnatilgan OT.
- **All Time Consumption** — VM yaratilgandan beri isteʼmolning umumiy qiymati.
- **Label** — VM nomi.
- **CPU**, **RAM** va **SSD** — vCore soni, xotira hajmi va disk hajmi.
- **Public IP** va **Private IP Address** — ommaviy va ichki IP manzillar (ularni nusxalash belgisi yordamida nusxalash mumkin).
- **SSH Port** — SSH orqali ulanish porti.
- **network 1**, **network 2**… — VM ulangan tarmoqlar.
- **Username** va **Provisioning Password** — standart kirish maʼlumotlari. Parolni koʻrsatish uchun koʻz belgisini bosing.
- **Affinity Groups** — VM’ning affinity guruhi (agar belgilangan boʻlsa).
- **Tag** — resurslarni tartibga solish uchun teglar. Teg qoʻshish uchun **+ Add Tag** ni bosing, kalit va qiymatni kiriting va saqlang.

### Resurslardan foydalanish

![Resurslardan foydalanish](../../images/instance-overview-resource-details.png)

- **Disk Size** va **Disk Backups** — disk hajmi va disk zaxira nusxalari soni.
- **Network Traffic** — tanlangan davrdagi yuborilgan va qabul qilingan trafik (standart holatda — oxirgi bir soat).
- **CPU** va **RAM** — protsessor va xotiraning joriy yuklamasi foizda.

### Xulosa

**Virtual Machine Overview** sahifasi VM konfiguratsiyasi haqida toʻliq tasavvur beradi va uning holatini tezkor boshqarish imkonini beradi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Virtual mashina](compute-instance.md)**
> - **[Resurslar monitoringi](monitoring-resources.md)**
> - **[Konsolga kirish](console-access.md)**
