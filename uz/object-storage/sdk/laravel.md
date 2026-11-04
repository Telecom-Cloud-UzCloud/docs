# Laravel

Laravel obyektli xotira bilan `Storage` fasadining oʻrnatilgan `s3` diski orqali ishlaydi. Yuklangan fayllar, avatarlar, hujjatlar va eksportlarni server diski oʻrniga bucketda saqlash mumkin.

## Oʻrnatish

Misollar Laravel 10 va undan yangi versiyalar uchun moʻljallangan. Flysystem uchun S3 adapterini oʻrnating:

```bash
composer require league/flysystem-aws-s3-v3 "^3.0"
```

## Sozlash

Ulanish parametrlarini `.env` fayliga qoʻshing:

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

`config/filesystems.php` dagi `s3` diski bu oʻzgaruvchilarni allaqachon oʻqiydi. Unga ortiqcha nazorat yigʻindisi sarlavhalarini oʻchiradigan ikki qatorni qoʻshing:

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

Ulanishni `php artisan tinker` da tekshiring:

```php
Storage::disk('s3')->put('test.txt', 'Hello, UzCloud!');
Storage::disk('s3')->get('test.txt');
```

## Fayllar bilan ishlash

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

## Shakldan fayllarni yuklash

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

## Fayllarga havolalar

Standart holatda fayllar yopiq. Yopiq fayllar uchun vaqtinchalik havola bering:

```php
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30));

// Force download with a file name
$url = Storage::disk('s3')->temporaryUrl($path, now()->addMinutes(30), [
    'ResponseContentDisposition' => 'attachment; filename="report.pdf"',
]);
```

Ommaviy fayllar uchun (masalan, mahsulot rasmlari) **[bucket siyosati](../buckets/bucket-policy.md)** yordamida papkaga oʻqish huquqini oching va doimiy havoladan foydalaning:

```php
$url = Storage::disk('s3')->url('public/products/1.jpg');
// https://s3.uzcstorage.uz/my-bucket/public/products/1.jpg
```

## Brauzerdan bevosita yuklash

Katta fayllarni PHP orqali oʻtkazmasdan, brauzerdan bevosita bucketga yuklagan maʼqul. `temporaryUploadUrl` usuli bilan vaqtinchalik yuklash havolasini yarating (Laravel’ning dolzarb versiyalarida mavjud; eski versiyalarda havolani **[PHP](php.md)** maqolasidagidek SDK orqali yarating):

```php
['url' => $url, 'headers' => $headers] = Storage::disk('s3')->temporaryUploadUrl(
    'uploads/' . Str::uuid() . '.mp4', now()->addMinutes(10)
);
return response()->json(compact('url', 'headers'));
```

Brauzer faylni `fetch(url, { method: "PUT", headers, body: file })` soʻrovi bilan yuboradi. Bucket uchun **[CORS](../buckets/cors.md)** ni sozlang.

> [!TIP]
> `public` va `local` disklarini vaqtinchalik fayllar uchun qoldiring, foydalanuvchi fayllarini esa `s3` ga oʻtkazing: shunda ilova serverlari holat saqlamaydi, ularni maʼlumotlarni yoʻqotmasdan masshtablash va qayta yaratish mumkin.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
