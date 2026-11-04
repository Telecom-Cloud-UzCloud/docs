# Database Backups

A snapshot of a VM with a running database is not always consistent. A reliable way to back up a database is a regular dump with native tools, uploaded to object storage.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for the `root` user. Replace `my-backups` with the name of your bucket.

## Backup Script

Create `/usr/local/bin/db-backup.sh`. The dump is compressed and uploaded to the bucket on the fly, without taking up disk space.

**PostgreSQL:**

```bash
#!/bin/bash
set -euo pipefail
DATE=$(date +%F-%H%M)
BUCKET=s3://my-backups/postgres
for DB in $(sudo -u postgres psql -Atc "SELECT datname FROM pg_database WHERE NOT datistemplate"); do
  sudo -u postgres pg_dump -Fc "$DB" | aws s3 cp - "$BUCKET/$DB/$DB-$DATE.dump" --expected-size 50000000000
done
```

**MySQL / MariaDB:**

```bash
#!/bin/bash
set -euo pipefail
DATE=$(date +%F-%H%M)
BUCKET=s3://my-backups/mysql
for DB in $(mysql -NBe "SHOW DATABASES" | grep -Ev '^(information_schema|performance_schema|sys)$'); do
  mysqldump --single-transaction --routines --triggers "$DB" | gzip \
    | aws s3 cp - "$BUCKET/$DB/$DB-$DATE.sql.gz" --expected-size 50000000000
done
```

`--expected-size` (in bytes) helps AWS CLI choose the part size when it uploads data from a pipe. Set a value larger than your biggest dump.

## Schedule

```bash
sudo chmod 700 /usr/local/bin/db-backup.sh
echo "30 2 * * * root /usr/local/bin/db-backup.sh >> /var/log/db-backup.log 2>&1" | sudo tee /etc/cron.d/db-backup
```

## Delete Old Dumps Automatically

Add a **[lifecycle rule](../buckets/lifecycle.md)** that deletes dumps after 30 days:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-backups --lifecycle-configuration '{
  "Rules": [
    {"ID": "db-30-days", "Status": "Enabled", "Filter": {"Prefix": "postgres/"}, "Expiration": {"Days": 30}},
    {"ID": "mysql-30-days", "Status": "Enabled", "Filter": {"Prefix": "mysql/"}, "Expiration": {"Days": 30}}
  ]
}'
```

## Restore

```bash
# PostgreSQL
aws s3 cp s3://my-backups/postgres/shop/shop-2026-11-04-0230.dump - \
  | sudo -u postgres pg_restore -d shop --clean --if-exists

# MySQL
aws s3 cp s3://my-backups/mysql/shop/shop-2026-11-04-0230.sql.gz - | gunzip | mysql shop
```

> [!TIP]
> Test restoring to a separate database or VM, not over the production database.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
