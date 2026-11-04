# Cyberduck

**Cyberduck** — бесплатный графический файловый менеджер для macOS и Windows. В нем можно просматривать бакеты, загружать и скачивать файлы перетаскиванием.

## Установка

Скачайте Cyberduck с [cyberduck.io](https://cyberduck.io/download/) и установите.

## Включение адресации path-style

Объектное хранилище UzCloud использует адреса path-style. Для них в Cyberduck есть отдельный профиль подключения:

1. Откройте **Preferences → Profiles** (в Windows — **Edit → Preferences → Profiles**).
2. Найдите **S3 (Deprecated path style requests)** и отметьте его флажком.
3. Перезапустите Cyberduck.

## Подключение

1. Нажмите **Open Connection**.
2. В списке протоколов выберите **S3 (Deprecated path style requests)**.
3. **Server**: `s3.uzcstorage.uz`, **Port**: `443`.
4. Введите **Access Key ID** и **Secret Access Key**.
5. Нажмите **Connect**. Откроется список ваших бакетов.

Чтобы сохранить подключение, создайте закладку **Bookmark → New Bookmark** с теми же параметрами.

## Полезные возможности

- Пункт **Share** в контекстном меню файла создает временную ссылку (presigned URL).
- **Info** показывает метаданные объекта и позволяет менять заголовки, например `Cache-Control`.

> [!TIP]
> **См. также:**
>
> - **[Инструменты и параметры подключения](overview.md)**
