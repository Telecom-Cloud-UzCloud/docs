# Kubernetes Dashboard’ga kirish

## Kubernetes Dashboard veb-interfeysiga kirish

**Kubernetes Dashboard** — Kubernetes klasterlarini boshqarish va monitoring qilish uchun veb-interfeys. U konteynerlashtirilgan ilovalarni joylashtirish, muammolarni tashxislash va klaster resurslarini boshqarish imkonini beradi.

---

### Proksini mahalliy ishga tushirish

Dashboard’ni ochish uchun kompyuteringizda Kubernetes proksisini ishga tushiring:

```bash
kubectl --kubeconfig /custom/path/kube.conf proxy
```

`http://localhost:8001` manzilida mahalliy server ishga tushadi.

### Dashboard’ni brauzerda ochish

Proksi ishga tushgach, brauzerda quyidagi manzilni oching:

```text
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

### Kubernetes Dashboard’ga kirish uchun token yaratish

Kubernetes **v1.24.0** dan boshlab xavfsizlik nuqtai nazaridan sekretlarga asoslangan xizmat akkaunti tokenlari avtomatik yaratilmaydi. Dashboard xizmat akkaunti uchun uzoq muddatli Bearer token yarating:

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

### Tokenni olish

Dashboard’ga kirish uchun tokenni quyidagi buyruq bilan oling:

```bash
kubectl --kubeconfig /custom/path/kube.conf describe secret $(kubectl --kubeconfig /custom/path/kube.conf get secrets -n kubernetes-dashboard | grep kubernetes-dashboard-token | awk '{print $1}') -n kubernetes-dashboard
```

### Qoʻshimcha maʼlumot

Kubernetes Dashboard’dan foydalanish va uni himoyalash haqida batafsil — rasmiy hujjatlarda:

🔗 [Accessing the Dashboard UI – Kubernetes Docs](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#accessing-the-dashboard-ui)

---

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz Kubernetes klasteri bilan Dashboard orqali xavfsiz ishlashingiz mumkin. Mahalliy proksi, xizmat akkaunti tokeni va brauzer orqali kirish klaster resurslarini koʻrish va boshqarishning qulay usulini taqdim etadi.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Kubernetes klasterini yaratish](create-kubernetes-cluster.md)**
> - **[CLI orqali Kubernetes klasteri](kubernetes-cluster-via-cli.md)**
> - **[Kubernetes klasterini boshqarish](kubernetes-cluster-overview.md)**
