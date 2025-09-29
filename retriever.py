# retriever.py
import json
import os
from pathlib import Path

# Global variables for lazy loading
_index = None
_embedder = None
_meta_docs = None

INDEX_FILE = "case_index.faiss"
META_FILE = "case_meta.jsonl"
EMBED_MODEL = "all-mpnet-base-v2"

def _load_components():
    """Lazy load the search components"""
    global _index, _embedder, _meta_docs
    
    try:
        # Only load if not already loaded
        if _index is None:
            import faiss
            import numpy as np
            from sentence_transformers import SentenceTransformer
            
            # Check if files exist
            if not os.path.exists(INDEX_FILE):
                print(f"Warning: {INDEX_FILE} not found")
                return False
            
            if not os.path.exists(META_FILE):
                print(f"Warning: {META_FILE} not found")
                return False
            
            # Load components
            _index = faiss.read_index(INDEX_FILE)
            _embedder = SentenceTransformer(EMBED_MODEL)
            
            # Load metadata
            _meta_docs = []
            with open(META_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    _meta_docs.append(json.loads(line))
            
            print(f"✅ Loaded search index with {len(_meta_docs)} documents")
            return True
            
    except Exception as e:
        print(f"❌ Error loading search components: {e}")
        return False
    
    return True

def retrieve(query, top_k=4):
    """Retrieve relevant documents for a query"""
    try:
        # Load components if needed
        if not _load_components():
            return []
        
        if _index is None or _embedder is None or _meta_docs is None:
            return []
        
        # Encode query
        query_emb = _embedder.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_emb)
        
        # Search
        scores, indices = _index.search(query_emb, top_k)
        
        # Return results
        results = []
        for i, (score, idx) in enumerate(zip(scores[0], indices[0])):
            if idx < len(_meta_docs):
                doc = _meta_docs[idx].copy()
                doc['score'] = float(score)
                results.append(doc)
        
        return results
        
    except Exception as e:
        print(f"❌ Error in retrieve function: {e}")
        return []
