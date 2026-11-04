# JavaScript (Node.js)

**AWS SDK for JavaScript v3** works in Node.js and in browsers. The example below is for Node.js 18 or later.

## Installation

```bash
npm install @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Example

```javascript
import { readFile, writeFile } from "node:fs/promises";
import {
  S3Client, PutObjectCommand, ListObjectsV2Command,
  GetObjectCommand, DeleteObjectCommand,
} from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3 = new S3Client({
  region: "default",
  endpoint: "https://s3.uzcstorage.uz",
  forcePathStyle: true,
  requestChecksumCalculation: "WHEN_REQUIRED",
  responseChecksumValidation: "WHEN_REQUIRED",
});

const Bucket = "my-bucket";

// 1. Upload a file
await s3.send(new PutObjectCommand({
  Bucket, Key: "docs/report.pdf",
  Body: await readFile("report.pdf"),
  ContentType: "application/pdf",
}));

// 2. List objects
const list = await s3.send(new ListObjectsV2Command({ Bucket, Prefix: "docs/" }));
for (const obj of list.Contents ?? []) console.log(obj.Key, obj.Size);

// 3. Download a file
const file = await s3.send(new GetObjectCommand({ Bucket, Key: "docs/report.pdf" }));
await writeFile("report-copy.pdf", await file.Body.transformToByteArray());

// 4. Temporary upload link (10 minutes) for the browser
const uploadUrl = await getSignedUrl(
  s3,
  new PutObjectCommand({ Bucket, Key: "uploads/photo.jpg", ContentType: "image/jpeg" }),
  { expiresIn: 600 },
);
console.log(uploadUrl);

// 5. Delete an object
await s3.send(new DeleteObjectCommand({ Bucket, Key: "docs/report.pdf" }));
```

Save the code to `s3.mjs` and run it with `node s3.mjs`. For large files, use `Upload` from the `@aws-sdk/lib-storage` package: it uploads files in parts.

> [!WARNING]
> Do not put access keys into browser code. To upload from a browser, generate a presigned URL on your server and configure **[CORS](../features/cors.md)** for the bucket.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
