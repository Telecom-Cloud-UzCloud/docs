# Kubernetes Cluster via CLI

## Accessing Kubernetes Cluster via CLI

**Kubernetes CLI access** allows you to interact with your cluster directly from the terminal using `kubectl`. This is useful for inspecting, managing, and troubleshooting resources running in your cloud environment via **UzCloud**.

---

### Download Kubeconfig for the Cluster

The `kubectl` command-line tool uses kubeconfig files to find the information it needs to choose a cluster and communicate with the API server of a cluster.

- Open your cluster on the **Kubernetes** page and click **Download Config** to download the kubeconfig file.

### Download kubectl Tool

Download the `kubectl` binary matching your cluster's Kubernetes version (the links below are for v1.27.3; replace the version in the URL if your cluster runs a different one):

- **Linux**: [Download](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/linux/amd64/kubectl)
- **macOS**: [Download](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/darwin/amd64/kubectl)
- **Windows**: [Download](https://storage.googleapis.com/kubernetes-release/release/v1.27.3/bin/windows/amd64/kubectl.exe)

### Use kubectl With Your Kubeconfig File

You can now run `kubectl` commands using your downloaded kubeconfig file.

```bash
kubectl --kubeconfig /custom/path/kube.conf {COMMAND}
```

- **List Pods:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get pods --all-namespaces
```

- **List Nodes:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get nodes --all-namespaces
```

- **List Services:**

```bash
kubectl --kubeconfig /custom/path/kube.conf get services --all-namespaces
```

---

### Conclusion

By following this guide, you can set up and use the `kubectl` CLI to manage your Kubernetes clusters via UzCloud. This method provides a powerful and flexible way to interact with cluster resources directly from your terminal.

> [!TIP]
> **See also:**
>
> - **[Create Kubernetes Cluster](create-kubernetes-cluster.md)**
> - **[Manage Kubernetes Cluster](kubernetes-cluster-overview.md)**
> - **[Kubernetes Cluster UI Access](kubernetes-dashboard-ui-access.md)**
