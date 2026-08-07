import time
import requests
import streamlit as st

def get_gemini_response(input_text):
    url = "https://langchain-chatbot-3.onrender.com/answer/invoke"
    payload = {"input":{"topic":input_text}}
    
    max_retries = 3
    delay = 2  # Start with a 2-second delay
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()["output"]["context"]
            
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                if attempt < max_retries - 1:
                    st.warning(f"Rate limited. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2  # Double the wait time for the next attempt
                    continue
                else:
                    return "Error: Server is too busy right now. Please try again later."
            else:
                return f"HTTP Error occurred: {e}"
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

st. title("YOUR CHATBOT 👾") 
input_text = st.text_input("Ask something:")
if input_text:
    result = get_gemini_response(input_text)
    st.write(result)

