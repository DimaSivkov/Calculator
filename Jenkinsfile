pipeline {
    agent any 
    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'python -m py_compile web/app.py'
                stash(name: 'compiled-results', includes: 'web/*.py*')
            }
        }
    }
}
