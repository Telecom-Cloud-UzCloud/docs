# Go

**AWS SDK for Go v2** — Go uchun rasmiy SDK.

## Oʻrnatish

```bash
go get github.com/aws/aws-sdk-go-v2/config
go get github.com/aws/aws-sdk-go-v2/service/s3
go get github.com/aws/aws-sdk-go-v2/feature/s3/manager
```

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Mijoz yaratish

```go
package main

import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

func newClient(ctx context.Context) *s3.Client {
	cfg, err := config.LoadDefaultConfig(ctx,
		config.WithRegion("default"),
		config.WithRetryMaxAttempts(5),
	)
	if err != nil {
		log.Fatal(err)
	}
	return s3.NewFromConfig(cfg, func(o *s3.Options) {
		o.BaseEndpoint = aws.String("https://s3.uzcstorage.uz")
		o.UsePathStyle = true
		o.RequestChecksumCalculation = aws.RequestChecksumCalculationWhenRequired
		o.ResponseChecksumValidation = aws.ResponseChecksumValidationWhenRequired
	})
}
```

Quyidagi misollarda `ctx`, `client := newClient(ctx)` va `bucket := aws.String("my-bucket")` ishlatiladi.

## Asosiy amallar

```go
// Upload a file
f, err := os.Open("report.pdf")
if err != nil {
	log.Fatal(err)
}
defer f.Close()
_, err = client.PutObject(ctx, &s3.PutObjectInput{
	Bucket: bucket, Key: aws.String("docs/report.pdf"), Body: f,
	ContentType: aws.String("application/pdf"),
})

// Copy and delete
_, err = client.CopyObject(ctx, &s3.CopyObjectInput{
	Bucket: bucket, Key: aws.String("archive/report.pdf"),
	CopySource: aws.String("my-bucket/docs/report.pdf"),
})
_, err = client.DeleteObject(ctx, &s3.DeleteObjectInput{Bucket: bucket, Key: aws.String("docs/report.pdf")})
```

## Barcha obyektlar roʻyxati

Bitta soʻrov koʻpi bilan 1 000 ta obyektni qaytaradi. Prefiksli barcha obyektlarni olish uchun paginatordan foydalaning:

```go
p := s3.NewListObjectsV2Paginator(client, &s3.ListObjectsV2Input{Bucket: bucket, Prefix: aws.String("docs/")})
for p.HasMorePages() {
	page, err := p.NextPage(ctx)
	if err != nil {
		log.Fatal(err)
	}
	for _, obj := range page.Contents {
		fmt.Println(*obj.Key, *obj.Size)
	}
}
```

## Katta fayllar

`manager.Uploader` faylni qismlarga boʻladi va ularni parallel yuklaydi:

```go
import "github.com/aws/aws-sdk-go-v2/feature/s3/manager"

uploader := manager.NewUploader(client, func(u *manager.Uploader) {
	u.PartSize = 64 * 1024 * 1024
	u.Concurrency = 4
})
f, _ := os.Open("backup.tar.gz")
defer f.Close()
_, err = uploader.Upload(ctx, &s3.PutObjectInput{Bucket: bucket, Key: aws.String("backups/backup.tar.gz"), Body: f})
```

## Oqimli uzatish

Katta obyektni xotiraga toʻliq yuklamaslik uchun uni qismlarga boʻlib oʻqing va yozing:

```go
out, err := client.GetObject(ctx, &s3.GetObjectInput{Bucket: bucket, Key: aws.String("media/video.mp4")})
if err != nil {
	log.Fatal(err)
}
defer out.Body.Close()

dst, _ := os.Create("video-copy.mp4")
defer dst.Close()
_, err = io.Copy(dst, out.Body) // copies in chunks, without loading the whole object
```

## Presigned URL

Presigned URL kalitlarni bermasdan obyektga vaqtinchalik kirish imkonini beradi. Yuklash havolasi brauzer yoki boshqa xizmatga faylni bevosita bucketga yuklash imkonini beradi — **[Presigned URL](../features/presigned-url.md)** va **[CORS](../features/cors.md)** ga qarang.

```go
presign := s3.NewPresignClient(client)

// Download link, valid for 1 hour
get, err := presign.PresignGetObject(ctx,
	&s3.GetObjectInput{Bucket: bucket, Key: aws.String("docs/report.pdf")},
	s3.WithPresignExpires(time.Hour))

// Upload link, valid for 10 minutes
put, err := presign.PresignPutObject(ctx,
	&s3.PutObjectInput{Bucket: bucket, Key: aws.String("uploads/photo.jpg"), ContentType: aws.String("image/jpeg")},
	s3.WithPresignExpires(10*time.Minute))
fmt.Println(get.URL, put.URL)
```

## Xatolar va qayta urinishlar

Eng keng tarqalgan xatolar — obyekt mavjud emas (`NoSuchKey` yoki `HeadObject` uchun `404`) va kirish huquqi yoʻq (`AccessDenied`, `403`). Tarmoq xatolari va `5xx` javoblari avtomatik qayta urinib koʻriladi; urinishlar soni mijoz yaratilganda belgilanadi.

```go
import (
	"errors"

	"github.com/aws/aws-sdk-go-v2/service/s3/types"
)

func objectExists(ctx context.Context, client *s3.Client, bucket, key string) (bool, error) {
	_, err := client.HeadObject(ctx, &s3.HeadObjectInput{Bucket: &bucket, Key: &key})
	var nf *types.NotFound
	if errors.As(err, &nf) {
		return false, nil
	}
	return err == nil, err
}

_, err = client.GetObject(ctx, &s3.GetObjectInput{Bucket: bucket, Key: aws.String("missing.txt")})
var nsk *types.NoSuchKey
if errors.As(err, &nsk) {
	fmt.Println("Object not found")
}
```

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
