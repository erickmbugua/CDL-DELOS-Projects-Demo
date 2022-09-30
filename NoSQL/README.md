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
## Step 1: Build a mongoclient app using pymongo
1. Using pymongo, access the MongoDB client using the username, password and DB url specificed in the environment
2. Create a collection and insert two records into the collection

## step 2: Dockerize mongo-client app
1. The Dockerfiles in the MongoClient folder specifies how to dockerize both the mongoclient app
2. cd into Server folder and run:
```Console
$ docker build -t username/mongo-client .
$ docker push username/mongo-client
```
## step 2: Deploy mongodb
1. In the root folder run
```Console
$ kubectl create namespace mongodb
$ kubectl apply -n mongodb -f mongo-config.yaml
$ kubectl apply -n mongodb -f mongo-secret.yaml
$ kubectl apply -n mongodb -f mongo.yaml
$ kubectl apply -n mongodb -f mongo-service.yaml
```

## step 3: Deploy the mongo-client
1. In the root folder run
```Console
$ kubectl apply -n mongodb -f mongo-client.yaml
$ kubectl apply -n mongodb -f mongo-client-service.yaml
```

## step 4: Check that the client successfully inserts record into the collection
```Console
$ kubectl logs -n mongodb -f -l app=mongo-client
```
## Step 5: Clean up
$ kubectl delete ns mongodb