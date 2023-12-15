### A Dashboard for the K3s Cluster

Now we install the K8s dashboard into our cluster:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

Then, we have to create an admin-user and set the role for him:

```bash
kubectl create -f dashboard.admin-user.yaml -f dashboard.admin-user-role.yaml
```

Finally, we have to create a token for UI access:

```bash
kubectl -n kubernetes-dashboard create token admin-user
```

Let's open a tunnel to the cluster:

```bash
kubectl proxy
```

And access the dashboard under this URL: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

To delete the user and role:
```bash
kubectl -n kubernetes-dashboard delete serviceaccount admin-user
kubectl -n kubernetes-dashboard delete clusterrolebinding admin-user
```