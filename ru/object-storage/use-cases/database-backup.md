# Бэкапы баз данных

Снимок ВМ с работающей базой данных не всегда согласован. Надежный способ резервного копирования базы — регулярный дамп штатными средствами с загрузкой в объектное хранилище.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для пользователя `root`. Замените `my-backups` на имя своего бакета.

## Скрипт резервного копирования

Создайте `/usr/local/bin/db-backup.sh`. Дамп сжимается и загружается в бакет на лету, не занимая место на диске.

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

`--expected-size` (в байтах) помогает AWS CLI выбрать размер части при загрузке данных из потока. Укажите значение больше размера самого большого дампа.

## Расписание

```bash
sudo chmod 700 /usr/local/bin/db-backup.sh
echo "30 2 * * * root /usr/local/bin/db-backup.sh >> /var/log/db-backup.log 2>&1" | sudo tee /etc/cron.d/db-backup
```

## Автоматическое удаление старых дампов

Добавьте **[правило жизненного цикла](../features/lifecycle.md)**, которое удаляет дампы через 30 дней:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-backups --lifecycle-configuration '{
  "Rules": [
    {"ID": "db-30-days", "Status": "Enabled", "Filter": {"Prefix": "postgres/"}, "Expiration": {"Days": 30}},
    {"ID": "mysql-30-days", "Status": "Enabled", "Filter": {"Prefix": "mysql/"}, "Expiration": {"Days": 30}}
  ]
}'
```

## Восстановление

```bash
# PostgreSQL
aws s3 cp s3://my-backups/postgres/shop/shop-2026-11-04-0230.dump - \
  | sudo -u postgres pg_restore -d shop --clean --if-exists

# MySQL
aws s3 cp s3://my-backups/mysql/shop/shop-2026-11-04-0230.sql.gz - | gunzip | mysql shop
```

> [!TIP]
> Проверяйте восстановление на отдельной базе или ВМ, а не поверх рабочей базы.

> [!TIP]
> **См. также:**
>
> - **[Сценарии использования](overview.md)**
