# Версионирование объектов

Если версионирование включено, бакет хранит все версии объекта. Если файл по ошибке перезаписали или удалили, можно восстановить предыдущую версию.

В примерах используется **[AWS CLI](../tools/aws-cli.md)**, настроенный для UzCloud. Замените `my-bucket` на имя своего бакета.

## Включение версионирования

**В консоли:** включите **Bucket Versioning** при создании бакета. См. **[Управление объектным хранилищем](../../object-storage/manage-object-storage.md)**.

**Через AWS CLI:**

```bash
aws s3api put-bucket-versioning --bucket my-bucket \
  --versioning-configuration Status=Enabled

# check the status
aws s3api get-bucket-versioning --bucket my-bucket
```

Версионирование нельзя выключить полностью, только приостановить (`Status=Suspended`). Уже созданные версии сохраняются.

## Просмотр версий

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf
```

У каждой версии есть `VersionId`. У текущей версии `"IsLatest": true`.

## Восстановление версии

Скачайте нужную версию:

```bash
aws s3api get-object --bucket my-bucket --key docs/report.pdf \
  --version-id <VersionId> report-old.pdf
```

Или снова сделайте ее текущей, скопировав поверх объекта:

```bash
aws s3api copy-object --bucket my-bucket --key docs/report.pdf \
  --copy-source "my-bucket/docs/report.pdf?versionId=<VersionId>"
```

## Восстановление удаленного объекта

В бакете с версионированием удаление объекта только добавляет **маркер удаления** (delete marker). Чтобы восстановить объект, удалите маркер:

```bash
aws s3api list-object-versions --bucket my-bucket --prefix docs/report.pdf \
  --query 'DeleteMarkers[?IsLatest].VersionId'

aws s3api delete-object --bucket my-bucket --key docs/report.pdf \
  --version-id <delete-marker-VersionId>
```

> [!NOTE]
> Все версии занимают место и оплачиваются. Чтобы ограничить число хранимых версий, настройте **[правило жизненного цикла](lifecycle.md)**, которое удаляет старые версии.

> [!TIP]
> **См. также:**
>
> - **[Параметры подключения](../connection.md)**
