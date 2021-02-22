https://kubernetes.io/docs/reference/kubectl/cheatsheet/

## Use 
in eerste instantie een pod.yaml maken met 
docker build -t message-api:v1 .

maken van een manifestfile
kubectl create deployment webserver --image message-api:v1 --namespace=ontwikkel --dry-run=client -o yaml > pod.yaml

skaffold init 
skaffold run 


## voorbeeld
https://dev.to/alissonzampietro/the-amazing-journey-of-docker-compose-17lj


## deel 2
Met een reverse proxy Nginx 
https://dev.to/sukhbirsekhon/what-is-docker-reverse-proxy-45mm