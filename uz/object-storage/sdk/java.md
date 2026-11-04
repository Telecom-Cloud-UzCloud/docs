# Java

**AWS SDK for Java 2.x** — Java uchun rasmiy SDK. Misollar Java 17+ va SDK 2.30+ versiyasi uchun moʻljallangan.

## Oʻrnatish

`pom.xml` ga bogʻliqliklarni qoʻshing (Maven):

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>software.amazon.awssdk</groupId>
      <artifactId>bom</artifactId>
      <version>2.31.0</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>

<dependencies>
  <dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
  </dependency>
  <dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3-transfer-manager</artifactId>
  </dependency>
</dependencies>
```

Gradle uchun: `implementation(platform("software.amazon.awssdk:bom:2.31.0"))`, `implementation("software.amazon.awssdk:s3")` va `implementation("software.amazon.awssdk:s3-transfer-manager")`.

## Kirish kalitlari

Kalitlarni muhit oʻzgaruvchilari orqali uzating — SDK ularni avtomatik oʻqiydi. Kalitlarni hech qachon manba kodida va repozitoriyda saqlamang.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Mijoz yaratish

```java
import java.net.URI;
import software.amazon.awssdk.core.checksums.RequestChecksumCalculation;
import software.amazon.awssdk.core.checksums.ResponseChecksumValidation;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;

static final URI ENDPOINT = URI.create("https://s3.uzcstorage.uz");
static final Region REGION = Region.of("default");
static final String BUCKET = "my-bucket";

S3Client s3 = S3Client.builder()
        .region(REGION)
        .endpointOverride(ENDPOINT)
        .forcePathStyle(true)
        .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
        .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
        .build();
```

`S3Client` oqimlar uchun xavfsiz: uni bir marta yarating va butun ilovada qayta foydalaning. Kalitlar muhit oʻzgaruvchilaridan avtomatik oʻqiladi.

## Asosiy amallar

```java
import java.nio.file.Paths;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.core.sync.ResponseTransformer;
import software.amazon.awssdk.services.s3.model.*;

// Upload a file
s3.putObject(r -> r.bucket(BUCKET).key("docs/report.pdf").contentType("application/pdf"),
        RequestBody.fromFile(Paths.get("report.pdf")));

// Upload a string
s3.putObject(r -> r.bucket(BUCKET).key("docs/hello.txt"), RequestBody.fromString("Hello, UzCloud!"));

// Download to a file
s3.getObject(r -> r.bucket(BUCKET).key("docs/report.pdf"),
        ResponseTransformer.toFile(Paths.get("report-copy.pdf")));

// Read a small object into memory
String text = s3.getObjectAsBytes(r -> r.bucket(BUCKET).key("docs/hello.txt")).asUtf8String();

// Copy and delete
s3.copyObject(r -> r.sourceBucket(BUCKET).sourceKey("docs/report.pdf")
        .destinationBucket(BUCKET).destinationKey("archive/report.pdf"));
s3.deleteObject(r -> r.bucket(BUCKET).key("docs/report.pdf"));
```

## Barcha obyektlar roʻyxati

Bitta soʻrov koʻpi bilan 1 000 ta obyektni qaytaradi. Prefiksli barcha obyektlarni olish uchun paginatordan foydalaning:

```java
s3.listObjectsV2Paginator(r -> r.bucket(BUCKET).prefix("docs/"))
        .contents()
        .forEach(o -> System.out.println(o.key() + " " + o.size()));
```

## Katta fayllar

**S3 Transfer Manager** katta fayllarni qismlarga boʻlib, parallel yuklaydi va yuklab oladi. U asinxron mijoz ustida ishlaydi:

```java
import software.amazon.awssdk.services.s3.S3AsyncClient;
import software.amazon.awssdk.transfer.s3.S3TransferManager;
import software.amazon.awssdk.transfer.s3.model.UploadFileRequest;
import software.amazon.awssdk.transfer.s3.progress.LoggingTransferListener;

S3AsyncClient asyncS3 = S3AsyncClient.builder()
        .region(REGION)
        .endpointOverride(ENDPOINT)
        .forcePathStyle(true)
        .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
        .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
        .multipartEnabled(true)
        .multipartConfiguration(c -> c.minimumPartSizeInBytes(64L * 1024 * 1024))
        .build();

try (S3TransferManager tm = S3TransferManager.builder().s3Client(asyncS3).build()) {
    tm.uploadFile(UploadFileRequest.builder()
                    .putObjectRequest(r -> r.bucket(BUCKET).key("backups/backup.tar.gz"))
                    .source(Paths.get("backup.tar.gz"))
                    .addTransferListener(LoggingTransferListener.create())
                    .build())
            .completionFuture()
            .join();
}
```

## Oqimli uzatish

Katta obyektni xotiraga toʻliq yuklamaslik uchun uni qismlarga boʻlib oʻqing va yozing:

```java
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.Files;

try (InputStream in = s3.getObject(r -> r.bucket(BUCKET).key("media/video.mp4"));
     OutputStream out = Files.newOutputStream(Paths.get("video-copy.mp4"))) {
    in.transferTo(out);
}

// Upload from a stream of known length (for example, an uploaded file in a web app)
try (InputStream in = Files.newInputStream(Paths.get("video.mp4"))) {
    long size = Files.size(Paths.get("video.mp4"));
    s3.putObject(r -> r.bucket(BUCKET).key("media/video.mp4"), RequestBody.fromInputStream(in, size));
}
```

## Presigned URL

Presigned URL kalitlarni bermasdan obyektga vaqtinchalik kirish imkonini beradi. Yuklash havolasi brauzer yoki boshqa xizmatga faylni bevosita bucketga yuklash imkonini beradi — **[Presigned URL](../features/presigned-url.md)** va **[CORS](../features/cors.md)** ga qarang.

```java
import java.time.Duration;
import software.amazon.awssdk.services.s3.S3Configuration;
import software.amazon.awssdk.services.s3.presigner.S3Presigner;

try (S3Presigner presigner = S3Presigner.builder()
        .region(REGION)
        .endpointOverride(ENDPOINT)
        .serviceConfiguration(S3Configuration.builder().pathStyleAccessEnabled(true).build())
        .build()) {

    // Download link, valid for 1 hour
    String getUrl = presigner.presignGetObject(p -> p
            .signatureDuration(Duration.ofHours(1))
            .getObjectRequest(r -> r.bucket(BUCKET).key("docs/report.pdf"))).url().toString();

    // Upload link, valid for 10 minutes
    String putUrl = presigner.presignPutObject(p -> p
            .signatureDuration(Duration.ofMinutes(10))
            .putObjectRequest(r -> r.bucket(BUCKET).key("uploads/photo.jpg").contentType("image/jpeg"))).url().toString();
}
```

## Xatolar va qayta urinishlar

Eng keng tarqalgan xatolar — obyekt mavjud emas (`NoSuchKey` yoki `HeadObject` uchun `404`) va kirish huquqi yoʻq (`AccessDenied`, `403`). Tarmoq xatolari va `5xx` javoblari avtomatik qayta urinib koʻriladi; urinishlar soni mijoz yaratilganda belgilanadi.

```java
import software.amazon.awssdk.services.s3.model.NoSuchKeyException;
import software.amazon.awssdk.services.s3.model.S3Exception;

boolean objectExists(String key) {
    try {
        s3.headObject(r -> r.bucket(BUCKET).key(key));
        return true;
    } catch (NoSuchKeyException e) {
        return false;
    }
}

try {
    s3.getObject(r -> r.bucket(BUCKET).key("missing.txt"));
} catch (NoSuchKeyException e) {
    System.out.println("Object not found");
} catch (S3Exception e) {
    if (e.statusCode() == 403) System.out.println("Check the keys and the bucket policy");
    else throw e;
}
```

## Spring Boot

Mijozni bean sifatida roʻyxatdan oʻtkazing va kerakli joyga kiriting. Manzil va bucketni `application.yml` da saqlang:

```yaml
uzcloud:
  s3:
    endpoint: https://s3.uzcstorage.uz
    bucket: my-bucket
```

```java
@Configuration
public class S3Config {
    @Bean
    S3Client s3Client(@Value("${uzcloud.s3.endpoint}") String endpoint) {
        return S3Client.builder()
                .region(Region.of("default"))
                .endpointOverride(URI.create(endpoint))
                .forcePathStyle(true)
                .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
                .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
                .build();
    }
}
```

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
