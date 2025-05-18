pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ishijapriyansha/translator"
    }

    stages {
        stage('Clone repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ishijapriyansha/Translator.git'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push --quiet ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig', variable: 'KUBECONFIG_FILE')]) {
                    script {
                        withEnv(["KUBECONFIG=$KUBECONFIG_FILE"]) {
                            docker.image('bitnami/kubectl:latest').inside("--entrypoint=''") {
                                sh 'kubectl apply -f k8s/deployment.yaml'
                                sh 'kubectl apply -f k8s/service.yaml'
                            }
                        }
                    }
                }
            }
        }
    }
}
