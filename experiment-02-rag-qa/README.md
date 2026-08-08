# Experiment 2: RAG-Based Question Answering System

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To design and implement a Retrieval-Augmented Generation (RAG) system for question answering over custom document collections using text chunking, embedding generation, vector store indexing, and grounded context synthesis.

---

## 📜 Problem Statement
Standard Large Language Models suffer from knowledge cutoffs, hallucination, and lack of access to private enterprise or domain-specific documents. Directly passing large documents into an LLM prompt exceeds context windows and increases latency and cost. A RAG architecture resolves this by dynamically retrieving relevant document chunks from a vector database and augmenting the LLM context to deliver grounded, source-backed answers.

---

## 🎯 Objectives
1. Build a document ingestion pipeline supporting PDF, Markdown, and TXT parsing.
2. Implement semantic chunking strategies (recursive character / token chunking with overlap).
3. Generate vector embeddings and index them using a local vector store (ChromaDB / FAISS).
4. Construct a grounded context retrieval pipeline to answer queries with explicit source citations.

---

## 💡 Agentic AI Concept Overview
This experiment covers **Retrieval-Augmented Generation (RAG) & Vector Semantic Search**.

Instead of relying solely on parametric LLM knowledge, RAG introduces non-parametric external memory. User queries are converted into dense vector embeddings, compared against document chunk embeddings using cosine similarity or distance metrics, and the top-$K$ most relevant passages are injected into the prompt as verified grounding context.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Document Files  │ ──> │ Chunking Engine  │ ──> │ Embedding Engine │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                                           │
                                                           ▼
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ Grounded Answer  │ <── │  LLM Generation  │ <── │ Vector Store DB  │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Frameworks:** LangChain / LlamaIndex
* **Vector Database:** ChromaDB / FAISS / Qdrant
* **Embeddings:** OpenAI `text-embedding-3-small` / HuggingFace `bge-small-en-v1.5`
* **User Interface:** Streamlit chatbot UI

---

## 📦 Installation Instructions

```bash
cd experiment-02-rag-qa
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Ingest documents and build vector index
python src/ingest.py

# Launch RAG QA web interface
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> *"What is the refund policy for digital products according to the lab handbook?"*

### Expected Output
> *"Digital products are eligible for a full refund within 14 days of purchase provided less than 20% of the content has been downloaded (Source: handbook.pdf, Page 12, Paragraph 3)."*

---

## 🖼️ Results & Screenshots
*(Screenshots to be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: Explain the difference between parametric and non-parametric memory in LLMs.**  
   *A:* Parametric memory refers to weights learned during model training. Non-parametric memory refers to external data retrieved dynamically at query time (e.g., vector database chunks).

2. **Q: Why is chunk size and chunk overlap selection critical in RAG pipelines?**  
   *A:* Too small chunks lack context; too large chunks dilute specific details and exceed context windows. Overlap ensures critical semantics spanning chunk boundaries are preserved.

3. **Q: How does semantic vector search differ from keyword (BM25) search?**  
   *A:* Vector search converts text into dense vector embeddings capturing semantic meaning regardless of specific word matches, whereas BM25 relies on exact lexical frequency.
