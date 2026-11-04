# SDK для S3

Объектное хранилище UzCloud совместимо с официальными AWS SDK. Для подключения укажите адрес UzCloud, регион `default` и адресацию path-style.

| Язык | Библиотека | Статья |
|---|---|---|
| Python | boto3 | [Python](python.md) |
| JavaScript / Node.js | AWS SDK for JavaScript v3 | [JavaScript](javascript.md) |
| PHP | AWS SDK for PHP | [PHP](php.md) |
| Go | AWS SDK for Go v2 | [Go](go.md) |

## Настройки для любого SDK

- **Адрес (endpoint):** `https://s3.uzcstorage.uz`
- **Регион:** `default`
- **Адресация path-style:** включена (`forcePathStyle`, `use_path_style_endpoint`, `UsePathStyle` и т. п.).
- **Контрольные суммы:** `when_required`. Новые версии SDK по умолчанию добавляют заголовки контрольных сумм к каждому запросу; эта настройка оставляет их только там, где этого требует S3 API.
- **Ключи:** Access Key и Secret Key из окна **Credentials** — см. **[Инструменты и параметры подключения](../tools/overview.md)**.

> [!TIP]
> Подойдет и любая другая библиотека, которая поддерживает собственный адрес S3: например, AWS SDK для Java и .NET или клиенты MinIO.
