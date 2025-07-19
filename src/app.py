import streamlit as st

from utils.ollama_chatbot import OllamaChatBot
from utils.render_sidebar import SideBar


def main():
    sidebar = SideBar()
    sidebar.render()

    chat_bot = OllamaChatBot(st.session_state.model)
    chat_bot.render()


if __name__ == "__main__":
    main()
