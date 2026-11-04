# JavaScript (Node.js)

**AWS SDK for JavaScript v3** работает в Node.js и в браузерах. Примеры рассчитаны на Node.js 18+ и ES-модули (файлы `.mjs` или `"type": "module"`).

## Установка

```bash
npm install @aws-sdk/client-s3 @aws-sdk/lib-storage @aws-sdk/s3-request-presigner
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Создание клиента

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

## Основные операции

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

## Список всех объектов

Один запрос возвращает не больше 1 000 объектов. Чтобы получить все объекты с префиксом, используйте пагинатор:

```javascript
import { paginateListObjectsV2 } from "@aws-sdk/client-s3";

for await (const page of paginateListObjectsV2({ client: s3 }, { Bucket, Prefix: "docs/" })) {
  for (const obj of page.Contents ?? []) console.log(obj.Key, obj.Size);
}
```

## Большие файлы

`Upload` из `@aws-sdk/lib-storage` делит файл на части, загружает их параллельно и сообщает о прогрессе:

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

## Потоковая передача

Чтобы не загружать большой объект в память целиком, читайте и записывайте его частями:

```javascript
import { createWriteStream } from "node:fs";
import { pipeline } from "node:stream/promises";

const { Body } = await s3.send(new GetObjectCommand({ Bucket, Key: "media/video.mp4" }));
await pipeline(Body, createWriteStream("video-copy.mp4"));
```

Для загрузки из потока используйте `Upload` (см. выше): `PutObjectCommand` требует заранее известную длину потока.

## Presigned URL

Presigned URL дает временный доступ к объекту без передачи ключей. Ссылка на загрузку позволяет браузеру или другому сервису загрузить файл прямо в бакет — см. **[Presigned URL](../features/presigned-url.md)** и **[CORS](../features/cors.md)**.

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

## Загрузка из браузера

Ключи должны оставаться на сервере. Сервер создает ссылку на загрузку, а браузер отправляет файл прямо в бакет, не пропуская его через ваш сервер:

**Сервер (Express):**

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

**Браузер:**

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
> Для загрузки из браузера разрешите домен сайта и метод `PUT` в правилах **[CORS](../features/cors.md)** бакета.

## Ошибки и повторные попытки

Самые частые ошибки — отсутствующий объект (`NoSuchKey` или `404` для `HeadObject`) и нет доступа (`AccessDenied`, `403`). Сетевые ошибки и ответы `5xx` повторяются автоматически; число попыток задается при создании клиента.

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
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
