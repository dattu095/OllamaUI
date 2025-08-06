import streamlit as st
from ollama import Client

from .select_model import get_model


def render():
    if "models" not in st.session_state:
        client = Client()
        st.session_state.models = list(
            map(lambda x: x.model, client.list()["models"]))
    if "model" not in st.session_state:
        client = Client()
        st.session_state.model = None

    st.session_state.model = get_model(st.session_state.models)


__all__ = [render]
