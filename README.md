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
