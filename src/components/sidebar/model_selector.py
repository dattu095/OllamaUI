import streamlit as st
from ollama import Client

from config import OLLAMA_URL


def select_model():
    if "models" not in st.session_state:
        ollama_client = Client(host=OLLAMA_URL)
        st.session_state.models = list(
            map(lambda x: x.model, ollama_client.list()["models"])
        )
    if "model" not in st.session_state:
        st.session_state.model = st.session_state.models[0]

    selected_model = st.selectbox("Select Model", st.session_state.models, index=0)
    st.session_state.model = selected_model
