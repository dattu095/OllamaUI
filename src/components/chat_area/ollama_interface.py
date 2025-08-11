import streamlit as st

from ollama import Client

from config import OLLAMA_URL


def ollama_chat(prompt):
    ollama_client = Client(host=OLLAMA_URL)

    return ollama_client.chat(
        model=st.session_state.model, messages=st.session_state.messages
    )["message"]["content"]
