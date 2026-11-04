# JavaScript (Node.js)

**AWS SDK for JavaScript v3** works in Node.js and in browsers. The examples are for Node.js 18 or later with ES modules (`.mjs` files or `"type": "module"`).

## Installation

```bash
npm install @aws-sdk/client-s3 @aws-sdk/lib-storage @aws-sdk/s3-request-presigner
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Create a Client

```javascript
// s3.mjs
import { S3Client } from "@aws-sdk/client-s3";

export const s3 = new S3Client({
  region: "default",
  endpoint: "https://s3.uzcstorage.uz",
  forcePathStyle: true,
  requestChecksumCalculation: "WHEN_REQUIRED",
  responseChecksumValidation: "WHEN_REQUIRED",
  maxAttempts: 5,
});
export const Bucket = "my-bucket";
```

## Basic Operations

```javascript
import { readFile } from "node:fs/promises";
import {
  PutObjectCommand, GetObjectCommand, CopyObjectCommand,
  DeleteObjectCommand, DeleteObjectsCommand,
} from "@aws-sdk/client-s3";
import { s3, Bucket } from "./s3.mjs";

// Upload a file
await s3.send(new PutObjectCommand({
  Bucket, Key: "docs/report.pdf",
  Body: await readFile("report.pdf"),
  ContentType: "application/pdf",
}));

// Read an object as a string (small objects only)
const obj = await s3.send(new GetObjectCommand({ Bucket, Key: "docs/hello.txt" }));
console.log(await obj.Body.transformToString());

// Copy and delete
await s3.send(new CopyObjectCommand({ Bucket, Key: "archive/report.pdf", CopySource: `${Bucket}/docs/report.pdf` }));
await s3.send(new DeleteObjectCommand({ Bucket, Key: "docs/report.pdf" }));

// Delete up to 1,000 objects in one request
await s3.send(new DeleteObjectsCommand({
  Bucket, Delete: { Objects: [{ Key: "tmp/a.txt" }, { Key: "tmp/b.txt" }] },
}));
```

## List All Objects

One request returns at most 1,000 objects. To get all objects with a prefix, use a paginator:

```javascript
import { paginateListObjectsV2 } from "@aws-sdk/client-s3";

for await (const page of paginateListObjectsV2({ client: s3 }, { Bucket, Prefix: "docs/" })) {
  for (const obj of page.Contents ?? []) console.log(obj.Key, obj.Size);
}
```

## Large Files

`Upload` from `@aws-sdk/lib-storage` splits a file into parts, uploads them in parallel and reports progress:

```javascript
import { createReadStream } from "node:fs";
import { Upload } from "@aws-sdk/lib-storage";

const upload = new Upload({
  client: s3,
  params: { Bucket, Key: "backups/backup.tar.gz", Body: createReadStream("backup.tar.gz") },
  partSize: 64 * 1024 * 1024,
  queueSize: 4,
});
upload.on("httpUploadProgress", (p) => console.log(`${p.loaded} / ${p.total ?? "?"} bytes`));
await upload.done();
```

## Streaming

To avoid loading a large object into memory, read and write it in chunks:

```javascript
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";

const { Body } = await s3.send(new GetObjectCommand({ Bucket, Key: "media/video.mp4" }));
await pipeline(Body, createWriteStream("video-copy.mp4"));
```

For uploads from a stream, use `Upload` (see above): `PutObjectCommand` requires the length of the stream to be known in advance.

## Presigned URLs

A presigned URL gives temporary access to an object without sharing your keys. An upload link lets a browser or another service upload a file directly to the bucket — see **[Presigned URL](../features/presigned-url.md)** and **[CORS](../features/cors.md)**.

```javascript
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

// Download link, valid for 1 hour
const downloadUrl = await getSignedUrl(s3, new GetObjectCommand({ Bucket, Key: "docs/report.pdf" }), { expiresIn: 3600 });

// Upload link, valid for 10 minutes
const uploadUrl = await getSignedUrl(
  s3,
  new PutObjectCommand({ Bucket, Key: "uploads/photo.jpg", ContentType: "image/jpeg" }),
  { expiresIn: 600 },
);
```

## Upload from a Browser

Keys must stay on the server. The server creates an upload link, and the browser sends the file directly to the bucket, without passing it through your server:

**Server (Express):**

```javascript
import express from "express";
import { randomUUID } from "node:crypto";

const app = express();
app.get("/upload-url", async (req, res) => {
  const type = String(req.query.type || "application/octet-stream");
  const Key = `uploads/${randomUUID()}`;
  const url = await getSignedUrl(s3, new PutObjectCommand({ Bucket, Key, ContentType: type }), { expiresIn: 300 });
  res.json({ url, key: Key });
});
app.listen(3000);
```

**Browser:**

```javascript
async function uploadFile(file) {
  const r = await fetch(`/upload-url?type=${encodeURIComponent(file.type)}`);
  const { url, key } = await r.json();
  const put = await fetch(url, { method: "PUT", headers: { "Content-Type": file.type }, body: file });
  if (!put.ok) throw new Error(`Upload failed: ${put.status}`);
  return key;
}
```

> [!IMPORTANT]
> For uploads from a browser, allow your site's domain and the `PUT` method in the bucket's **[CORS](../features/cors.md)** rules.

## Errors and Retries

The most common errors are a missing object (`NoSuchKey`, or `404` for `HeadObject`) and no access (`AccessDenied`, `403`). Network errors and `5xx` responses are retried automatically; the number of attempts is set when you create the client.

```javascript
import { HeadObjectCommand } from "@aws-sdk/client-s3";

async function objectExists(Key) {
  try {
    await s3.send(new HeadObjectCommand({ Bucket, Key }));
    return true;
  } catch (e) {
    if (e.name === "NotFound" || e.$metadata?.httpStatusCode === 404) return false;
    throw e;
  }
}

try {
  await s3.send(new GetObjectCommand({ Bucket, Key: "missing.txt" }));
} catch (e) {
  if (e.name === "NoSuchKey") console.log("Object not found");
  else if (e.name === "AccessDenied") console.log("Check the keys and the bucket policy");
  else throw e;
}
```

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
