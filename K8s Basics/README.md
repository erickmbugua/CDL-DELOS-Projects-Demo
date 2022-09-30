# K8s Basics

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
## Step 1: Build server-client app using python socket module
1. Create a server that listens to a port that will be provided as an environment variable on kubernetes config files.
2. Create a client that connects to the server's address and port as specificed in the environment variables

## Step 2: Dockerize server-client app
1. The Dockerfiles in the Server and Client folders specify how to dockerize both the server and client
2. cd into Server folder and run:
```Console
$ docker build -t username/server .
$ docker push username/server
```
3. cd into Client folder and run:
```Console
$ docker build . -t username/client
$ docker push username/client
```
## Step 3: Create k8s deployments and services for the server and client
1. Deploy the server and client in different pods and create a service for each so that they can communicate
```Console
$ kubectl create namespace server-client
$ kubectl apply -n server-client -f server.yaml
$ kubectl apply -n server-client -f server-service.yaml
$ kubectl apply -n server-client -f client.yaml
$ kubectl apply -n server-client -f client-service.yaml
$ kubectl apply -n server-client -f average-time.yaml
```
1. To see the communication between the server and client. Run the following two commands on different terminals
```Console
$ kubectl logs -n server-client -f -l app=server
$ kubectl logs -n server-client -f -l app=client
```

## Step 4: Delete Resources
1. Run
```console
$ kubectl delete ns server-client
```
### Comments
For the configmap file with the average time between sending two messages between the two pods, I could not figure out how to write to the configmap file programmatically while the files have been applied since after writing to the configmap file, I would have to somehow rerun 
```Console
$ kubectl apply -n server-client -f average-time.yaml
```

## DEMO

https://user-images.githubusercontent.com/23630122/193200457-651e0b3a-db27-4f88-84f1-a24a86638ef3.mp4



