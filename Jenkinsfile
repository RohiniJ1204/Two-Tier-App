pipeline {
    agent any

    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning source code from GitHub'
                git branch: 'main',
                    url: 'https://github.com/RohiniJ1204/Two-Tier-App.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images using Docker Compose'
                sh 'docker-compose build'
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying application containers'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully. Application deployed.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
