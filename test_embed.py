from app.services.embedder import Embedder
from app.services.vector_store import VectorStore

embedder = Embedder()
texts = ["AI is the future", "Quantum computing is evolving fast"]
vectors = embedder.embed(texts)

store = VectorStore(dim=vectors.shape[1])
store.add(vectors, texts)

# query
query_vec = embedder.embed(["Tell me about AI"])[0]
results = store.query(query_vec, top_k=1)

for text, dist in results:
    print(f"Text: {text}, Distance: {dist}")





