from sentence_transformers import SentenceTransformer
from typing import List
from app.core.config import settings

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed(self, texts: List[str]):
        return self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True)