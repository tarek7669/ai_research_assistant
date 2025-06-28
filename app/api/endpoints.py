import tempfile
import os
from fastapi import APIRouter, File, Form, UploadFile
from services.embedder import Embedder
from services.vector_store import VectorStore
from services.pdf_processor import PDFProcessor
from services.qa_engine import QAEngine

router = APIRouter()

# Instantiate global services
embedder = Embedder()
store = VectorStore(dim=embedder.dim, index_path="data/index.faiss", meta_path="data/meta.pkl")
pdf_processor = PDFProcessor(embedder, store)
qa = QAEngine()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        pdf_processor.process_pdf(tmp_path)
        os.remove(tmp_path)
        return {"status": "success", "message": "PDF processed successfully"}
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return {"status": "error", "message": f"Error processing PDF: {e}"}

@router.post("/ask")
async def ask_question(question: str = Form(...)):
    query_vec = embedder.embed([question])[0]
    results = store.query(query_vec, top_k=5)

    context_chunks = [chunk for chunk, _ in results]
    answer = qa.generate_answer(question, context_chunks)

    return{
        "question": question,
        "answer": answer,
        "sources": results
    }









