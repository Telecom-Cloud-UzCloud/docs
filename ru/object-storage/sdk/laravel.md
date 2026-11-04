# Laravel

Laravel работает с объектным хранилищем через встроенный диск `s3` фасада `Storage`. Загруженные файлы, аватары, документы и выгрузки можно хранить в бакете, а не на диске сервера.

## Установка

Примеры рассчитаны на Laravel 10 и новее. Установите адаптер S3 для Flysystem:

```bash
composer require league/flysystem-aws-s3-v3 "^3.0"
```

## Настройка

Добавьте параметры подключения в `.env`:

```ini
FILESYSTEM_DISK=s3
AWS_ACCESS_KEY_ID=<Access Key>
AWS_SECRET_ACCESS_KEY=<Secret Key>
AWS_DEFAULT_REGION=default
AWS_BUCKET=my-bucket
AWS_ENDPOINT=https://s3.uzcstorage.uz
AWS_USE_PATH_STYLE_ENDPOINT=true
AWS_URL=https://s3.uzcstorage.uz/my-bucket
```

Диск `s3` в `config/filesystems.php` уже читает эти переменные. Добавьте в него две строки, которые отключают лишние заголовки контрольных сумм:

```php
's3' => [
    'driver' => 's3',
    'key' => env('AWS_ACCESS_KEY_ID'),
    'secret' => env('AWS_SECRET_ACCESS_KEY'),
    'region' => env('AWS_DEFAULT_REGION'),
    'bucket' => env('AWS_BUCKET'),
    'url' => env('AWS_URL'),
    'endpoint' => env('AWS_ENDPOINT'),
    'use_path_style_endpoint' => env('AWS_USE_PATH_STYLE_ENDPOINT', false),
    'request_checksum_calculation' => 'when_required',
    'response_checksum_validation' => 'when_required',
    'throw' => true,
],
```

Проверьте подключение в `php artisan tinker`:

```php
Storage::disk('s3')->put('test.txt', 'Hello, UzCloud!');
Storage::disk('s3')->get('test.txt');
```

## Работа с файлами

```php
use Illuminate\Support\Facades\Storage;

$disk = Storage::disk('s3');

$disk->put('docs/hello.txt', 'Hello, UzCloud!');          // write
$text = $disk->get('docs/hello.txt');                     // read
$exists = $disk->exists('docs/hello.txt');                // check
$disk->copy('docs/hello.txt', 'archive/hello.txt');       // copy
$disk->delete('docs/hello.txt');                          // delete
$files = $disk->files('docs');                            // list a folder
$disk->putFileAs('backups', new \Illuminate\Http\File('/tmp/backup.zip'), 'backup.zip'); // stream a large file
```

## Загрузка файлов из формы

```php
public function store(Request $request)
{
    $request->validate(['avatar' => 'required|image|max:5120']);

    // Saves to s3 under avatars/<random name>.<ext> and returns the path
    $path = $request->file('avatar')->store('avatars', 's3');

    $request->user()->update(['avatar_path' => $path]);
    return back();
}
```

## Ссылки на файлы

По умолчанию файлы закрыты. Для закрытых файлов выдавайте временную ссылку:

```php
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30));

// Force download with a file name
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30), [
    'ResponseContentDisposition' => 'attachment; filename="report.pdf"',
]);
```

Для публичных файлов (например, изображений товаров) откройте доступ на чтение к папке **[политикой бакета](../buckets/bucket-policy.md)** и используйте постоянную ссылку:

```php
$url = Storage::disk('s3')->url('public/products/1.jpg');
// https://s3.uzcstorage.uz/my-bucket/public/products/1.jpg
```

## Прямая загрузка из браузера

Большие файлы лучше загружать из браузера прямо в бакет, не пропуская через PHP. Создайте временную ссылку на загрузку методом `temporaryUploadUrl` (есть в актуальных версиях Laravel; в старых версиях создайте ссылку через SDK, как в статье **[PHP](php.md)**):

```php
['url' => $url, 'headers' => $headers] = Storage::disk('s3')->temporaryUploadUrl(
    'uploads/' . Str::uuid() . '.mp4', now()->addMinutes(10)
);
return response()->json(compact('url', 'headers'));
```

Браузер отправляет файл запросом `fetch(url, { method: "PUT", headers, body: file })`. Настройте для бакета **[CORS](../buckets/cors.md)**.

> [!TIP]
> Оставьте диски `public` и `local` для временных файлов, а пользовательские файлы перенесите на `s3`: тогда серверы приложения не хранят состояние, их можно масштабировать и пересоздавать без потери данных.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
