import streamlit as st

from .message_renderer import render_messages, show_message
from .ollama_interface import ollama_chat


def render():
    render_messages()

    prompt = st.chat_input("Ask anything")
    if prompt:
        msg = {"role": "user", "content": prompt}
        st.session_state.messages.append(msg)
        show_message(msg)

        with st.chat_message("assistant"):
            with st.spinner("Generating Response..."):
                response = ollama_chat(prompt)
            st.markdown(response)
        res = {"role": "assistant", "content": response}
        st.session_state.messages.append(res)
