FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install --no-cache-dir fastapi uvicorn "elasticsearch>=8.0.0,<9.0.0" aiohttp httpx google-genai pydantic-settings loguru

COPY api/ ./api/

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8001"]
