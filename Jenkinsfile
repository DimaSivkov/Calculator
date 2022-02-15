pipeline {
    agent none 
    environment {
        registryName = "dsivkovregistry/calculator:${env.BUILD_ID}"
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
                    dockerImage = docker.build(registryName, "-f ./webDockerfile .") 
                    stage ('Test') {
                        dockerImage.withRun('-p 5000:5000') {
                            def result = sh(script: "CURL -X GET http://0.0.0.0:5000/operate?operation=%2b&a=2&b=3", returnStdout: true)
                            echo result
                        }
                    }
                }
            }
        }
    }
}
