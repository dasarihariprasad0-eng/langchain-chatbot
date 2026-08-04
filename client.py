import requests
import streamlit as st

def get_gemini_response(input_text):
    payload = {"input": {'topic': input_text}}
    response = requests.post("https://langchain-chatbot-3.onrender.com/answer/invoke",json = payload)
    response.raise_for_status()
    return response.json()["output"]["content"]

st.title("simple chatbot")
input_text = st.text_input("text what you want")

if input_text:
    st.write(get_gemini_response(input_text))
