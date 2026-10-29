# CLI orqali Kubernetes klasteri

## Kubernetes klasteriga CLI orqali kirish

**Kubernetes’ga CLI orqali kirish** `kubectl` yordamida klaster bilan bevosita terminaldan ishlash imkonini beradi. Bu **UzCloud** bulut muhitidagi resurslarni koʻrish, boshqarish va tashxislash uchun qulay.

---

### Klaster kubeconfig faylini yuklab olish

`kubectl` buyruqlar satri vositasi klasterni aniqlash va uning API serveriga ulanish uchun kubeconfig fayllaridan foydalanadi.

- **Kubernetes** sahifasida klasterni oching va holat satridagi **Download config file** tugmasini bosing yoki **Access** yorligʻiga oʻting va **Download Kubernetes cluster config** ni bosing.
- **Access** yorligʻida ushbu koʻrsatma klasteringizning Kubernetes versiyasi uchun havolalar va buyruqlar bilan ham keltirilgan.

### kubectl’ni yuklab olish

Klasteringizdagi Kubernetes versiyasiga mos `kubectl` ni yuklab oling (quyidagi havolalar v1.36.0 uchun; klaster versiyasi boshqacha boʻlsa, URL’dagi versiyani almashtiring):

- **Linux**: [Yuklab olish](https://dl.k8s.io/release/v1.36.0/bin/linux/amd64/kubectl)
- **macOS**: [Yuklab olish](https://dl.k8s.io/release/v1.36.0/bin/darwin/amd64/kubectl)
- **Windows**: [Yuklab olish](https://dl.k8s.io/release/v1.36.0/bin/windows/amd64/kubectl.exe)

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
