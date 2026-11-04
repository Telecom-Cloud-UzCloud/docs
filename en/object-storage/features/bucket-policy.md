# Bucket Policy

A **bucket policy** is a set of access rules in JSON format. Use it to make some objects public, restrict access by IP address or forbid deleting objects.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

**In the console**, you can set a policy in the **Bucket Policy** field when you create a bucket. **With AWS CLI**, save the policy to a file and apply it:

```bash
aws s3api put-bucket-policy --bucket my-bucket --policy file://policy.json
aws s3api get-bucket-policy --bucket my-bucket
aws s3api delete-bucket-policy --bucket my-bucket   # remove the policy
```

## Public Read for a Folder

Anyone can download objects with the `public/` prefix; the rest of the bucket stays private:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadForPublicFolder",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::my-bucket/public/*"]
    }
  ]
}
```

The objects are then available at `https://s3.uzcstorage.uz/my-bucket/public/<file>`.

## Access Only from Your IP Addresses

Deny all requests except those from the specified addresses:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOutsideOffice",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"],
      "Condition": {
        "NotIpAddress": { "aws:SourceIp": ["203.0.113.0/24"] }
      }
    }
  ]
}
```

> [!WARNING]
> If you make a mistake in the list of addresses, you may lose access to the bucket from your tools as well. Check the policy on a test bucket first. To remove the policy, use the console or `delete-bucket-policy` from an allowed address.

## Forbid Deleting Objects

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyDelete",
      "Effect": "Deny",
      "Principal": "*",
      "Action": ["s3:DeleteObject", "s3:DeleteObjectVersion"],
      "Resource": ["arn:aws:s3:::my-bucket/*"]
    }
  ]
}
```

For reliable protection of backups, use **[Object Lock](object-lock.md)**: unlike a policy, it cannot be removed by anyone who has your keys.

> [!TIP]
> **See also:**
>
> - **[Supported Features](overview.md)**
