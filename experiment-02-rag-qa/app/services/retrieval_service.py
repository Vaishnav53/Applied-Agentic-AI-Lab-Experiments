"""
Vector Retrieval Service
Experiment 02 — RAG-Based Question Answering System (MR23-1CS0436)

Embeds user query, searches vector index, applies relevance thresholding,
and formats retrieved source evidence.
"""

from typing import Dict, Any, List, Tuple
from app.config import settings
from app.services.embedding_service import get_embedding_engine
from app.services.vector_store import global_vector_store

def retrieve_relevant_chunks(question: str, top_k: int = None) -> Dict[str, Any]:
    """
    Embeds question, performs Cosine Similarity search, retrieves top_k chunks,
    and applies relevance threshold filtering.
    """
    if top_k is None:
        top_k = settings.DEFAULT_TOP_K

    embedding_engine = get_embedding_engine()
    query_vector = embedding_engine.embed_text(question)

    # Search top-K similar chunks
    search_results = global_vector_store.search_similar_chunks(query_vector, top_k=top_k)

    sources = []
    max_score = 0.0

    for chunk_dict, score in search_results:
        if score > max_score:
            max_score = score

        # Clean excerpt string (first 220 chars)
        raw_text = chunk_dict["text"]
        excerpt = raw_text[:220] + "..." if len(raw_text) > 220 else raw_text

        sources.append({
            "document": chunk_dict["title"],
            "chunk_id": chunk_dict["chunk_id"],
            "score": round(float(score), 4),
            "excerpt": excerpt,
            "full_text": raw_text
        })

    # Check if top score meets relevance threshold
    is_out_of_scope = (max_score < settings.RELEVANCE_THRESHOLD)

    return {
        "question": question,
        "sources": sources,
        "max_score": round(float(max_score), 4),
        "is_out_of_scope": is_out_of_scope,
        "chunks_searched": len(global_vector_store.index_data.get("entries", [])),
        "top_k": top_k
    }
