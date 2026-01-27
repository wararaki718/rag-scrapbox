from google import genai

from .config import settings
from .models import SearchResult


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model_name = settings.GEMINI_MODEL_NAME

    async def generate_answer(self, query: str, contexts: list[SearchResult]) -> str:
        if not contexts:
            return "関連する情報が見つかりませんでした。"

        context_text = "\n\n".join(
            [f"--- Source: {c.title} ({c.url}) ---\n{c.text}" for c in contexts]
        )

        prompt = f"""あなたはScrapboxの知識を熟知したアシスタントです。
提供されたコンテキスト情報のみを使用して、ユーザーの質問に回答してください。
回答の最後には、参考にしたページのタイトルとURLを記載してください。

# コンテキスト
{context_text}

# ユーザーの質問
{query}
"""

        response = await self.client.aio.models.generate_content(
            model=self.model_name, contents=prompt
        )
        return response.text
