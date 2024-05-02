from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch('app.main.llm.generate')
def test_openai_interaction(mock_generate):
    # Mock the response of the llm.generate method
    mock_generate.return_value = ["Mocked response"]

    response = client.post("/openai", json={"prompt": "Hello", "max_tokens": 5})
    assert response.status_code == 200
    # The response structure and content will depend on the actual OpenAI API response
    # Here we check for the structure only, as we're using a placeholder for the API key
    assert "response" in response.json()
    # Additionally, we check if the mocked response is returned
    assert response.json() == {"response": ["Mocked response"]}
