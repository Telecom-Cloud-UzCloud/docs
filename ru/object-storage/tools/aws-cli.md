# AWS CLI

**AWS CLI** — официальная утилита командной строки Amazon. Она поддерживает все возможности S3 и работает с объектным хранилищем UzCloud.

## Установка

**Linux:**

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
```

**macOS:** `brew install awscli`. **Windows:** скачайте и запустите установщик со [страницы AWS CLI](https://aws.amazon.com/cli/).

Проверьте версию (нужна 2.13 или новее):

```bash
aws --version
```

## Настройка

Выполните `aws configure` и введите ключи. В поле **Default region name** укажите `default`:

```text
AWS Access Key ID [None]: <Access Key>
AWS Secret Access Key [None]: <Secret Key>
Default region name [None]: default
Default output format [None]: json
```

Затем добавьте адрес UzCloud в `~/.aws/config` (в Windows — `%USERPROFILE%\.aws\config`), чтобы не указывать его в каждой команде:

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
> Параметры `request_checksum_calculation` и `response_checksum_validation` отключают новые заголовки контрольных сумм, которые AWS CLI отправляет по умолчанию начиная с версии 2.23. Без них загрузка в S3-совместимые хранилища может завершаться ошибкой.

Проверьте подключение:

```bash
aws s3 ls
```

## Работа с файлами

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

Добавьте `--delete` к `aws s3 sync`, чтобы также удалять из бакета объекты, которых больше нет локально. Сначала запустите с `--dryrun`, чтобы увидеть, что изменится.

## Большие файлы

AWS CLI автоматически делит файлы больше 8 МБ на части и загружает их параллельно (мультипарт-загрузка). См. **[Мультипарт-загрузка](../features/multipart-upload.md)**.

## Временные ссылки

Создайте ссылку, которая дает доступ к закрытому объекту на ограниченное время (в секундах):

```bash
aws s3 presign s3://my-bucket/docs/report.pdf --expires-in 3600
```

См. **[Presigned URL](../features/presigned-url.md)**.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
