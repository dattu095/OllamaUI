import streamlit as st


def get_model(models):
    with st.sidebar:
        model = st.selectbox("Select Model", models,
                             index=models.index("llama3.2:3b"))
        return model
