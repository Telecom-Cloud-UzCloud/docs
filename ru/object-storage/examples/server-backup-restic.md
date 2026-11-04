# Бэкапы сервера с restic

**restic** — утилита резервного копирования, которая шифрует данные, хранит только измененные блоки (дедупликация) и ведет историю копий. Работает в Linux, macOS и Windows.

## Установка

```bash
sudo apt install restic        # Ubuntu, Debian
sudo dnf install restic        # Rocky Linux, AlmaLinux (EPEL)
```

## Настройка

Создайте файл с параметрами подключения, например `/root/.restic-env`:

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
export RESTIC_REPOSITORY=s3:https://s3.uzcstorage.uz/my-backups/server-1
export RESTIC_PASSWORD_FILE=/root/.restic-password
```

```bash
openssl rand -base64 32 > /root/.restic-password
chmod 600 /root/.restic-env /root/.restic-password
```

> [!WARNING]
> restic шифрует бэкапы этим паролем. **Без пароля восстановить данные невозможно.** Сохраните его копию вне сервера, например в менеджере паролей.

Инициализируйте репозиторий:

```bash
source /root/.restic-env
restic -o s3.bucket-lookup=path -o s3.region=default init
```

## Создание бэкапа

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R backup /etc /var/www /home --exclude-caches
$R snapshots
```

## Автоматизация и ротация

Создайте скрипт `/usr/local/bin/restic-backup.sh`, который делает бэкап и хранит 7 ежедневных, 4 еженедельные и 6 ежемесячных копий:

```bash
#!/bin/bash
set -e
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"
$R backup /etc /var/www /home --exclude-caches --quiet
$R forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune --quiet
```

Сделайте его исполняемым и запускайте каждую ночь в 03:00 через cron:

```bash
sudo chmod 700 /usr/local/bin/restic-backup.sh
echo "0 3 * * * root /usr/local/bin/restic-backup.sh >> /var/log/restic.log 2>&1" | sudo tee /etc/cron.d/restic
```

## Восстановление

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R restore latest --target /restore                      # the whole latest backup
$R restore latest --target /restore --include /etc/nginx # one folder
$R check                                                 # verify the repository
```

Регулярно проверяйте восстановление: копия, из которой ни разу не восстанавливались, — не гарантия.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
