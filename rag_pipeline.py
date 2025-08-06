import os
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def process_pdf(file):
    from utils.pdf_loader import extract_text_from_pdf
    return extract_text_from_pdf(file)

def process_url(url):
    from utils.url_loader import extract_text_from_url
    return extract_text_from_url(url)

def query_gemini(context, question):
    prompt = f"""Based on the following content, answer the question below:\n\nCONTENT:\n{context[:6000]}\n\nQUESTION:\n{question}"""
    response = model.generate_content(prompt)
    return response.text
