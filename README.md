# 🧠 AI Research Assistant

A fully containerized, production-ready AI Research Assistant that allows users to upload academic PDFs and ask natural language questions about their contents. Powered by open-source LLMs and a FAISS-based retrieval pipeline, the assistant delivers accurate, context-aware answers from research papers.

---

## 🚀 Features

- 🔍 **PDF Ingestion & Chunking**: Automatically parses uploaded research papers into meaningful text chunks for efficient retrieval.
- 🧠 **Embedding & Vector Search**: Transforms text into vector representations using Hugging Face models and stores them in a **FAISS index** for fast semantic search.
- 🗃️ **RAG-based QA System**: Combines dense retrieval with a decoder-only LLM (e.g., Falcon or Phi-2) for generating relevant, grounded answers.
- 🌐 **FastAPI Backend**: Clean, modular API built with FastAPI and served via **Docker**.
- 🖼️ **Streamlit Frontend**: Lightweight, user-friendly interface for uploading files and interacting with the assistant.
- ☁️ **Cloud Native**: Backend is fully containerized with Docker and deployed on cloud platforms like **AWS EC2** or **Hugging Face Spaces**.

---

## 🛠️ Tech Stack

- **Python 3.10**
- **FastAPI** – for building RESTful APIs
- **Streamlit** – for frontend UI
- **Hugging Face Transformers** – for LLM and embeddings
- **FAISS** – for fast vector similarity search
- **PyMuPDF / PDFMiner** – for PDF parsing
- **Docker** – for containerization and deployment
- **AWS EC2 / Hugging Face Spaces** – for hosting backend

---

 ## TRY IT: https://ai-research-assist.streamlit.app/


