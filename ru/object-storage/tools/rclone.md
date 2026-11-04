# rclone

**rclone** — утилита для синхронизации файлов с облачными хранилищами. Она хорошо подходит для резервного копирования и переноса данных между облаками, а также умеет подключать бакет как папку.

## Установка

```bash
sudo -v ; curl https://rclone.org/install.sh | sudo bash
```

Для Windows и macOS скачайте rclone с [rclone.org/downloads](https://rclone.org/downloads/).

## Настройка

Добавьте подключение в `~/.config/rclone/rclone.conf`:

```ini
[uzcloud]
type = s3
provider = Ceph
access_key_id = <Access Key>
secret_access_key = <Secret Key>
endpoint = https://s3.uzcstorage.uz
force_path_style = true
acl = private
```

Подключение можно создать и интерактивно командой `rclone config`: выберите **Amazon S3 Compliant Storage Providers**, затем **Ceph Object Storage**, и введите ключи и адрес.

## Работа с файлами

```bash
rclone lsd uzcloud:                          # list buckets
rclone ls uzcloud:my-bucket                  # list objects
rclone copy ./report.pdf uzcloud:my-bucket/docs/
rclone copy uzcloud:my-bucket/docs/ ./docs/  # download
rclone sync ./site uzcloud:my-bucket/site --progress
rclone delete uzcloud:my-bucket/tmp/
```

> [!WARNING]
> `rclone sync` делает получателя идентичным источнику и **удаляет** в получателе файлы, которых нет в источнике. Сначала проверьте результат с `--dry-run`.

## Подключение бакета как папки

```bash
mkdir -p ~/s3
rclone mount uzcloud:my-bucket ~/s3 --vfs-cache-mode writes --daemon
```

Чтобы отключить: `fusermount -u ~/s3` (Linux) или `umount ~/s3` (macOS).

## Перенос из другого облака

Добавьте второе подключение для исходного хранилища и скопируйте данные напрямую:

```bash
rclone copy old-cloud:source-bucket uzcloud:my-bucket --transfers 16 --progress
```

> [!TIP]
> **См. также:**
>
> - **[Инструменты и параметры подключения](overview.md)**
