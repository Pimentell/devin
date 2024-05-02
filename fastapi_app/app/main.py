from fastapi import FastAPI
from langchain_openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

# Placeholder for OpenAI API key
openai_api_key = "openai_api_key_placeholder"

# Initialize Langchain with OpenAI LLM
llm = OpenAI(api_key=openai_api_key)

class OpenAIRequest(BaseModel):
    prompt: str
    max_tokens: int

@app.get('/')
async def read_root():
    return {'Hello': 'World'}

@app.get('/healthcheck')
async def healthcheck():
    return {'status': 'ok'}

@app.post('/openai')
async def openai_interaction(request: OpenAIRequest):
    response = llm.generate(request.prompt, max_tokens=request.max_tokens)
    return {'response': response}
