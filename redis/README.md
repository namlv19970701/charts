# Deploy Redis

## Create namespace for Postgresql
```
kubectl create namespace datatbase
```

## Check k8s chart
```
helm template redis redis/ -n database > redis.yaml
```

## Apply rancher chart 
```
kubectl apply -f redis.yaml
```