import streamlit as st

import components.sidebar as sidebar
import components.chat_area as chat_area


def main():
    st.title("OllamaUI")
    sidebar.render()
    chat_area.render()


if __name__ == "__main__":
    main()
