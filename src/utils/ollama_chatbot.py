import streamlit as st
from ollama import Client
from config.config import OLLAMA_HOST


class OllamaChatBot:
    def __init__(self, model):
        self.model = model
        self.client = Client(host=OLLAMA_HOST)
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system",
                    "content": "You are a helpfull AI assistant"
                }
            ]

    def render_msg(self, role, content):
        with st.chat_message(role):
            st.write(content)
        st.session_state.messages.append({"role": role, "content": content})

    def chat_prompt(self, prompt):
        self.render_msg("user", prompt)

        response = self.client.chat(
            model=self.model, messages=st.session_state.messages
        )

        self.render_msg("assistant", response["message"]["content"])

    def render(self):
        if prompt := st.chat_input():
            self.chat_prompt(prompt)


if __name__ == "__main__":
    chat_bot = OllamaChatBot("llama3.2:3b")
    chat_bot.render()
