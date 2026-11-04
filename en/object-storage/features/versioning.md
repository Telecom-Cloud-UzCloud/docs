# Object Versioning

With versioning enabled, a bucket keeps every version of an object. If a file is overwritten or deleted by mistake, you can restore a previous version.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

## Enable Versioning

**In the console:** turn on **Bucket Versioning** when you create a bucket. See **[Manage Object Storage](../../object-storage/manage-object-storage.md)**.

**With AWS CLI:**

```bash
aws s3api put-bucket-versioning --bucket my-bucket \
  --versioning-configuration Status=Enabled

# check the status
aws s3api get-bucket-versioning --bucket my-bucket
```

Versioning cannot be turned off completely, only suspended (`Status=Suspended`). Existing versions are kept.

## View Versions

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf
```

Each version has a `VersionId`. The current version has `"IsLatest": true`.

## Restore a Version

Download a specific version:

```bash
aws s3api get-object --bucket my-bucket --key docs/report.pdf \
  --version-id <VersionId> report-old.pdf
```

Or make it current again by copying it over the object:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source "my-bucket/docs/report.pdf?versionId=<VersionId>"
```

## Restore a Deleted Object

In a versioned bucket, deleting an object only adds a **delete marker**. To restore the object, delete the marker:

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf \
  --query 'DeleteMarkers[?IsLatest].VersionId'

aws s3api delete-object --bucket my-bucket --key docs/report.pdf \
  --version-id <delete-marker-VersionId>
```

> [!NOTE]
> All versions take up space and are billed. To limit the number of stored versions, set up a **[lifecycle rule](lifecycle.md)** that deletes old versions.

> [!TIP]
> **See also:**
>
> - **[Supported Features](overview.md)**
