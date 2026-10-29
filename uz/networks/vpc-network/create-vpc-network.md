# VPC tarmoqlarini yaratish

## VPC tarmoqlarini yaratish

UzCloud’dagi **VPC tarmogʻi** (Virtual Private Cloud) tarmoq ustidan toʻliq nazorat beradi. Xavfsizlik devori qoidalari, portlarni yoʻnaltirish va masofaviy kirish VPN’idan tashqari, unda VPN shlyuzlari va «tarmoq — tarmoq» VPN ulanishlarini sozlash, bir nechta tarmoq (qatlam) qoʻshish va ular orasidagi trafikni ACL yordamida boshqarish mumkin.

- Chap menyuning **NETWORKING** boʻlimida **Networks** ni bosing. **Your Networks** sahifasi **VPC Network** yorligʻida ochiladi.
- Yuqori oʻng burchakdagi **+ Create New** tugmasini bosing. **Create VPC Network** sahifasi ochiladi.

![Networks sahifasi](../../../images/vpc-networks-1.png)

### Loyihani tanlang

- Resurslarni tartibga solish uchun VPC’ni loyihalaringizdan biriga biriktiring.

![Loyihani tanlash](../../../images/vpc-networks-3.png)

### Joylashuvni tanlang

- VPC yaratiladigan maʼlumotlar markazini tanlang: **TASHKENT** yoki **FERGANA**. VPC faqat oʻsha joylashuvdagi resurslarni oʻz ichiga olishi mumkin.

![Joylashuvni tanlash](../../../images/vpc-networks-2.png)

### Tarmoq konfiguratsiyasi

- **Network Address** — VPC manzillar maydonining asosiy manzili (masalan, `10.10.0.0`).
- **Network Size** — manzillar maydonining hajmi: **/16** (65 536 manzil) dan **/30** gacha. Standart holatda — **/24** (256 manzil).

![Tarmoq konfiguratsiyasi](../../../images/vpc-networks-4.png)

### VPC maʼlumotlari

- **Network Name** maydoniga noyob nom va **Network Description** maydoniga VPC vazifasining tavsifini kiriting.

![VPC maʼlumotlari](../../../images/vpc-networks-5.png)

### VPC’ni yarating

- Sahifaning pastki qismida **Billing Cycle** (toʻlov davri) ni tanlang: **Monthly** (oylik) yoki **Yearly** (yillik). **Price Summary** da narx koʻrsatiladi.
- Konfiguratsiyani tekshiring va **Create VPC** tugmasini bosing.

![VPC’ni yaratish](../../../images/vpc-networks-6.png)

### Xulosa

UzCloud’dagi **VPC tarmogʻi** — bulut resurslari uchun xavfsiz, izolyatsiya qilingan va moslashuvchan muhit. VPC yaratilgach, unga tarmoqlar qoʻshing va kerak boʻlsa ACL hamda VPN’ni sozlang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPC tarmogʻi sharhi](network-overview.md)**
> - **[Tarmoq qoʻshish](add-network.md)**
> - **[Tarmoq ACL roʻyxati](network-acl-list.md)**
> - **[VPN ulanishlari](vpn-connections.md)**
