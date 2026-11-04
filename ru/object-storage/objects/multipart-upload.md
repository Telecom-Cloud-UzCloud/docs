# Мультипарт-загрузка

**Мультипарт-загрузка** делит большой файл на части и загружает их параллельно. При обрыве соединения заново загружается только неудачная часть. Используйте ее для файлов больше 100 МБ.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

## Ограничения

- размер части — от 5 МБ до 5 ГБ (последняя часть может быть меньше);
- до 10 000 частей на файл;
- максимальный размер объекта — 5 ТБ.

## Автоматическая мультипарт-загрузка

`aws s3 cp`, `aws s3 sync`, rclone и SDK используют мультипарт-загрузку автоматически для больших файлов. В AWS CLI можно настроить размер части и число параллельных запросов:

```bash
aws configure set default.s3.multipart_threshold 64MB
aws configure set default.s3.multipart_chunksize 64MB
aws configure set default.s3.max_concurrent_requests 10

aws s3 cp ./backup.tar.gz s3://my-bucket/backups/
```

## Мультипарт-загрузка вручную

Низкоуровневые команды полезны в скриптах и для понимания того, как это работает:

**1.** Разделите файл на части:

```bash
split -b 100M backup.tar.gz part-
```

**2.** Начните загрузку и сохраните `UploadId`:

```bash
UPLOAD_ID=$(aws s3api create-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --query UploadId --output text)
```

**3.** Загрузите части, нумеруя их с 1:

```bash
n=1
for f in part-*; do
  ETAG=$(aws s3api upload-part --bucket my-bucket --key backups/backup.tar.gz \
    --upload-id "$UPLOAD_ID" --part-number $n --body "$f" \
    --query ETag --output text)
  echo "{\"PartNumber\": $n, \"ETag\": $ETAG}" >> parts.txt
  n=$((n+1))
done
echo "{\"Parts\": [$(paste -sd, parts.txt)]}" > parts.json
```

**4.** Завершите загрузку:

```bash
aws s3api complete-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id "$UPLOAD_ID" \
  --multipart-upload file://parts.json
```

## Незавершенные загрузки

Части незавершенной загрузки занимают место и оплачиваются, хотя их не видно в списке объектов. Найдите и отмените их:

```bash
aws s3api list-multipart-uploads --bucket my-bucket

aws s3api abort-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id <UploadId>
```

Чтобы удалять их автоматически, добавьте **[правило жизненного цикла](../buckets/lifecycle.md)** `AbortIncompleteMultipartUpload`.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
