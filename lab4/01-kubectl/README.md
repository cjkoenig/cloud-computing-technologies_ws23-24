### K3s Setup and Cluster Control

## Step 1: K3s and Cluster Setup

Local installation of k3sup and kubectl:
```bash
curl -sLS https://get.k3sup.dev | sh
sudo install k3sup /usr/local/bin/

# test
k3sup --help

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# test
kubectl version --client
```


Remote installation of K3s cluster:
```bash
export IP=<IP of VM>
# exchange ssh keys for login
ssh-copy-id azureuser@$IP
k3sup install --ip=$IP --k3s-channel=stable --user azureuser
```

You have to export the KUBECONFIG line as environment variable to let kubectl access the remote cluster. Further, you have to open port 6443 for incoming TCP traffic in the VM.

Let's check the cluster:
```bash
kubectl get node -o wide
```

Now we deploy a pod to our cluster:
```bash
kubectl apply -f 01a-pod/pod.yaml
kubectl logs myapp-pod
kubectl get po -w
kubectl delete po myapp-pod
```

This pod is restarted from K8s over and over...let's move on to the next step.

## Step 2: Deploy a Web-Application

Create a deployment of nginx:

``` bash
kubectl create deploy nginx --image=nginx:1.22-alpine
kubectl get deploy
kubectl get replicaset
kubectl get po
```

Describe the pod and look at the image:

``` bash
kubectl describe po/<pod name>
kubectl get po/<pod name> -o yaml | less
```

Scale the Deployment manually:

``` bash
kubectl scale deploy/nginx --replicas=3
kubectl rollout status deploy/nginx
kubectl get deploy
kubectl get po
```

What happens if we upgrade with a bad image?

``` bash
kubectl set image deploy/nginx nginx=nginx:1.23-alpne
kubectl rollout status deploy/nginx
kubectl get po
```

We can edit/fix it or redo the upgrade from the manifest.

``` bash
kubectl edit deploy/nginx
kubectl rollout undo deploy/nginx
```

### ConfigMaps

ConfigMaps allow us to override data within the container.

``` bash
kubectl exec -it <pod-name> -- ash
cat /usr/share/nginx/html/index.html
```

We can see that the HTML file is the default. We can override this directory with a ConfigMap

``` bash
cd 01b-deployment/base
cat configs/index.html
cat deployment.yaml  # how is the ConfigMap created?
```

Create a DNS name for your VM and change it in `overlay/development/ingress.yaml`. Then use the tool called Kustomize, built into `kubectl`, can assemble all of this from templates.

``` bash
cd 01b-deployment
cat kustomization.yaml
kubectl apply -k .
```

Forward the service to your local machine, e.g., the dev deployment:

```bash
kubectl port-forward dev-nginx-75b5d7cd66-84k7m 8080:80
```
Now you can access the container in the cluster on localhost:8080.


Credits:
https://github.com/rancher/k8s-intro-training
https://www.youtube.com/watch?v=5h1TCrh_hZ0
