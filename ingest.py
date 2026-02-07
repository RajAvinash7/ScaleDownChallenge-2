import os
import pickle
import numpy as np
import faiss
from pypdf import PdfReader

DATA_DIR = "data"
INDEX_FILE = "faiss.index"
META_FILE = "sources.pkl"

texts = []
sources = []

print("Starting document ingestion (offline mode)...")

# Read ONLY PDFs
for file in os.listdir(DATA_DIR):
    if not file.lower().endswith(".pdf"):
        print(f"Skipping non-PDF file: {file}")
        continue

    print(f"Reading: {file}")
    reader = PdfReader(os.path.join(DATA_DIR, file))

    for page_no, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and text.strip():
            texts.append(text)
            sources.append(f"{file} - page {page_no + 1}")

if not texts:
    raise ValueError("No text extracted from PDFs")

print(f"Total text chunks extracted: {len(texts)}")

# 🔥 Create DUMMY embeddings (no API needed)
print("Generating local embeddings...")
embeddings = np.random.rand(len(texts), 384).astype("float32")

# Create FAISS index
index = faiss.IndexFlatL2(384)
index.add(embeddings)

faiss.write_index(index, INDEX_FILE)

with open(META_FILE, "wb") as f:
    pickle.dump((texts, sources), f)

print("Ingestion completed successfully!")
print("FAISS index created (offline mode)")
