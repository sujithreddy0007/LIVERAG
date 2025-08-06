# 🤖 LiveRAG – Smart Q&A Assistant

LiveRAG is an intelligent, real-time **Question Answering system** that blends the power of **Retrieval-Augmented Generation (RAG)** and **LLMs (Gemini Flash 2.0)** to deliver fast, context-aware responses.

Whether you upload a PDF, paste a URL, or just want to chat – LiveRAG is here to answer your queries with precision.

👉 **Live App**: [https://liverag.streamlit.app](https://liverag.streamlit.app)  
🔗 **GitHub**: [@sujithreddy0007](https://github.com/sujithreddy0007/LIVERAG)

---

## 🌟 Features

✅ **Ask from PDFs & URLs** – Upload any document or link and ask natural questions  
✅ **Contextual Answers** – Uses advanced RAG pipeline for accurate, grounded responses  
✅ **General Chat Mode** – No context? No problem. Just chat with the assistant  
✅ **Streamlit UI** – Clean, fast, mobile-friendly interface  
✅ **Secure** – API keys managed via Streamlit secrets  

---

## 🧠 How It Works

LiveRAG combines:

### 1. **Document Retrieval**
- Extracts clean text from PDFs or URLs using `PyMuPDF`, `BeautifulSoup`, and custom loaders

### 2. **RAG Pipeline**
- Embeds content with `Sentence-Transformers`
- Stores embeddings using `ChromaDB`
- Retrieves relevant context with `LangChain`
- Passes context to `Gemini Flash 2.0` for final answer generation

### 3. **LLM Power**
- Uses Google’s `gemini-2.0-flash` via `google-generativeai` to generate concise, intelligent answers

---

## 🧪 Example Use Cases

📝 Upload a **research paper** and ask for summaries or explanations  
🌐 Paste a **news article URL** and query insights instantly  
💬 Switch to **chat mode** to ask general knowledge or casual questions  

---

## 🛠️ Tech Stack

| Functionality       | Libraries/Tools                          |
|---------------------|-------------------------------------------|
| UI Framework        | Streamlit                                |
| LLM API             | Google Gemini Flash (via `google-generativeai`) |
| Document Parsing    | `PyMuPDF`, `BeautifulSoup`               |
| RAG & Embeddings    | `LangChain`, `ChromaDB`, `sentence-transformers` |
| Environment Config  | `streamlit.secrets`, `dotenv`            |
| Deployment          | Streamlit Cloud                          |

---

## 🚀 How to Run Locally

1. **Clone the Repo**  
```bash
git clone https://github.com/sujithreddy0007/LIVERAG.git
cd LIVERAG
```

2. **Install Requirements**
```bash 
pip install -r requirements.txt
```

3. **Set API Key in .streamlit/secrets.toml**
```bash 
GEMINI_API_KEY = "your_google_gemini_api_key"

```
4. **Run the app**
```bash 
streamlit run main.py

```
## 📁 Project Structure
```
LIVERAG/
├── app/
│   ├── __init__.py
│   ├── main.py                   # Streamlit app entry point
│   ├── rag_pipeline.py          # Core RAG pipeline (embeddings + Gemini)
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── embed_utils.py       # Functions for embedding and retrieval
│   │   ├── helpers.py           # Common utility functions
│   │   ├── pdf_loader.py        # Extracts text from uploaded PDFs
│   │   └── url_loader.py        # Scrapes and cleans content from URLs
├── config/
│   └── config.json              # Configs (if used for paths/settings)
├── frontend/                    # Frontend assets (if any)
├── .env                         # Environment file (not used for Streamlit Cloud)
├── .gitignore                   # Ignore files for Git
├── .huggingface.yml             # Metadata if hosted on Hugging Face Spaces
├── logo.png                     # App logo for branding
├── README.md                    # Project documentation
├── venv/                        # Local virtual environment (ignored in Git)
└── .streamlit/
    └── secrets.toml             # Secure storage for API keys (Gemini)


```

## ✨ Credits
Sujith Reddy
sujeethreddy0007@gmail.com

Inspired by real-world applications of AI in knowledge workflows.



