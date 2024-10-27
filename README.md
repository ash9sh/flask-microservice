# flask-microservice
Python based Flask microservice application

# Flask Microservice CI/CD Project

## Project Structure
- `app/`: Contains the main Flask application.
- `kubernetes/`: Kubernetes manifests for deployment.
- `tests/`: Unit tests for the Flask application.

## Setup

### 1. Build and Run Docker Image
```bash
docker build -t flask-microservice .
docker run -p 5000:5000 flask-microservice
 
