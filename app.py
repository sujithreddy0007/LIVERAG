import streamlit as st
from rag_pipeline import process_pdf, process_url, query_gemini

st.set_page_config(page_title="LiveRAG - Real-Time Q&A", layout="centered")

st.title("📄 LiveRAG: Real-Time Q&A from PDFs or URLs")

option = st.radio("Choose input type:", ("PDF Upload", "URL Input"))

text_data = ""

if option == "PDF Upload":
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file:
        text_data = process_pdf(uploaded_file)
        st.success("✅ PDF text extracted!")

elif option == "URL Input":
    url = st.text_input("Paste a URL:")
    if url:
        text_data = process_url(url)
        st.success("✅ Article content loaded!")

if text_data:
    st.subheader("Ask a question or get a summary:")
    query = st.text_input("Type your question here (e.g. 'Summarize this document')")
    if query:
        with st.spinner("Thinking..."):
            response = query_gemini(text_data, query)
        st.markdown("**🔍 Answer:**")
        st.write(response)
