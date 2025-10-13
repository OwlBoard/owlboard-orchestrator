# OwlBoard - Orchestrator & API Gateway

This repository serves as the central control plane for the entire OwlBoard application. It contains the primary **API Gateway** and the master `docker-compose.yml` file responsible for orchestrating the deployment of all distributed microservices.

The API Gateway, built with **FastAPI**, acts as the single entry point for all client requests from the React frontend. Its main responsibilities are:

  - **Request Routing**: Intelligently forwards incoming requests to the appropriate backend service (`User_Service`, `Comments_Service`, `Canvas_Service`).
  - **Centralized Logic**: Provides a single place to manage cross-cutting concerns like authentication, rate limiting, and CORS.
  - **Decoupling**: Decouples the client application from the internal architecture of the backend services, improving security and maintainability.

## How It Works

This repository uses a multi-repo orchestration strategy. The `docker-compose.yml` file is configured to:

1.  Build the API Gateway from the local directory.
2.  Clone and build the other microservices (`Desktop_Front_End`, `User_Service`, etc.) directly from their respective Git repositories.
3.  Launch the entire containerized application stack on a unified Docker network.

## Getting Started

To run the entire OwlBoard application, clone this repository and use Docker Compose.

```bash
# Clone the orchestrator repository
git clone https://github.com/OwlBoard/owlboard-orchestrator.git
cd owlboard-orchestrator

# Build and run all services
docker-compose up --build
```

The application will be available at the following endpoints:

  - **Frontend Application**: `http://localhost:3000`
  - **API Gateway**: `http://localhost:8000`