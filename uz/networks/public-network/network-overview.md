# Tarmoq sharhi

## Ommaviy tarmoq sharhi

Ommaviy tarmoqni ochish uchun **Networks** sahifasining **Public Network** yorligʻida uning nomini bosing. Tarmoq sahifasida yaratilgan sana va joylashuv koʻrsatiladi. Yuqori oʻng burchakdagi amal tugmalari tarmoqni tahrirlash, maʼlumotlarni yangilash va tarmoqni oʻchirish imkonini beradi.

![Ommaviy tarmoq sahifasi](../../../images/pub-net-1.png)

### Maʼlumotlar

**Details** yorligʻida tarmoqning asosiy parametrlari koʻrsatiladi.

![Tarmoq maʼlumotlari](../../../images/pub-net-2.png)

- **Name** — tarmoq nomi.
- **Type** — tarmoq turi (**Isolated**).
- **Traffic Type** — trafik turi (**Guest** — VM trafigi).
- **Restart Required** — oʻzgarishlarni qoʻllash uchun tarmoqni qayta ishga tushirish kerakmi.
- **Redundant Router** — zaxira virtual marshrutizator ishlatiladimi.
- **Persistant** — ishlayotgan VM’lar boʻlmasa ham tarmoq faol qoladimi.
- **Gateway**, **Netmask** va **CIDR** — tarmoq shlyuzi, niqobi va manzillar oraligʻi.
- **Account** — tarmoq tegishli boʻlgan hisob.

### Tarmoq yorliqlari

- **[Egress rules](egress-rules.md)** — chiquvchi trafik qoidalari.
- **[Public IP Addresses](public-ip-addresses.md)** — tarmoqning ommaviy IP manzillari.
- **[Associated VMs](associated-vms.md)** — tarmoqqa ulangan VM’lar.

### Xulosa

Tarmoq sahifasi uning konfiguratsiyasi haqidagi asosiy maʼlumotlarni — turi, shlyuzi, niqobi va CIDR’ni — koʻrsatadi hamda chiquvchi trafik qoidalari va IP manzillarga kirish imkonini beradi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ommaviy tarmoq yaratish](create-public-network.md)**
> - **[Ommaviy IP manzillar](public-ip-addresses.md)**
