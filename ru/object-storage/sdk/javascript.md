# JavaScript (Node.js)

**AWS SDK for JavaScript v3** работает в Node.js и в браузерах. Пример ниже — для Node.js 18 и новее.

## Установка

```bash
npm install @aws-sdk/client-s3 @aws-sdk/s3-request-presigner
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Пример

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

Сохраните код в `s3.mjs` и запустите командой `node s3.mjs`. Для больших файлов используйте `Upload` из пакета `@aws-sdk/lib-storage` — он загружает файлы частями.

> [!WARNING]
> Не размещайте ключи доступа в коде, который выполняется в браузере. Для загрузки из браузера создавайте presigned URL на своем сервере и настройте для бакета **[CORS](../features/cors.md)**.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
