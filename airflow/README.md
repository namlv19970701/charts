# Deploy Airflow

## Create namespace for Airflow
```
kubectl create namespace analytics
```

## Check k8s chart
```
helm template airflow airflow/ -n analytics > airflow.yaml
```

## Apply airflow chart 
```
kubectl apply -f airflow.yaml
```

## Apply ingress to call hostname instead of service ip
```
kubectl apply -f certificates/airflow.yaml
```

## Enable addons ingress in minikube
```
minikube addons enable ingress -p k8s-node
```

## Add host to your local machine
Check minikube ip
```minikube ip -p node
```

Add host ```airflow.levietnam.local```
```
echo "<minikube_ip> airflow.levietnam.local" | sudo tee -a /etc/hosts > /dev/null
```


## Demo
![Alt text](/images/airflow.png)

