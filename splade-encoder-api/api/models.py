from pydantic import BaseModel
from typing import Dict, Optional

class EncodeRequest(BaseModel):
    text: str

class EncodeResponse(BaseModel):
    sparse_vector: Dict[str, float]
    token_ids: Optional[Dict[str, float]] = None
