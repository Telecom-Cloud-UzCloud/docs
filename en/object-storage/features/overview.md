# Supported Features

UzCloud Object Storage is built on Ceph and supports the core Amazon S3 API. The table below lists the features and how to use them.

| Feature | What it is for | Console | S3 API |
|---|---|---|---|
| [Versioning](versioning.md) | Keep previous versions of objects | ✓ | ✓ |
| [Object Lock](object-lock.md) | Protect objects from deletion (WORM) | ✓ | ✓ |
| [Lifecycle rules](lifecycle.md) | Delete old objects automatically | — | ✓ |
| [CORS](cors.md) | Access from web pages on other domains | — | ✓ |
| [Bucket Policy](bucket-policy.md) | Access rules for a bucket | ✓ | ✓ |
| [Object headers](object-headers.md) | Content-Type, Cache-Control, metadata | — | ✓ |
| [Multipart upload](multipart-upload.md) | Upload large files in parts | — | ✓ |
| [Presigned URL](presigned-url.md) | Temporary links to private objects | — | ✓ |
| [Static website](static-website.md) | Host a static site in a bucket | — | ✓ |

To work with features that are not available in the console, use the **[tools](../tools/overview.md)** or an **[SDK](../sdk/overview.md)**.
