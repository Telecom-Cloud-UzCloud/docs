# Mijoz VPN shlyuzi

## Mijoz VPN shlyuzi (VPN Customer Gateway)

**Mijoz VPN shlyuzi** — mahalliy tarmogʻingiz va bulut oʻrtasida himoyalangan VPN ulanishini oʻrnatish uchun asosiy komponent. UzCloud’da u xususiy tarmogʻingiz va virtual xususiy bulut (VPC) oʻrtasida himoyalangan aloqani taʼminlaydi. Quyida UzCloud’da mijoz VPN shlyuzini sozlash va qoʻshish bosqichma-bosqich tushuntiriladi.

- Chap menyuda **Networks** yorligʻini oching.
- **Networks** sahifasi ochiladi. **VPN Customer Gateway** yorligʻiga oʻting.
- Mijoz VPN shlyuzini qoʻshish uchun **plyus (+)** belgisini bosing. Parametrlarni kiritish shakli ochiladi.

![VPN Customer Gateway yorligʻi](../../images/vpn-gate-1.png)

- **Select Project** — shlyuz yaratiladigan loyiha.
- **Select Zone** — VPN shlyuzi uchun zona yoki hudud.
- **Name** — shlyuzning noyob va tushunarli nomi.
- **CIDR List** — tarmogʻingiz va bulut oʻrtasida almashish uchun ruxsat etilgan IP manzillar diapazoni (CIDR formatida).
- **Gateway** — mahalliy VPN qurilmangizning (marshrutizator yoki tarmoqlararo ekran) ommaviy IP manzili.

![Shlyuz parametrlari](../../images/vpn-gate-2.png)

### Shlyuz sozlamalari

Himoyalangan ulanishni oʻrnatish uchun IPsec va IKE (Internet Key Exchange) parametrlarini belgilang:

- **IPsec Pre-Shared Key** — VPN qurilmalari oʻrtasida autentifikatsiya uchun umumiy maxfiy kalit.
- **IKE Lifetime** — IKE sessiyasining soniyalardagi amal qilish muddati (masalan, 28800).
- **ESP Lifetime** — ESP (Encapsulating Security Payload) sessiyasining amal qilish muddati.
- **IKE Encryption Algorithm** — IKE bosqichi uchun shifrlash algoritmi (masalan, AES-256, AES-128).
- **IKE Hash Algorithm** — yaxlitlikni nazorat qilish uchun xeshlash algoritmi (masalan, SHA-256, SHA-512).
- **IKE Version** — IKEv1 yoki IKEv2 (xavfsizroq boʻlgani uchun IKEv2 tavsiya etiladi).
- **IKE DH (Diffie-Hellman Group)** — kalit almashinuvini himoyalash uchun Diffi — Xellman guruhi (masalan, Group 14, Group 19).
- **Perfect Forward Secrecy (PFS)** — har bir kalit almashinuvi mustaqil boʻlishi uchun PFS’ni yoqing.
- **ESP Encryption Algorithm** — ESP uchun shifrlash algoritmi (masalan, AES-256).
- **ESP Hash Algorithm** — ESP yaxlitligini tekshirish uchun xeshlash algoritmi (masalan, SHA-256).

![IPsec va IKE sozlamalari](../../images/vpn-gate-3.png)

### Qoʻshimcha imkoniyatlar (ixtiyoriy)

UzCloud kengaytirilgan sozlamalarda yoqiladigan qoʻshimcha xavfsizlik va unumdorlik funksiyalarini qoʻllab-quvvatlaydi:

- **Dead Peer Detection (DPD)** — uzilgan VPN ulanishlarini kuzatadi va avtomatik tiklaydi.
- **Force Encapsulation** — VPN trafigining tarmoqlararo ekranlar va NAT orqali oʻtishini taʼminlaydi.
- **Split Connections** — zaxiralash va unumdorlik uchun bir nechta VPN tunnellaridan foydalanish imkonini beradi.

![Qoʻshimcha imkoniyatlar](../../images/vpn-gate-4.png)

- **Submit** tugmasini bosing — mijoz VPN shlyuzi yaratiladi.

### Xulosa

**Mijoz VPN shlyuzi** mahalliy infratuzilma va bulutdagi VPC oʻrtasida himoyalangan ulanishni taʼminlaydi. Sozlanadigan shifrlash, autentifikatsiya va qoʻshimcha funksiyalar gibrid muhitlarda ishonchli, maxfiy va yuqori unumli aloqani kafolatlaydi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[VPN foydalanuvchilari](vpn-users.md)**
