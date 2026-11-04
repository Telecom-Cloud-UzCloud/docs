# Object Lifecycle

Lifecycle rules automatically delete objects after a set period: old backups, logs, temporary files, previous versions and unfinished uploads. This keeps storage tidy and reduces costs.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

## Create Rules

Describe the rules in a `lifecycle.json` file. In this example:

- objects with the `logs/` prefix are deleted after 30 days;
- objects with the `tmp/` prefix are deleted after 1 day;
- previous versions of all objects are deleted 14 days after they become noncurrent;
- unfinished multipart uploads are cleaned up after 3 days.

```json
{
  "Rules": [
    {
      "ID": "expire-logs",
      "Status": "Enabled",
      "Filter": { "Prefix": "logs/" },
      "Expiration": { "Days": 30 }
    },
    {
      "ID": "expire-tmp",
      "Status": "Enabled",
      "Filter": { "Prefix": "tmp/" },
      "Expiration": { "Days": 1 }
    },
    {
      "ID": "old-versions-and-uploads",
      "Status": "Enabled",
      "Filter": { "Prefix": "" },
      "NoncurrentVersionExpiration": { "NoncurrentDays": 14 },
      "AbortIncompleteMultipartUpload": { "DaysAfterInitiation": 3 }
    }
  ]
}
```

Apply the rules to the bucket and check them:

```bash
aws s3api put-bucket-lifecycle-configuration --bucket my-bucket \
  --lifecycle-configuration file://lifecycle.json

aws s3api get-bucket-lifecycle-configuration --bucket my-bucket
```

To remove all rules: `aws s3api delete-bucket-lifecycle --bucket my-bucket`.

> [!NOTE]
> Rules are applied in the background, usually once a day, so objects may be deleted with a delay of up to a day after the period ends. Objects protected by **[Object Lock](object-lock.md)** are not deleted until the lock expires.

> [!WARNING]
> A rule with an empty prefix and `Expiration` deletes **all** objects in the bucket after the period. Double-check filters before applying rules.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
