# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title("PoetGPT")
content = st.text_input("Please suggest the theme of the poem")

if st.button("Poem Request"):
    with st.spinner("writing your poem..."):
        result = chat_model.predict("write me a poem about" + content)
        st.write(result)


# result = chat_model.predict("write me about" + content)
# st.write("Theme: ", title)

# content = "Coding"

# result = chat_model.predict("write me about" + content)
# print(result)
