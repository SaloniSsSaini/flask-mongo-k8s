# 🚀 Flask MongoDB Kubernetes Project

### *Production-Ready Backend Application with Docker & Kubernetes*

---

## 📌 Project Overview

This project demonstrates an **end-to-end, production-style backend application**
built using **Flask**, **MongoDB**, **Docker**, and **Kubernetes**.

The application provides REST APIs to store and retrieve data from MongoDB,
is containerized using Docker, and deployed on a Kubernetes cluster with
secure configuration, persistent storage, autoscaling, and resource management.

The goal of this project is to showcase **real-world backend deployment practices**
and cloud-native application design.

---

## ✨ Key Features

- RESTful APIs using Flask (`/` and `/data`)
- MongoDB with authentication enabled
- Dockerized Flask application
- Kubernetes Deployment (Flask) & StatefulSet (MongoDB)
- Persistent storage using PV & PVC
- Secure credentials via Kubernetes Secrets
- Horizontal Pod Autoscaler (HPA)
- Resource requests & limits for stability
- Internal DNS-based service communication

---

## 🔌 API Endpoints

### `GET /`
Returns a welcome message with the current timestamp.

### `POST /data`
Stores JSON data into MongoDB.

**Sample Request Body**
```json
{
  "name": "sample",
  "value": 123
}
GET /data
Fetches all stored records from MongoDB.

🗂️ Project Structure
nix
Copy code
flask-mongo-k8s/
├── app/                    # Flask application source code
├── docker/                 # Dockerfile
├── k8s/                    # Kubernetes manifests
│   ├── flask/              # Deployment, Service, HPA
│   ├── mongo/              # StatefulSet, Service, PV, PVC
│   └── secrets.yaml        # Kubernetes Secrets
├── requirements.txt
├── .env.example
└── README.md
🛠️ Technology Stack
Backend
Python

Flask

Database
MongoDB

Containerization
Docker

Orchestration
Kubernetes (Minikube)

Storage
Persistent Volumes & Claims

Scaling
Horizontal Pod Autoscaler (HPA)

⚙️ Environment Configuration
Local (for understanding)
Environment variables are defined in .env.example.

env
Copy code
MONGO_USER=admin
MONGO_PASSWORD=admin123
MONGO_HOST=mongodb
MONGO_DB=flask_db
Kubernetes (Production)
Sensitive configuration is stored in Kubernetes Secrets and injected
into pods as environment variables.

🐳 Docker Setup
Build Docker Image
bash
Copy code
docker build -t yourdockerhubusername/flask-mongo-app -f docker/Dockerfile .
Push Image to DockerHub
bash
Copy code
docker push yourdockerhubusername/flask-mongo-app:latest
☸️ Kubernetes Deployment
Start Minikube
bash
Copy code
minikube start
Apply Kubernetes Resources
bash
Copy code
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo/
kubectl apply -f k8s/flask/
Access the Application
bash
Copy code
minikube service flask-service
🗄️ MongoDB Architecture
MongoDB runs as a StatefulSet

Authentication enabled using root credentials

Data persistence ensured using PV & PVC

MongoDB exposed internally using ClusterIP Service

🌐 DNS Resolution in Kubernetes
Kubernetes provides built-in DNS resolution via CoreDNS.

The Flask application connects to MongoDB using the service name:

nginx
Copy code
mongodb
This enables reliable inter-pod communication without hardcoding IP addresses.

📈 Autoscaling (HPA)
Minimum Replicas: 2

Maximum Replicas: 5

Scaling Metric: CPU utilization (>70%)

The Horizontal Pod Autoscaler dynamically scales Flask pods
based on runtime load.

🧮 Resource Management
Both Flask and MongoDB pods are configured with:

Resource Requests – guaranteed minimum resources

Resource Limits – prevents excessive resource usage

This ensures stability and efficient cluster utilization.

🧪 Testing Strategy
Verified API endpoints using browser and curl

Tested MongoDB data persistence after pod restarts

Simulated load to validate autoscaling behavior

Verified environment variables inside running pods

🧠 Design Decisions
Used StatefulSet for MongoDB due to its stateful nature

Used Deployment for Flask as it is stateless

Used Secrets for secure configuration

Used HPA for scalability

Kept application code and infrastructure configuration separate

🚀 Future Enhancements
Add health and readiness probes

Introduce Ingress with HTTPS

CI/CD pipeline using GitHub Actions

Centralized logging and monitoring

Improved validation and error handling

✅ Conclusion
This project demonstrates a complete backend deployment lifecycle,
from application development to containerization and orchestration
using Kubernetes.

By integrating Flask, MongoDB, Docker, and Kubernetes, the project follows
industry best practices for scalability, security, and maintainability.
The architecture is modular, production-ready, and can be extended further
with monitoring, CI/CD pipelines, and advanced cloud-native features.

⭐ If you find this project useful, feel free to star the repository!
Happy Coding 🚀
