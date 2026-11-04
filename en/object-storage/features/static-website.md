# Static Website

A static website (HTML, CSS, JavaScript, images) can be hosted in a bucket. This works well for landing pages, documentation and single-page applications (React, Vue, Angular) without a server-side part.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

## Step 1. Upload the Site

```bash
aws s3 sync ./dist s3://my-site/ --delete --cache-control "public, max-age=300"
```

## Step 2. Open Public Access

Apply a policy that allows anyone to read the site files:

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

The files are now available at `https://s3.uzcstorage.uz/my-site/index.html`.

## Step 3. Connect Your Domain

To open the site at `https://example.com` and to serve `index.html` for folder addresses, put Nginx in front of the bucket. Use the configuration from **[Nginx Proxy for S3](nginx-proxy.md)** and replace the `location` block:

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

For a regular multi-page site, replace the last line with `error_page 404 /404.html;`.

> [!TIP]
> After deploying a new version, files with long `Cache-Control` may stay in browser caches. Give assets versioned names (for example, `app.3f9c2.js`) and keep a short cache time for `index.html`.

> [!TIP]
> **See also:**
>
> - **[Supported Features](overview.md)**
