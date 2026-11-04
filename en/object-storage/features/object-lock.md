# Object Lock

**Object Lock** stores objects in WORM mode (write once, read many): a locked object cannot be deleted or overwritten until the retention period ends. This protects backups from accidental deletion and from ransomware.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

> [!IMPORTANT]
> Object Lock can be enabled only when the bucket is created, and cannot be disabled afterwards. It automatically enables **[versioning](versioning.md)**.

## Create a Bucket with Object Lock

**In the console:** turn on **Bucket Versioning** and **Object Locking** when you create the bucket.

**With AWS CLI:**

```bash
aws s3api create-bucket --bucket my-backups --object-lock-enabled-for-bucket
```

## Retention Modes

- **GOVERNANCE** — objects are protected, but a user with special permission can remove the lock with `--bypass-governance-retention`. Good for most cases.
- **COMPLIANCE** — no user can delete the object or shorten the period until it ends, including the account owner.

> [!WARNING]
> In COMPLIANCE mode, locked objects are stored and billed until the end of the retention period, even if you no longer need them. Start with GOVERNANCE and short periods.

## Default Retention for a Bucket

All new objects in the bucket will be locked for the specified period:

```bash
aws s3api put-object-lock-configuration --bucket my-backups \
  --object-lock-configuration \
  'ObjectLockEnabled=Enabled,Rule={DefaultRetention={Mode=GOVERNANCE,Days=30}}'

aws s3api get-object-lock-configuration --bucket my-backups
```

## Lock a Single Object

```bash
aws s3api put-object-retention --bucket my-backups --key db/2026-11-01.sql.gz \
  --retention 'Mode=GOVERNANCE,RetainUntilDate=2026-12-31T00:00:00Z'

aws s3api get-object-retention --bucket my-backups --key db/2026-11-01.sql.gz
```

**Legal hold** locks an object indefinitely, until you remove it:

```bash
aws s3api put-object-legal-hold --bucket my-backups --key db/2026-11-01.sql.gz \
  --legal-hold Status=ON
```

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
