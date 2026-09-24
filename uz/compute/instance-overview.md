# Virtual mashina sharhi

## UzCloud’da virtual mashina sharhi

**Instance Overview** sahifasida virtual mashina (VM) haqida batafsil maʼlumot va uni boshqarish vositalari jamlangan: holati, joylashuvi, operatsion tizimi, unumdorligi haqidagi maʼlumotlar hamda tezkor amallar.

---

### Amal tugmalari

- Amal tugmalari — VM bilan bajariladigan odatiy amallarga tezkor kirish.
- Tezkor amallar uchun oʻng tomondagi uchta nuqtani bosib, amallar menyusini oching.

![Amal tugmalari](../../images/instance-cloudstack.png)

- Barcha amal tugmalarini koʻrish uchun virtual mashina ustiga bosing — **Virtual Machine Overview** sahifasi ochiladi.

![Batafsil amal tugmalari](../../images/instance-overview-action-buttons.png)

- **Refresh** — VM holati va sahifadagi maʼlumotlarni yangilaydi.
- **Console Access** — VM bilan bevosita ishlash uchun konsolni ochadi.
- **VM Volume Snapshots** — snapshotlar roʻyxatini koʻrsatadi yoki zaxira nusxa yoki keyinchalik tiklash uchun VM’ning joriy holatidan snapshot olish imkonini beradi.
- **Power Off** — virtual mashinani oʻchiradi.
- **Reboot** — virtual mashinani qayta ishga tushiradi.
- **Attach ISO for VM** — tizimni oʻrnatish yoki tiklash uchun VM’ga ISO faylni ulaydi.
- **Delete** — virtual mashinani butunlay oʻchirib tashlaydi.

### Virtual mashina haqida maʼlumot

![VM haqida maʼlumot](../../images/instance-overview-info.png)

- **Instance Name** — virtual mashina nomi.
- **Created on** — yaratilgan sana va vaqt.
- **Status** — VM’ning joriy ish holati.

### Virtual mashina tafsilotlari

![VM tafsilotlari](../../images/instance-overview-info-location.png)

- **Location** — VM joylashgan maʼlumotlar markazi.
- **Operating System** — VM’dagi operatsion tizim.
- **Cost** — VM’ning butun davr mobaynidagi isteʼmol qiymati.

### Resurs xususiyatlari

![Resurs xususiyatlari](../../images/instance-overview-details.png)

- **Label** — VM’ning foydalanuvchi belgisi.
- **CPU** — ajratilgan vCPU soni.
- **RAM** — mavjud xotira hajmi.
- **Disk Size** — disk hajmi.
- **Public IP Address** — VM’ning ommaviy IP manzili.
- **Private IP Address** — tarmoqdagi ichki IP manzil.
- **Network** — bogʻlangan tarmoq.
- **Username** — kirish uchun standart foydalanuvchi nomi.
- **Password** — VM paroli.
- **Affinity Group** — optimal unumdorlik uchun guruh doirasida VM’larni joylashtirish qoidalari.
- **Tag** — turkumlash va tartibga solish uchun teglar. Teg qoʻshish uchun **Add Tag** ni bosing, Key (kalit) va Value (qiymat) ni kiriting va **Submit** tugmasini bosing.

### Resurslardan foydalanish

- Resurslardan foydalanish bloki CPU, RAM, disk va tarmoq yuklamasini vaqt boʻyicha kuzatishga yordam beradi.

![Resurslardan foydalanish](../../images/instance-overview-resource-details.png)

- **Disk Size** — diskning bandligi.
- **Network Traffic** — tanlangan davr uchun tarmoq trafigi metrikalari (standart holatda — oxirgi 24 soat).
- **CPU Usage** — protsessorning joriy yuklamasi foizda.
- **RAM Usage** — isteʼmol qilinayotgan xotira hajmi.

### Xulosa

**Instance Overview** sahifasi VM konfiguratsiyasi va uni boshqarish imkoniyatlari haqida toʻliq va koʻrgazmali tasavvur beradi. Amal tugmalari VM holatini tezkor boshqarish imkonini beradi, resurs xususiyatlari esa uning unumdorligi va ishlashini kuzatishga yordam beradi. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Virtual mashina](compute-instance.md)**
> - **[Resurslar monitoringi](monitoring-resources.md)**
> - **[Konsolga kirish](console-access.md)**
