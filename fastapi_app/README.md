## FastAPI 'Hello World' Application

This application is a simple FastAPI web service that returns a 'Hello World' JSON response at the root endpoint.

### Setup

1. Clone the repository and navigate to the 'fastapi_app' directory.
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, use the following command:
```
uvicorn main:app --reload
```

The application will be available at 'http://127.0.0.1:8000/'.


