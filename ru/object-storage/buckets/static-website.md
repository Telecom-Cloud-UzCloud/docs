# Статический сайт

Статический сайт (HTML, CSS, JavaScript, изображения) можно разместить в бакете. Это подходит для лендингов, документации и одностраничных приложений (React, Vue, Angular) без серверной части.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

## Шаг 1. Загрузите сайт

```bash
aws s3 sync ./dist s3://my-site/ --delete --cache-control "public, max-age=300"
```

## Шаг 2. Откройте публичный доступ

Примените политику, которая разрешает всем читать файлы сайта:

```bash
cat > policy.json <<'EOF'
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicReadWebsite",
    "Effect": "Allow",
    "Principal": "*",
    "Action": ["s3:GetObject"],
    "Resource": ["arn:aws:s3:::my-site/*"]
  }]
}
EOF
aws s3api put-bucket-policy --bucket my-site --policy file://policy.json
```

Теперь файлы доступны по адресу `https://s3.uzcstorage.uz/my-site/index.html`.

## Шаг 3. Подключите свой домен

Чтобы сайт открывался по адресу `https://example.com`, а для адресов папок отдавался `index.html`, поставьте перед бакетом Nginx. Возьмите конфигурацию из статьи **[Проксирование S3 через Nginx](../examples/nginx-proxy.md)** и замените блок `location`:

```nginx
location / {
    limit_except GET HEAD { deny all; }

    # /about/ -> /about/index.html
    rewrite ^(.*)/$ $1/index.html break;

    proxy_pass https://s3.uzcstorage.uz/my-site;
    proxy_set_header Host s3.uzcstorage.uz;
    proxy_ssl_server_name on;
    proxy_intercept_errors on;
    error_page 403 404 = /index.html;   # for single-page applications
}
```

Для обычного многостраничного сайта замените последнюю строку на `error_page 404 /404.html;`.

> [!TIP]
> После выкладки новой версии файлы с долгим `Cache-Control` могут оставаться в кеше браузеров. Давайте ресурсам имена с версией (например, `app.3f9c2.js`), а для `index.html` оставляйте короткий срок кеширования.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
