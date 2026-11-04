# Use Cases

Object storage is cheaper than disks and grows without limits, so it is well suited for data that you need to keep but don't change often.

| Scenario | Article |
|---|---|
| Backups of server files with encryption and deduplication | [Server Backups with restic](server-backup-restic.md) |
| Daily dumps of PostgreSQL and MySQL databases | [Database Backups](database-backup.md) |
| File storage for Nextcloud | [Nextcloud with S3](nextcloud.md) |
| Images, video and other static files of a website | [Nginx Proxy for S3](../features/nginx-proxy.md) |
| Hosting a static website | [Static Website](../features/static-website.md) |

> [!TIP]
> Store backups in a separate bucket with **[Object Lock](../features/object-lock.md)** and **[lifecycle rules](../features/lifecycle.md)**: backups are then protected from deletion and old copies are removed automatically.
