from google import genai
from loguru import logger
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from .config import settings
from .models import SearchResult


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model_name = settings.GEMINI_MODEL_NAME

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),  # 必要に応じて特定の例外に絞り込む
        before_sleep=lambda retry_state: logger.warning(
            f"Gemini API request failed. Retrying... (attempt {retry_state.attempt_number})"
        ),
    )
    async def _generate_with_retry(self, prompt: str) -> str:
        response = await self.client.aio.models.generate_content(
            model=self.model_name, contents=prompt
        )
        return response.text

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

        return await self._generate_with_retry(prompt)
