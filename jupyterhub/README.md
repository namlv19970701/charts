# Deploy Jupyterhub

## Create namespace for Jupyterhub
```
kubectl create namespace analytics
```

## Check k8s chart
```
helm template jupyterhub jupyterhub/ -n analytics > jupyterhub.yaml
```

## Apply jupyterhub chart 
```
kubectl apply -f jupyterhub.yaml
```

## Apply ingress to call hostname instead of service ip
```
kubectl apply -f certificates/jupyterhub.yaml
```

## Enable addons ingress in minikube
```
minikube addons enable ingress -p k8s-node
```

## Add host to your local machine
Check minikube ip
```minikube ip -p node
```

Add host ```jupyterhub.levietnam.local```
```
echo "<minikube_ip> jupyterhub.levietnam.local" | sudo tee -a /etc/hosts > /dev/null
```


## Demo
![Alt text](/images/jupyterhub.png)

