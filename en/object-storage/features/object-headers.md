# Object Headers

Each object stores HTTP headers that are returned when the object is downloaded. They tell the browser how to display the file and how long to cache it. You can also store your own metadata with an object.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

| Header | What it does | Example |
|---|---|---|
| `Content-Type` | File type | `image/png`, `text/html; charset=utf-8` |
| `Cache-Control` | Browser and CDN caching | `public, max-age=86400` |
| `Content-Disposition` | Download instead of opening, file name | `attachment; filename="report.pdf"` |
| `Content-Encoding` | Compressed content | `gzip` |
| `x-amz-meta-*` | Your own metadata | `x-amz-meta-author: Demo` |

## Set Headers on Upload

```bash
aws s3 cp ./logo.png s3://my-bucket/img/logo.png \
  --content-type image/png \
  --cache-control "public, max-age=31536000" \
  --metadata author=Demo
```

When you upload a folder, AWS CLI sets `Content-Type` automatically by file extension. You can set the same `Cache-Control` for all files:

```bash
aws s3 sync ./static s3://my-bucket/static/ --cache-control "public, max-age=86400"
```

## View Headers

```bash
aws s3api head-object --bucket my-bucket --key img/logo.png
```

## Change Headers of an Existing Object

Headers cannot be edited in place. Copy the object onto itself with new headers:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source my-bucket/docs/report.pdf \
  --metadata-directive REPLACE \
  --content-type application/pdf \
  --content-disposition 'attachment; filename="report.pdf"'
```

> [!NOTE]
> With `--metadata-directive REPLACE`, all headers and metadata that you don't specify are reset. List all the headers you need in the command.

> [!TIP]
> **See also:**
>
> - **[Supported Features](overview.md)**
