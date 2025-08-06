import os
from dotenv import load_dotenv
import google.generativeai as genai

from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.url_loader import extract_text_from_url

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

# For PDF/URL context-based RAG
def query_gemini_rag(context, question):
    prompt = f"""Based on the following content, answer the question below:\n\nCONTENT:\n{context[:6000]}\n\nQUESTION:\n{question}"""
    response = model.generate_content(prompt)
    return response.text

# For general chat
def query_gemini_general(message):
    response = model.generate_content(message)
    return response.text
