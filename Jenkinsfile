import groovy.json.JsonSlurperClassic

pipeline {
    agent any
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
                    dir("./web") {
                        dockerImage = docker.build(registryName) 
                        stage ('Test') {
                            dockerImage.withRun('-p 5000:5000') {
                                def expectedResult = 5
                                def actualResult = 0
                                timeout(time: 5, unit: 'SECONDS') {
                                    while(actualResult != expectedResult) {
                                        def result = sh(script: "curl -X GET 'http://0.0.0.0:5000/operate?operation=%2b&a=2&b=3'", returnStdout: true)
                                        echo result
                                        def data = new JsonSlurperClassic().parseText(result)
                                        actualResult = data.result
                                    }
                                }
                            }
                        }
                        if(env.BRANCH_NAME == 'main') { 
                            stage('Upload Image to ACR') {  
                                    script {
                                        docker.withRegistry( "http://${registryUrl}", registryCredential ) {
                                        dockerImage.push()
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }   
    }
}

