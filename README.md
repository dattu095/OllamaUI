# OllamaUI
A simple and elegant **Streamlit UI** for interacting with **Ollama LLMs** on your local machine.

## Features
- Lightweight Streamlit interface
- Chat with your local Ollama models
- Easy to set up and run

## Setup
Make sure **Ollama** is running locally and accessible at `http://localhost:11434`

If you're using Docker, ensure the container is running and port `11434` is mapped correctly.

## Installation
``` bash
# Clone the repository
git clone https://github.com/dattu095/OllamaUI.git
cd OllamaUI

# Create a virtual environment
python -m venv .venv

# Activate venn
source .venv/bin/activate   # Linux or macOS
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
## Running the App
``` bash
streamlit run src/main.py
```
After launching, open your browser and go to: `http://localhost:8501`
