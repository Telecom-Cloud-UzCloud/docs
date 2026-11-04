# SDK for S3

UzCloud Object Storage is compatible with the official AWS SDKs. To connect, set the UzCloud endpoint, the `default` region and path-style addressing.

| Language | Library | Article |
|---|---|---|
| Python | boto3 | [Python](python.md) |
| JavaScript / Node.js | AWS SDK for JavaScript v3 | [JavaScript](javascript.md) |
| PHP | AWS SDK for PHP | [PHP](php.md) |
| Go | AWS SDK for Go v2 | [Go](go.md) |

## Settings for Any SDK

- **Endpoint:** `https://s3.uzcstorage.uz`
- **Region:** `default`
- **Path-style addressing:** enabled (`forcePathStyle`, `use_path_style_endpoint`, `UsePathStyle` and so on).
- **Checksums:** `when_required`. New SDK versions add checksum headers to every request by default; this setting keeps them only where the S3 API requires them.
- **Keys:** Access Key and Secret Key from the **Credentials** window — see **[Tools and Connection Parameters](../tools/overview.md)**.

> [!TIP]
> Any other library that supports custom S3 endpoints also works: for example, the AWS SDKs for Java and .NET, or MinIO clients.
