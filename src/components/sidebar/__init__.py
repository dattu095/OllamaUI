import streamlit as st

from .model_selector import select_model


def render():
    with st.sidebar:
        select_model()
