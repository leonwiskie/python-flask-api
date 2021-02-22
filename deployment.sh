#!/bin/bash
echo 'Interact with minikube docker'
eval $(minikube docker-env)
echo 'build docker images'
docker build -t facturen-api:v1 facturen/.
docker build -t debiteuren-api:v1 debiteuren/.
docker build -t rekenmodule-api:v1 rekenmodule/.
docker build -t proxy-api:v1 proxy/.

echo 'Set Context use minikube'
kubectl config use-context minikube

echo 'Remove running pods'
kubectl delete pod,service webserver --namespace ontwikkel
echo 'Create pods - Deployment'
#kubectl create deployment webserver --image message-api:v1 --namespace=ontwikkel -o yaml > pod.yaml
echo 'Apply deployment'
kubectl apply -f pod.yaml
echo 'Create Service'
#kubectl expose deployment webserver --type=LoadBalancer --port=5000 --namespace=ontwikkel -o yaml > service.yaml
echo 'Access Service'
#minikube service webserver -n ontwikkel
echo 'Scaling up!'
#kubectl scale --current-replicas=1 --replicas=3 webserver --namespace=ontwikkel


#kubectl set image deployment/webserver www=message-api:v1  