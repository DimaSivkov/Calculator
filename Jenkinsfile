pipeline {
    agent none 
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
    }
}
