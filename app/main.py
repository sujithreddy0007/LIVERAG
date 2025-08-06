import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.rag_pipeline import query_gemini_rag, query_gemini_general
from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.url_loader import extract_text_from_url

# Page config
st.set_page_config(page_title="LiveRAG Q&A", layout="wide")

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

if "mode" not in st.session_state:
    st.session_state.mode = "RAG"

# Display chat history
def display_chat():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# App entry
def run_app():
    st.markdown(
        "<h2 style='text-align:center;'>🤖 LiveRAG: PDF / URL / Chat Q&A (Gemini Flash)</h2><hr>",
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.header("🛠️ Mode Selection")
        mode = st.radio("Choose a mode:", ["RAG (PDF/URL)", "General Chat"])
        st.session_state.mode = "RAG" if mode == "RAG (PDF/URL)" else "Chat"

        if st.button("🔄 Reset Chat"):
            st.session_state.messages = []
            st.session_state.context = ""
            st.experimental_rerun()

        if st.session_state.mode == "RAG":
            input_type = st.radio("📥 Input Type", ["PDF", "URL"])
            if input_type == "PDF":
                uploaded_file = st.file_uploader("📎 Upload PDF", type="pdf")
                if uploaded_file:
                    with st.spinner("Extracting text from PDF..."):
                        st.session_state.context = extract_text_from_pdf(uploaded_file)
                        st.success("✅ PDF text extracted")

            elif input_type == "URL":
                url = st.text_input("🔗 Enter a URL")
                if url:
                    with st.spinner("Extracting text from URL..."):
                        st.session_state.context = extract_text_from_url(url)
                        st.success("✅ URL content extracted")

    # Show chat
    display_chat()

    # Chat logic
    user_input = st.chat_input("Type your message...")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Thinking..."):
            try:
                if st.session_state.mode == "RAG":
                    if not st.session_state.context:
                        st.warning("Please provide a PDF or URL first.")
                        return
                    answer = query_gemini_rag(st.session_state.context, user_input)
                else:
                    answer = query_gemini_general(user_input)

                st.chat_message("assistant").markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
