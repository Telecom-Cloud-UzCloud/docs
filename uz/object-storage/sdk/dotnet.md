# C# / .NET

**AWS SDK for .NET** (`AWSSDK.S3` paketi) — C# va boshqa .NET tillari uchun rasmiy SDK. Misollar .NET 8+ va `AWSSDK.S3` 4.x uchun moʻljallangan.

## Oʻrnatish

```bash
dotnet add package AWSSDK.S3
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Mijoz yaratish

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

## Asosiy amallar

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

## Barcha obyektlar roʻyxati

Bitta soʻrov koʻpi bilan 1 000 ta obyektni qaytaradi. Prefiksli barcha obyektlarni olish uchun paginatordan foydalaning:

```csharp
var paginator = s3.Paginators.ListObjectsV2(new ListObjectsV2Request { BucketName = Bucket, Prefix = "docs/" });
await foreach (var obj in paginator.S3Objects)
    Console.WriteLine($"{obj.Key} {obj.Size}");
```

## Katta fayllar

`TransferUtility` katta fayllarni qismlarga boʻlib yuklaydi va jarayon haqida xabar beradi:

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

## Oqimli uzatish

Katta obyektni xotiraga toʻliq yuklamaslik uchun uni qismlarga boʻlib oʻqing va yozing:

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

Presigned URL kalitlarni bermasdan obyektga vaqtinchalik kirish imkonini beradi. Yuklash havolasi brauzer yoki boshqa xizmatga faylni bevosita bucketga yuklash imkonini beradi — **[Presigned URL](../objects/presigned-url.md)** va **[CORS](../buckets/cors.md)** ga qarang.

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

## Xatolar va qayta urinishlar

Eng keng tarqalgan xatolar — obyekt mavjud emas (`NoSuchKey` yoki `HeadObject` uchun `404`) va kirish huquqi yoʻq (`AccessDenied`, `403`). Tarmoq xatolari va `5xx` javoblari avtomatik qayta urinib koʻriladi; urinishlar soni mijoz yaratilganda belgilanadi.

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

Mijozni `Program.cs` da bir marta roʻyxatdan oʻtkazing va `IAmazonS3` ni kontrollerlar va servislarga kiriting:

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
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
