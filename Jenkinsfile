pipeline {
    agent none 
    environment {
        registryName = "dSivkovRegistry/calculator"
        registryCredential = 'ACR'
        dockerImage = ''
        registryUrl = 'dsivkovregistry.azurecr.io'
    }
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:latest' 
                }
            }
            steps {
                sh 'python -m py_compile web/app.py' 
                stash(name: 'compiled-results', includes: 'web/*.py*') 
            }
        }
        stage ('Build Docker image') {
            steps { 
                script {
                    dockerImage = docker.build registryName
                }
            }
        }
    }
}
