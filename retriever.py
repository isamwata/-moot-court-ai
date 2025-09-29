# retriever.py
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_FILE = "case_index.faiss"
META_FILE = "case_meta.jsonl"
EMBED_MODEL = "all-mpnet-base-v2"

# Load index and metadata
index = faiss.read_index(INDEX_FILE)
embedder = SentenceTransformer(EMBED_MODEL)

# Load metadata
meta_docs = []
with open(META_FILE, "r", encoding="utf-8") as f:
    for line in f:
        meta_docs.append(json.loads(line))

def retrieve(query, top_k=4):
    """Retrieve relevant documents for a query"""
    # Encode query
    query_emb = embedder.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_emb)
    
    # Search
    scores, indices = index.search(query_emb, top_k)
    
    # Return results
    results = []
    for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
        if idx < len(meta_docs):
            doc = meta_docs[idx].copy()
            doc['score'] = float(score)
            results.append(doc)
    
    return results
