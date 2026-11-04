# PHP

**AWS SDK for PHP** Composer orqali oʻrnatiladi va PHP 8.1 yoki undan yangi versiyani talab qiladi.

## Oʻrnatish

```bash
composer require aws/aws-sdk-php
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Mijoz yaratish

```php
<?php
require 'vendor/autoload.php';

use Aws\S3\S3Client;

$s3 = new S3Client([
    'version' => 'latest',
    'region' => 'default',
    'endpoint' => 'https://s3.uzcstorage.uz',
    'use_path_style_endpoint' => true,
    'request_checksum_calculation' => 'when_required',
    'response_checksum_validation' => 'when_required',
    'retries' => 5,
]);
$bucket = 'my-bucket';
```

## Asosiy amallar

```php
// Upload a file
$s3->putObject(['Bucket' => $bucket, 'Key' => 'docs/report.pdf',
                'SourceFile' => 'report.pdf', 'ContentType' => 'application/pdf']);

// Upload a string
$s3->putObject(['Bucket' => $bucket, 'Key' => 'docs/hello.txt', 'Body' => 'Hello, UzCloud!']);

// Download to a file
$s3->getObject(['Bucket' => $bucket, 'Key' => 'docs/report.pdf', 'SaveAs' => 'report-copy.pdf']);

// Read an object into memory (small objects only)
$text = (string) $s3->getObject(['Bucket' => $bucket, 'Key' => 'docs/hello.txt'])['Body'];

// Copy and delete
$s3->copyObject(['Bucket' => $bucket, 'Key' => 'archive/report.pdf', 'CopySource' => "$bucket/docs/report.pdf"]);
$s3->deleteObject(['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
```

## Barcha obyektlar roʻyxati

Bitta soʻrov koʻpi bilan 1 000 ta obyektni qaytaradi. Prefiksli barcha obyektlarni olish uchun paginatordan foydalaning:

```php
$pages = $s3->getPaginator('ListObjectsV2', ['Bucket' => $bucket, 'Prefix' => 'docs/']);
foreach ($pages as $page) {
    foreach ($page['Contents'] ?? [] as $obj) {
        echo $obj['Key'], ' ', $obj['Size'], PHP_EOL;
    }
}
```

## Katta fayllar

`MultipartUploader` faylni qismlarga boʻlib yuklaydi va uzilgan yuklashni davom ettira oladi:

```php
use Aws\Exception\MultipartUploadException;
use Aws\S3\MultipartUploader;

$uploader = new MultipartUploader($s3, 'backup.tar.gz', [
    'bucket' => $bucket,
    'key' => 'backups/backup.tar.gz',
    'part_size' => 64 * 1024 * 1024,
    'concurrency' => 4,
]);

do {
    try {
        $result = $uploader->upload();
    } catch (MultipartUploadException $e) {
        // resume from the parts that were already uploaded
        $uploader = new MultipartUploader($s3, 'backup.tar.gz', ['state' => $e->getState()]);
    }
} while (!isset($result));
```

## Oqimli uzatish

Katta obyektni xotiraga toʻliq yuklamaslik uchun uni qismlarga boʻlib oʻqing va yozing:

```php
// Send an object to the user without saving it on the server
$result = $s3->getObject(['Bucket' => $bucket, 'Key' => 'media/video.mp4']);
header('Content-Type: ' . $result['ContentType']);
header('Content-Length: ' . $result['ContentLength']);
$body = $result['Body'];
while (!$body->eof()) {
    echo $body->read(1024 * 1024);
    flush();
}
```

## Presigned URL

Presigned URL kalitlarni bermasdan obyektga vaqtinchalik kirish imkonini beradi. Yuklash havolasi brauzer yoki boshqa xizmatga faylni bevosita bucketga yuklash imkonini beradi — **[Presigned URL](../features/presigned-url.md)** va **[CORS](../features/cors.md)** ga qarang.

```php
// Download link, valid for 1 hour
$cmd = $s3->getCommand('GetObject', ['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
$downloadUrl = (string) $s3->createPresignedRequest($cmd, '+1 hour')->getUri();

// Upload link, valid for 10 minutes
$cmd = $s3->getCommand('PutObject', ['Bucket' => $bucket, 'Key' => 'uploads/photo.jpg', 'ContentType' => 'image/jpeg']);
$uploadUrl = (string) $s3->createPresignedRequest($cmd, '+10 minutes')->getUri();
```

## Xatolar va qayta urinishlar

Eng keng tarqalgan xatolar — obyekt mavjud emas (`NoSuchKey` yoki `HeadObject` uchun `404`) va kirish huquqi yoʻq (`AccessDenied`, `403`). Tarmoq xatolari va `5xx` javoblari avtomatik qayta urinib koʻriladi; urinishlar soni mijoz yaratilganda belgilanadi.

```php
use Aws\S3\Exception\S3Exception;

if (!$s3->doesObjectExistV2($bucket, 'docs/report.pdf')) {
    echo 'Object not found', PHP_EOL;
}

try {
    $s3->getObject(['Bucket' => $bucket, 'Key' => 'missing.txt']);
} catch (S3Exception $e) {
    match ($e->getAwsErrorCode()) {
        'NoSuchKey' => print("Object not found\n"),
        'AccessDenied' => print("Check the keys and the bucket policy\n"),
        default => throw $e,
    };
}
```

> [!TIP]
> Laravel loyihalari uchun SDK’ni bevosita chaqirish oʻrniga oʻrnatilgan **[S3 diskidan](laravel.md)** foydalaning.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
