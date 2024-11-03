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


######	Project Structure  ######

flask-microservice-ci-cd/
├── app/
│   ├── app.py                # Main Flask application entry point
│   ├── requirements.txt      # Application dependencies
│   └── Dockerfile            # Docker configuration for building the app
├── kubernetes/               # Directory for Kubernetes manifests
│   ├── deployment.yaml       # Deployment configuration for Kubernetes
│   └── service.yaml          # Service configuration for Kubernetes (if applicable)
├── tests/                    # Directory for test files
│   └── test_app.py           # Test file for the Flask application
├── buildspec.yml             # Build specification for AWS CodeBuild
└── README.md                 # Project documentation
 
