# Жизненный цикл объектов

Правила жизненного цикла автоматически удаляют объекты по истечении заданного срока: старые бэкапы, логи, временные файлы, предыдущие версии и незавершенные загрузки. Это поддерживает порядок в хранилище и снижает расходы.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

## Создание правил

Опишите правила в файле `lifecycle.json`. В этом примере:

- объекты с префиксом `logs/` удаляются через 30 дней;
- объекты с префиксом `tmp/` удаляются через 1 день;
- предыдущие версии всех объектов удаляются через 14 дней после того, как перестали быть текущими;
- незавершенные мультипарт-загрузки удаляются через 3 дня.

```json
{
  "Rules": [
    {
      "ID": "expire-logs",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Expiration": { "Days": 30 }
    },
    {
      "ID": "expire-tmp",
      "Status": "Enabled",
      "Filter": { "Prefix": "tmp/" },
      "Expiration": { "Days": 1 }
    },
    {
      "ID": "old-versions-and-uploads",
      "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "NoncurrentVersionExpiration": { "NoncurrentDays": 14 },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 3 }
    }
  ]
}
```

Примените правила к бакету и проверьте их:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json

aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
```

Чтобы удалить все правила: `aws s3api delete-bucket-lifecycle --bucket my-bucket`.

> [!NOTE]
> Правила применяются в фоне, как правило раз в сутки, поэтому объекты могут удаляться с задержкой до суток после окончания срока. Объекты под защитой **[Object Lock](object-lock.md)** не удаляются до окончания блокировки.

> [!WARNING]
> Правило с пустым префиксом и `Expiration` удаляет **все** объекты бакета по истечении срока. Перед применением правил внимательно проверьте фильтры.

> [!TIP]
> **См. также:**
>
> - **[Поддерживаемые возможности](overview.md)**
