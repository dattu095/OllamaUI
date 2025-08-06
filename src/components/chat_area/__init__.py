import streamlit as st

from .inputbox import get_input
from .msg_renderer import render_messages
from .ollama_client import chat_response


def render():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    render_messages(st.session_state.messages)

    prompt = get_input()
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Generating Response"):
                response = chat_response(
                    st.session_state.model, st.session_state.messages
                )

            st.markdown(response.message["content"])
        st.session_state.messages.append(
            {"role": "assistant", "content": response.message["content"]}
        )
