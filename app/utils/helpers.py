import requests
from PyPDF2 import PdfReader
import google.generativeai as genai

# Load Gemini model (make sure API key is set via environment or genai.configure)
genai.configure(api_key="your_api_key_here")
model = genai.GenerativeModel("gemini-pro")

def gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf = PdfReader(uploaded_file)
    for page in pdf.pages:
        text += page.extract_text()
    return text

def extract_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error extracting text from URL: {e}"
