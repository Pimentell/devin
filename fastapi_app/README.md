## FastAPI 'Hello World' Application

This application is a simple FastAPI web service that returns a 'Hello World' JSON response at the root endpoint, provides a HealthCheck endpoint, and allows interaction with the OpenAI API to obtain text embeddings.

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
poetry run uvicorn app.main:app --reload
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

### Embeddings Endpoint

The `/embeddings` endpoint can be accessed by sending a POST request with a JSON body containing the text for which you want to obtain embeddings. For example:

```
POST /embeddings
Content-Type: application/json

{
  "text": "Your text here"
}
```

This will return the embeddings for the provided text using the OpenAI API.

### Configuring OpenAI API Key

To use the OpenAI API, you must provide your API key. Replace the placeholder key in `app/main.py` with your actual OpenAI API key.

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

### Unit Testing

Unit tests for the application are located in the `tests` directory. To run the tests, use the following command:

```
poetry run pytest
```

This will execute all tests and provide a report. Ensure all tests pass before pushing changes to the repository.

### Contributing

To contribute to this project, please create a branch for your feature or fix, commit your changes, and create a pull request for review.
