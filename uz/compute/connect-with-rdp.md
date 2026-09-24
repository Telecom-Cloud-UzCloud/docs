# RDP orqali ulanish

## UzCloud’da Windows VM’ga RDP orqali kirish

**Remote Desktop Protocol (RDP)** Windows virtual mashinasiga (VM) xavfsiz ulanish va uni masofadan boshqarish imkonini beradi. Ushbu qoʻllanmada UzCloud’da hisob maʼlumotlarini olish va Windows VM’ga RDP orqali ulanish bosqichma-bosqich tushuntiriladi.

---

### Virtual mashina sharhini oching

- Chap menyuda **Instances** ni bosing.
- **Virtual Machine Instance** sahifasida kerakli VM’ni tanlang.
- **VM Overview** yorligʻida **Username** va **Password** maydonlarini toping va ularning qiymatlarini nusxalang.

![Virtual mashina sharhi](../../images/instance-overview-rdp.png)

### RDP mijozini ishga tushiring

VM’ga ulanish uchun kompyuteringizda RDP mijozini oching:

- **Windows**:

  - Win + R ni bosing, `mstsc` ni kiriting va Enter ni bosing.
  - Yoki «Pusk» menyusida **Remote Desktop Connection** ni toping.

- **macOS**:

  - Agar ilova oʻrnatilmagan boʻlsa, Mac App Store’dan **Microsoft Remote Desktop** ni oʻrnating.
  - Microsoft Remote Desktop’ni oching.

- **Linux**:

  - RDP mijozini oʻrnating, masalan **Remmina** (Ubuntu/Debian’da: `sudo apt install remmina`).
  - Remmina’ni oching va **RDP** protokolini tanlang.

### Windows VM’ga ulaning

- Kompyuteringizda RDP mijozini ishga tushiring.
- UzCloud’dagi **Overview** yorligʻida VM’ning **Public IP Address** ini toping.
- RDP mijozida **Public IP Address** ni kiriting.
- Soʻrov paydo boʻlganda UzCloud’dan nusxalangan **Username** va **Password** ni kiriting.
- Agar masofaviy kompyuterning haqiqiyligi haqida xavfsizlik ogohlantirishi chiqsa, **«Don't ask me again for connections to this computer»** ni belgilang va **Yes** tugmasini bosing.
- Masofaviy seansni oʻrnatish uchun **OK** yoki **Connect** tugmasini bosing.

### Windows VM bilan ishlash

RDP orqali ulangandan soʻng siz:

- Windows VM’ni xuddi jismoniy kompyuter kabi toʻliq boshqarishingiz;
- dasturlarni oʻrnatishingiz va tizimni sozlashingiz;
- nusxalash va joylashtirish yoki umumiy papkalar orqali kompyuter va VM oʻrtasida fayllarni uzatishingiz mumkin.

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz UzCloud’dagi Windows VM’ga RDP protokoli orqali osongina ulanishingiz mumkin. RDP — boshqarish, dasturlarni oʻrnatish va fayllarni uzatish uchun virtual mashinalarga kirishning xavfsiz va samarali usuli. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[SSH orqali ulanish](connect-with-ssh.md)**
> - **[Konsolga kirish](console-access.md)**
