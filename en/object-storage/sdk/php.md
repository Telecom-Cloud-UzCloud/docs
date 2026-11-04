# PHP

**AWS SDK for PHP** is installed with Composer and requires PHP 8.1 or later.

## Installation

```bash
composer require aws/aws-sdk-php
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Create a Client

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

## Basic Operations

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

## List All Objects

One request returns at most 1,000 objects. To get all objects with a prefix, use a paginator:

```php
$pages = $s3->getPaginator('ListObjectsV2', ['Bucket' => $bucket, 'Prefix' => 'docs/']);
foreach ($pages as $page) {
    foreach ($page['Contents'] ?? [] as $obj) {
        echo $obj['Key'], ' ', $obj['Size'], PHP_EOL;
    }
}
```

## Large Files

`MultipartUploader` uploads a file in parts and can resume an interrupted upload:

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

## Streaming

To avoid loading a large object into memory, read and write it in chunks:

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

## Presigned URLs

A presigned URL gives temporary access to an object without sharing your keys. An upload link lets a browser or another service upload a file directly to the bucket — see **[Presigned URL](../features/presigned-url.md)** and **[CORS](../features/cors.md)**.

```php
// Download link, valid for 1 hour
$cmd = $s3->getCommand('GetObject', ['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
$downloadUrl = (string) $s3->createPresignedRequest($cmd, '+1 hour')->getUri();

// Upload link, valid for 10 minutes
$cmd = $s3->getCommand('PutObject', ['Bucket' => $bucket, 'Key' => 'uploads/photo.jpg', 'ContentType' => 'image/jpeg']);
$uploadUrl = (string) $s3->createPresignedRequest($cmd, '+10 minutes')->getUri();
```

## Errors and Retries

The most common errors are a missing object (`NoSuchKey`, or `404` for `HeadObject`) and no access (`AccessDenied`, `403`). Network errors and `5xx` responses are retried automatically; the number of attempts is set when you create the client.

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
> For Laravel projects, use the built-in **[S3 disk](laravel.md)** instead of calling the SDK directly.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
