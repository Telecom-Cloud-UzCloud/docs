# AWS CLI

**AWS CLI** — Amazon’ning rasmiy buyruqlar satri vositasi. U S3’ning barcha imkoniyatlarini qoʻllab-quvvatlaydi va UzCloud obyektli xotirasi bilan ishlaydi.

## Oʻrnatish

**Linux:**

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
```

**macOS:** `brew install awscli`. **Windows:** oʻrnatuvchini [AWS CLI sahifasidan](https://aws.amazon.com/cli/) yuklab oling va ishga tushiring.

Versiyani tekshiring (2.13 yoki undan yangi versiya kerak):

```bash
aws --version
```

## Sozlash

`aws configure` ni bajaring va kalitlarni kiriting. **Default region name** maydoniga `default` ni kiriting:

```text
AWS Access Key ID [None]: <Access Key>
AWS Secret Access Key [None]: <Secret Key>
Default region name [None]: default
Default output format [None]: json
```

Soʻngra UzCloud manzilini `~/.aws/config` fayliga qoʻshing (Windows’da — `%USERPROFILE%\.aws\config`), shunda uni har bir buyruqda koʻrsatish shart boʻlmaydi:

```ini
[default]
region = default
output = json
endpoint_url = https://s3.uzcstorage.uz
request_checksum_calculation = when_required
response_checksum_validation = when_required
s3 =
    addressing_style = path
```

> [!NOTE]
> `request_checksum_calculation` va `response_checksum_validation` parametrlari AWS CLI 2.23 versiyasidan boshlab standart holatda yuboradigan yangi nazorat yigʻindisi sarlavhalarini oʻchiradi. Ularsiz S3 bilan mos xotiralarga yuklash xato bilan tugashi mumkin.

Ulanishni tekshiring:

```bash
aws s3 ls
```

## Fayllar bilan ishlash

```bash
# List objects in a bucket
aws s3 ls s3://my-bucket/

# Upload a file
aws s3 cp ./report.pdf s3://my-bucket/docs/report.pdf

# Download a file
aws s3 cp s3://my-bucket/docs/report.pdf ./report.pdf

# Upload a folder recursively
aws s3 cp ./site s3://my-bucket/site/ --recursive

# Sync a local folder with a bucket (uploads only new and changed files)
aws s3 sync ./backups s3://my-bucket/backups/

# Delete an object
aws s3 rm s3://my-bucket/docs/report.pdf

# Delete all objects with a prefix
aws s3 rm s3://my-bucket/tmp/ --recursive
```

Mahalliy ravishda endi mavjud boʻlmagan obyektlarni bucketdan ham oʻchirish uchun `aws s3 sync` ga `--delete` ni qoʻshing. Avval nima oʻzgarishini koʻrish uchun `--dryrun` bilan ishga tushiring.

## Katta fayllar

AWS CLI 8 MB dan katta fayllarni avtomatik ravishda qismlarga boʻladi va ularni parallel yuklaydi (multipart yuklash). **[Multipart yuklash](../objects/multipart-upload.md)** ga qarang.

## Vaqtinchalik havolalar

Yopiq obyektga cheklangan vaqt (soniyalarda) kirish imkonini beradigan havola yarating:

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

**[Presigned URL](../objects/presigned-url.md)** ga qarang.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Ulanish parametrlari](../connection.md)**
