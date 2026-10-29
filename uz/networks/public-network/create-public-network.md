# Ommaviy tarmoq yaratish

## Ommaviy tarmoq yaratish

UzCloud’dagi **ommaviy tarmoq** — oʻrnatilgan bulutli xavfsizlik devoriga ega izolyatsiya qilingan mehmon tarmogʻi. U VM’larga ommaviy IP manzil orqali internetga chiqish imkonini beradi, trafik qoidalari, portlarni yoʻnaltirish va masofaviy kirish VPN’i esa murakkab sozlashlarsiz belgilanadi.

- Chap menyuning **NETWORKING** boʻlimida **Networks** ni bosing va **Public Network** yorligʻini oching.
- Yuqori oʻng burchakdagi **+ Create New** tugmasini bosing. **Create Isolated Network** sahifasi ochiladi.

![Public Network yorligʻi](../../../images/public-networks-1.png)

### Loyihani tanlang

- Resurslarni tartibga solish uchun tarmoqni loyihalaringizdan biriga biriktiring.

![Loyihani tanlash](../../../images/public-networks-3.png)

### Joylashuvni tanlang

- Tarmoq joylashadigan maʼlumotlar markazini tanlang: **TASHKENT** yoki **FERGANA**.

![Joylashuvni tanlash](../../../images/public-networks-2.png)

### Tarmoq maʼlumotlari

- **Network Name** maydoniga noyob nom va xohishga koʻra **Network Description** maydoniga tavsif kiriting.

![Tarmoq maʼlumotlari](../../../images/public-networks-4.png)

### Tarmoq konfiguratsiyasi

- Kerak boʻlsa, tarmoq shlyuzini (**Gateway**, masalan `10.0.0.1`) va niqobini (**Netmask**, masalan `255.255.255.0`) belgilang. Maydonlar boʻsh qoldirilsa, standart qiymatlar ishlatiladi.

![Tarmoq konfiguratsiyasi](../../../images/public-networks-5.png)

### Tarmoqni yarating

- Sahifaning pastki qismida **Billing Cycle** (toʻlov davri) ni tanlang: **Monthly** (oylik) yoki **Yearly** (yillik). **Price Summary** da narx koʻrsatiladi.
- Konfiguratsiyani tekshiring va **Create Network** tugmasini bosing.

![Tarmoqni yaratish](../../../images/public-networks-6.png)

### Xulosa

Ommaviy tarmoq VM’larni internetga ulaydi va ularni oʻrnatilgan xavfsizlik devori bilan himoya qiladi. Tarmoq yaratilgach, chiquvchi trafik qoidalarini va uning ommaviy IP manzilini sozlang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ommaviy tarmoq sharhi](network-overview.md)**
> - **[Ommaviy IP manzillar](public-ip-addresses.md)**
