import streamlit as st


def show_message(msg):
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


def render_messages():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        show_message(message)
