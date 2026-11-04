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

## Misol

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
]);

$bucket = 'my-bucket';

// 1. Upload a file
$s3->putObject([
    'Bucket' => $bucket,
    'Key' => 'docs/report.pdf',
    'SourceFile' => 'report.pdf',
    'ContentType' => 'application/pdf',
]);

// 2. List objects
$list = $s3->listObjectsV2(['Bucket' => $bucket, 'Prefix' => 'docs/']);
foreach ($list['Contents'] ?? [] as $obj) {
    echo $obj['Key'], ' ', $obj['Size'], PHP_EOL;
}

// 3. Download a file
$s3->getObject(['Bucket' => $bucket, 'Key' => 'docs/report.pdf', 'SaveAs' => 'report-copy.pdf']);

// 4. Temporary download link (1 hour)
$cmd = $s3->getCommand('GetObject', ['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
echo (string) $s3->createPresignedRequest($cmd, '+1 hour')->getUri(), PHP_EOL;

// 5. Delete an object
$s3->deleteObject(['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
```

Katta fayllar uchun `Aws\S3\MultipartUploader` dan foydalaning.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
