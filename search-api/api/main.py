from fastapi import FastAPI, Depends, HTTPException
from .models import SearchRequest, ChatResponse
from .deps import get_search_client, get_splade_client, get_gemini_client
from .search import SearchClient
from .encoder import SpladeClient
from .llm import GeminiClient
from loguru import logger

print("Starting RAG Search API...")
app = FastAPI(title="RAG Search API")

@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: SearchRequest,
    search_client: SearchClient = Depends(get_search_client),
    splade_client: SpladeClient = Depends(get_splade_client),
    gemini_client: GeminiClient = Depends(get_gemini_client)
):
    try:
        logger.info(f"Query: {request.query}")
        
        # 1. クエリのベクトル化
        sparse_vector = await splade_client.encode(request.query)
        
        # 2. スパース検索
        contexts = await search_client.search(sparse_vector)
        
        # 3. 回答生成
        answer = await gemini_client.generate_answer(request.query, contexts)
        
        return ChatResponse(
            answer=answer,
            sources=contexts
        )
    except Exception as e:
        logger.error(f"Error during chat: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok"}
