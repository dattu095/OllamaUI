FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY . .

RUN uv sync --frozen --no-dev

ENV OLLAMA_URL=http://host.docker.internal:11434

CMD ["uv", "run", "streamlit", "run", "src/main.py"]
