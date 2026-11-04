# Object Lock

**Object Lock** хранит объекты в режиме WORM (write once, read many — однократная запись, многократное чтение): заблокированный объект нельзя удалить или перезаписать до окончания срока хранения. Это защищает резервные копии от случайного удаления и от шифровальщиков.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

> [!IMPORTANT]
> Object Lock можно включить только при создании бакета, и отключить его потом нельзя. Он автоматически включает **[версионирование](versioning.md)**.

## Создание бакета с Object Lock

**В консоли:** при создании бакета включите **Bucket Versioning** и **Object Locking**.

**Через AWS CLI:**

```bash
aws s3api create-bucket --bucket my-backups --object-lock-enabled-for-bucket
```

## Режимы хранения

- **GOVERNANCE** — объекты защищены, но пользователь со специальным правом может снять блокировку с `--bypass-governance-retention`. Подходит для большинства случаев.
- **COMPLIANCE** — ни один пользователь не может удалить объект или сократить срок до его окончания, включая владельца аккаунта.

> [!WARNING]
> В режиме COMPLIANCE заблокированные объекты хранятся и оплачиваются до конца срока, даже если они больше не нужны. Начинайте с GOVERNANCE и коротких сроков.

## Срок хранения по умолчанию

Все новые объекты в бакете будут блокироваться на указанный срок:

```bash
aws s3api put-object-lock-configuration --bucket my-backups \
  --object-lock-configuration \
  'ObjectLockEnabled=Enabled,Rule={DefaultRetention={Mode=GOVERNANCE,Days=30}}'

aws s3api get-object-lock-configuration --bucket my-backups
```

## Блокировка отдельного объекта

```bash
aws s3api put-object-retention --bucket my-backups --key db/2026-11-01.sql.gz \
  --retention 'Mode=GOVERNANCE,RetainUntilDate=2026-12-31T00:00:00Z'

aws s3api get-object-retention --bucket my-backups --key db/2026-11-01.sql.gz
```

**Legal hold** блокирует объект бессрочно — до снятия блокировки:

```bash
aws s3api put-object-legal-hold --bucket my-backups --key db/2026-11-01.sql.gz \
  --legal-hold Status=ON
```

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
