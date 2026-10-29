# Tarmoq qoʻshish

## VPC’ga tarmoq qoʻshish

**Network** yorligʻida VPC ichida yaratilgan tarmoqlar (qatlamlar) keltirilgan. VM’lar ushbu tarmoqlarga ulanadi va har bir tarmoq oʻz ACL’iga ega boʻlishi mumkin.

- VPC sahifasida **Network** yorligʻini oching va **Add Networks** ni bosing.

![Network yorligʻi](../../../images/vpc-net-3.png)

- **Add VPC Network** shaklini toʻldiring:
  - **Name** — tarmoq nomi.
  - **Description** — tarmoq vazifasining tavsifi.
  - **Network ACL List** — tarmoqning kiruvchi va chiquvchi trafigini boshqaradigan ACL (masalan, `default_allow` yoki `default_deny`).
  - **Gateway** — tarmoq shlyuzi (masalan, `10.0.0.1`). U VPC manzillar maydoniga kirishi kerak.
  - **Netmask** — tarmoq niqobi (masalan, `255.255.255.0`).
- **Submit** tugmasini bosing.

![Add VPC Network shakli](../../../images/vpc-net-4.png)

### Xulosa

VPC’ga tarmoqlar qoʻshish uni oʻz shlyuzlari va ACL’lariga ega quyi tarmoqlarga boʻlish, trafikni yaxshiroq boshqarish va resurslarni tartibga solish imkonini beradi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPC tarmogʻi sharhi](network-overview.md)**
> - **[Tarmoq ACL roʻyxati](network-acl-list.md)**
> - **[VPN shlyuzi](vpn-gateway.md)**
> - **[VPN ulanishlari](vpn-connections.md)**
