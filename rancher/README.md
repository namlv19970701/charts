# Deploy Rancher

NGINX requires certificate files (SSL/TLS certificates) when you want to set up HTTPS (secure HTTP) for a website or web application.
## Prerequisite
- ```cert-manager``` 

## Create namespace for Rancher
The resources created by the Chart should be installed. This should always be cattle-system:
```
kubectl create namespace cattle-system
```

## Check k8s chart
```
helm template rancher rancher/ -n cattle-system > rancher.yaml
```

## Apply rancher chart 
```
kubectl apply -f rancher.yaml
```

## Apply ingress to call hostname instead of service ip
```
kubectl apply -f certificates/rancher.yaml
```

## Enable addons ingress in minikube
```
minikube addons enable ingress -p k8s-node
```

## Add host to your local machine
Check minikube ip
```minikube ip -p k8s-node
```

Add host ```rancher.levietnam.local```
```
echo "<minikube_ip> rancher.levietnam.local" | sudo tee -a /etc/hosts > /dev/null
```


## Demo
![Alt text](images/rancher.png)

