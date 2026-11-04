# Go

**AWS SDK for Go v2** is the official SDK for Go.

## Installation

```bash
go get github.com/aws/aws-sdk-go-v2/config
go get github.com/aws/aws-sdk-go-v2/service/s3
```

## Access Keys

Pass the keys through environment variables — the SDK reads them automatically. Never store keys in the source code or in a repository.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Example

```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
	ctx := context.Background()
	cfg, err := config.LoadDefaultConfig(ctx, config.WithRegion("default"))
	if err != nil {
		log.Fatal(err)
	}
	client := s3.NewFromConfig(cfg, func(o *s3.Options) {
		o.BaseEndpoint = aws.String("https://s3.uzcstorage.uz")
		o.UsePathStyle = true
		o.RequestChecksumCalculation = aws.RequestChecksumCalculationWhenRequired
		o.ResponseChecksumValidation = aws.ResponseChecksumValidationWhenRequired
	})
	bucket := aws.String("my-bucket")

	// 1. Upload a file
	f, err := os.Open("report.pdf")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	_, err = client.PutObject(ctx, &s3.PutObjectInput{
		Bucket: bucket, Key: aws.String("docs/report.pdf"), Body: f,
		ContentType: aws.String("application/pdf"),
	})
	if err != nil {
		log.Fatal(err)
	}

	// 2. List objects
	list, err := client.ListObjectsV2(ctx, &s3.ListObjectsV2Input{Bucket: bucket, Prefix: aws.String("docs/")})
	if err != nil {
		log.Fatal(err)
	}
	for _, obj := range list.Contents {
		fmt.Println(*obj.Key, *obj.Size)
	}

	// 3. Temporary download link (15 minutes)
	presign := s3.NewPresignClient(client)
	req, err := presign.PresignGetObject(ctx,
		&s3.GetObjectInput{Bucket: bucket, Key: aws.String("docs/report.pdf")},
		s3.WithPresignExpires(15*time.Minute))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(req.URL)

	// 4. Delete an object
	_, err = client.DeleteObject(ctx, &s3.DeleteObjectInput{Bucket: bucket, Key: aws.String("docs/report.pdf")})
	if err != nil {
		log.Fatal(err)
	}
}
```

For large files, use the `manager.Uploader` from `github.com/aws/aws-sdk-go-v2/feature/s3/manager`.

> [!TIP]
> **See also:**
>
> - **[Connection Parameters](../connection.md)**
