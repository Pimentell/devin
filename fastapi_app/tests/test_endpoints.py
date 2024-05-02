from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_openai_interaction():
    response = client.post("/openai", json={"prompt": "Hello", "max_tokens": 5})
    assert response.status_code == 200
    # The response structure and content will depend on the actual OpenAI API response
    # Here we check for the structure only, as we're using a placeholder for the API key
    assert "response" in response.json()
