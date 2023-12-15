# Kubernetes Autoscaling

For more information to the different Kubernetes components, refer to our dedicated blog post: An introduction to Kubernetes Horizontal vs. Vertical Scaling
	    Horizontal 	            Vertical
Pod 	Adds or removes Pods 	Modifies CPU and/or RAM resources allocated to the Pod
Node 	Adds or removes Nodes 	Modifies CPU and/or RAM resources allocated to the Node


Horizontal Scaling means modifying the compute resources of an existing cluster, for example, by adding new nodes to it or by adding new pods by increasing the replica count of pods (Horizontal Pod Autoscaler).
Vertical Scaling means to modify the attributed resources (like CPU or RAM) of each node in the cluster. In most cases, this means creating an entirely new node pool using machines that have different hardware configurations. Vertical scaling on pods means dynamically adjusting the resource requests and limits based on the current application requirements (Vertical Pod Autoscaler). 

https://blog.scaleway.com/understanding-kubernetes-autoscaling/


## Horizontal Pod Autoscaling

HPA allows us to scale pods when their resource utilisation goes over a threshold.

For all autoscaling guides, we'll need a simple app, that generates some CPU load. We will use aimvector/application-cpu:v1.0.0 from dockerhub.

### Configure resource requirements in deployment.yaml

The settings here depend on the size of your VM (1 CPU core=1000m).
```bash
resources:
  requests:
    memory: "50Mi"
    cpu: "500m"
  limits:
    memory: "500Mi"
    cpu: "2000m"
```

### Deploy 
```bash
kubectl apply -f deployment.yaml
```

### Get metrics
```bash
kubectl top pods
```

## Cluster Autoscaler

For cluster autoscaling, you should be able to scale the pods manually and watch the cluster scale. 

### Generate some traffic

For traffic generation, we use [wrk](https://github.com/wg/wrk). Let's deploy a simple traffic generator pod:

```bash
kubectl apply -f traffic-generator.yaml

# get a terminal to the traffic-generator
kubectl exec -it traffic-generator sh

# install wrk
apk add --no-cache wrk

# simulate some load
wrk -c 5 -t 5 -d 99999 -H "Connection: Close" http://application-cpu

#you can scale to pods manually and see roughly 6-7 pods will satisfy resource requests.
kubectl scale deploy/application-cpu --replicas 2
```

## Deploy an autoscaler

```bash
# scale the deployment back down to 2
kubectl scale deploy/application-cpu --replicas 2

# deploy the autoscaler
kubectl autoscale deploy/application-cpu --cpu-percent=95 --min=1 --max=10

# pods should scale to roughly 6-7 to match criteria of 95% of resource requests
kubectl get pods
kubectl top pods
kubectl get hpa/application-cpu  -owide

kubectl describe hpa/application-cpu 
```



Credits:
https://github.com/marcel-dempers/docker-development-youtube-series/tree/master/kubernetes/autoscaling
https://www.youtube.com/watch?v=jM36M39MA3I
https://www.youtube.com/watch?v=FfDI08sgrYY




