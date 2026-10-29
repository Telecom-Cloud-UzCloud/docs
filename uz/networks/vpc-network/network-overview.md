# Tarmoq sharhi

## VPC tarmogʻi sharhi

VPC’ni ochish uchun **Networks** sahifasining **VPC Network** yorligʻida uning nomini bosing. VPC sahifasida yaratilgan va uzaytirilgan sanalar, loyiha va joylashuv koʻrsatiladi. Chap tomondagi yorliqlar VPC sozlamalarini ochadi.

![VPC sahifasi](../../../images/vpc-net-1.png)

### Amal tugmalari

Amal tugmalari VPC kartochkasining yuqori oʻng burchagida joylashgan:

- **Update vpc** — VPC nomi va tavsifini oʻzgartiradi.
- **Restart** — VPC tarmogʻini qayta ishga tushiradi.
- **Refresh** — VPC maʼlumotlarini yangilaydi.
- **Delete** — VPC’ni oʻchiradi.

### Maʼlumotlar

**Details** yorligʻida VPC’ning asosiy parametrlari koʻrsatiladi.

![VPC maʼlumotlari](../../../images/vpc-net-2.png)

- **ID** — VPC identifikatori.
- **Joylashuv** — VPC maʼlumotlar markazi.
- **Description** — VPC tavsifi.
- **Restart Network** — oʻzgarishlarni qoʻllash uchun tarmoqni qayta ishga tushirish kerakmi (true/false).
- **Account** va **Domain** — VPC tegishli boʻlgan hisob va domen.
- **Network Domain** — VPC ichidagi oʻzaro aloqa uchun DNS domeni.
- **CIDR** — VPC manzillar maydoni.

### VPC yorliqlari

- **[Network](add-network.md)** — VPC ichida yaratilgan tarmoqlar (qatlamlar).
- **[Public IP Addresses](public-ip-address.md)** — VPC’ning ommaviy IP manzillari.
- **[Network ACL List](network-acl-list.md)** — VPC tarmoqlari uchun kirishni boshqarish roʻyxatlari.
- **[VPN Gateway](vpn-gateway.md)** — «tarmoq — tarmoq» ulanishlari uchun VPC’ning VPN shlyuzi.
- **[VPN Connections](vpn-connections.md)** — «tarmoq — tarmoq» VPN ulanishlari.
- **[Associated VMs](associated-vms.md)** — VPC’ga ulangan VM’lar.
- **Static Routes** — VPC’ning statik marshrutlari (quyida qarang).

### Statik marshrutlar

Statik marshrutlar belgilangan manzillar oraligʻi uchun trafikni koʻrsatilgan keyingi tugunga yoʻnaltiradi.

![Statik marshrutlar](../../../images/vpc-net-13.png)

- **Static Routes** yorligʻida **+ Add Static Route** ni bosing.
- **CIDR** maydoniga manzil oraligʻini va **Next Hop** maydoniga keyingi tugun manzilini kiriting, soʻng **Add** tugmasini bosing.

![Statik marshrut qoʻshish](../../../images/vpc-net-14.png)

### Xulosa

VPC sahifasi virtual xususiy bulut haqidagi asosiy maʼlumotlarni koʻrsatadi va uning barcha sozlamalariga kirish imkonini beradi: tarmoqlar, IP manzillar, ACL, VPN va marshrutlar.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPC tarmogʻini yaratish](create-vpc-network.md)**
> - **[VPN shlyuzi](vpn-gateway.md)**
> - **[VPN ulanishlari](vpn-connections.md)**
