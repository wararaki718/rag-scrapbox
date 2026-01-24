import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .encoder import SpladeEncoder


app = FastAPI(title="SPLADE Encoder API")

# Initialize encoder
# In production, you might want to load this from an environment variable or config
MODEL_ID = os.getenv("MODEL_ID", "hotchpotch/japanese-splade-v2")
encoder = SpladeEncoder(model_id=MODEL_ID)

class EncodeRequest(BaseModel):
    text: str

class EncodeResponse(BaseModel):
    sparse_vector: dict
    tokens: dict | None = None

@app.post("/encode", response_model=EncodeResponse)
async def encode(request: EncodeRequest):
    try:
        sparse_vector = encoder.encode(request.text)
        return EncodeResponse(sparse_vector=sparse_vector)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/encode_debug", response_model=EncodeResponse)
async def encode_debug(request: EncodeRequest):
    try:
        sparse_vector = encoder.encode(request.text)
        tokens = encoder.get_tokens_and_weights(sparse_vector)
        return EncodeResponse(sparse_vector=sparse_vector, tokens=tokens)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "model": MODEL_ID}
