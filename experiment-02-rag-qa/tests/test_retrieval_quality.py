"""
Deterministic Retrieval Quality Tests
Experiment 02 — RAG-Based Question Answering System (MR23-1CS0436)
"""

from app.services.retrieval_service import retrieve_relevant_chunks

def test_retrieval_firewall_quality():
    res = retrieve_relevant_chunks("What does a firewall do in network defense?", top_k=4)
    sources = res["sources"]
    assert len(sources) > 0
    top_doc = sources[0]["document"]
    assert "Firewall" in top_doc or "Network Defense" in top_doc or "Network Security" in top_doc

def test_retrieval_phishing_quality():
    res = retrieve_relevant_chunks("What is phishing and spear phishing?", top_k=4)
    sources = res["sources"]
    assert len(sources) > 0
    top_doc = sources[0]["document"]
    assert "Phishing" in top_doc

def test_retrieval_ransomware_quality():
    res = retrieve_relevant_chunks("What is ransomware and how to prevent it?", top_k=4)
    sources = res["sources"]
    assert len(sources) > 0
    top_doc = sources[0]["document"]
    assert "Ransomware" in top_doc or "Malware" in top_doc
