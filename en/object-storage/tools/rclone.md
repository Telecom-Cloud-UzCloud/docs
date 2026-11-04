# rclone

**rclone** is a tool for syncing files with cloud storage. It is well suited for backups and for moving data between clouds, and it can mount a bucket as a folder.

## Installation

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

For Windows and macOS, download rclone from [rclone.org/downloads](https://rclone.org/downloads/).

## Configuration

Add a remote to `~/.config/rclone/rclone.conf`:

```ini
[uzcloud]
type = s3
provider = Ceph
access_key_id = <Access Key>
secret_access_key = <Secret Key>
endpoint = https://s3.uzcstorage.uz
force_path_style = true
acl = private
```

You can also create it interactively with `rclone config`: choose **Amazon S3 Compliant Storage Providers**, then **Ceph Object Storage**, and enter the keys and endpoint.

## Working with Files

```bash
rclone lsd uzcloud:                          # list buckets
rclone ls uzcloud:my-bucket                  # list objects
rclone copy ./report.pdf uzcloud:my-bucket/docs/
rclone copy uzcloud:my-bucket/docs/ ./docs/  # download
rclone sync ./site uzcloud:my-bucket/site --progress
rclone delete uzcloud:my-bucket/tmp/
```

> [!WARNING]
> `rclone sync` makes the destination identical to the source and **deletes** files in the destination that don't exist in the source. Check the result first with `--dry-run`.

## Mount a Bucket

```bash
mkdir -p ~/s3
rclone mount uzcloud:my-bucket ~/s3 --vfs-cache-mode writes --daemon
```

To unmount: `fusermount -u ~/s3` (Linux) or `umount ~/s3` (macOS).

## Migrate from Another Cloud

Add a second remote for the source storage and copy the data directly:

```bash
rclone copy old-cloud:source-bucket uzcloud:my-bucket --transfers 16 --progress
```

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
