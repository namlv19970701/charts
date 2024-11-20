# Deploy Postgress

## Create namespace for Postgresql
```
kubectl create namespace datatbase
```

## Check k8s chart
```
helm template postgesql postgresql/ -n database > postgresql.yaml
```

## Apply rancher chart 
```
kubectl apply -f postgresql.yaml
```