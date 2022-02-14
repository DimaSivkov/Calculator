pipeline {
    agent any 
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile web/app.py'
                stash(name: 'compiled-results', includes: 'web/*.py*')
            }
        }
    }
}
