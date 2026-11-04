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

## Пример

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

Для больших файлов используйте `Aws\S3\MultipartUploader`.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
