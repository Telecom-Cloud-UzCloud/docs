# CORS Setup

Browsers block requests from a web page to another domain unless the server allows them. **CORS** (Cross-Origin Resource Sharing) rules let your website load files from a bucket or upload files to it directly from the browser.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

## Create Rules

Describe the rules in a `cors.json` file. This example allows the site `https://example.com` to read objects and upload them with presigned URLs:

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

- `AllowedOrigins` — the domains of your site. Avoid `*` unless the files are public.
- `AllowedMethods` — allowed HTTP methods.
- `MaxAgeSeconds` — how long the browser caches the result of the preflight request.

Apply and check the rules:

```bash
aws s3api put-bucket-cors --bucket my-bucket --cors-configuration file://cors.json
aws s3api get-bucket-cors --bucket my-bucket
```

## Check from the Command Line

Send a preflight request as the browser does. The response must contain the `Access-Control-Allow-Origin` header:

```bash
curl -i -X OPTIONS "https://s3.uzcstorage.uz/my-bucket/image.png" \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: GET"
```

To remove the rules: `aws s3api delete-bucket-cors --bucket my-bucket`.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
