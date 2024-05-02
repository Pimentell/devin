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

@patch('app.main.OpenAI')
def test_openai_interaction(mock_openai_class):
    # Mock the OpenAI class to return a mock object with a create method
    mock_openai_instance = mock_openai_class.return_value
    mock_openai_instance.generate.return_value = ["Mocked response"]

    response = client.post("/openai", json={"prompt": "Hello", "max_tokens": 5})
    assert response.status_code == 200
    # The response structure and content will depend on the actual OpenAI API response
    # Here we check for the structure only, as we're using a placeholder for the API key
    assert "response" in response.json()
    # Additionally, we check if the mocked response is returned
    assert response.json() == {"response": ["Mocked response"]}

@patch('app.main.OpenAI')
def test_get_embeddings(mock_openai_class):
    # Mock the OpenAI class to return a mock object with an embeddings method
    mock_openai_instance = mock_openai_class.return_value
    mock_openai_instance.embeddings.return_value = {"data": [{"embedding": [0.1, 0.2, 0.3]}]}

    response = client.post("/embeddings", json={"text": "Test embedding"})
    assert response.status_code == 200
    # The response structure and content will depend on the actual OpenAI API response
    # Here we check for the structure only, as we're using a placeholder for the API key
    assert "embeddings" in response.json()
    # Additionally, we check if the mocked response is returned
    assert response.json() == {"embeddings": {"data": [{"embedding": [0.1, 0.2, 0.3]}]}}
