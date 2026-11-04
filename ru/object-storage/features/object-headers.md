# Заголовки объектов

Каждый объект хранит HTTP-заголовки, которые возвращаются при его скачивании. Они сообщают браузеру, как показывать файл и сколько его кешировать. Также с объектом можно хранить собственные метаданные.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

| Заголовок | Что делает | Пример |
|---|---|---|
| `Content-Type` | Тип файла | `image/png`, `text/html; charset=utf-8` |
| `Cache-Control` | Кеширование в браузере и CDN | `public, max-age=86400` |
| `Content-Disposition` | Скачивание вместо открытия, имя файла | `attachment; filename="report.pdf"` |
| `Content-Encoding` | Сжатое содержимое | `gzip` |
| `x-amz-meta-*` | Собственные метаданные | `x-amz-meta-author: Demo` |

## Заголовки при загрузке

```bash
aws s3 cp ./logo.png s3://my-bucket/img/logo.png \
  --content-type image/png \
  --cache-control "public, max-age=31536000" \
  --metadata author=Demo
```

При загрузке папки AWS CLI определяет `Content-Type` автоматически по расширению файла. `Cache-Control` можно задать сразу для всех файлов:

```bash
aws s3 sync ./static s3://my-bucket/static/ --cache-control "public, max-age=86400"
```

## Просмотр заголовков

```bash
aws s3api head-object --bucket my-bucket --key img/logo.png
```

## Изменение заголовков существующего объекта

Заголовки нельзя изменить на месте. Скопируйте объект сам в себя с новыми заголовками:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source my-bucket/docs/report.pdf \
  --metadata-directive REPLACE \
  --content-type application/pdf \
  --content-disposition 'attachment; filename="report.pdf"'
```

> [!NOTE]
> С `--metadata-directive REPLACE` все заголовки и метаданные, которые вы не указали, сбрасываются. Перечислите в команде все нужные заголовки.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
