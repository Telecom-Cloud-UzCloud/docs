# Multipart Upload

**Multipart upload** splits a large file into parts and uploads them in parallel. If the connection drops, only the failed part is uploaded again. Use it for files larger than 100 MB.

The examples use **[AWS CLI](../tools/aws-cli.md)** configured for UzCloud. Replace `my-bucket` with the name of your bucket.

## Limits

- part size: from 5 MB to 5 GB (the last part can be smaller);
- up to 10,000 parts per file;
- maximum object size: 5 TB.

## Automatic Multipart Upload

`aws s3 cp`, `aws s3 sync`, rclone and the SDKs use multipart upload automatically for large files. In AWS CLI, you can tune the part size and the number of parallel requests:

```bash
aws configure set default.s3.multipart_threshold 64MB
aws configure set default.s3.multipart_chunksize 64MB
aws configure set default.s3.max_concurrent_requests 10

aws s3 cp ./backup.tar.gz s3://my-bucket/backups/
```

## Manual Multipart Upload

The low-level commands are useful in scripts and for understanding how it works:

**1.** Split the file into parts:

```bash
split -b 100M backup.tar.gz part-
```

**2.** Start the upload and save the `UploadId`:

```bash
UPLOAD_ID=$(aws s3api create-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --query UploadId --output text)
```

**3.** Upload the parts, numbering them from 1:

```bash
n=1
for f in part-*; do
  ETAG=$(aws s3api upload-part --bucket my-bucket --key backups/backup.tar.gz \
    --upload-id "$UPLOAD_ID" --part-number $n --body "$f" \
    --query ETag --output text)
  echo "{\"PartNumber\": $n, \"ETag\": $ETAG}" >> parts.txt
  n=$((n+1))
done
echo "{\"Parts\": [$(paste -sd, parts.txt)]}" > parts.json
```

**4.** Complete the upload:

```bash
aws s3api complete-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id "$UPLOAD_ID" \
  --multipart-upload file://parts.json
```

## Unfinished Uploads

Parts of an unfinished upload take up space and are billed, although they are not visible in the list of objects. Find and abort them:

```bash
aws s3api list-multipart-uploads --bucket my-bucket

aws s3api abort-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id <UploadId>
```

To clean them up automatically, add the `AbortIncompleteMultipartUpload` **[lifecycle rule](lifecycle.md)**.

> [!TIP]
> **See also:**
>
> - **[Supported Features](overview.md)**
