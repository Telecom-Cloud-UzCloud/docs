# JavaScript (Node.js)

**AWS SDK for JavaScript v3** Node.js’da va brauzerlarda ishlaydi. Quyidagi misol Node.js 18 va undan yangi versiyalar uchun.

## Oʻrnatish

```bash
npm install @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Misol

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

Kodni `s3.mjs` fayliga saqlang va `node s3.mjs` buyrugʻi bilan ishga tushiring. Katta fayllar uchun `@aws-sdk/lib-storage` paketidagi `Upload` dan foydalaning — u fayllarni qismlarga boʻlib yuklaydi.

> [!WARNING]
> Kirish kalitlarini brauzerda bajariladigan kodga joylashtirmang. Brauzerdan yuklash uchun presigned URL’ni serveringizda yarating va bucket uchun **[CORS](../features/cors.md)** ni sozlang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[S3 uchun SDK](overview.md)**
