import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown
import textwrap
import os

# Replace 'your_gemini_api_key_here' with your actual Gemini API key
gemini_api_key = 'AIzaSyCgubcjkfqdY6mJV8E5OkpIjXf0fWQ8uQA'

# Configure genai with the Gemini API key
genai.configure(api_key=gemini_api_key)

def to_markdown(text):
    text = text.replace('•', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_gemini_response(question):
    # 🛠 Correct Model name used here
    model = genai.GenerativeModel('gemini-1.5-pro-latest')  # <<< ✅ Fixed here
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="Q&A with Gemini")
st.header("Gemini Application✨")

input_text = st.text_input("Input your question here:", key="input")
submit = st.button("Get Answer")

if submit and input_text:
    response = get_gemini_response(input_text)
    st.subheader("The Response is")
    st.write(response)
