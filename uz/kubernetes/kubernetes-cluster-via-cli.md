# CLI orqali Kubernetes klasteri

## Kubernetes klasteriga CLI orqali kirish

**Kubernetes’ga CLI orqali kirish** `kubectl` yordamida klaster bilan bevosita terminaldan ishlash imkonini beradi. Bu **UzCloud** bulut muhitidagi resurslarni koʻrish, boshqarish va tashxislash uchun qulay.

---

### Klaster kubeconfig faylini yuklab olish

`kubectl` buyruqlar satri vositasi klasterni aniqlash va uning API serveriga ulanish uchun kubeconfig fayllaridan foydalanadi.

- **Kubernetes** sahifasida klasterni oching va kubeconfig faylini yuklab olish uchun **Download Config** tugmasini bosing.

### kubectl’ni yuklab olish

Klasteringizdagi Kubernetes versiyasiga mos `kubectl` ni yuklab oling (quyidagi havolalar v1.27.3 uchun; klaster versiyasi boshqacha boʻlsa, URL’dagi versiyani almashtiring):

- **Linux**: [Yuklab olish](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/linux/amd64/kubectl)
- **macOS**: [Yuklab olish](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/darwin/amd64/kubectl)
- **Windows**: [Yuklab olish](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/windows/amd64/kubectl.exe)

### kubectl’dan kubeconfig fayli bilan foydalanish

Endi yuklab olingan kubeconfig faylini koʻrsatib, `kubectl` buyruqlarini bajarishingiz mumkin.

```bash
kubectl --kubeconfig /custom/path/kube.conf {COMMAND}
```

- **Podlar roʻyxati:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get pods --all-namespaces
```

- **Tugunlar roʻyxati:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get nodes --all-namespaces
```

- **Xizmatlar roʻyxati:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get services --all-namespaces
```

---

### Xulosa

Ushbu qoʻllanmaga amal qilib, siz `kubectl` ni sozlashingiz va UzCloud’dagi Kubernetes klasterlarini boshqarishingiz mumkin. Bu klaster resurslari bilan bevosita terminaldan ishlashning kuchli va moslashuvchan usuli.

> [!TIP]
> **Shuningdek qarang:**
>
> - **[Kubernetes klasterini yaratish](create-kubernetes-cluster.md)**
> - **[Kubernetes klasterini boshqarish](kubernetes-cluster-overview.md)**
> - **[Kubernetes Dashboard’ga kirish](kubernetes-dashboard-ui-access.md)**
