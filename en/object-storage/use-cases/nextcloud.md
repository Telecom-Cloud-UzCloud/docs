# Nextcloud with S3

**Nextcloud** is a self-hosted platform for file storage and collaboration. Object storage can serve as its file storage: the VM disk then holds only the application and the database.

There are two ways to connect S3:

- **primary storage** — all user files are stored in the bucket;
- **external storage** — the bucket is mounted as a separate folder.

## Primary Storage

> [!WARNING]
> Configure primary storage **before the first start** of Nextcloud. Files that were already uploaded to the local disk are not moved to S3 automatically.

Add the `objectstore` block to `config/config.php`:

```php
'objectstore' => [
    'class' => '\\OC\\Files\\ObjectStore\\S3',
    'arguments' => [
        'bucket' => 'my-nextcloud',
        'hostname' => 's3.uzcstorage.uz',
        'port' => 443,
        'use_ssl' => true,
        'region' => 'default',
        'key' => '<Access Key>',
        'secret' => '<Secret Key>',
        'use_path_style' => true,
        'autocreate' => false,
    ],
],
```

Nextcloud stores files in the bucket as objects named `urn:oid:<id>`, so the files are not readable directly in the bucket. Back up the Nextcloud database too: without it, the files cannot be matched to users.

## External Storage

1. Enable the **External storage support** app in **Apps**.
2. Open **Administration settings → External storage**.
3. Add a storage of the **Amazon S3** type and fill in: **Bucket** — the bucket name, **Hostname** — `s3.uzcstorage.uz`, **Port** — `443`, **Region** — `default`, select **Enable SSL** and **Enable Path Style**, and enter the **Access key** and **Secret key**.
4. Choose the users or groups that can access the folder. A green indicator next to the storage means the connection works.

> [!TIP]
> **See also:**
>
> - **[Use Cases](overview.md)**
