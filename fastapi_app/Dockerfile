# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the 'pyproject.toml' and 'poetry.lock' (if available) to the container
COPY pyproject.toml poetry.lock* /app/

# Install Poetry in the container
RUN pip install poetry

# Disable virtualenv creation by Poetry and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the codebase into the container
COPY . /app

# Set the OpenAI API key as an environment variable
ENV OPENAI_API_KEY=""

# Command to run the application using Uvicorn
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
