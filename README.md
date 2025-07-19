# 🧠 OllamaUI

A simple and interactive Streamlit-based UI to run and chat with Ollama models. This app allows you to interact with locally hosted Ollama models like LLaMA, Mistral, or any other supported LLM.

---

## 📦 Features

- Chat with LLMs running through Ollama
- Lightweight Streamlit UI
- Docker support for easy deployment

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally (`ollama serve`)
- A model pulled using `ollama pull <model-name>`, e.g.:
  ```bash
  ollama pull llama3
  ```

---

## 🔧 Local Development

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/OllamaUI.git
   cd OllamaUI
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   streamlit run src/app.py
   ```

> ⚠️ Make sure Ollama is running (`ollama serve`) and your desired model is already pulled.

---

## 🐳 Running with Docker

This project includes a `Dockerfile` for containerized execution.

### 🏗️ Build the image:
```bash
docker build -t ollama-ui .
```

### ▶️ Run the container:
```bash
docker run -p 8501:8501 --add-host=host.docker.internal:host-gateway ollama-ui
```

> This allows the Docker container to access `ollama` hosted on the host machine via `host.docker.internal`.

### ⛔ Common Issue:
If you get connection errors to Ollama:
- Ensure Ollama is running with `ollama serve`
- Bind Ollama to `0.0.0.0`:
  ```bash
  ollama serve --host 0.0.0.0
  ```
- Or modify the code to access `host.docker.internal` inside the container.

---

## 🧪 Example Usage

After launching, open [http://localhost:8501](http://localhost:8501) in your browser.

Type your question in the chat, and receive a response from the selected Ollama model.
