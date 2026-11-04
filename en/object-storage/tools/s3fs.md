# s3fs

**s3fs** mounts a bucket as a folder in Linux. Applications can then read and write objects as regular files.

> [!WARNING]
> A mounted bucket is not a real disk: operations are slower, and files are rewritten entirely on every change. Do not use s3fs for databases or for applications that frequently modify files. It works well for archives, media and backups.

## Installation

```bash
sudo apt install s3fs          # Ubuntu, Debian
sudo dnf install s3fs-fuse     # Rocky Linux, AlmaLinux (EPEL)
```

## Configuration

Save the keys to a file and restrict access to it:

```bash
echo "<Access Key>:<Secret Key>" | sudo tee /etc/passwd-s3fs
sudo chmod 600 /etc/passwd-s3fs
```

## Mount the Bucket

```bash
sudo mkdir -p /mnt/s3
sudo s3fs my-bucket /mnt/s3 \
  -o passwd_file=/etc/passwd-s3fs \
  -o url=https://s3.uzcstorage.uz \
  -o use_path_request_style \
  -o allow_other
```

Check that the bucket is mounted:

```bash
df -h /mnt/s3 && ls /mnt/s3
```

## Mount at Startup

Add a line to `/etc/fstab`:

```text
my-bucket /mnt/s3 fuse.s3fs _netdev,allow_other,use_path_request_style,url=https://s3.uzcstorage.uz,passwd_file=/etc/passwd-s3fs 0 0
```

Check the entry without rebooting: `sudo mount -a`. To unmount: `sudo umount /mnt/s3`.

> [!TIP]
> **See also:**
>
> - **[Tools and connection parameters](overview.md)**
