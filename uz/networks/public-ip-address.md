# Ommaviy IP manzil

## Ommaviy IP manzil

UzCloud’dagi **ommaviy IP manzil** — bulutli resurslarga tayinlanadigan va ularga xususiy tarmoqdan tashqaridan murojaat qilish imkonini beradigan, internetdan foydalanish mumkin boʻlgan IP manzil. Ommaviy IP manzillar veb-serverlar, API va internetga bevosita kirish kerak boʻlgan boshqa xizmatlar uchun zarur.

---

### Ommaviy IP manzillarni koʻrish

- Chap menyuda **Networks** yorligʻini oching.
- **Networks** sahifasi ochiladi. **Public IP Address** yorligʻiga oʻting — bu yerda ommaviy IP manzillar roʻyxati keltirilgan.

![Ommaviy IP manzillar roʻyxati](../../images/public-ip-1.png)

### Ommaviy IP manzil tafsilotlari

- Batafsil maʼlumot uchun ommaviy IP manzil ustiga bosing.
- **Details** yorligʻida IP manzil, tarmoq nomi, akkaunt maʼlumotlari va zona koʻrsatiladi.

![Ommaviy IP manzil tafsilotlari](../../images/public-ip-2.png)

### Tarmoqlararo ekran qoidasini qoʻshish

- **Firewall** yorligʻiga oʻting — bu yerda avval belgilangan tarmoqlararo ekran qoidalari koʻrsatiladi.
- Qoida qoʻshish uchun **Add Firewall Rule** tugmasini bosing.

![Firewall yorligʻi](../../images/public-ip-3.png)

- Source CIDR (manba) ni kiriting va protokolni tanlang: TCP, UDP yoki ICMP.
- Boshlangʻich va oxirgi portlarni (Start va End) kiriting va **Add Firewall Rule** tugmasini bosing.

![Tarmoqlararo ekran qoidasini qoʻshish shakli](../../images/public-ip-4.png)

### Portlarni yoʻnaltirish qoidasini qoʻshish

- **Port Forwarding** yorligʻiga oʻting — bu yerda avval belgilangan portlarni yoʻnaltirish qoidalari koʻrsatiladi.
- Qoida qoʻshish uchun **Add Rule** tugmasini bosing.

![Port Forwarding yorligʻi](../../images/public-ip-5.png)

- **Private Port Range (Start - End)** — trafik yoʻnaltiriladigan ichki (xususiy) tarmoqdagi portlar diapazoni.
- **Public Port Range (Start - End)** — internetdan foydalanish mumkin boʻlgan tashqi (ommaviy) portlar.
- **Protocol** — xizmat talablariga qarab TCP, UDP yoki Both (ikkalasi).
- **Instance** — yoʻnaltirilgan trafikni qabul qiladigan virtual mashina.
- Qoidani saqlash va yaratish uchun **Submit** tugmasini bosing.

![Portlarni yoʻnaltirish qoidasini qoʻshish](../../images/public-ip-6.png)

### Masofaviy kirish VPN’ini yoqish

- **Remote Access VPNs** yorligʻiga oʻting — bu yerda masofaviy kirish VPN’i sozlanadi.
- Agar xususiy tarmoqqa himoyalangan masofaviy kirish kerak boʻlsa, VPN ulanishini yoqish uchun **Enable Remote Access VPN** tugmasini bosing.

![Masofaviy kirish VPN’ini yoqish](../../images/public-ip-7.png)

---

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’da ommaviy IP manzillarni samarali boshqarishingiz mumkin: IP manzillarni tayinlash, tarmoqlararo ekran qoidalarini qoʻllash, portlarni yoʻnaltirishni sozlash va VPN kirishini yoqish. Bu imkoniyatlar virtual infratuzilmaning mavjudligi va xavfsizligini taʼminlaydi.
