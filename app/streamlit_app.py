import streamlit as st

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inference import generate_response


st.title("🤖 Transformer Chatbot")

st.write("Chat with your AI Bot")


user_input = st.text_input("You:")


if st.button("Send"):

    if user_input:

        response = generate_response(user_input)

        st.text_area("Bot:", value=response, height=200)