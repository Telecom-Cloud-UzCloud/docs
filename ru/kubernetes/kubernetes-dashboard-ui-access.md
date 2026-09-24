# Доступ к Kubernetes Dashboard

## Доступ к веб-интерфейсу Kubernetes Dashboard

**Kubernetes Dashboard** — веб-интерфейс для управления кластерами Kubernetes и их мониторинга. Он позволяет развертывать контейнерные приложения, диагностировать проблемы и управлять ресурсами кластера.

---

### Запуск прокси локально

Чтобы открыть Dashboard, запустите прокси Kubernetes на своем компьютере:

```bash
kubectl --kubeconfig /custom/path/kube.conf proxy
```

Будет запущен локальный сервер по адресу `http://localhost:8001`.

### Открытие Dashboard в браузере

После запуска прокси откройте в браузере следующий адрес:

```text
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

### Создание токена для входа в Kubernetes Dashboard

Начиная с Kubernetes **v1.24.0**, токены сервисных аккаунтов на основе секретов не создаются автоматически из соображений безопасности. Создайте долгосрочный Bearer-токен для сервисного аккаунта Dashboard:

```bash
kubectl --kubeconfig /custom/path/kube.conf apply -f - <<EOF
apiVersion: v1
kind: Secret
type: kubernetes.io/service-account-token
metadata:
  name: kubernetes-dashboard-token
  namespace: kubernetes-dashboard
  annotations:
    kubernetes.io/service-account.name: kubernetes-dashboard-admin-user
EOF
```

### Получение токена

Получите токен для входа в Dashboard командой:

```bash
kubectl --kubeconfig /custom/path/kube.conf describe secret $(kubectl --kubeconfig /custom/path/kube.conf get secrets -n kubernetes-dashboard | grep kubernetes-dashboard-token | awk '{print $1}') -n kubernetes-dashboard
```

### Дополнительная информация

Подробнее об использовании и защите Kubernetes Dashboard — в официальной документации:

🔗 [Accessing the Dashboard UI – Kubernetes Docs](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#accessing-the-dashboard-ui)

---

### Заключение

Следуя этому руководству, вы сможете безопасно работать с кластером Kubernetes через Dashboard. Локальный прокси, токен сервисного аккаунта и вход через браузер дают удобный способ просматривать ресурсы кластера и управлять ими.

> [!TIP]
> **См. также:**
>
> - **[Создание кластера Kubernetes](create-kubernetes-cluster.md)**
> - **[Кластер Kubernetes через CLI](kubernetes-cluster-via-cli.md)**
> - **[Управление кластером Kubernetes](kubernetes-cluster-overview.md)**
