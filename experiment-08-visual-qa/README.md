# Experiment 8: Image Retrieval / Visual QA System

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To build a Multimodal Visual Question Answering (VQA) and Image Retrieval Pipeline capable of indexing image embeddings, performing cross-modal text-to-image search, and leveraging Vision LLMs for visual reasoning over images.

---

## 📜 Problem Statement
Text-only AI workflows are blind to visual media such as charts, technical schematics, architectural blueprints, and medical scans. Extracting insight from image repositories requires multimodal processing: generating joint vision-language vector embeddings for cross-modal search and calling Vision LLMs (e.g., GPT-4o-vision, LLaVA, Claude 3 Vision) for detailed image visual reasoning.

---

## 🎯 Objectives
1. Implement a multimodal embedding generator (CLIP / OpenCLIP) for images and text queries.
2. Build a vector index for fast image search using text or image input.
3. Integrate a Vision LLM to perform zero-shot Visual Question Answering (VQA) over retrieved images.
4. Construct an interactive multimodal web interface for uploading, searching, and querying image databases.

---

## 💡 Agentic AI Concept Overview
This experiment explores **Multimodal AI Pipelines & Cross-Modal Retrieval**.

Multimodal architectures project visual data and textual tokens into a shared high-dimensional vector space (e.g., CLIP space). This allows natural language queries to retrieve visual assets via cosine similarity. Vision-Language LLMs take the retrieved visual tokens alongside text prompts to generate grounded natural language answers about image contents.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  Image Dataset   │ ──> │ CLIP Vision Embedder │ ──> │ Multimodal Vector DB │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                 │
                                                                 ▼
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ VQA Answer & UI  │ <── │  Vision LLM Engine   │ <── │ Top-K Image Vector   │
│ Visual Rendering │     │ (GPT-4o/Claude/LLaVA)│     │ Retrieval            │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Multimodal Embeddings:** CLIP / OpenCLIP / HuggingFace Transformers
* **Vision LLM:** GPT-4o / Claude 3.5 Sonnet / LLaVA (Ollama)
* **Vector Store:** ChromaDB / Qdrant
* **User Interface:** Streamlit Multimodal Gallery & Chat UI

---

## 📦 Installation Instructions

```bash
cd experiment-08-visual-qa
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Build image embeddings index
python src/index_images.py

# Launch Visual QA web application
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> Text Search Query: *"Find electrical schematic diagrams with step-down transformers."*  
> VQA Query on Image #2: *"What is the output voltage specified on transformer T1?"*

### Expected Output
> **Retrieved Image:** `schematic_t1.png` (Similarity Score: 0.89)  
> **VQA Response:** *"According to schematic T1, the output secondary voltage is specified as 12V AC at 2A."*

---

## 🖼️ Results & Screenshots
*(Multimodal VQA interface screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: How does contrastive learning enable CLIP to align text and image representations?**  
   *A:* CLIP is trained on pairs of text and images to maximize cosine similarity of matched pairs while minimizing similarity for unmatched pairs in a shared vector space.

2. **Q: What is the main structural difference between a text LLM and a Vision LLM?**  
   *A:* Vision LLMs pass images through a Vision Transformer (ViT) encoder to create visual patch tokens, which are concatenated alongside text tokens for autoregressive decoding.
