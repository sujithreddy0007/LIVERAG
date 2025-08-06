import google.generativeai as genai
import streamlit as st

from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.url_loader import extract_text_from_url

# ✅ Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Function for context-based RAG (PDF/URL)
def query_gemini_rag(context, question):
    prompt = f"""Based on the following content, answer the question below:\n\nCONTENT:\n{context[:6000]}\n\nQUESTION:\n{question}"""
    response = model.generate_content(prompt)
    return response.text

# Function for general chat
def query_gemini_general(message):
    response = model.generate_content(message)
    return response.text
