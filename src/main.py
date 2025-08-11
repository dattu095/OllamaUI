import streamlit as st

import components.sidebar as sidebar
import components.chat_area as chat_area


def main():
    st.set_page_config(page_title="OllamaUI", layout='wide')

    sidebar.render()
    chat_area.render()


if __name__ == "__main__":
    main()
