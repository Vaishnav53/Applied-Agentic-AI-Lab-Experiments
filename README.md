# Applied Agentic AI — Laboratory Experiments

**Course Code:** MR23-1CS0436  
**Laboratory:** Applied Agentic AI Laboratory  
**Academic Year:** 2025–2026  

---

## 📋 Course & Repository Overview

Welcome to the **Applied Agentic AI Laboratory Experiments** repository. This repository serves as a comprehensive, modular suite of 12 laboratory experiments designed for course **MR23-1CS0436**.

The curriculum advances from foundational prompt engineering and single-turn retrieval pipelines to autonomous ReAct agents, multi-agent coordination systems, reasoning benchmarks, model fine-tuning/optimization, and an end-to-end Capstone mini-project.

### Repository Objectives
1. **Practical Agentic Engineering:** Build hands-on, production-grade agent workflows combining LLMs, vector search, tool execution, memory, and orchestration.
2. **Independent Reproducibility:** Ensure every experiment is self-contained with isolated dependencies, configuration, dedicated documentation, and execution scripts.
3. **Interactive & Visual Demonstration:** Provide web-based interfaces (chatbots, control dashboards, visualization suites) tailored to each experiment's workflow.
4. **Dual-Purpose Presentation:** Format every experiment to meet rigorous university laboratory evaluation standards while serving as a high-impact GitHub portfolio piece.

---

## 🧪 Laboratory Experiments Matrix

| Exp # | Experiment Title | Short Objective | Status |
| :---: | :--- | :--- | :---: |
| **01** | [Text-to-SQL Workflow](file:///d:/Agentic%20AI%20Experiments/experiment-01-text-to-sql) | Build an end-to-end LLM workflow with retrieval and query generation. | ✅ Completed |
| **02** | [RAG-Based Question Answering System](file:///d:/Agentic%20AI%20Experiments/experiment-02-rag-qa) | Implement indexing, retrieval, and response generation pipelines. | ✅ Completed |
| **03** | [Prompt Chaining for Summarization](file:///d:/Agentic%20AI%20Experiments/experiment-03-prompt-chaining) | Experiment with multi-step prompt pipelines and structured decomposition. | ✅ Completed |
| **04** | [SQL Agent with Tool Use](file:///d:/Agentic%20AI%20Experiments/experiment-04-sql-agent) | Develop a ReAct-based agent using database tools and schema reflection. | ⬜ Pending |
| **05** | [Multi-Agent SDR System](file:///d:/Agentic%20AI%20Experiments/experiment-05-multi-agent-sdr) | Design agents for lead generation, qualification, and outbound emailing. | ⬜ Pending |
| **06** | [Policy Compliance Agent](file:///d:/Agentic%20AI%20Experiments/experiment-06-policy-compliance) | Build an agent with rule-based evaluation and synthetic data validation. | ⬜ Pending |
| **07** | [Deep Research Agent Workflow](file:///d:/Agentic%20AI%20Experiments/experiment-07-deep-research) | Implement planning + reflection loops for complex content generation. | ⬜ Pending |
| **08** | [Image Retrieval / Visual QA System](file:///d:/Agentic%20AI%20Experiments/experiment-08-visual-qa) | Develop a multimodal pipeline for visual questioning and image search. | ⬜ Pending |
| **09** | [Reasoning Model Benchmarking](file:///d:/Agentic%20AI%20Experiments/experiment-09-reasoning-benchmark) | Compare outputs across different prompting and reasoning strategies. | ⬜ Pending |
| **10** | [Fine-Tuning for Domain Adaptation](file:///d:/Agentic%20AI%20Experiments/experiment-10-fine-tuning) | Train, fine-tune, and evaluate a domain-specialized LLM. | ⬜ Pending |
| **11** | [Model Optimization Experiment](file:///d:/Agentic%20AI%20Experiments/experiment-11-model-optimization) | Apply quantization or distillation techniques to improve efficiency. | ⬜ Pending |
| **12** | [Mini Project (Capstone)](file:///d:/Agentic%20AI%20Experiments/experiment-12-capstone) | Build an end-to-end agentic system integrating RAG, tools, and multi-agent systems. | ⬜ Pending |

> **Status Legend:**  
> 🔄 **In Development** — Active development in progress  
> ⬜ **Pending** — Scheduled for upcoming lab sessions  
> ✅ **Completed** — Fully implemented, tested, and verified  

---

## 🛠️ Key Technologies & Ecosystem

The experiments utilize modern agentic frameworks, database engines, vector stores, and UI tools:

* **Language & Runtime:** Python 3.10+ / Node.js
* **LLM Architectures & APIs:** OpenAI API, Anthropic Claude, Google Gemini, Ollama (Local LLMs)
* **Agent Frameworks:** LangChain, LangGraph, CrewAI, AutoGen, LlamaIndex
* **Databases & Vector Stores:** SQLite, PostgreSQL, ChromaDB, FAISS, Qdrant
* **Frontend Interfaces:** Streamlit, Gradio, React / Next.js, HTML5/Vanilla CSS
* **Evaluation & Optimization:** PyTorch, Hugging Face Transformers, PEFT, bitsandbytes, MLflow

---

## 📂 Repository Structure

```
Agentic AI Experiments/
│
├── README.md                           # Main repository documentation & status matrix
├── .gitignore                          # Excludes secrets, venvs, cache, and DBs
├── LICENSE                             # MIT License
│
├── experiment-01-text-to-sql/          # Exp 1: Text-to-SQL Workflow (🔄 In Development)
│   └── README.md
├── experiment-02-rag-qa/               # Exp 2: RAG-Based QA System (⬜ Pending)
│   └── README.md
├── experiment-03-prompt-chaining/      # Exp 3: Prompt Chaining Summarization (⬜ Pending)
│   └── README.md
├── experiment-04-sql-agent/            # Exp 4: ReAct SQL Agent with Tool Use (⬜ Pending)
│   └── README.md
├── experiment-05-multi-agent-sdr/      # Exp 5: Multi-Agent SDR System (⬜ Pending)
│   └── README.md
├── experiment-06-policy-compliance/   # Exp 6: Policy Compliance Agent (⬜ Pending)
│   └── README.md
├── experiment-07-deep-research/        # Exp 7: Deep Research Agent Workflow (⬜ Pending)
│   └── README.md
├── experiment-08-visual-qa/            # Exp 8: Visual QA & Image Retrieval (⬜ Pending)
│   └── README.md
├── experiment-09-reasoning-benchmark/  # Exp 9: Reasoning Model Benchmarking (⬜ Pending)
│   └── README.md
├── experiment-10-fine-tuning/          # Exp 10: Fine-Tuning Domain Adaptation (⬜ Pending)
│   └── README.md
├── experiment-11-model-optimization/  # Exp 11: Model Quantization & Distillation (⬜ Pending)
│   └── README.md
├── experiment-12-capstone/             # Exp 12: Mini Project Capstone (⬜ Pending)
│   └── README.md
│
└── docs/                               # System diagrams, workflow charts, & viva guides
    └── README.md
```

---

## ⚙️ General Setup & Execution Guidelines

### Prerequisites
* **Python:** 3.10 or higher
* **Git:** 2.x or higher
* **API Credentials:** Copy `.env.example` to `.env` in the target experiment directory and insert your required API keys (e.g., `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).

### Execution Workflow
Each experiment is independently runnable and maintains its own dependency configuration:

1. Navigate to the desired experiment directory:
   ```bash
   cd experiment-01-text-to-sql
   ```
2. Create and activate a isolated virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```
3. Install experiment dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   ```
5. Follow the specific execution instructions inside the experiment's `README.md`.

---

## 🛡️ Code Quality & Security Standards

To maintain high software engineering standards throughout the course:
* **No Secret Leaks:** Never commit `.env` files, private keys, or raw API credentials. `.gitignore` is strictly enforced.
* **Modular Architecture:** Logic is decomposed into clear modules (retriever, prompt pipeline, agent tools, UI wrapper).
* **Interactive UI Standard:** Every conversational or workflow experiment features a modern user interface tailored to demonstrate internal execution steps.
* **Empirical Verification:** Each completed experiment includes actual execution traces, performance metrics, and verified visual screenshots.

---

## 📚 Documentation Approach

Documentation in this repository follows a standard format across all 12 modules:
* **Aim & Objectives:** Clear problem statement and pedagogical purpose.
* **Theoretical Foundation:** Explanation of underlying Agentic AI concepts (ReAct, RAG indexing, Prompt Chaining, PEFT, etc.).
* **Architecture Diagrams:** High-level system topology and sequence flow charts stored in `docs/`.
* **Viva Voce Preparation:** Standardized Q&A set covering foundational and advanced concepts evaluated during lab viva examinations.

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE) — created for educational purposes under course **MR23-1CS0436**.
