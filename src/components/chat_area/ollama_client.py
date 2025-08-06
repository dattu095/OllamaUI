from ollama import Client


def chat_response(model, messages):
    ollama = Client()
    return ollama.chat(model=model, messages=messages)
