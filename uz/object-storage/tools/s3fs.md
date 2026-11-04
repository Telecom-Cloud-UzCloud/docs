# s3fs

**s3fs** bucketni Linux’da papka sifatida ulaydi. Shundan soʻng ilovalar obyektlarni oddiy fayllar kabi oʻqishi va yozishi mumkin.

> [!WARNING]
> Ulangan bucket haqiqiy disk emas: amallar sekinroq bajariladi va fayl har bir oʻzgarishda toʻliq qayta yoziladi. s3fs’dan maʼlumotlar bazalari va fayllarni tez-tez oʻzgartiradigan ilovalar uchun foydalanmang. U arxivlar, media va zaxira nusxalar uchun juda mos.

## Oʻrnatish

```bash
sudo apt install s3fs          # Ubuntu, Debian
sudo dnf install s3fs-fuse     # Rocky Linux, AlmaLinux (EPEL)
```

## Sozlash

Kalitlarni faylga saqlang va unga kirishni cheklang:

```bash
echo "<Access Key>:<Secret Key>" | sudo tee /etc/passwd-s3fs
sudo chmod 600 /etc/passwd-s3fs
```

## Bucketni ulash

```bash
sudo mkdir -p /mnt/s3
sudo s3fs my-bucket /mnt/s3 \
  -o passwd_file=/etc/passwd-s3fs \
  -o url=https://s3.uzcstorage.uz \
  -o use_path_request_style \
  -o allow_other
```

Bucket ulanganini tekshiring:

```bash
df -h /mnt/s3 && ls /mnt/s3
```

## Yuklanishda ulash

`/etc/fstab` fayliga qator qoʻshing:

```text
my-bucket /mnt/s3 fuse.s3fs _netdev,allow_other,use_path_request_style,url=https://s3.uzcstorage.uz,passwd_file=/etc/passwd-s3fs 0 0
```

Yozuvni qayta ishga tushirmasdan tekshiring: `sudo mount -a`. Uzish uchun: `sudo umount /mnt/s3`.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Vositalar va ulanish parametrlari](overview.md)**
