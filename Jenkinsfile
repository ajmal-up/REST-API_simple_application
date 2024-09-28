pipeline {
    agent any

    environment {
        // Define environment variables
        AWS_ACCOUNT_ID = 'AWS_ACCOUNT_ID'
        CREDENTIAL_ID = 'app-cluster'
        AWS_REGION = "us-east-1"
        REPOSITORY_URI = '850995554565.dkr.ecr.us-east-1.amazonaws.com/rest-api'
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKER_IMAGE = "${REPOSITORY_URI}:${IMAGE_TAG}"

    }

    stages {
        stage('Build, Tag, Login & Push Docker Image to ECR') {
            steps {
                script {

                    // Login to ECR
                    sh """
                    aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${REPOSITORY_URI}
                    """
                    
                    // Build the Docker image
                    sh """
                    docker build -t ${DOCKER_IMAGE} .
                    """
                    
                    // Push the Docker image to ECR
                    sh """
                    docker push ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Update the docker image name in K8s deployment') {
           steps {
                script {
                    echo 'Update the docker image in k8s manifest file'
                    sh 'envsubst < K8S/deployment.yaml > K8S/deployment.yaml'
                }
            }
        }
    
        stage('Run the k8s deployment files') {
            steps {
                script {
                    withKubeConfig(credentialsId: "${CREDENTIAL_ID}", serverUrl: '') {
                    sh('kubectl apply -f K8S/.')
                    }
                }
            }
        
        }
    }
}
