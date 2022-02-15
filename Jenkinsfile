pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        checkout scm
        sh 'pip install -r web/requirements.txt --user'
      }
    }
  }
}
