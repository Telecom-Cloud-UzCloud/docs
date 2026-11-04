# Bucket Policy

**Bucket Policy** — набор правил доступа к бакету в формате JSON. С его помощью можно сделать часть объектов публичными, ограничить доступ по IP-адресу или запретить удаление объектов.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

**В консоли** политику можно задать в поле **Bucket Policy** при создании бакета. **Через AWS CLI** сохраните политику в файл и примените ее:

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
aws s3api get-bucket-policy --bucket my-bucket
aws s3api delete-bucket-policy --bucket my-bucket   # remove the policy
```

## Публичный доступ к папке

Любой может скачивать объекты с префиксом `public/`, остальные объекты бакета остаются закрытыми:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadForPublicFolder",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-bucket/public/*"]
    }
  ]
}
```

После этого объекты доступны по адресу `https://s3.uzcstorage.uz/my-bucket/public/<файл>`.

## Доступ только с ваших IP-адресов

Запретите все запросы, кроме запросов с указанных адресов:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOutsideOffice",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
      "Condition": {
        "NotIpAddress": { "aws:SourceIp": ["203.0.113.0/24"] }
      }
    }
  ]
}
```

> [!WARNING]
> Если ошибиться в списке адресов, можно потерять доступ к бакету и из своих инструментов. Сначала проверьте политику на тестовом бакете. Удалить политику можно в консоли или командой `delete-bucket-policy` с разрешенного адреса.

## Запрет удаления объектов

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyDelete",
      "Effect": "Deny",
      "Principal": "*",
      "Action": ["s3:DeleteObject", "s3:DeleteObjectVersion"],
      "Resource": ["arn:aws:s3:::my-bucket/*"]
    }
  ]
}
```

Для надежной защиты бэкапов используйте **[Object Lock](object-lock.md)**: в отличие от политики, его не сможет снять тот, у кого есть ваши ключи.

> [!TIP]
> **См. также:**
>
> - **[Поддерживаемые возможности](overview.md)**
