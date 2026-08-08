# Experiment 12: Mini Project (Capstone)

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To architect, build, and deploy an end-to-end autonomous agentic enterprise system that integrates Retrieval-Augmented Generation (RAG), ReAct SQL tools, multi-agent orchestration, human-in-the-loop controls, and a production web interface.

---

## 📜 Problem Statement
Individual AI components (RAG pipelines, SQL agents, prompt chains, visual QA modules) solve isolated problems. Real-world enterprise AI systems require unifying these disparate components into a cohesive, multi-agent platform capable of handling complex hybrid requests (e.g., querying relational databases, retrieving corporate policy documents, performing deep web research, and executing automated workflows with human approval).

---

## 🎯 Objectives
1. Design a master multi-agent orchestration architecture uniting RAG, SQL tool execution, and web research agents.
2. Implement a unified state graph (via LangGraph) with branching router nodes and dynamic tool selection.
3. Integrate Human-in-the-Loop (HITL) approval nodes for sensitive actions (financial database updates, outbound emails).
4. Deploy an end-to-end interactive web application dashboard showcasing real-time agent execution traces, vector storage, and analytical report generation.

---

## 💡 Agentic AI Concept Overview
This experiment represents the **Capstone Integration of Full-Stack Agentic AI Systems**.

It unifies:
* **Hybrid RAG & Vector Indexing** (Experiment 2)
* **ReAct Tool Engine & Database Agents** (Experiment 4)
* **Multi-Agent Orchestration & Role Handoffs** (Experiment 5)
* **Policy Guardrails & Evaluation** (Experiment 6)
* **Plan-Execute Deep Research Loops** (Experiment 7)

---

## 🏗️ System Architecture & Workflow

```
                               ┌────────────────────────────────────────────────────────┐
                               │                    Unified User Input                  │
                               └───────────────────────────┬────────────────────────────┘
                                                           │
                                                           ▼
                               ┌────────────────────────────────────────────────────────┐
                               │               Master Intent Router & Supervisor        │
                               └──────┬────────────────────┬────────────────────┬───────┘
                                      │                    │                    │
                                      ▼                    ▼                    ▼
                           ┌────────────────────┐┌───────────────────┐┌───────────────────┐
                           │  RAG Knowledge Agent││  ReAct SQL Agent  ││ Deep Research Agent│
                           └──────────┬─────────┘└─────────┬─────────┘└─────────┬─────────┘
                                      │                    │                    │
                                      └────────────────────┼────────────────────┘
                                                           │
                                                           ▼
                               ┌────────────────────────────────────────────────────────┐
                               │           Human-in-the-Loop Approval & Policy Guard    │
                               └───────────────────────────┬────────────────────────────┘
                                                           │
                                                           ▼
                               ┌────────────────────────────────────────────────────────┐
                               │             Interactive Web Application UI             │
                               └────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+ / TypeScript
* **State & Graph Orchestration:** LangGraph / CrewAI
* **Retrieval & DB:** ChromaDB + PostgreSQL + SQLite
* **Guardrails & Evaluation:** Guardrails AI / Pydantic
* **Frontend Framework:** Next.js / Streamlit / React

---

## 📦 Installation Instructions

```bash
cd experiment-12-capstone
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Launch background agent backend service
python src/backend.py

# Launch Capstone interactive production dashboard UI
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> *"Analyze our Q4 sales performance from the database, check compliance against our discount policy handbook, and draft an executive report."*

### Expected Output
> 1. **SQL Agent Execution:** Queries sales database for Q4 revenue breakdown.  
> 2. **RAG Agent Execution:** Retrieves discount policy guidelines from internal vector DB.  
> 3. **Policy Guard Check:** Confirms Q4 promotional discounts were compliant.  
> 4. **Executive Dashboard:** Renders interactive analytics report with data tables, source citations, and draft email.

---

## 🖼️ Results & Screenshots
*(Capstone end-to-end system screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: How does LangGraph handle complex agentic state and cyclic workflows?**  
   *A:* LangGraph models multi-agent workflows as state graphs where nodes represent agent actions/tools and edges represent conditional routing logic, maintaining persistent state across cycles.

2. **Q: Why are Human-in-the-Loop (HITL) interrupt points critical in enterprise agent deployment?**  
   *A:* HITL prevents unintended actions (e.g., executing unauthorized transactions, sending unreviewed emails) by pausing state graph execution until human approval is granted.
