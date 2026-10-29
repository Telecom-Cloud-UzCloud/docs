# Ommaviy IP manzil

## Ommaviy IP manzil

UzCloud’dagi **ommaviy IP manzil** — internetdan foydalanish mumkin boʻlgan manzil boʻlib, u orqali bulut resurslariga tashqaridan murojaat qilish mumkin. Har bir manzil uchun xavfsizlik devori qoidalari, portlarni yoʻnaltirish va masofaviy kirish VPN’ini sozlash mumkin.

---

### Ommaviy IP manzillarni koʻrish

- Chap menyuning **NETWORKING** boʻlimida **Networks** ni bosing va **Public IP Address** yorligʻini oching. Unda manzillaringiz keltirilgan: tarmoq yoki VPC, VM’lar, loyiha va yaratilgan sana. **SOURCE-NAT** belgisi tarmoq yoki VPC chiquvchi trafik uchun ishlatadigan manzilni bildiradi.

![Ommaviy IP manzillar roʻyxati](../../images/public-ip-1.png)

### IP manzil maʼlumotlari

- Manzil sahifasini ochish uchun uni bosing. Kartochkada yaratilgan sana, joylashuv, VM’lar va bogʻlangan tarmoq koʻrsatiladi. **Details** yorligʻida IP manzil, yaratilgan sana, u **SOURCE-NAT** yoki **Static NAT** manzilimi, tarmoq nomi, hisob va mamlakat koʻrsatiladi.

![IP manzil maʼlumotlari](../../images/public-ip-2.png)

### Xavfsizlik devori qoidalari

Xavfsizlik devori qoidalari manzilga qaysi kiruvchi trafik yetib borishi mumkinligini belgilaydi.

- **Firewall** yorligʻini oching. Unda qoidalar keltirilgan: manba CIDR, protokol, ICMP turi va kodi, portlar oraligʻi. Qoidani oʻchirish uchun uning qatoridagi oʻchirish belgisini bosing.
- **+ Add A Firewall Rule** ni bosing.

![Firewall yorligʻi](../../images/public-ip-3.png)

- **Source CIDR** maydoniga manba oraligʻini kiriting (masalan, `0.0.0.0/0` — istalgan manzil), protokolni tanlang (**TCP**, **UDP** yoki **ICMP**), **Start port** va **End port** ni kiriting va **Add Firewall Rule** tugmasini bosing.

![Xavfsizlik devori qoidasini qoʻshish](../../images/public-ip-4.png)

### Portlarni yoʻnaltirish qoidalari

Portlarni yoʻnaltirish ommaviy portga kelgan trafikni tarmoqdagi VM portiga yuboradi.

- **Port Forwarding** yorligʻini oching. Unda qoidalar keltirilgan: ommaviy va ichki portlar, protokol, VM nomi, VM’ning ichki IP manzili va holat.
- **+ Add Rule** ni bosing.

![Port Forwarding yorligʻi](../../images/public-ip-5.png)

- **Private Port** — VM’dagi portlar oraligʻi (boshi va oxiri).
- **Public Port** — ommaviy IP manzildagi portlar oraligʻi (boshi va oxiri).
- **Select Protocol** — **TCP** yoki **UDP**.
- **Select Instances** — trafikni qabul qiladigan VM.
- **Submit** tugmasini bosing.

![Portlarni yoʻnaltirish qoidasini qoʻshish](../../images/public-ip-6.png)

> [!NOTE]
> Port internetdan ochiq boʻlishi uchun unga xavfsizlik devori qoidasi ham kerak.

### Masofaviy kirish VPN’i

- **Remote Access VPNs** yorligʻini oching. Xususiy tarmoqqa xavfsiz masofaviy kirish uchun **Enable Remote Access** ni bosing. Soʻng **Networks** sahifasining **[VPN Users](vpn-users.md)** yorligʻida foydalanuvchilarni qoʻshing.

![Masofaviy kirish VPN’i](../../images/public-ip-7.png)

---

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da ommaviy IP manzillarni boshqarishingiz mumkin: ular haqidagi maʼlumotlarni koʻrish, xavfsizlik devori qoidalarini belgilash, portlarni yoʻnaltirishni sozlash va VPN orqali kirishni yoqish.
