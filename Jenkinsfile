pipeline{
  agent any
  environment {
    DOCKER_IMAGE = "kshakanksha/ak-app"
  }
  stages{
    stage('Checkout') {
      steps{ git url: 'https://github.com/AkankshaKsh/POC9.git', branch: 'main'}
    }
    stage ('Build') {
      steps{ sh "docker build -t ${DOCKER_IMAGE}:latest ."}
    }
    stage('Push') {
      steps{
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push ${DOCKER_IMAGE}:latest"
        }
      }
    }
    stage('Deploy') {
      steps{
        ansiblePlaybook(
          playbook: 'deploy.yml',
          inventory: 'inventory.ini',
          credentialsID: 'ansible-ssh-creds'
        )
      }
    }
  }
}
