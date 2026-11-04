# C# / .NET

**AWS SDK for .NET** (пакет `AWSSDK.S3`) — официальный SDK для C# и других языков .NET. Примеры рассчитаны на .NET 8+ и `AWSSDK.S3` 4.x.

## Установка

```bash
dotnet add package AWSSDK.S3
```

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Создание клиента

```csharp
using Amazon.Runtime;
using Amazon.S3;
using Amazon.S3.Model;

var config = new AmazonS3Config
{
    ServiceURL = "https://s3.uzcstorage.uz",
    AuthenticationRegion = "default",
    ForcePathStyle = true,
    RequestChecksumCalculation = RequestChecksumCalculation.WHEN_REQUIRED,
    ResponseChecksumValidation = ResponseChecksumValidation.WHEN_REQUIRED,
    MaxErrorRetry = 5,
};
using var s3 = new AmazonS3Client(config);   // keys from environment variables
const string Bucket = "my-bucket";
```

## Основные операции

```csharp
// Upload a file
await s3.PutObjectAsync(new PutObjectRequest
{
    BucketName = Bucket, Key = "docs/report.pdf",
    FilePath = "report.pdf", ContentType = "application/pdf",
});

// Upload a string
await s3.PutObjectAsync(new PutObjectRequest { BucketName = Bucket, Key = "docs/hello.txt", ContentBody = "Hello, UzCloud!" });

// Download to a file
using (var resp = await s3.GetObjectAsync(Bucket, "docs/report.pdf"))
    await resp.WriteResponseStreamToFileAsync("report-copy.pdf", false, CancellationToken.None);

// Copy and delete
await s3.CopyObjectAsync(Bucket, "docs/report.pdf", Bucket, "archive/report.pdf");
await s3.DeleteObjectAsync(Bucket, "docs/report.pdf");
```

## Список всех объектов

Один запрос возвращает не больше 1 000 объектов. Чтобы получить все объекты с префиксом, используйте пагинатор:

```csharp
var paginator = s3.Paginators.ListObjectsV2(new ListObjectsV2Request { BucketName = Bucket, Prefix = "docs/" });
await foreach (var obj in paginator.S3Objects)
    Console.WriteLine($"{obj.Key} {obj.Size}");
```

## Большие файлы

`TransferUtility` загружает большие файлы частями и сообщает о прогрессе:

```csharp
using Amazon.S3.Transfer;

var transfer = new TransferUtility(s3);
var request = new TransferUtilityUploadRequest
{
    BucketName = Bucket,
    Key = "backups/backup.tar.gz",
    FilePath = "backup.tar.gz",
    PartSize = 64 * 1024 * 1024,
};
request.UploadProgressEvent += (_, e) => Console.WriteLine($"{e.PercentDone}%");
await transfer.UploadAsync(request);
```

## Потоковая передача

Чтобы не загружать большой объект в память целиком, читайте и записывайте его частями:

```csharp
// Download as a stream
using (var resp = await s3.GetObjectAsync(Bucket, "media/video.mp4"))
await using (var file = File.Create("video-copy.mp4"))
    await resp.ResponseStream.CopyToAsync(file);

// Upload from a stream (for example, IFormFile.OpenReadStream() in ASP.NET Core)
await using (var stream = File.OpenRead("video.mp4"))
    await transfer.UploadAsync(stream, Bucket, "media/video.mp4");
```

## Presigned URL

Presigned URL дает временный доступ к объекту без передачи ключей. Ссылка на загрузку позволяет браузеру или другому сервису загрузить файл прямо в бакет — см. **[Presigned URL](../features/presigned-url.md)** и **[CORS](../features/cors.md)**.

```csharp
// Download link, valid for 1 hour
string getUrl = await s3.GetPreSignedURLAsync(new GetPreSignedUrlRequest
{
    BucketName = Bucket, Key = "docs/report.pdf",
    Verb = HttpVerb.GET, Expires = DateTime.UtcNow.AddHours(1),
});

// Upload link, valid for 10 minutes
string putUrl = await s3.GetPreSignedURLAsync(new GetPreSignedUrlRequest
{
    BucketName = Bucket, Key = "uploads/photo.jpg",
    Verb = HttpVerb.PUT, ContentType = "image/jpeg",
    Expires = DateTime.UtcNow.AddMinutes(10),
});
```

## Ошибки и повторные попытки

Самые частые ошибки — отсутствующий объект (`NoSuchKey` или `404` для `HeadObject`) и нет доступа (`AccessDenied`, `403`). Сетевые ошибки и ответы `5xx` повторяются автоматически; число попыток задается при создании клиента.

```csharp
using System.Net;

async Task<bool> ObjectExists(string key)
{
    try
    {
        await s3.GetObjectMetadataAsync(Bucket, key);
        return true;
    }
    catch (AmazonS3Exception e) when (e.StatusCode == HttpStatusCode.NotFound)
    {
        return false;
    }
}

try
{
    using var resp = await s3.GetObjectAsync(Bucket, "missing.txt");
}
catch (AmazonS3Exception e) when (e.ErrorCode == "NoSuchKey")
{
    Console.WriteLine("Object not found");
}
catch (AmazonS3Exception e) when (e.StatusCode == HttpStatusCode.Forbidden)
{
    Console.WriteLine("Check the keys and the bucket policy");
}
```

## ASP.NET Core

Зарегистрируйте клиент один раз в `Program.cs` и внедряйте `IAmazonS3` в контроллеры и сервисы:

```csharp
builder.Services.AddSingleton<IAmazonS3>(_ => new AmazonS3Client(new AmazonS3Config
{
    ServiceURL = builder.Configuration["S3:Endpoint"],
    AuthenticationRegion = "default",
    ForcePathStyle = true,
    RequestChecksumCalculation = RequestChecksumCalculation.WHEN_REQUIRED,
    ResponseChecksumValidation = ResponseChecksumValidation.WHEN_REQUIRED,
}));

app.MapPost("/upload", async (IFormFile file, IAmazonS3 s3) =>
{
    var key = $"uploads/{Guid.NewGuid()}{Path.GetExtension(file.FileName)}";
    await using var stream = file.OpenReadStream();
    await s3.PutObjectAsync(new PutObjectRequest
    {
        BucketName = "my-bucket", Key = key, InputStream = stream, ContentType = file.ContentType,
    });
    return Results.Ok(new { key });
}).DisableAntiforgery();
```

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
