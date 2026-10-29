# Kubernetes klasteri sharhi

## UzCloud’da Kubernetes klasteri sharhi

**Kubernetes Overview** sahifasida klaster haqida batafsil maʼlumot va uni boshqarish uchun tezkor amallar jamlangan: konfiguratsiya, tugun rejalari, bogʻliq virtual mashinalar, yuklama muvozanatlagichlar va tomlar.

---

### Amal tugmalari

- **Kubernetes** sahifasida har bir klaster kartochkasida **Power Off** va **Delete** tugmalari bor. **Kubernetes Overview** sahifasini ochish uchun klaster nomini bosing.
- Amal tugmalari holat satrining oʻng tomonida joylashgan.

![Amal tugmalari](../../images/kb-m-1.png)

- **Refresh** — klaster holati va maʼlumotlarini yangilaydi.
- **Upgrade Kubernetes Version** — klasterni Kubernetes’ning yangiroq versiyasiga yangilaydi.
- **Download config file** — `kubectl` va boshqa CLI vositalari orqali ishlash uchun `kubeconfig` faylini yuklab oladi.
- **Scale Kubernetes Cluster** — ishchi tugunlar sonini oʻzgartiradi.
- **Power Off** — butun klasterni oʻchiradi.
- **Delete** — klaster va uning barcha resurslarini butunlay oʻchirib tashlaydi.

Sahifada quyidagi yorliqlar bor:

- **Overview** — quyida tavsiflangan klaster sharhi.
- **Access** — klaster konfiguratsiyasini yuklab olish hamda CLI va Kubernetes Dashboard orqali ulanish boʻyicha koʻrsatmalar.
- **Settings** — **Change Plan** (boshqaruv va ishchi tugunlar rejalarini oʻzgartirish), **Upgrade Version**, **Firewall** va **Port Forwarding**.
- **Virtual Machines** — klaster tugunlari.
- **Load Balancer** — klasterning yuklama muvozanatlagichlari (API uchun muvozanatlagich ham).
- **Volumes** — klaster tugunlarining disklari.

### Klaster sharhi

![Klaster sharhi](../../images/kb-m-6.png)

- **Total CPU** — klasterning barcha tugunlaridagi vCPU’larning umumiy soni.
- **Total RAM** — klasterga ajratilgan xotiraning umumiy hajmi.
- **Control nodes** — klaster holatini boshqaradigan tugunlar soni.
- **Worker Nodes** — yuklamalaringiz bajariladigan tugunlar soni.
- **Network** — klaster joylashgan tarmoq.
- **Status** — klasterning joriy holati (masalan, Running).

### Klaster haqida maʼlumot

![Klaster haqida maʼlumot](../../images/kb-m-2.png)

- **Project Name** — klaster tegishli boʻlgan loyiha.
- **Created at** — klaster yaratilgan sana va vaqt.
- **IP Address** — klasterning ommaviy IP manzili.
- **End Point** — Kubernetes API serverining manzili. Uni nusxalash uchun nusxalash belgisini bosing.
- **User name** — klaster tugunlaridagi standart foydalanuvchi nomi.
- **Joylashuv** — klaster ishlaydigan maʼlumotlar markazi.
- **Kubernetes Version** — klasterdagi Kubernetes versiyasi.
- **Auto Scaling** — tugunlarni avtomatik masshtablash yoqilganmi yoki yoʻqmi.
- **All Time Consumption** — klaster yaratilgandan beri uning umumiy qiymati.
- **Network** — klaster tarmogʻining nomi.
- **SSH key** — klaster tugunlariga kirish uchun SSH kalit.

### Tugunlar konfiguratsiyasi

![Tugunlar konfiguratsiyasi](../../images/kb-m-3.png)

- **Master Node Config** va **Worker Node Config** — boshqaruv va ishchi tugunlarning rejalari: **Current Plan**, **CPU** va **Memory**.

### Kubernetes servisini ochish

Kubernetes servislari maʼlum bir portda ishlaydi. Servisni internetdan foydalanish mumkin boʻlishi uchun klasterning **Settings → Firewall** yorligʻida ushbu portni oching va **Settings → Port Forwarding** yorligʻida qoida yarating. **+ Add Port Forwarding Rule** ni bosing va ommaviy port, ichki port, protokol va tugunni koʻrsating.

![Portlarni yoʻnaltirish qoidalari](../../images/kb-m-5.png)

---

### Xulosa

**Kubernetes Overview** sahifasi klaster holati, konfiguratsiyasi va resurslardan foydalanish haqida markazlashgan tasavvur beradi. Amal tugmalari klasterga xizmat koʻrsatishni soddalashtiradi, batafsil xususiyatlar esa monitoring va rejalashtirishga yordam beradi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Kubernetes klasterini yaratish](create-kubernetes-cluster.md)**
> - **[CLI orqali Kubernetes klasteri](kubernetes-cluster-via-cli.md)**
> - **[Kubernetes Dashboard’ga kirish](kubernetes-dashboard-ui-access.md)**
