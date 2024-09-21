import google.generativeai as genai
import streamlit
import dotenv
import os

dotenv.load_dotenv()

env_api_key=os.getenv("api_key")

genai.configure(api_key=env_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate(data):
    return model.generate_content(data)

streamlit.title("Generative Text AI")

streamlit.header("Ask Anything!")
value = streamlit.text_input("Enter Prompt: ")

if value:
    streamlit.divider()
    streamlit.header("Response:")
    response = generate(value)
    streamlit.write(response.text)
