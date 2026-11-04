# Server Backups with restic

**restic** is a backup tool that encrypts data, stores only changed blocks (deduplication) and keeps the history of copies. It works on Linux, macOS and Windows.

## Installation

```bash
sudo apt install restic        # Ubuntu, Debian
sudo dnf install restic        # Rocky Linux, AlmaLinux (EPEL)
```

## Configuration

Create a file with the connection settings, for example `/root/.restic-env`:

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
> restic encrypts backups with this password. **Without the password, the backups cannot be restored.** Store a copy of it outside the server, for example in a password manager.

Initialize the repository:

```bash
source /root/.restic-env
restic -o s3.bucket-lookup=path -o s3.region=default init
```

## Create a Backup

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R backup /etc /var/www /home --exclude-caches
$R snapshots
```

## Automate and Rotate

Create a `/usr/local/bin/restic-backup.sh` script that makes a backup and keeps 7 daily, 4 weekly and 6 monthly copies:

```bash
#!/bin/bash
set -e
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"
$R backup /etc /var/www /home --exclude-caches --quiet
$R forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune --quiet
```

Make it executable and run it every night at 03:00 with cron:

```bash
sudo chmod 700 /usr/local/bin/restic-backup.sh
echo "0 3 * * * root /usr/local/bin/restic-backup.sh >> /var/log/restic.log 2>&1" | sudo tee /etc/cron.d/restic
```

## Restore

```bash
source /root/.restic-env
R="restic -o s3.bucket-lookup=path -o s3.region=default"

$R restore latest --target /restore                      # the whole latest backup
$R restore latest --target /restore --include /etc/nginx # one folder
$R check                                                 # verify the repository
```

Test restoring regularly: a backup that has never been restored is not a guarantee.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
