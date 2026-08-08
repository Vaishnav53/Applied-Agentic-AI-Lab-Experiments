# Experiment 5: Multi-Agent SDR System

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To design and orchestrate a Multi-Agent Sales Development Representative (SDR) system where autonomous agents with specialized roles collaborate to perform automated prospect lead research, lead qualification, and personalized email outreach generation.

---

## 📜 Problem Statement
Outbound sales development involves distinct skill sets: research, lead qualification against ideal customer profiles (ICP), and persuasive copywriting. Relying on a single monolithic LLM prompt to perform all these steps results in generic emails and shallow research. Orchestrating specialized AI agents with distinct roles, tasks, memory, and handoff rules mirrors human sales teams and yields superior conversions.

---

## 🎯 Objectives
1. Define specialized agent roles: **Researcher Agent**, **Qualifier Agent**, and **Email Copywriter Agent**.
2. Establish inter-agent communication channels and task dependency handoffs.
3. Integrate web search and scrapers as agent tools for real-time lead enrichment.
4. Develop a multi-agent control dashboard to visualize agent delegation and generated outreach artifacts.

---

## 💡 Agentic AI Concept Overview
This experiment demonstrates **Multi-Agent Collaboration, Specialization, and Task Delegation**.

In a multi-agent framework (e.g., CrewAI or AutoGen), each agent is assigned a system persona, background context, specific tools, and delegated responsibilities. Agents pass structured artifacts to downstream agents, forming a collaborative assembly line.

---

## 🏗️ System Architecture & Workflow

```
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  Prospect Input │ ──> │   Researcher Agent   │ ──> │   Qualifier Agent    │ ──> │  Copywriter Agent    │
│ (Company/Name)  │     │ (Enriches & Scrapes) │     │  (Scores against ICP)│     │(Generates Email Copy)│
└─────────────────┘     └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                                             │
                                                                                             ▼
                                                                                  ┌──────────────────────┐
                                                                                  │ Final Outreach Draft │
                                                                                  └──────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Multi-Agent Framework:** CrewAI / AutoGen / LangGraph
* **Tools:** Serper API / Tavily Search / BeautifulSoup
* **User Interface:** Streamlit Multi-Agent Command Dashboard

---

## 📦 Installation Instructions

```bash
cd experiment-05-multi-agent-sdr
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run multi-agent orchestration script
python src/main.py

# Launch multi-agent SDR dashboard UI
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> Prospect Company: *"Acme Cloud Solutions"* | Contact: *"VP of Engineering"*

### Expected Output
> **Research Dossier:** Recent Series-B funding, expansion into AI infrastructure.  
> **ICP Score:** 92/100 (High Priority Target).  
> **Personalized Email:** Tailored 3-paragraph cold email mentioning recent funding and AI scale challenges.

---

## 🖼️ Results & Screenshots
*(Multi-agent execution dashboard screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: What are the benefits of role specialization in multi-agent systems?**  
   *A:* Specialized system prompts reduce task complexity per agent, improve focus, allow task-specific tool assignment, and increase output quality.

2. **Q: How is state and data handed off between agents in a multi-agent framework?**  
   *A:* State is managed via shared context buffers, structured schema handoffs (Pydantic objects), or message passing queues.
