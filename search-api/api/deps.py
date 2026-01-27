from .search import SearchClient
from .encoder import SpladeClient
from .llm import GeminiClient

# Singleton-like instances
_search_client = SearchClient()
_splade_client = SpladeClient()
_gemini_client = GeminiClient()

def get_search_client():
    return _search_client

def get_splade_client():
    return _splade_client

def get_gemini_client():
    return _gemini_client
