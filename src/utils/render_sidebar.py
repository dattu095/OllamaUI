import ollama
import streamlit as st


class SideBar:
    def __init__(self):
        self.models = ollama.list()["models"]
        if 'model' not in st.session_state:
            st.session_state['model'] = self.models[0]['model']

    def select_button(self, model_name):
        st.session_state.model = model_name

    def render_button(self, model):
        if st.session_state.model == model:
            button_type = "primary"
        else:
            button_type = "secondary"

        model_name, param_size = model.split(":")
        st.button(
            f"model: {model_name}\nparam_size: {param_size}",
            type=button_type,
            on_click=self.select_button,
            args=[model],
            use_container_width=True,
        )

    def render(self):
        with st.sidebar:
            for model in self.models:
                self.render_button(model.model)


if __name__ == "__main__":
    sidebar = SideBar()
    sidebar.render()

    st.write(f"Selected Model: {st.session_state.model}")
