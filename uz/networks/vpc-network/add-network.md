# Tarmoq qoʻshish

## VPC’ga tarmoq qoʻshish

Network yorligʻida VPC ichida yaratilgan barcha tarmoqlar koʻrsatiladi. Kerak boʻlsa, yangi tarmoq qoʻshish mumkin.

- **Network** yorligʻiga oʻting va yangi tarmoq yaratish uchun **Add Network** tugmasini bosing.

![Network yorligʻi](../../../images/vpc-net-3.png)

- Tarmoq parametrlari bilan shaklni toʻldiring.

![Tarmoq qoʻshish shakli](../../../images/vpc-net-4.png)

- **Name** — tarmoq nomi.
- **Description** — tarmoq maqsadi tavsifi.
- **Network** — quyi tarmoqning CIDR bloki (masalan, 192.168.1.0/24).
- **ACL (Access Control List)** — kiruvchi va chiquvchi trafikni boshqarish uchun mavjud yoki yangi kirishni nazorat qilish roʻyxati.
- **Gateway** — trafikni marshrutlash uchun tarmoq shlyuzi.
- **Network Mask** — tarmoq niqobi.
- Tarmoqni yaratish uchun **Submit** tugmasini bosing.

### Xulosa

**VPC**’ga tarmoqlar qoʻshish trafikni yaxshiroq nazorat qilish va tartibga solish uchun oʻz quyi tarmoqlari, shlyuzlari va ACL’larini belgilash imkonini beradi. Toʻgʻri sozlash bilan loyiha vazifalariga mos xavfsiz va samarali tarmoq muhitini qurish mumkin.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPC tarmogʻi sharhi](network-overview.md)**
> - **[Tarmoq ACL roʻyxati](network-acl-list.md)**
> - **[VPN shlyuzi](vpn-gateway.md)**
> - **[VPN ulanishlari](vpn-connections.md)**
