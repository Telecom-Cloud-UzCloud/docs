# PHP

**AWS SDK for PHP** устанавливается через Composer и требует PHP 8.1 или новее.

## Установка

```bash
composer require aws/aws-sdk-php
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Создание клиента

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

## Основные операции

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

## Список всех объектов

Один запрос возвращает не больше 1 000 объектов. Чтобы получить все объекты с префиксом, используйте пагинатор:

```php
$pages = $s3->getPaginator('ListObjectsV2', ['Bucket' => $bucket, 'Prefix' => 'docs/']);
foreach ($pages as $page) {
    foreach ($page['Contents'] ?? [] as $obj) {
        echo $obj['Key'], ' ', $obj['Size'], PHP_EOL;
    }
}
```

## Большие файлы

`MultipartUploader` загружает файл частями и умеет продолжить прерванную загрузку:

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

## Потоковая передача

Чтобы не загружать большой объект в память целиком, читайте и записывайте его частями:

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

Presigned URL дает временный доступ к объекту без передачи ключей. Ссылка на загрузку позволяет браузеру или другому сервису загрузить файл прямо в бакет — см. **[Presigned URL](../features/presigned-url.md)** и **[CORS](../features/cors.md)**.

```php
// Download link, valid for 1 hour
$cmd = $s3->getCommand('GetObject', ['Bucket' => $bucket, 'Key' => 'docs/report.pdf']);
$downloadUrl = (string) $s3->createPresignedRequest($cmd, '+1 hour')->getUri();

// Upload link, valid for 10 minutes
$cmd = $s3->getCommand('PutObject', ['Bucket' => $bucket, 'Key' => 'uploads/photo.jpg', 'ContentType' => 'image/jpeg']);
$uploadUrl = (string) $s3->createPresignedRequest($cmd, '+10 minutes')->getUri();
```

## Ошибки и повторные попытки

Самые частые ошибки — отсутствующий объект (`NoSuchKey` или `404` для `HeadObject`) и нет доступа (`AccessDenied`, `403`). Сетевые ошибки и ответы `5xx` повторяются автоматически; число попыток задается при создании клиента.

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
> Для проектов на Laravel используйте встроенный **[диск S3](laravel.md)** вместо прямых вызовов SDK.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
