# index_cases.py
import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from pathlib import Path

EMBED_MODEL = "all-mpnet-base-v2"  # good default
INDEX_FILE = "case_index.faiss"
META_FILE = "case_meta.jsonl"
DOCS_JSONL = "cases_sections.jsonl"  # one JSON per line: {"id": "...", "text": "...", "source": "..."}
DIM = 768

# Load model
embedder = SentenceTransformer(EMBED_MODEL)

# Load docs
docs = []
with open(DOCS_JSONL, "r", encoding="utf-8") as f:
    for line in f:
        docs.append(json.loads(line))

texts = [d["text"] for d in docs]
ids = [d.get("id", str(i)) for i,d in enumerate(docs)]

# create embeddings
embs = embedder.encode(texts, show_progress_bar=True, convert_to_numpy=True)
# ensure dims
assert embs.shape[1] == embs.shape[1]

# build faiss index
index = faiss.IndexFlatIP(embs.shape[1])  # inner-product; we'll normalize
faiss.normalize_L2(embs)
index.add(embs)
faiss.write_index(index, INDEX_FILE)

# store meta
with open(META_FILE, "w", encoding="utf-8") as f:
    for d in docs:
        f.write(json.dumps(d, ensure_ascii=False) + "\n")
print("Saved faiss index and meta.")
