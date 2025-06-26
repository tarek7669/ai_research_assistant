from app.services.embedder import Embedder


embedder = Embedder()
vectors = embedder.embed(["Hello, world!", "This is a test"])
print(vectors)