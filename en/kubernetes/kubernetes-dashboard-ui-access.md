# Kubernetes Dashboard UI Access

## Kubernetes Dashboard UI Access

**Kubernetes Dashboard** is a web-based UI that allows users to manage and monitor Kubernetes clusters through a visual interface. It supports deploying containerized applications, troubleshooting, and managing cluster resources.

---

### Run Proxy Locally

To access the dashboard, start the Kubernetes proxy service locally:

```bash
kubectl --kubeconfig /custom/path/kube.conf proxy
```

This will start a local server at `http://localhost:8001`.

### Open the Dashboard in Your Browser

Once the proxy is running, open the following URL in your browser to access the Kubernetes Dashboard:

```text
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

### Create a Token for Kubernetes Dashboard Login

Since Kubernetes **v1.24.0**, secret-based service account tokens are no longer generated automatically for security reasons. Create a long-lived Bearer Token for the dashboard service account:

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

### Retrieve the Token

Use the following command to retrieve the token for dashboard login:

```bash
kubectl --kubeconfig /custom/path/kube.conf describe secret $(kubectl --kubeconfig /custom/path/kube.conf get secrets -n kubernetes-dashboard | grep kubernetes-dashboard-token | awk '{print $1}') -n kubernetes-dashboard
```

### More Information

For more details on using and securing the Kubernetes Dashboard, refer to the official documentation:

🔗 [Accessing the Dashboard UI – Kubernetes Docs](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#accessing-the-dashboard-ui)

---

### Conclusion

By following this guide, you can securely access and manage your Kubernetes cluster using the Dashboard UI. Running the proxy locally, generating a service account token, and logging in via a secure browser interface gives you a convenient way to view and interact with your cluster resources.

> [!TIP]
> **See also:**
>
> - **[Create Kubernetes Cluster](create-kubernetes-cluster.md)**
> - **[Kubernetes Cluster CLI](kubernetes-cluster-via-cli.md)**
> - **[Manage Kubernetes Cluster](kubernetes-cluster-overview.md)**
