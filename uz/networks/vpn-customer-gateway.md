# Mijoz VPN shlyuzi

## Mijoz VPN shlyuzi (VPN Customer Gateway)

**Mijoz VPN shlyuzi** «tarmoq — tarmoq» VPN ulanishining sizning tomoningizni tavsiflaydi: mahalliy VPN qurilmasi va uning IPsec sozlamalari. U UzCloud’dagi VPC’ni xususiy tarmogʻingiz bilan ulash uchun kerak.

- Chap menyuning **NETWORKING** boʻlimida **Networks** ni bosing va **VPN Customer Gateway** yorligʻini oching.
- **+ Create New** ni bosing. **Add VPN Customer Gateway** shakli ochiladi.

![VPN Customer Gateway yorligʻi](../../images/vpn-gate-1.png)

### Asosiy sozlamalar

- **Select Project** — shlyuz uchun loyiha.
- **Select Zone** — shlyuz zonasi (joylashuvi).
- **Name** — shlyuzning noyob nomi.
- **CIDR List** — mahalliy tarmogʻingizning CIDR formatidagi manzillar oraliqlari.
- **Gateway** — VPN qurilmangizning (marshrutizator yoki xavfsizlik devori) ommaviy IP manzili.
- **IPsec Preshared Key** — VPN qurilmalarini autentifikatsiya qilish uchun umumiy maxfiy kalit.
- **IKE Lifetime** — IKE seansining amal qilish muddati, soniyalarda (standart holatda 86400).
- **ESP Lifetime** — ESP seansining amal qilish muddati, soniyalarda (standart holatda 3600).

![Asosiy sozlamalar](../../images/vpn-gate-2.png)

### Shifrlash sozlamalari

Qiymatlar VPN qurilmangiz sozlamalariga mos kelishi kerak.

- **IKE Encryption** va **IKE Hash** — IKE bosqichi uchun shifrlash va xeshlash algoritmlari (standart holatda AES 128 va SHA-1).
- **IKE Version** — IKE protokoli versiyasi.
- **IKE DH** — kalit almashish uchun Diffi — Xellman guruhi (standart holatda MODP 1024).
- **Perfect Forward Secrecy** — PFS uchun DH guruhi (standart holatda Group 5 (modp 1536)).
- **ESP Encryption** va **ESP Hash** — ESP uchun shifrlash va xeshlash algoritmlari (standart holatda AES 128 va SHA-1).
- **Dead Peer Detection** — ulanish uzilganini aniqlaydi va uni tiklaydi.
- **Force Encapsulation** — VPN NAT orqali ishlashi uchun ESP paketlarini majburiy ravishda UDP’ga inkapsulyatsiya qiladi.
- **Split Connections** — roʻyxatdagi har bir CIDR uchun alohida tunnel yaratadi.
- **Submit** tugmasini bosing.

![Shifrlash sozlamalari](../../images/vpn-gate-3.png)

> [!TIP]
> Agar VPN qurilmangiz qoʻllab-quvvatlasa, kuchliroq algoritmlardan (masalan, AES 256 va SHA-256) foydalaning.

Shlyuz yaratilgach, VPC sahifasida VPN ulanishini yaratishda uni tanlang — **[VPN ulanishlari](vpc-network/vpn-connections.md)** ga qarang.

### Xulosa

**Mijoz VPN shlyuzi** mahalliy infratuzilmangiz va UzCloud’dagi VPC oʻrtasida xavfsiz ulanishni taʼminlaydi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPN foydalanuvchilari](vpn-users.md)**
