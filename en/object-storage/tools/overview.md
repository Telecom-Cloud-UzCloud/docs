# Tools for Object Storage

UzCloud Object Storage is compatible with the Amazon S3 API. You can work with it from the console and from any S3 client: command-line tools, desktop file managers and SDKs for programming languages.

## Connection Parameters

Every tool needs the same parameters:

| Parameter | Value |
|---|---|
| Endpoint | `https://s3.uzcstorage.uz` |
| Region | `default` |
| Addressing style | path-style: `https://s3.uzcstorage.uz/<bucket>/<object>` |
| Access Key / Secret Key | the keys of your object store |

### Where to Get the Keys

1. Open **Object Storage** in the console and click the name of your object store.
2. Click **Credentials**. The Access Key is shown in the **Access Keys** list.
3. The Secret Key is shown only within 5 minutes after you click **Create Key**. Copy it right away and store it in a password manager. If you lost the secret, create a new key and revoke the old one.

![S3 credentials](../../../images/ob-17.png)

See **[Manage Object Storage](../../object-storage/manage-object-storage.md#view-credentials)**.

> [!IMPORTANT]
> Use the bucket name exactly as it is shown in the console, for example `demo-store-001045`.

## Choose a Tool

| Tool | Type | Best for |
|---|---|---|
| [AWS CLI](aws-cli.md) | Command line | Scripts, automation, all S3 features |
| [s3cmd](s3cmd.md) | Command line | Simple uploads and sync on Linux servers |
| [rclone](rclone.md) | Command line | Sync, backups, migration between clouds |
| [s3fs](s3fs.md) | File system | Mounting a bucket as a folder on Linux |
| [Cyberduck](cyberduck.md) | Graphical | Working with files on macOS and Windows |
| [S3 Browser](s3-browser.md) | Graphical | Working with files on Windows |

For applications, use the [SDK](../sdk/overview.md) for your programming language.
