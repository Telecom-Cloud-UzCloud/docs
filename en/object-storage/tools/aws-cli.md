# AWS CLI

**AWS CLI** is the official Amazon command-line tool. It supports all S3 features and works with UzCloud Object Storage.

## Installation

**Linux:**

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
```

**macOS:** `brew install awscli`. **Windows:** download and run the installer from the [AWS CLI page](https://aws.amazon.com/cli/).

Check the version (version 2.13 or later is required):

```bash
aws --version
```

## Configuration

Run `aws configure` and enter your keys. For **Default region name**, enter `default`:

```text
AWS Access Key ID [None]: <Access Key>
AWS Secret Access Key [None]: <Secret Key>
Default region name [None]: default
Default output format [None]: json
```

Then add the UzCloud endpoint to `~/.aws/config` (on Windows: `%USERPROFILE%\.aws\config`), so that you don't have to pass it in every command:

```ini
[default]
region = default
output = json
endpoint_url = https://s3.uzcstorage.uz
request_checksum_calculation = when_required
response_checksum_validation = when_required
s3 =
    addressing_style = path
```

> [!NOTE]
> The `request_checksum_calculation` and `response_checksum_validation` settings disable the new checksum headers that AWS CLI sends by default since version 2.23. Without them, uploads to S3-compatible storage may fail.

Check the connection:

```bash
aws s3 ls
```

## Working with Files

```bash
# List objects in a bucket
aws s3 ls s3://my-bucket/

# Upload a file
aws s3 cp ./report.pdf s3://my-bucket/docs/report.pdf

# Download a file
aws s3 cp s3://my-bucket/docs/report.pdf ./report.pdf

# Upload a folder recursively
aws s3 cp ./site s3://my-bucket/site/ --recursive

# Sync a local folder with a bucket (uploads only new and changed files)
aws s3 sync ./backups s3://my-bucket/backups/

# Delete an object
aws s3 rm s3://my-bucket/docs/report.pdf

# Delete all objects with a prefix
aws s3 rm s3://my-bucket/tmp/ --recursive
```

Add `--delete` to `aws s3 sync` to also delete objects in the bucket that no longer exist locally. Use `--dryrun` first to see what will change.

## Large Files

AWS CLI automatically splits files larger than 8 MB into parts and uploads them in parallel (multipart upload). See **[Multipart Upload](../features/multipart-upload.md)**.

## Temporary Links

Create a link that gives access to a private object for a limited time (in seconds):

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

See **[Presigned URL](../features/presigned-url.md)**.

> [!TIP]
> **See also:**
>
> - **[Tools and connection parameters](overview.md)**
