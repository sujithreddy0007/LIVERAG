import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.rag_pipeline import query_gemini
from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.url_loader import extract_text_from_url


def run_app():
    st.title("LiveRAG: PDF/URL Q&A powered by Gemini Flash")

    input_type = st.radio("Choose input type:", ["PDF", "URL"])
    context = ""

    if input_type == "PDF":
        uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
        if uploaded_file:
            context = extract_text_from_pdf(uploaded_file)

    elif input_type == "URL":
        url = st.text_input("Enter a URL:")
        if url:
            context = extract_text_from_url(url)

    # Show question input **only if** context is ready
    if context:
        user_question = st.text_input("Ask a question:")
        if user_question:
            with st.spinner("Generating answer..."):
                result = query_gemini(context, user_question)
                st.subheader("Answer:")
                st.write(result)

if __name__=="__main__":
    run_app()