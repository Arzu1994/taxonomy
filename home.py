import streamlit as st
import base64
st.set_page_config(
    page_title="Multi",
    page_icon='😇',
    layout="wide"
)

st.title ("DoDo Pizza")
st.sidebar.success ("Select a page")

custom_style = """
<style>
    .custom-title {
        background-color: #1C2833; /* Цвет фона () */
        color: #ffffff; /* Цвет текста (белый) */
        padding: 10px; /* Отступы вокруг текста */
        # text-align: center; /* Выравнивание текста по центру */
    }
</style>
"""

# Отображение заголовка с настройками стиля
st.markdown(custom_style, unsafe_allow_html=True)
st.markdown("<h1 class='custom-title'> The story of success</h1>", unsafe_allow_html=True)


# """### gif from url"""
# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")

file_ = open("data/dodo-pizza-logo.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)