# Experiment 7: Deep Research Agent Workflow

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To build an autonomous Deep Research Agent Workflow that executes iterative research planning, web search query expansion, document reflection, critique, and synthesis of long-form analytical reports.

---

## 📜 Problem Statement
Answering complex, open-ended research topics (e.g., *"Analyze the economic impact of quantum computing on modern cryptography"*) cannot be accomplished in a single search or single LLM prompt generation. Single-turn searches produce superficial answers. Deep research requires generating a structured outline, performing recursive multi-angle search queries, critiquing retrieved sources, identifying knowledge gaps, and synthesizing a fully cited report.

---

## 🎯 Objectives
1. Implement a **Planner Module** to break high-level research questions into sub-topic query trees.
2. Develop an **Iterative Search & Reflection Loop** to retrieve web content, evaluate source quality, and identify missing facts.
3. Build a **Critique & Revision Agent** that evaluates report drafts against strict coverage and citation criteria.
4. Create an interactive research studio web UI displaying real-time research plans, web search steps, and generated markdown reports.

---

## 💡 Agentic AI Concept Overview
This experiment demonstrates **Plan-Execute-Reflect (Deep Research Loop)** architecture.

The agent transitions from linear generation to cyclic refinement:
* **Plan:** Break prompt into sub-hypotheses and targeted search strings.
* **Execute:** Run parallel web search tools and extract relevant content.
* **Reflect & Critique:** Check if retrieved facts answer the sub-hypothesis. If gaps exist, formulate secondary search queries.
* **Synthesize:** Compile validated evidence into a structured markdown report.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────┐     ┌───────────────────────────────────────┐
│ Research Topic   │ ──> │ Planning Agent   │ ──> │       Iterative Research Loop         │
└──────────────────┘     └──────────────────┘     │  ┌──────────────┐   ┌──────────────┐  │
                                                  │  │ Search Tools │ ->│ Reflection & │  │
                                                  │  │ & Scrapers   │   │ Gap Analysis │  │
                                                  │  └──────────────┘   └──────────────┘  │
                                                  └──────────────────┬────────────────────┘
                                                                     │
                                                                     ▼
┌──────────────────┐                              ┌───────────────────────────────────────┐
│ Final Deep Report│ <─────────────────────────── │ Report Synthesis & Critique Engine    │
└──────────────────┘                              └───────────────────────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Orchestration:** LangGraph / LlamaIndex / Custom Loop State Machine
* **Search Tools:** Tavily API / DuckDuckGo Search API / Newspaper3k
* **User Interface:** Streamlit Research Studio UI

---

## 📦 Installation Instructions

```bash
cd experiment-07-deep-research
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run deep research terminal agent
python src/research_runner.py

# Launch research studio web interface
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> *"Investigate current state-of-the-art methods for reducing hallucination in small language models (SLMs)."*

### Expected Output
> **Research Outline:** 4 sub-sections generated during planning.  
> **Search Execution:** 12 web queries executed across academic and industry sources.  
> **Final Report:** 2,500-word comprehensive markdown report with inline URL citations and comparative summary tables.

---

## 🖼️ Results & Screenshots
*(Research studio screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: How does a reflection loop improve deep research agent output quality?**  
   *A:* Reflection forces the agent to critique its draft, check for unsupported claims, and execute targeted follow-up searches to fill missing facts before finalizing output.

2. **Q: What is query expansion in search agents?**  
   *A:* Query expansion breaks a broad user prompt into multiple specific search terms targeting diverse angles of the topic.
