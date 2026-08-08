"""
End-to-End RAG Pipeline Orchestrator Service
Experiment 02 — RAG-Based Question Answering System (MR23-1CS0436)

Executes the visible 6-step RAG pipeline:
Index Check -> Query Embedding -> Vector Retrieval -> Context Building -> Response Gen -> Grounded Answer
"""

from typing import Dict, Any, List
from app.config import settings
from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.llm_service import get_llm_provider
from app.services.vector_store import global_vector_store

def process_rag_query(question: str, top_k: int = None) -> Dict[str, Any]:
    """
    Executes RAG pipeline, constructs grounded answer, formats retrieved sources,
    populates RAG Inspector metadata, and tracks 6 pipeline workflow steps.
    """
    if top_k is None:
        top_k = settings.DEFAULT_TOP_K

    workflow = []

    # Step 1: Document Index Check
    status = global_vector_store.get_status()
    total_chunks = status.get("chunks_indexed", 0)
    workflow.append({
        "step": "Document Index Check",
        "status": "completed",
        "details": f"Index ready. Total chunks searched: {total_chunks}"
    })

    # Step 2: Query Embedding
    workflow.append({
        "step": "Query Embedding",
        "status": "completed",
        "details": f"Generated {settings.EMBEDDING_MODEL} dense 384-dimensional query vector"
    })

    # Step 3: Vector Retrieval & Relevance Filtering
    retrieval_res = retrieve_relevant_chunks(question, top_k=top_k)
    sources = retrieval_res["sources"]
    max_score = retrieval_res["max_score"]
    is_out_of_scope = retrieval_res["is_out_of_scope"]

    workflow.append({
        "step": "Vector Retrieval",
        "status": "completed",
        "details": f"Retrieved top {len(sources)} chunk(s). Max Cosine Similarity: {max_score}"
    })

    # Step 4: Context Building
    if is_out_of_scope:
        context_details = f"Query score ({max_score}) below threshold ({settings.RELEVANCE_THRESHOLD}). Flagged out-of-scope."
        sources_for_response = []
    else:
        context_details = f"Constructed grounded prompt context from {len(sources)} source document(s)."
        sources_for_response = sources

    workflow.append({
        "step": "Context Building",
        "status": "completed",
        "details": context_details
    })

    # Step 5: Response Generation
    provider = get_llm_provider()
    answer = provider.generate_grounded_answer(question, sources_for_response, is_out_of_scope)

    workflow.append({
        "step": "Response Generation",
        "status": "completed",
        "details": f"Synthesized answer using {settings.LLM_PROVIDER} provider mode"
    })

    # Step 6: Grounded Answer & Source Attribution
    workflow.append({
        "step": "Grounded Answer",
        "status": "completed",
        "details": f"Attached {len(sources_for_response)} evidence source reference(s)"
    })

    # Build RAG Inspector Metadata
    inspector = {
        "query": question,
        "chunks_searched": total_chunks,
        "top_k": top_k,
        "max_relevance_score": max_score,
        "embedding_model": settings.EMBEDDING_MODEL,
        "vector_store": "LocalJSONVectorStore",
        "response_mode": f"{settings.LLM_PROVIDER} (Grounded RAG)",
        "out_of_scope": is_out_of_scope
    }

    # Format Source Evidence for response (without internal full_text)
    clean_sources = [
        {
            "document": s["document"],
            "chunk_id": s["chunk_id"],
            "score": s["score"],
            "excerpt": s["excerpt"]
        }
        for s in sources_for_response
    ]

    return {
        "question": question,
        "answer": answer,
        "sources": clean_sources,
        "retrieval_metadata": {
            "top_k": top_k,
            "embedding_model": settings.EMBEDDING_MODEL,
            "chunks_searched": total_chunks,
            "max_score": max_score,
            "relevance_threshold": settings.RELEVANCE_THRESHOLD
        },
        "inspector": inspector,
        "workflow": workflow,
        "provider": settings.LLM_PROVIDER,
        "success": True,
        "error": None
    }
