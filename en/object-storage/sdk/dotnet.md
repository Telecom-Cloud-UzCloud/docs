# C# / .NET

**AWS SDK for .NET** (the `AWSSDK.S3` package) is the official SDK for C# and other .NET languages. The examples require .NET 8 or later and `AWSSDK.S3` 4.x.

## Installation

```bash
dotnet add package AWSSDK.S3
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Create a Client

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

## Basic Operations

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

## List All Objects

One request returns at most 1,000 objects. To get all objects with a prefix, use a paginator:

```csharp
var paginator = s3.Paginators.ListObjectsV2(new ListObjectsV2Request { BucketName = Bucket, Prefix = "docs/" });
await foreach (var obj in paginator.S3Objects)
    Console.WriteLine($"{obj.Key} {obj.Size}");
```

## Large Files

`TransferUtility` uploads large files in parts and reports progress:

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

## Streaming

To avoid loading a large object into memory, read and write it in chunks:

```csharp
// Download as a stream
using (var resp = await s3.GetObjectAsync(Bucket, "media/video.mp4"))
await using (var file = File.Create("video-copy.mp4"))
    await resp.ResponseStream.CopyToAsync(file);

// Upload from a stream (for example, IFormFile.OpenReadStream() in ASP.NET Core)
await using (var stream = File.OpenRead("video.mp4"))
    await transfer.UploadAsync(stream, Bucket, "media/video.mp4");
```

## Presigned URLs

A presigned URL gives temporary access to an object without sharing your keys. An upload link lets a browser or another service upload a file directly to the bucket — see **[Presigned URL](../features/presigned-url.md)** and **[CORS](../features/cors.md)**.

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

## Errors and Retries

The most common errors are a missing object (`NoSuchKey`, or `404` for `HeadObject`) and no access (`AccessDenied`, `403`). Network errors and `5xx` responses are retried automatically; the number of attempts is set when you create the client.

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

Register the client once in `Program.cs` and inject `IAmazonS3` into controllers and services:

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
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
