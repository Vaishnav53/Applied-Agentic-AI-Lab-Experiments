# Applied Agentic AI — Laboratory Experiments

**Course Code:** MR23-1CS0436
**Laboratory:** Applied Agentic AI Laboratory
**Academic Year:** 2025–2026

---

> 📖 **Complete Laboratory Guide:**
> Access the living master technical documentation, execution procedures, visual workflow diagrams, faculty demonstration cheat sheets, and viva voce Q&A preparation in the **[Master Laboratory Guide](AGENTIC_AI_LAB_COMPLETE_GUIDE.md)**.

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

| Exp # | Experiment Title | Short Objective | Status | Default Port |
| :---: | :--- | :--- | :---: | :---: |
| **01** | [Text-to-SQL Workflow](file:///d:/Agentic%20AI%20Experiments/experiment-01-text-to-sql) | Build an end-to-end LLM workflow with retrieval and query generation. | ✅ Completed | `8000` |
| **02** | [RAG-Based Question Answering System](file:///d:/Agentic%20AI%20Experiments/experiment-02-rag-qa) | Implement indexing, hybrid retrieval, and response generation pipelines. | ✅ Completed | `8001` |
| **03** | [Prompt Chaining for Summarization](file:///d:/Agentic%20AI%20Experiments/experiment-03-prompt-chaining) | Experiment with 6-stage prompt pipelines and structured decomposition. | ✅ Completed | `8002` |
| **04** | [SQL Agent with Tool Use](file:///d:/Agentic%20AI%20Experiments/experiment-04-sql-agent) | Develop a ReAct-based agent using database tools and schema reflection. | ✅ Completed | `8003` |
| **05** | [Multi-Agent SDR System](file:///d:/Agentic%20AI%20Experiments/experiment-05-multi-agent-sdr) | Design agents for lead generation, qualification, and outbound emailing. | ⬜ Pending | `8004` |
| **06** | [Policy Compliance Agent](file:///d:/Agentic%20AI%20Experiments/experiment-06-policy-compliance) | Build an agent with rule-based evaluation and synthetic data validation. | ⬜ Pending | `8005` |
| **07** | [Deep Research Agent Workflow](file:///d:/Agentic%20AI%20Experiments/experiment-07-deep-research) | Implement planning + reflection loops for complex content generation. | ⬜ Pending | `8006` |
| **08** | [Image Retrieval / Visual QA System](file:///d:/Agentic%20AI%20Experiments/experiment-08-visual-qa) | Develop a multimodal pipeline for visual questioning and image search. | ⬜ Pending | `8007` |
| **09** | [Reasoning Model Benchmarking](file:///d:/Agentic%20AI%20Experiments/experiment-09-reasoning-benchmark) | Compare outputs across different prompting and reasoning strategies. | ⬜ Pending | `8008` |
| **10** | [Fine-Tuning for Domain Adaptation](file:///d:/Agentic%20AI%20Experiments/experiment-10-fine-tuning) | Train, fine-tune, and evaluate a domain-specialized LLM. | ⬜ Pending | `8009` |
| **11** | [Model Optimization Experiment](file:///d:/Agentic%20AI%20Experiments/experiment-11-model-optimization) | Apply quantization or distillation techniques to improve efficiency. | ⬜ Pending | `8010` |
| **12** | [Mini Project (Capstone)](file:///d:/Agentic%20AI%20Experiments/experiment-12-capstone) | Build an end-to-end agentic system integrating RAG, tools, and multi-agent systems. | ⬜ Pending | `8011` |

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
├── AGENTIC_AI_LAB_COMPLETE_GUIDE.md    # Complete Master Laboratory Guide
├── .gitignore                          # Excludes secrets, venvs, cache, and DBs
├── LICENSE                             # MIT License
│
├── experiment-01-text-to-sql/          # Exp 1: Text-to-SQL Workflow (✅ Completed)
│   └── README.md
├── experiment-02-rag-qa/               # Exp 2: RAG-Based QA System (✅ Completed)
│   └── README.md
├── experiment-03-prompt-chaining/      # Exp 3: Prompt Chaining Summarization (✅ Completed)
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
└── docs/                               # System diagrams & supplementary resources
    └── README.md
```

---

## ⚙️ Quick Execution Reference

For detailed step-by-step instructions, view the **[Master Laboratory Guide](AGENTIC_AI_LAB_COMPLETE_GUIDE.md)**.

```powershell
# Experiment 01 — Text-to-SQL Workflow (Port 8000)
cd experiment-01-text-to-sql; python -m app.main

# Experiment 02 — RAG-Based Question Answering System (Port 8001)
cd experiment-02-rag-qa; python -m app.main

# Experiment 03 — Prompt Chaining for Summarization (Port 8002)
cd experiment-03-prompt-chaining; python -m app.main
```

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE) — created for educational purposes under course **MR23-1CS0436**.
