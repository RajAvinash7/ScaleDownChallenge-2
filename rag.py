import os
import faiss
import pickle
import numpy as np

INDEX_FILE = "faiss.index"
META_FILE = "sources.pkl"

# Safety checks
if not os.path.exists(INDEX_FILE):
    raise FileNotFoundError(
        "faiss.index not found. Please run ingest.py first."
    )

if not os.path.exists(META_FILE):
    raise FileNotFoundError(
        "sources.pkl not found. Please run ingest.py first."
    )

# Load FAISS index and metadata
index = faiss.read_index(INDEX_FILE)

with open(META_FILE, "rb") as f:
    texts, sources = pickle.load(f)

EMBEDDING_DIM = index.d

def mock_embed(text: str) -> np.ndarray:
    """
    Generate a deterministic pseudo-embedding
    (so same question gives same retrieval)
    """
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(EMBEDDING_DIM).astype("float32")

def mock_answer_generator(question: str, context: str) -> str:
    """
    Simple mock answer generator for submission/demo.
    """
    if not context.strip():
        return "I do not have that information in the provided documents."

    return (
        "Based on the available university documents, here is the information:\n\n"
        f"{context.strip()[:500]}...\n\n"
        "For more accurate details, please refer to the official university policy documents."
    )

def ask(question: str):
    """
    Main RAG pipeline:
    - Embed question
    - Retrieve top-k chunks
    - Generate mock answer
    """
    # Create question embedding
    q_embedding = mock_embed(question)
    q_embedding = np.expand_dims(q_embedding, axis=0)

    # Search FAISS
    k = min(3, len(texts))
    _, indices = index.search(q_embedding, k)

    retrieved_texts = []
    retrieved_sources = []

    for i in indices[0]:
        retrieved_texts.append(texts[i])
        retrieved_sources.append(sources[i])

    context = "\n".join(retrieved_texts)

    answer = mock_answer_generator(question, context)

    return answer, retrieved_sources
