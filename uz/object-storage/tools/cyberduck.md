# Cyberduck

**Cyberduck** — macOS va Windows uchun bepul grafik fayl menejeri. Unda bucketlarni koʻrish, fayllarni sudrab tashlash orqali yuklash va yuklab olish mumkin.

## Oʻrnatish

Cyberduck’ni [cyberduck.io](https://cyberduck.io/download/) dan yuklab oling va oʻrnating.

## Path-style manzillashni yoqish

UzCloud obyektli xotirasi path-style manzillardan foydalanadi. Cyberduck’da ular uchun alohida ulanish profili bor:

1. **Preferences → Profiles** ni oching (Windows’da — **Edit → Preferences → Profiles**).
2. **S3 (Deprecated path style requests)** ni toping va uni belgilang.
3. Cyberduck’ni qayta ishga tushiring.

## Ulanish

1. **Open Connection** ni bosing.
2. Protokollar roʻyxatidan **S3 (Deprecated path style requests)** ni tanlang.
3. **Server**: `s3.uzcstorage.uz`, **Port**: `443`.
4. **Access Key ID** va **Secret Access Key** ni kiriting.
5. **Connect** ni bosing. Bucketlaringiz roʻyxati ochiladi.

Ulanishni saqlash uchun xuddi shu parametrlar bilan **Bookmark → New Bookmark** xatchoʻpini yarating.

## Foydali imkoniyatlar

- Fayl kontekst menyusidagi **Share** bandi vaqtinchalik havola (presigned URL) yaratadi.
- **Info** obyekt metamaʼlumotlarini koʻrsatadi va `Cache-Control` kabi sarlavhalarni oʻzgartirish imkonini beradi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Vositalar va ulanish parametrlari](overview.md)**
