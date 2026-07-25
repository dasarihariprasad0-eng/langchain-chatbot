import requests
import streamlit as st

def get_gemini_response(input_text):
    payload = {"input": {'topic': input_text}}
    response = requests.post(" http://0.0.0.0:5000/answer/invoke",json = payload)
    response.raise_for_status()
    return response.json()["output"]["content"]

st.title("langchain demo with gemini")
input_text = st.text_input("whats the problem big guy")

if input_text:
    st.write(get_gemini_response(input_text))
