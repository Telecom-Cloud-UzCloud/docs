# Maʼlumotlar bazalari zaxira nusxalari

Ishlayotgan maʼlumotlar bazasi bor VM snapshoti har doim ham yaxlit boʻlmaydi. Maʼlumotlar bazasini zaxiralashning ishonchli usuli — standart vositalar bilan muntazam damp olish va uni obyektli xotiraga yuklash.

Misollarda `root` foydalanuvchisi uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-backups` ni oʻz bucketingiz nomiga almashtiring.

## Zaxira nusxalash skripti

`/usr/local/bin/db-backup.sh` faylini yarating. Damp siqiladi va diskda joy egallamasdan bevosita bucketga yuklanadi.

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

`--expected-size` (baytlarda) AWS CLI’ga oqimdan maʼlumotlarni yuklashda qism hajmini tanlashga yordam beradi. Eng katta dampingiz hajmidan kattaroq qiymatni koʻrsating.

## Jadval

```bash
sudo chmod 700 /usr/local/bin/db-backup.sh
echo "30 2 * * * root /usr/local/bin/db-backup.sh >> /var/log/db-backup.log 2>&1" | sudo tee /etc/cron.d/db-backup
```

## Eski damplarni avtomatik oʻchirish

Damplarni 30 kundan keyin oʻchiradigan **[hayot sikli qoidasini](../features/lifecycle.md)** qoʻshing:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-backups --lifecycle-configuration '{
  "Rules": [
    {"ID": "db-30-days", "Status": "Enabled", "Filter": {"Prefix": "postgres/"}, "Expiration": {"Days": 30}},
    {"ID": "mysql-30-days", "Status": "Enabled", "Filter": {"Prefix": "mysql/"}, "Expiration": {"Days": 30}}
  ]
}'
```

## Tiklash

```bash
# PostgreSQL
aws s3 cp s3://my-backups/postgres/shop/shop-2026-11-04-0230.dump - \
  | sudo -u postgres pg_restore -d shop --clean --if-exists

# MySQL
aws s3 cp s3://my-backups/mysql/shop/shop-2026-11-04-0230.sql.gz - | gunzip | mysql shop
```

> [!TIP]
> Tiklashni ishchi baza ustida emas, alohida baza yoki VM’da tekshiring.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
