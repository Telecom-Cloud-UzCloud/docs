# Laravel

Laravel works with object storage through the built-in `s3` disk of the `Storage` facade. Uploaded files, avatars, documents and exports can be stored in a bucket instead of the server disk.

## Installation

The examples are for Laravel 10 or later. Install the S3 adapter for Flysystem:

```bash
composer require league/flysystem-aws-s3-v3 "^3.0"
```

## Configuration

Add the connection settings to `.env`:

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

The `s3` disk in `config/filesystems.php` already reads these variables. Add two lines to it that disable unnecessary checksum headers:

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

Check the connection with `php artisan tinker`:

```php
Storage::disk('s3')->put('test.txt', 'Hello, UzCloud!');
Storage::disk('s3')->get('test.txt');
```

## Working with Files

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

## Upload Files from a Form

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

## Links to Files

Files are private by default. For private files, give a temporary link:

```php
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30));

// Force download with a file name
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30), [
    'ResponseContentDisposition' => 'attachment; filename="report.pdf"',
]);
```

For public files (for example, product images), open read access to a folder with a **[bucket policy](../buckets/bucket-policy.md)** and use a permanent link:

```php
$url = Storage::disk('s3')->url('public/products/1.jpg');
// https://s3.uzcstorage.uz/my-bucket/public/products/1.jpg
```

## Direct Upload from a Browser

Large files are better uploaded by the browser directly to the bucket, without passing them through PHP. Create a temporary upload link with `temporaryUploadUrl` (available in recent Laravel versions; in older versions, create the link with the SDK as shown in the **[PHP](php.md)** article):

```php
['url' => $url, 'headers' => $headers] = Storage::disk('s3')->temporaryUploadUrl(
    'uploads/' . Str::uuid() . '.mp4', now()->addMinutes(10)
);
return response()->json(compact('url', 'headers'));
```

The browser sends the file with `fetch(url, { method: "PUT", headers, body: file })`. Configure **[CORS](../buckets/cors.md)** for the bucket.

> [!TIP]
> Keep `public` and `local` disks for temporary files and move user files to `s3`: then the application servers stay stateless and can be scaled or recreated without losing data.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
