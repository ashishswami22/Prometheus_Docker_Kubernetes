# Prometheus_Docker_Kubernetes
demo application

## There are two applications in this repository which can run in containers. To build container images, you can follow below steps:

- cd ./target-app
- docker image build -t target-app:1.0 .
- cd ../prometheus
- docker image build -t prometheus:1.0 .

## NOTE: If you are using minicube, make sure you run the below command before building the images:
- eval $(minikube docker-env)

this command points local docker environment to minikube. Without this step, the local images will not be available during the deployment within the minikube vm.

## You can deploy both the containers manually using docker command as follows:

- docker container run --publish 8080:5000 --detach --name target-app target-app:1.0
- docker container run --publish 8081:9090 --detach --name prom prometheus:1.0

## OR, you can deploy them on a kubernetes cluster using the kubernetes deployment configuration file.

- kubectl create -f kube-deploy.yml
