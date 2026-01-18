pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: '<YOUR_GITHUB_REPO_URL>'
      }
    }

    stage('Build Docker Images') {
      steps {
        sh 'docker compose build'
      }
    }

    stage('Deploy') {
      steps {
        // Stop any running containers
        sh 'docker compose down || true'
        // Start containers
        sh 'docker compose up -d'
      }
    }
  }
}

  
