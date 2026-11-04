# s3fs

**s3fs** подключает бакет как папку в Linux. После этого приложения могут читать и записывать объекты как обычные файлы.

> [!WARNING]
> Подключенный бакет — не настоящий диск: операции выполняются медленнее, а файл при каждом изменении перезаписывается целиком. Не используйте s3fs для баз данных и приложений, которые часто меняют файлы. Он хорошо подходит для архивов, медиафайлов и резервных копий.

## Установка

```bash
sudo apt install s3fs          # Ubuntu, Debian
sudo dnf install s3fs-fuse     # Rocky Linux, AlmaLinux (EPEL)
```

## Настройка

Сохраните ключи в файл и ограничьте к нему доступ:

```bash
echo "<Access Key>:<Secret Key>" | sudo tee /etc/passwd-s3fs
sudo chmod 600 /etc/passwd-s3fs
```

## Подключение бакета

```bash
sudo mkdir -p /mnt/s3
sudo s3fs my-bucket /mnt/s3 \
  -o passwd_file=/etc/passwd-s3fs \
  -o url=https://s3.uzcstorage.uz \
  -o use_path_request_style \
  -o allow_other
```

Проверьте, что бакет подключен:

```bash
df -h /mnt/s3 && ls /mnt/s3
```

## Подключение при загрузке

Добавьте строку в `/etc/fstab`:

```text
my-bucket /mnt/s3 fuse.s3fs _netdev,allow_other,use_path_request_style,url=https://s3.uzcstorage.uz,passwd_file=/etc/passwd-s3fs 0 0
```

Проверьте запись без перезагрузки: `sudo mount -a`. Чтобы отключить: `sudo umount /mnt/s3`.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
