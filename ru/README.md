# Документация UzCloud

Руководство пользователя консоли управления облаком UzCloud — **[console.uzcloud.uz](https://console.uzcloud.uz)**.

Другие языки: [English](../en/README.md) · [Oʻzbekcha](../uz/README.md)

## Содержание

### Начало работы

- [Введение](getting-started/introduction.md)
- [Регистрация аккаунта](getting-started/account-signup.md)
- [Настройка профиля](getting-started/profile-setup.md)

### Проекты

- [Создание проекта](projects/create-project.md)

### Вычисления

- [Виртуальная машина](compute/compute-instance.md)
- [Обзор виртуальной машины](compute/instance-overview.md)
- [Мониторинг ресурсов](compute/monitoring-resources.md)
- **Настройки ВМ**
  - [Блочное хранилище](compute/vm-settings/block-storage.md)
  - [Смена тарифного плана](compute/vm-settings/change-plan.md)
  - [Изменение имени хоста](compute/vm-settings/change-hostname.md)
  - [Смена ОС](compute/vm-settings/change-os.md)
  - [Изменение скрипта запуска](compute/vm-settings/change-startup-script.md)
  - [Межсетевой экран](compute/vm-settings/firewall.md)
  - [Проброс портов](compute/vm-settings/port-forwarding.md)
  - [Сети](compute/vm-settings/networks.md)
  - [SSH-ключи](compute/vm-settings/ssh-keys.md)
- [Доступ к консоли](compute/console-access.md)
- [Резервные копии ВМ](compute/instance-backups.md)
- [Журнал активности ВМ](compute/vm-activity-logs.md)
- [Подключение по SSH](compute/connect-with-ssh.md)
- [Подключение по RDP](compute/connect-with-rdp.md)

### Тома

- [Создание тома](volumes/create-volume.md)

### Снимки томов

- [Создание снимка тома](volume-snapshots/create-volume-snapshot.md)

### Снимки ВМ

- [Создание снимка ВМ](vm-snapshots/create-instance-snapshot.md)

### Резервные копии

- [Создание резервных копий](backups/create-backups.md)

### Шаблоны

- [Создание шаблонов](templates/create-templates.md)

### ISO-образы

- [Импорт ISO](isos/import-iso.md)

### Группы привязки

- [Создание групп привязки](affinity-groups/create-affinity-groups.md)

### Veeam Backup

- [Veeam Backup](veeam-backup/create-veeam-backup.md)
- [Управление Veeam Backup](veeam-backup/manage-veeam-backup.md)

### Kubernetes

- [Создание кластера Kubernetes](kubernetes/create-kubernetes-cluster.md)
- [Обзор кластера Kubernetes](kubernetes/kubernetes-cluster-overview.md)
- [Кластер Kubernetes через CLI](kubernetes/kubernetes-cluster-via-cli.md)
- [Доступ к Kubernetes Dashboard](kubernetes/kubernetes-dashboard-ui-access.md)

### Автомасштабирование

- [Создание автомасштабирования](auto-scaling/create-auto-scaling.md)

### Объектное хранилище (Ceph)

- [Создание объектного хранилища](object-storage/create-object-storage.md)
- [Управление объектным хранилищем](object-storage/manage-object-storage.md)

### Сети

- **VPC-сеть**
  - [Создание VPC-сетей](networks/vpc-network/create-vpc-network.md)
  - [Обзор сети](networks/vpc-network/network-overview.md)
  - [Добавление сети](networks/vpc-network/add-network.md)
  - [Публичный IP-адрес](networks/vpc-network/public-ip-address.md)
  - [Список сетевых ACL](networks/vpc-network/network-acl-list.md)
  - [VPN-шлюз](networks/vpc-network/vpn-gateway.md)
  - [VPN-соединения](networks/vpc-network/vpn-connections.md)
  - [Связанные ВМ](networks/vpc-network/associated-vms.md)
- **Публичная сеть**
  - [Создание публичной сети](networks/public-network/create-public-network.md)
  - [Обзор сети](networks/public-network/network-overview.md)
  - [Правила исходящего трафика](networks/public-network/egress-rules.md)
  - [Публичные IP-адреса](networks/public-network/public-ip-addresses.md)
  - [Связанные ВМ](networks/public-network/associated-vms.md)
- [Публичный IP-адрес](networks/public-ip-address.md)
- [Пользователи VPN](networks/vpn-users.md)
- [Клиентский VPN-шлюз](networks/vpn-customer-gateway.md)

### Балансировщик нагрузки

- [Балансировщик нагрузки](load-balancer/load-balancer.md)

### DNS

- [Создание DNS](dns/create-dns.md)
- [Управление DNS](dns/manage-dns.md)

### VNF-устройства

- [VNF-устройства](vnf-appliances/vnf-appliances.md)

### Биллинг

- [Сводка по биллингу](billing/billing-summary.md)
- [Подписки](billing/subscriptions.md)
- [Способы оплаты](billing/payment-methods.md)
- [Транзакции](billing/transactions.md)
- [Выписка по аккаунту](billing/account-statement.md)

### Поддержка

- [Поддержка](support/support.md)
