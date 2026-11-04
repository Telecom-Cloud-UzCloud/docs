# Проксирование S3 через Nginx

Прокси на Nginx перед бакетом позволяет раздавать файлы со своего домена (например, `https://cdn.example.com/...`), кешировать их на сервере и скрывать служебные заголовки S3.

## Подготовка

- ВМ с Nginx и домен, направленный на ее публичный IP-адрес;
- публичный доступ на чтение к файлам, которые нужно раздавать, — см. **[Bucket Policy](../buckets/bucket-policy.md#публичный-доступ-к-папке)**.

## Конфигурация Nginx

Создайте `/etc/nginx/conf.d/s3-proxy.conf`. Замените `cdn.example.com` на свой домен, а `my-bucket` — на имя бакета:

```nginx
proxy_cache_path /var/cache/nginx/s3 levels=1:2 keys_zone=s3cache:10m
                 max_size=10g inactive=7d use_temp_path=off;

server {
    listen 80;
    server_name cdn.example.com;

    location / {
        limit_except GET HEAD { deny all; }

        proxy_pass https://s3.uzcstorage.uz/my-bucket/;
        proxy_set_header Host s3.uzcstorage.uz;
        proxy_ssl_server_name on;
        proxy_set_header Authorization "";

        proxy_hide_header x-amz-id-2;
        proxy_hide_header x-amz-request-id;
        proxy_hide_header x-rgw-object-type;
        proxy_hide_header Set-Cookie;
        proxy_ignore_headers Set-Cookie;

        proxy_cache s3cache;
        proxy_cache_valid 200 304 24h;
        proxy_cache_valid 404 1m;
        proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

Проверьте конфигурацию и перезагрузите Nginx:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Получите HTTPS-сертификат, например от Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d cdn.example.com
```

Проверьте: `curl -I https://cdn.example.com/public/logo.png`. При повторном запросе заголовок `X-Cache-Status: HIT` показывает, что файл отдан из кеша.

> [!TIP]
> Откройте порты 80 и 443 в брандмауэре ВМ. См. **[Брандмауэр](../../compute/vm-settings/firewall.md)**.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
