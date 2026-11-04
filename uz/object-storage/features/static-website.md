# Statik sayt

Statik saytni (HTML, CSS, JavaScript, rasmlar) bucketda joylashtirish mumkin. Bu lendinglar, hujjatlar va server qismi boʻlmagan bir sahifali ilovalar (React, Vue, Angular) uchun mos.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

## 1-qadam. Saytni yuklang

```bash
aws s3 sync ./dist s3://my-site/ --delete --cache-control "public, max-age=300"
```

## 2-qadam. Ommaviy kirishni oching

Hammaga sayt fayllarini oʻqish imkonini beradigan siyosatni qoʻllang:

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

Endi fayllar `https://s3.uzcstorage.uz/my-site/index.html` manzilida mavjud.

## 3-qadam. Oʻz domeningizni ulang

Sayt `https://example.com` manzilida ochilishi va papka manzillari uchun `index.html` berilishi uchun bucket oldiga Nginx qoʻying. **[S3’ni Nginx orqali proksilash](../use-cases/nginx-proxy.md)** maqolasidagi konfiguratsiyani oling va `location` blokini almashtiring:

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

Oddiy koʻp sahifali sayt uchun oxirgi qatorni `error_page 404 /404.html;` ga almashtiring.

> [!TIP]
> Yangi versiyani joylashtirgandan soʻng uzoq `Cache-Control` ga ega fayllar brauzerlar keshida qolishi mumkin. Resurslarga versiyali nomlar bering (masalan, `app.3f9c2.js`), `index.html` uchun esa qisqa keshlash muddatini qoldiring.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Qoʻllab-quvvatlanadigan imkoniyatlar](overview.md)**
