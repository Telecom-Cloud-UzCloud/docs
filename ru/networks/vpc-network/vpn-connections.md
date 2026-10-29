# VPN-соединения

## VPN-соединения

VPN-соединение «сеть — сеть» связывает VPC с удаленной сетью через клиентский VPN-шлюз.

- На странице VPC откройте вкладку **VPN Connections**. На ней перечислены VPN-соединения VPC.
- Нажмите **+ Create Site To Site VPN**.

![VPN-соединения](../../../images/vpc-net-10.png)

- В окне **Create VPN Connection** выберите клиентский шлюз в поле **VPN Customer Gateway** или создайте новый с помощью **+ Create Customer Gateway**.
- Отметьте **Passive**, если соединение должна инициировать удаленная сторона.
- Нажмите **Submit**.

![Создание VPN-соединения](../../../images/vpc-net-11.png)

### Заключение

Вкладка **VPN Connections** позволяет настраивать защищенные VPN-соединения «сеть — сеть» между VPC и внешними сетями и управлять ими.

> [!TIP]
> **См. также:**
>
> - **[Обзор VPC-сети](network-overview.md)**
> - **[Список сетевых ACL](network-acl-list.md)**
> - **[VPN-шлюз](vpn-gateway.md)**
> - **[Клиентский VPN-шлюз](../vpn-customer-gateway.md)**
