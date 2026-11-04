# Java

**AWS SDK for Java 2.x** — официальный SDK для Java. Примеры рассчитаны на Java 17+ и SDK версии 2.30+.

## Установка

Добавьте зависимости в `pom.xml` (Maven):

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

Для Gradle: `implementation(platform("software.amazon.awssdk:bom:2.31.0"))`, `implementation("software.amazon.awssdk:s3")` и `implementation("software.amazon.awssdk:s3-transfer-manager")`.

## Ключи доступа

Передавайте ключи через переменные окружения — SDK прочитает их автоматически. Никогда не храните ключи в исходном коде и в репозитории.

```bash
export AWS_ACCESS_KEY_ID=<Access Key>
export AWS_SECRET_ACCESS_KEY=<Secret Key>
```

## Создание клиента

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

`S3Client` потокобезопасен: создайте его один раз и используйте во всем приложении. Ключи читаются из переменных окружения автоматически.

## Основные операции

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

## Список всех объектов

Один запрос возвращает не больше 1 000 объектов. Чтобы получить все объекты с префиксом, используйте пагинатор:

```java
s3.listObjectsV2Paginator(r -> r.bucket(BUCKET).prefix("docs/"))
        .contents()
        .forEach(o -> System.out.println(o.key() + " " + o.size()));
```

## Большие файлы

**S3 Transfer Manager** загружает и скачивает большие файлы частями, параллельно. Он работает поверх асинхронного клиента:

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

## Потоковая передача

Чтобы не загружать большой объект в память целиком, читайте и записывайте его частями:

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

Presigned URL дает временный доступ к объекту без передачи ключей. Ссылка на загрузку позволяет браузеру или другому сервису загрузить файл прямо в бакет — см. **[Presigned URL](../features/presigned-url.md)** и **[CORS](../features/cors.md)**.

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

## Ошибки и повторные попытки

Самые частые ошибки — отсутствующий объект (`NoSuchKey` или `404` для `HeadObject`) и нет доступа (`AccessDenied`, `403`). Сетевые ошибки и ответы `5xx` повторяются автоматически; число попыток задается при создании клиента.

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

Зарегистрируйте клиент как бин и внедряйте его там, где он нужен. Адрес и бакет храните в `application.yml`:

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
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
