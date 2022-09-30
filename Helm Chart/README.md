# Helm Chart

## Requirements
1. Dockerhub Account
2. Minikube ([link](https://minikube.sigs.k8s.io/docs/start/))
3. kubectl ([link](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/))

## Step 0: Setup Minikube Environment
1. start minikube cluster on a virtual machine
```console
$ minikube start
```
2. log into your dockerhub account, and enter your credentials
```console 
$ docker login
```
## Step 1: Install ingress-nginx and tunnel through minikube
```Console
$ minikube tunnel
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.1/deploy/static/provider/cloud/deploy.yaml
```
## Step 2: Dockerize FastApi app
1. The Dockerfiles in the FastApi folder specifies how to dockerize the FastApi app
2. cd into FastApi folder and run:
```Console
$ docker build -t username/fastapi .
$ docker push username/fastapi
```
## Step 3: Deploy the FastApi app as well as Ingress
1. In the root folder run
```Console
$ kubectl create namespace fastapi
$ kubectl apply -n fastapi -f fastapi.yaml
$ kubectl apply -n fastapi -f fastapi-ingress.yaml
```
## Step 4: Ping the url
1. In your browser type
```Console
$ http://kubernetes.docker.internal/initiate
```
2. You will see "Microservice has been started successfully"

## step 4: CleanUp
```Console
$ kubectl delete ns fastapi
```
## Step 5: Install helm chart with prometheus subchart
```console
$ helm install helm-chart helmchart/ --values helmchart/values.yaml
```

https://user-images.githubusercontent.com/23630122/193200842-25b0ba14-5e1c-4840-a2e6-4ac7df85da8a.mp4


