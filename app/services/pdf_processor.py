import fitz
from typing import List
from app.services.embedder import Embedder
from app.services.vector_store import VectorStore

class PDFProcessor:
    def __init__(self, embedder: Embedder, store: VectorStore):
        self.embedder = embedder
        self.store = store

    def process_pdf(self, file_path: str, chunk_size: int = 500, overlap: int = 100):
        doc = fitz.open(file_path)
        raw_text = ""

        for page in doc:
            raw_text += page.get_text() + "\n" # type: ignore

        chunks = self._chunk_text(raw_text, chunk_size, overlap)

        embeddings = self.embedder.embed(chunks)
        self.store.add(embeddings, chunks)

        print(f"Processed and Embedded {len(chunks)} chunks from {file_path}")

    
    def _chunk_text(self, text: str, chunk_size: int, overlap: int) -> List[str]:
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size - overlap):
            chunks.append(" ".join(words[i:i+chunk_size]))

        return chunks

