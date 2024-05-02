from fastapi import FastAPI
from langchain_openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

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
    # Placeholder for OpenAI API key
    openai_api_key = "openai_api_key_placeholder"
    # Initialize Langchain with OpenAI LLM inside the function
    llm = OpenAI(api_key=openai_api_key)
    # Wrap the prompt in a list to match the expected input type for llm.generate
    response = llm.generate([request.prompt], max_tokens=request.max_tokens)
    return {'response': response}

@app.post('/embeddings')
async def get_embeddings(request: EmbeddingRequest):
    # Placeholder for OpenAI API key
    openai_api_key = "openai_api_key_placeholder"
    # Initialize Langchain with OpenAI LLM inside the function
    llm = OpenAI(api_key=openai_api_key)
    # Call the OpenAI API to get embeddings for the input text
    embeddings = llm.embeddings([request.text])
    return {'embeddings': embeddings}
