## FastAPI 'Hello World' Application

This application is a simple FastAPI web service that returns a 'Hello World' JSON response at the root endpoint and provides a HealthCheck endpoint.

### Setup with Poetry

1. Clone the repository and navigate to the 'fastapi_app' directory.
2. Install Poetry for dependency management:
   ```
   pip install poetry
   ```
3. Install the required packages using Poetry:
   ```
   poetry install
   ```

### Running the Application with Uvicorn

To run the application, use the following command:
```
poetry run uvicorn main:app --reload
```

The application will be available at 'http://127.0.0.1:8000/'.

### Running the Application with Docker

To build the Docker image and run the application in a container, use the following commands:

1. Build the Docker image:
   ```
   docker build -t fastapi-helloworld .
   ```
2. Run the Docker container:
   ```
   docker run -d -p 8000:80 fastapi-helloworld
   ```

The application will be accessible at 'http://127.0.0.1:8000/'.

### HealthCheck Endpoint

The HealthCheck endpoint can be accessed at 'http://127.0.0.1:8000/healthcheck' and will return a JSON response with the status of the application.

### Docker Configuration

The `Dockerfile` and `.dockerignore` files are used to configure the Docker environment for the application. The `Dockerfile` contains instructions for building the Docker image, and the `.dockerignore` file lists files and directories that should be ignored by the Docker build context.

### Managing Dependencies with Poetry

Poetry is used to manage the application's dependencies. The `pyproject.toml` file contains the configuration for Poetry and the application's dependencies.

To add a new package:
```
poetry add <package>
```

To update a package:
```
poetry update <package>
```
