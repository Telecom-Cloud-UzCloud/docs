# Nginx Proxy for S3

An Nginx proxy in front of a bucket lets you serve files from your own domain (for example, `https://cdn.example.com/...`), cache them on the server and hide S3 service headers.

## Before You Start

- a VM with Nginx and a domain pointing to its public IP address;
- public read access to the files you want to serve — see **[Bucket Policy](../features/bucket-policy.md#public-read-for-a-folder)**.

## Nginx Configuration

Create `/etc/nginx/conf.d/s3-proxy.conf`. Replace `cdn.example.com` with your domain and `my-bucket` with the name of your bucket:

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

Check the configuration and reload Nginx:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Get an HTTPS certificate, for example with Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d cdn.example.com
```

Check: `curl -I https://cdn.example.com/public/logo.png`. On the second request, the `X-Cache-Status: HIT` header shows that the file was served from the cache.

> [!TIP]
> Open ports 80 and 443 on the VM firewall. See **[Firewall](../../compute/vm-settings/firewall.md)**.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
