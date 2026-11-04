# JavaScript (Node.js)

**AWS SDK for JavaScript v3** Node.js’da va brauzerlarda ishlaydi. Misollar Node.js 18+ va ES-modullar (`.mjs` fayllar yoki `"type": "module"`) uchun moʻljallangan.

## Oʻrnatish

```bash
npm install @aws-sdk/client-s3 @aws-sdk/lib-storage @aws-sdk/s3-request-presigner
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Mijoz yaratish

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

## Asosiy amallar

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

## Barcha obyektlar roʻyxati

Bitta soʻrov koʻpi bilan 1 000 ta obyektni qaytaradi. Prefiksli barcha obyektlarni olish uchun paginatordan foydalaning:

```javascript
import { paginateListObjectsV2 } from "@aws-sdk/client-s3";

for await (const page of paginateListObjectsV2({ client: s3 }, { Bucket, Prefix: "docs/" })) {
  for (const obj of page.Contents ?? []) console.log(obj.Key, obj.Size);
}
```

## Katta fayllar

`@aws-sdk/lib-storage` dagi `Upload` faylni qismlarga boʻladi, ularni parallel yuklaydi va jarayon haqida xabar beradi:

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

## Oqimli uzatish

Katta obyektni xotiraga toʻliq yuklamaslik uchun uni qismlarga boʻlib oʻqing va yozing:

```javascript
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";

const { Body } = await s3.send(new GetObjectCommand({ Bucket, Key: "media/video.mp4" }));
await pipeline(Body, createWriteStream("video-copy.mp4"));
```

Oqimdan yuklash uchun `Upload` dan foydalaning (yuqoriga qarang): `PutObjectCommand` oqim uzunligini oldindan bilishni talab qiladi.

## Presigned URL

Presigned URL kalitlarni bermasdan obyektga vaqtinchalik kirish imkonini beradi. Yuklash havolasi brauzer yoki boshqa xizmatga faylni bevosita bucketga yuklash imkonini beradi — **[Presigned URL](../objects/presigned-url.md)** va **[CORS](../buckets/cors.md)** ga qarang.

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

## Brauzerdan yuklash

Kalitlar serverda qolishi kerak. Server yuklash havolasini yaratadi, brauzer esa faylni serveringiz orqali oʻtkazmasdan bevosita bucketga yuboradi:

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

**Brauzer:**

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
> Brauzerdan yuklash uchun bucketning **[CORS](../buckets/cors.md)** qoidalarida sayt domeni va `PUT` usuliga ruxsat bering.

## Xatolar va qayta urinishlar

Eng keng tarqalgan xatolar — obyekt mavjud emas (`NoSuchKey` yoki `HeadObject` uchun `404`) va kirish huquqi yoʻq (`AccessDenied`, `403`). Tarmoq xatolari va `5xx` javoblari avtomatik qayta urinib koʻriladi; urinishlar soni mijoz yaratilganda belgilanadi.

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
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
