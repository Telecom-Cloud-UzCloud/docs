# Настройка CORS

Браузеры блокируют запросы веб-страницы к другому домену, если сервер их явно не разрешил. Правила **CORS** (Cross-Origin Resource Sharing) позволяют вашему сайту загружать файлы из бакета или отправлять файлы в бакет прямо из браузера.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

## Создание правил

Опишите правила в файле `cors.json`. Этот пример разрешает сайту `https://example.com` читать объекты и загружать их по presigned URL:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://example.com"],
      "AllowedMethods": ["GET", "HEAD", "PUT"],
      "AllowedHeaders": ["*"],
      "ExposeHeaders": ["ETag"],
      "MaxAgeSeconds": 3600
    }
  ]
}
```

- `AllowedOrigins` — домены вашего сайта. Не используйте `*`, если файлы не публичные.
- `AllowedMethods` — разрешенные HTTP-методы.
- `MaxAgeSeconds` — сколько браузер кеширует результат предварительного запроса.

Примените и проверьте правила:

```bash
aws s3api put-bucket-cors --bucket my-bucket --cors-configuration file://cors.json
aws s3api get-bucket-cors --bucket my-bucket
```

## Проверка из командной строки

Отправьте предварительный запрос так же, как это делает браузер. В ответе должен быть заголовок `Access-Control-Allow-Origin`:

```bash
curl -i -X OPTIONS "https://s3.uzcstorage.uz/my-bucket/image.png" \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: GET"
```

Чтобы удалить правила: `aws s3api delete-bucket-cors --bucket my-bucket`.

> [!TIP]
> **См. также:**
>
> - **[Поддерживаемые возможности](overview.md)**
