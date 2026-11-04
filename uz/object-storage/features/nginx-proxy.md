# S3’ni Nginx orqali proksilash

Bucket oldidagi Nginx proksi fayllarni oʻz domeningizdan (masalan, `https://cdn.example.com/...`) tarqatish, ularni serverda keshlash va S3 xizmat sarlavhalarini yashirish imkonini beradi.

## Tayyorgarlik

- Nginx oʻrnatilgan VM va uning ommaviy IP manziliga yoʻnaltirilgan domen;
- tarqatmoqchi boʻlgan fayllaringizga ommaviy oʻqish huquqi — **[Bucket Policy](bucket-policy.md#papkaga-ommaviy-kirish)** ga qarang.

## Nginx konfiguratsiyasi

`/etc/nginx/conf.d/s3-proxy.conf` faylini yarating. `cdn.example.com` ni oʻz domeningizga, `my-bucket` ni esa bucket nomiga almashtiring:

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

Konfiguratsiyani tekshiring va Nginx’ni qayta yuklang:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

HTTPS sertifikatini oling, masalan, Let's Encrypt’dan:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d cdn.example.com
```

Tekshiring: `curl -I https://cdn.example.com/public/logo.png`. Takroriy soʻrovda `X-Cache-Status: HIT` sarlavhasi fayl keshdan berilganini koʻrsatadi.

> [!TIP]
> VM xavfsizlik devorida 80 va 443 portlarini oching. **[Xavfsizlik devori](../../compute/vm-settings/firewall.md)** ga qarang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Qoʻllab-quvvatlanadigan imkoniyatlar](overview.md)**
