# Kubernetes klasterini yaratish

## Kubernetes klasteri

**Kubernetes** klasteri — bu konteynerlashtirilgan ilovalarni avtomatik va masshtablanuvchan tarzda birgalikda ishga tushiradigan oldindan sozlangan mashinalar (tugunlar) toʻplami. Kubernetes bir nechta tugunlarda ilova konteynerlarini joylashtirish, masshtablash va ishlatishni boshqaradi.

**UzCloud**’da boshqariladigan Kubernetes klasteri bir necha qadamda yaratiladi: konsol boshqaruv va ishchi tugunlarni, klaster tarmogʻini hamda API uchun yuklama muvozanatlagichni oʻzi yaratadi.

---

### Kubernetes sahifasini oching

- Chap menyuning **CONTAINERS** boʻlimida **Kubernetes** ni bosing. Sahifada klasterlaringiz koʻrsatiladi: loyiha, IP manzil, yaratilgan sana, joylashuv, toʻlov davri va holat.
- Yuqori oʻng burchakdagi **+ Create New** tugmasini bosing. **Create Kubernetes** sahifasi ochiladi.

![Kubernetes sahifasi](../../images/kb-1.png)

### Loyihani tanlang

- Resurslarni tartibga solish uchun klasterni loyihalaringizdan biriga biriktiring.

![Loyihani tanlash](../../images/kb-2.png)

### Joylashuv va versiyani tanlang

- Klaster joylashadigan maʼlumotlar markazini tanlang: **TASHKENT** yoki **FERGANA**.
- **Select Version** blokida Kubernetes versiyasini tanlang.

![Joylashuv va versiya](../../images/kb-7.png)

### Tugun guruhlarini sozlang

- **Master Group** — boshqaruv tugunlari uchun **Node Plan** ni tanlang. Bitta oʻrniga bir nechta boshqaruv tugunini ishga tushirish uchun **Enable High Availability** ni yoqing (standart holatda **Control Nodes: 1**).
- **Worker Group** — ishchi tugunlar uchun **Node Plan** ni tanlang va **Node Count** maydonida ularning sonini belgilang (standart holatda 2). Yuklamalaringiz ishchi tugunlarda bajariladi.

![Tugun guruhlari](../../images/kb-3.png)

### Diskni tanlang

- **Select Disk Offering** blokida disk turini (**SSD**, **HDD** yoki **NVMe**) va tugunlar uchun diskni tanlang. Har bir variant uchun oylik va soatlik narx koʻrsatilgan.

![Diskni tanlash](../../images/kb-4.png)

### SSH kalit, xotira va klaster nomi

- SSH kalit majburiy. **Add SSH Key To Your Instance** yonidagi **Add now** ni bosing, mavjud kalitni tanlang yoki nom kiriting va ommaviy kalitni joylashtiring, soʻng **Add SSH Key** tugmasini bosing.

![SSH kalit maʼlumotlari](../../images/kb-10.png)

- CSI (Container Storage Interface) drayverini avtomatik sozlash uchun **Enable Cloud Storage Integration** ni yoqing. Shunda Kubernetes yuklamalari doimiy tomlarni dinamik yaratishi va boshqarishi mumkin boʻladi.
- **Cluster Name** maydoniga klasterning noyob nomini kiriting.

### Klasterni yarating

- Sahifaning pastki qismida **Billing Cycle** (toʻlov davri) ni tanlang: **Monthly** (oylik) yoki **Yearly** (yillik). **Price Summary** da tanlangan konfiguratsiya narxi koʻrsatiladi.
- Konfiguratsiyani tekshiring va **Review & Create Cluster** tugmasini bosing.

![Klasterni yaratish](../../images/kb-6.png)

> [!NOTE]
> Tarmoqni tanlash shart emas: UzCloud klaster uchun alohida tarmoq (masalan, `k8s-test-network`) va Kubernetes API uchun yuklama muvozanatlagich yaratadi.

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da Kubernetes klasterini bir necha daqiqada yaratishingiz mumkin. Kubernetes klasterlari konteynerlashtirilgan ilovalarni yuqori mavjudlik bilan joylashtirish, masshtablash va boshqarishning kuchli vositasidir. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Kubernetes klasterini boshqarish](kubernetes-cluster-overview.md)**
> - **[Yuklama muvozanatlagich](../load-balancer/load-balancer.md)**
> - **[Affinity guruhlari](../affinity-groups/create-affinity-groups.md)**
