from fastapi import FastAPI, Depends
from langchain_openai import OpenAI
from pydantic import BaseModel
import os

app = FastAPI()

# Retrieve the OpenAI API key from environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize Langchain with OpenAI LLM using the API key from the environment variable
llm = OpenAI(api_key=openai_api_key)

class OpenAIRequest(BaseModel):
    prompt: str
    max_tokens: int

class EmbeddingRequest(BaseModel):
    text: str

@app.get('/')
async def read_root():
    return {'Hello': 'World'}

@app.get('/healthcheck')
async def healthcheck():
    return {'status': 'ok'}

@app.post('/openai')
async def openai_interaction(request: OpenAIRequest):
    # Check if the API key is not set and return a mock response if it is
    if not openai_api_key:
        # Mock response for demonstration purposes
        return {'response': 'This is a mock response for the OpenAI interaction.'}
    else:
        # Wrap the prompt in a list to match the expected input type for llm.generate
        response = llm.generate([request.prompt], max_tokens=request.max_tokens)
        return {'response': response}

@app.post('/embeddings')
async def get_embeddings(request: EmbeddingRequest):
    # Check if the API key is not set and return a mock response if it is
    if not openai_api_key:
        # Mock response for demonstration purposes
        return {'embeddings': 'This is a mock response for the embeddings.'}
    else:
        # Call the OpenAI API to get embeddings for the input text
        embeddings = llm.embeddings([request.text])
        return {'embeddings': embeddings}
