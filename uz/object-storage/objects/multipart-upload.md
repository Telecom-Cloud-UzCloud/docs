# Multipart yuklash

**Multipart yuklash** katta faylni qismlarga boʻladi va ularni parallel yuklaydi. Ulanish uzilsa, faqat muvaffaqiyatsiz qism qayta yuklanadi. Undan 100 MB dan katta fayllar uchun foydalaning.

Misollarda UzCloud uchun sozlangan **[AWS CLI](../tools/aws-cli.md)** ishlatiladi. `my-bucket` ni oʻz bucketingiz nomiga almashtiring.

## Cheklovlar

- qism hajmi — 5 MB dan 5 GB gacha (oxirgi qism kichikroq boʻlishi mumkin);
- bitta faylga 10 000 tagacha qism;
- obyektning maksimal hajmi — 5 TB.

## Avtomatik multipart yuklash

`aws s3 cp`, `aws s3 sync`, rclone va SDK’lar katta fayllar uchun multipart yuklashdan avtomatik foydalanadi. AWS CLI’da qism hajmini va parallel soʻrovlar sonini sozlash mumkin:

```bash
aws configure set default.s3.multipart_threshold 64MB
aws configure set default.s3.multipart_chunksize 64MB
aws configure set default.s3.max_concurrent_requests 10

aws s3 cp ./backup.tar.gz s3://my-bucket/backups/
```

## Qoʻlda multipart yuklash

Past darajadagi buyruqlar skriptlarda va bu qanday ishlashini tushunish uchun foydali:

**1.** Faylni qismlarga boʻling:

```bash
split -b 100M backup.tar.gz part-
```

**2.** Yuklashni boshlang va `UploadId` ni saqlang:

```bash
UPLOAD_ID=$(aws s3api create-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --query UploadId --output text)
```

**3.** Qismlarni 1 dan boshlab raqamlab yuklang:

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

**4.** Yuklashni yakunlang:

```bash
aws s3api complete-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id "$UPLOAD_ID" \
  --multipart-upload file://parts.json
```

## Tugallanmagan yuklashlar

Tugallanmagan yuklash qismlari obyektlar roʻyxatida koʻrinmasa ham joy egallaydi va toʻlanadi. Ularni toping va bekor qiling:

```bash
aws s3api list-multipart-uploads --bucket my-bucket

aws s3api abort-multipart-upload --bucket my-bucket \
  --key backups/backup.tar.gz --upload-id <UploadId>
```

Ularni avtomatik tozalash uchun `AbortIncompleteMultipartUpload` **[hayot sikli qoidasini](../buckets/lifecycle.md)** qoʻshing.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
