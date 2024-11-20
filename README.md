# Charts
In progress...

## Prerequisite
- Ubuntu
- Kubectl
- Minikube

## Create k8s cluster via Minikube 
To install ```minikube``` and ```kubectl```, please watch these following links:
- Kubectl: https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
- Minikube: https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download

### Start K8s cluster
```
minikube start -p k8s-node  -n 2 --cpus=6 --memory=7000
```

### Set up network routes to enable services running in the Minikube cluster to be accessed externally
```
minikube tunnel -p k8s-node
```

### Checkout k8s cluster via UI
```
minikube dashboard -p k8s-node
```

### Demo
https://www.youtube.com/watch?v=nJVRJt4G-l0

### Deploy
- rancher [here](rancher)
