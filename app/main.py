import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.rag_pipeline import query_gemini
from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.url_loader import extract_text_from_url

# Page config
st.set_page_config(page_title="LiveRAG Q&A", layout="wide")

# Chat message formatter
def display_chat(question, answer):
    with st.chat_message("user"):
        st.markdown(f"**You:** {question}")
    with st.chat_message("ai"):
        st.markdown(f"**Gemini:** {answer}")

# App function
def run_app():
    st.markdown(
        "<h2 style='text-align:center;'>📄 LiveRAG: PDF/URL Q&A powered by Gemini Flash</h2><hr>",
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.header("Input Type")
        input_type = st.radio("Choose input type:", ["PDF", "URL"])

        context = ""
        if input_type == "PDF":
            uploaded_file = st.file_uploader("📎 Upload your PDF file", type="pdf")
            if uploaded_file:
                with st.spinner("Extracting text from PDF..."):
                    context = extract_text_from_pdf(uploaded_file)
                    st.success("PDF text extracted ✅")

        elif input_type == "URL":
            url = st.text_input("🔗 Enter a URL")
            if url:
                with st.spinner("Extracting text from URL..."):
                    context = extract_text_from_url(url)
                    st.success("URL content extracted ✅")

    # Main Q&A UI
    if context:
        st.markdown("<br>", unsafe_allow_html=True)
        user_question = st.chat_input("Ask a question...")

        if user_question:
            with st.spinner("Generating answer..."):
                try:
                    result = query_gemini(context, user_question)
                    display_chat(user_question, result)
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    else:
        st.info("Please upload a PDF or enter a URL to get started.")

# # Run app
# if __name__ == "__main__":
#     run_app()
