    kubectl create namespace database
    kubectl apply -f mysql-statefulset.yaml

    kubectl create namespace backend
    docker build -t product-service:v1 car-store/product-service
    minikube image load product-service:v1

Run this one in Bash!:

    kubectl get secret mysql-secret -n database -o yaml | sed 's/namespace: database/namespace: backend/' | kubectl apply -f -
then:

    kubectl apply -f car-store/product-service/product-deployment.yaml
