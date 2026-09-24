# SSH orqali ulanish

## UzCloud’da SSH orqali ulanish

Virtual mashinani terminal orqali SSH yordamida boshqarish mumkin. Bu xavfsiz ulanish va maʼmuriy vazifalarni masofadan bajarish imkonini beradi — SSH mijozi yordamida yoki bevosita terminaldan. Ushbu qoʻllanmada bulutdagi VM’ga SSH orqali ulanish bosqichma-bosqich tushuntiriladi.

---

### SSH orqali ulanishga tayyorgarlik

Ulanishdan oldin sizda quyidagi maʼlumotlar borligiga ishonch hosil qiling:

- **IP manzil** — VM kartochkasida yoki Virtual Machine Overview sahifasida koʻrsatilgan.

- **Standart foydalanuvchi nomi** — operatsion tizimga bogʻliq (`root`, `ubuntu`, `ec2-user`).

- **Autentifikatsiya usuli**:

  - **SSH kalit (tavsiya etiladi)** — sizda maxfiy kalit fayli borligiga ishonch hosil qiling.
  - **Standart parol** — SSH kalit ishlatilmasa, Virtual Machine Overview sahifasida koʻrsatilgan.

![VM kartochkasi](../../images/instance.png)

### Virtual mashina haqida maʼlumot

- VM’ning **IP manzili** yaratilgandan soʻng uning kartochkasida koʻrsatiladi. Nusxalash uchun kursorni uning ustiga olib boring.
- VM haqida batafsil maʼlumot **Virtual Machine Overview** sahifasida — uni kartochkadagi VM nomini bosib ochishingiz mumkin.

![Resurs xususiyatlari](../../images/instance-overview-details.png)

### Virtual mashinaga ulanish

- Terminalni oching:

  - **Windows’da**: Command Prompt, PowerShell yoki Git Bash.
  - **macOS yoki Linux’da**: oʻrnatilgan terminal.

- Ulanish uchun SSH buyrugʻini bajaring:

  - **Agar SSH kalitdan foydalansangiz**:

    ```bash
    ssh -i /path/to/your/private/key [username]@[ip_address]
    ```

  - **Agar paroldan foydalansangiz**:

    ```bash
    ssh [username]@[ip_address]
    ```

- Soʻralganda parolni kiriting. **Parol bilan ulanish misoli**:

  ```bash
  ssh root@192.168.1.1
  ```

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz bulutdagi VM’ga SSH orqali xavfsiz ulanishingiz mumkin. SSH kalit yoki paroldan foydalanasizmi, SSH masofaviy kirish va boshqarishning ishonchli va xavfsiz usulidir. Yordam kerak boʻlsa, UzCloud hujjatlarini oʻrganing yoki qoʻllab-quvvatlash xizmatiga murojaat qiling.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[RDP orqali ulanish](connect-with-rdp.md)**
> - **[Konsolga kirish](console-access.md)**
> - **[SSH kalitlar](vm-settings/ssh-keys.md)**
