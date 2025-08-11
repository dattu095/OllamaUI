# OllamaUI
A lightweight Streamlit-based UI for running and interacting with Ollama models locally.

## Features
- Clean, minimal chat interface
- Connects to your local Ollama instance
- Supports multiple models
- Real-time streaming responses

## Prerequisites
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed
- [Ollama](https://ollama.com/) installed and running locally

## Installation
```bash
# Clone the repository
git clone https://github.com/dattu095/OllamaUI.git
cd OllamaUI

# Install dependencies with uv
uv pip install -r requirements.txt
```

## Running the App
Make sure Ollama is running locally:
```bash
ollama serve
```

Then run the Streamlit app:
```bash
uv run streamlit run main.py
```

### Using Docker
```bash
# build docker image
docker build -t ollamaui .

# Using when ollama hosted on localhost directly
docker run -d --name ollama_ui -p 8501:8501 ollama_ui:latest

# Using when ollama is running on other devices
docker run -d \
    --name ollama_ui \
    -p 8501:8501 \
    --add-host=host.docker.internal:host-gateway \
    -e OLLAMA_URL=http://host.docker.internal:11434 \ # If ollama running on docker
    # Give any url where ollama is hosted on
    ollamaui:latest
```
