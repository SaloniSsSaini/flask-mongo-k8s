# Flask MongoDB Kubernetes Project

## Overview
This project demonstrates an end-to-end **production-style backend application**
built using **Flask**, **MongoDB**, **Docker**, and **Kubernetes**.

The application exposes REST APIs to store and retrieve data from MongoDB,
is fully containerized using Docker, and deployed on a Kubernetes cluster
with secure configuration, persistent storage, autoscaling, and resource management.

---

## Features
- Flask REST API (`/` and `/data`)
- MongoDB database with authentication enabled
- Dockerized Flask application
- Kubernetes Deployment & StatefulSet
- Persistent storage using PV & PVC
- Secure credentials using Kubernetes Secrets
- Horizontal Pod Autoscaler (HPA)
- Resource requests and limits
- Internal DNS-based service communication

---

## Application Endpoints

### `GET /`
Returns a welcome message with the current timestamp.

### `POST /data`
Stores JSON data into MongoDB.

Example:
```json
{
  "name": "sample",
  "value": 123
}
GET /data
Fetches all stored records from MongoDB.

Project Structure
graphql
Copy code
flask-mongo-k8s/
├── app/                    # Flask application source code
├── docker/                 # Dockerfile for Flask app
├── k8s/                    # Kubernetes manifests
│   ├── flask/              # Flask Deployment, Service, HPA
│   ├── mongo/              # MongoDB StatefulSet, Service, PV, PVC
│   └── secrets.yaml        # Kubernetes Secrets
├── requirements.txt
├── .env.example
└── README.md

Technology Stack
Backend: Python, Flask

Database: MongoDB

Containerization: Docker

Orchestration: Kubernetes (Minikube)

Storage: Persistent Volumes

Scaling: Horizontal Pod Autoscaler

Environment Configuration
Local (for understanding)
Environment variables are defined in .env.example.

env
Copy code
MONGO_USER=admin
MONGO_PASSWORD=admin123
MONGO_HOST=mongodb
MONGO_DB=flask_db
Kubernetes (Production)
Sensitive values are stored in Kubernetes Secrets and injected into pods
as environment variables.

Docker Setup
Build Docker Image
bash
Copy code
docker build -t yourdockerhubusername/flask-mongo-app -f docker/Dockerfile .
Push Image to DockerHub
bash
Copy code
docker push yourdockerhubusername/flask-mongo-app:latest
Kubernetes Deployment
Start Minikube
bash
Copy code
minikube start
Apply Kubernetes Resources (in order)
bash
Copy code
kubectl apply -f k8s/secrets.yaml
kubectl apply -f k8s/mongo/
kubectl apply -f k8s/flask/
Access the Application
bash
Copy code
minikube service flask-service
MongoDB Setup
MongoDB is deployed using a StatefulSet

Authentication is enabled using root credentials

Data is persisted using Persistent Volume & PVC

MongoDB is exposed internally using ClusterIP Service

DNS Resolution in Kubernetes
Kubernetes provides built-in DNS resolution via CoreDNS.

The Flask application connects to MongoDB using the service name:

nginx
Copy code
mongodb
This allows reliable inter-pod communication without hardcoding IP addresses.

Autoscaling (HPA)
Minimum replicas: 2

Maximum replicas: 5

Scaling based on CPU utilization (>70%)

The Horizontal Pod Autoscaler automatically scales Flask pods
based on runtime load.

Resource Management
Both Flask and MongoDB pods are configured with resource requests and limits:

Requests: Guaranteed minimum resources for scheduling

Limits: Prevents excessive resource consumption

This ensures cluster stability and fair resource usage.

Testing Strategy
Verified API endpoints using browser and curl

Tested MongoDB data persistence after pod restarts

Simulated load to validate autoscaling behavior

Confirmed environment variables inside running pods

Design Decisions
Used StatefulSet for MongoDB to ensure stable storage

Used Deployment for Flask as it is stateless

Used Secrets for sensitive configuration

Used HPA for scalability and efficiency

Separated application code and infrastructure configuration

Future Improvements
Add health and readiness probes

Enable HTTPS ingress

Implement CI/CD pipeline

Add centralized logging and monitoring

Add application-level validation and error handling
## Conclusion
This project demonstrates a complete backend deployment lifecycle,
starting from application development to containerization and
orchestration using Kubernetes.

By combining Flask, MongoDB, Docker, and Kubernetes, the project follows
industry best practices for scalability, security, and maintainability.
It highlights practical knowledge of containerized applications,
persistent storage, environment-based configuration, and autoscaling.

The architecture is modular, production-ready, and can be extended further
with monitoring, CI/CD pipelines, and advanced security features.



