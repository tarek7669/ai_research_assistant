import os
import faiss
import numpy as np
from typing import List, Tuple
import pickle

class VectorStore:
    def __init__(self, dim: int, index_path: str = "data/index.faiss", meta_path: str = "data/meta.pkl"):
        self.dim = dim
        self.index_path = index_path
        self.meta_path = meta_path

        self.index: faiss.IndexFlatL2 = faiss.IndexFlatL2(dim)
        self.metadata: List[str] = []

        self._load()

    def add(self, vectors: np.ndarray, texts: List[str]):
        vectors = np.array(vectors, dtype=np.float32)
        assert vectors.shape[0] == len(texts), "Vector and text length mismatch"

        self.index.add(vectors) # type: ignore
        self.metadata.extend(texts) 
        self._save()

    def query(self, vector: np.ndarray, top_k: int = 5) -> List[Tuple[str, float]]:
        # D: distances, I: indices
        D, I = self.index.search(np.array([vector], dtype=np.float32), top_k) # type: ignore

        results = []
        for i, dist in zip(I[0], D[0]):
            if i < len(self.metadata):
                results.append((self.metadata[i], float(dist)))

        return results

    def _save(self):
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def _load(self):
        if os.path.exists(self.index_path) and os.path.exists(self.meta_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.meta_path, "rb") as f:
                self.metadata = pickle.load(f)


