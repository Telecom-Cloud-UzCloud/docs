# Кластер Kubernetes через CLI

## Доступ к кластеру Kubernetes через CLI

**Доступ к Kubernetes через CLI** позволяет работать с кластером прямо из терминала с помощью `kubectl`. Это удобно для просмотра, управления и диагностики ресурсов в облачной среде **UzCloud**.

---

### Загрузка kubeconfig кластера

Утилита командной строки `kubectl` использует файлы kubeconfig, чтобы определить кластер и подключиться к его API-серверу.

- Откройте кластер на странице **Kubernetes** и нажмите **Download Config**, чтобы скачать файл kubeconfig.

### Загрузка kubectl

Скачайте `kubectl` той же версии, что и Kubernetes в вашем кластере (ссылки ниже — для v1.27.3; если версия кластера другая, замените ее в URL):

- **Linux**: [Скачать](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/linux/amd64/kubectl)
- **macOS**: [Скачать](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/darwin/amd64/kubectl)
- **Windows**: [Скачать](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/windows/amd64/kubectl.exe)

### Использование kubectl с файлом kubeconfig

Теперь можно выполнять команды `kubectl`, указывая скачанный файл kubeconfig.

```bash
kubectl --kubeconfig /custom/path/kube.conf {COMMAND}
```

- **Список подов:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get pods --all-namespaces
```

- **Список узлов:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get nodes --all-namespaces
```

- **Список сервисов:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get services --all-namespaces
```

---

### Заключение

Следуя этому руководству, вы сможете настроить `kubectl` и управлять кластерами Kubernetes в UzCloud. Это мощный и гибкий способ работать с ресурсами кластера прямо из терминала.

> [!TIP]
> **См. также:**
>
> - **[Создание кластера Kubernetes](create-kubernetes-cluster.md)**
> - **[Управление кластером Kubernetes](kubernetes-cluster-overview.md)**
> - **[Доступ к Kubernetes Dashboard](kubernetes-dashboard-ui-access.md)**
