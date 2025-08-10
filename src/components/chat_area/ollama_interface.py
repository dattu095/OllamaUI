import streamlit as st

from ollama import Client


def ollama_chat(prompt):
    ollama_client = Client(host="http://localhost:11434")

    return ollama_client.chat(
        model=st.session_state.model, messages=st.session_state.messages
    )["message"]["content"]
