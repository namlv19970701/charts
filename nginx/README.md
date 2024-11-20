# Deploy Nginx

NGINX requires certificate files (SSL/TLS certificates) when you want to set up HTTPS (secure HTTP) for a website or web application.
## Prerequisite
- ```cert-manager``` 

## Create namespace for Nginx
```
kubectl create namespace webservers
```

## Check k8s chart
```
helm template nginx nginx/ -n webservers > nginx.yaml
```

## Apply nginx chart 
```
kubectl apply -f nginx.yaml
```

## Apply ingress to call hostname instead of service ip
```
kubectl apply -f certificates/nginx.yaml
```

## Enable addons ingress in minikube
```
minikube addons enable ingress -p k8s-node
```

## Add host to your local machine
Check minikube ip
```
minikube ip -p k8s-node
```

Add host ```nginx.levietnam.local```
```
echo "<minikube_ip> nginx.levietnam.local" | sudo tee -a /etc/hosts > /dev/null
```


## Demo
![Alt text](/images/nginx.png)

