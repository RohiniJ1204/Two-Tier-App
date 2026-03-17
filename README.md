# 🚀 Two-Tier Web Application with Docker & Jenkins CI/CD

## 📌 Project Overview
This project implements a Two-Tier Web Application deployed using Docker and Docker Compose, integrated with a Jenkins CI/CD pipeline for automated build and deployment. 
The application and database are containerized as separate services, enabling modular design and easy scalability. Jenkins automates the workflow by pulling the latest code from GitHub, building Docker images, and deploying the application using Docker Compose on a linux environment.

---

## 🏗️ Architecture

                ┌───────────────┐
                │ User / Browser│
                └───────┬───────┘
                        │
                        │ HTTP Request
                        ▼
                ┌──────────────────┐
                │  Web Application │
                │  (App Container) │
                └───────┬──────────┘
                        │
                        │ Database Request
                        ▼
                ┌──────────────────┐
                │   Database       │
                │ (DB Container)   │
                └──────────────────┘
    
## Architecture Explanation

---

- The application follows a Two-Tier Architecuture.
- Frontend/Application Layer runs inside a Docker container.
- Database Layer runs in a separate Docker container.
- Containers communicate using a Docker container.
- Containers communicate using Docker network via docker compose.
- Jenkins automates build,test, and deployment.

---

## CI/CD Architecture Flow

```
Developer 
    │
    │ Push Code
    ▼
GitHub Repository
    │
    │ HTTP Request
    ▼
    Jenkins
    ├── Build Docker Images
    ├── Run docker compose
    └── Deploy Containers
```
    
  
## 🛠️ Tools & Technologies Used


---

- Docker
- Docker Compose
- Jenkins (Declarative pipeline)
- Git & GitHub
- Linux (Ubuntu / Cloud VM)

---

## 📁 Project Structure

```
Two-Tier-App/
│
├── app/                      # Application code (Backend)
│   ├── app.py               # Main application file
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Docker image for app
│
├── db/                      # Database setup
│   └── init.sql            # Database initialization script
│
├── docker-compose.yml       # Multi-container setup (App + DB)
├── Jenkinsfile              # Jenkins CI/CD pipeline script 
└── README.md                # Project documentation
```

## 🔄 CI/CD Pipeline Workflow

---

The Jenkins pipeline performs the following steps:
1. Checkout Code - Pulls latest code from GitHub
2. Build Docker Images - Builds images using Docker Compose
3. Deploy Application - Starts application and database containers

---
   
## Jenkinsfile (key Commands)

---

docker compose build

docker compose up -d

Any new container added to docker-compose.yml will be automatically built and deployed without modifying the Jenkinfile.

---

## ▶️ How to Run the project manually

---

prerequisites
- Docker installed
- Docker compose v2 enabled

Steps:
- git clone https://github.com/RohiniJ1204/Two-Tier-App.git

- cd Two-Tier-App

- docker compose build

- docker compose up -d

- Access the application:
http://localhost:<application_port>

---

## 🧪 Jenkins Setup Summary

---

- Jenkins installed on Linux instance
- Jenkins user added to Docker group
- Pipeline triggered manually or via GitHub webhook
- Successful pipeline results in running containers

---

## 📈 What This Project Demonstrates

---

- Containerization of applications using Docker
- Multi-container orchestration using Docker Compose
- CI/CD automation using Jenkins
- Basic DevOps workflow from code to deployment

---

## 🚀Future improvements

---

- Add automated testing stage in Jenkins
- Push Docker images to Docker Hub
- Deploy using Kubernetes
- Add monitoring using Prometheus & Grafana

---

## 👤 Author

---

Rohini Javvaji

Aspiring DevOps Engineer

GitHub: https://github.com/RohiniJ1204
