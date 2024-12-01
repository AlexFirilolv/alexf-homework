Bar Ilan DevSecOps 16,
solution to Lab3 as part of Hudi's assignments.

Set up:

    We'll be using Minikube inorder to complete and test the assignment.

    create all relevant namespaces:

        kubectl create namespace frontend
        kubectl create namespace backend

    Create docker image locally for the 'flask-backend' applicaton:

        docker build -t flask-backend flask-backend/.
        (Or CD into the folder and run docker build -t flask-backend:v1 .)
        
        !Important: Load the image into the minikube enviornment:
            minikube image load flask-backend:v1

    deploy all deployments (make sure you are in the root folder - lab3):

        kubectl apply -f .

    Connect to the frontend container via terminal via the following command:

         kubectl exec -it -n frontend <frontend-pod-name> -- /bin/bash 

    Install curl inorder to test connectivity to the flask API,
    and run the curl command to the backend-service via its FQDN:

        apt-get install curl

        curl backend-service.backend.svc.cluster.local:5000

    After running the curl command, you should get the following reply in the terminal:

        "Hello from Backend!"

And that's it folks!