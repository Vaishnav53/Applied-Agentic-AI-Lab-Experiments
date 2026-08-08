# Experiment 3: Prompt Chaining for Summarization

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To experiment with multi-step sequential prompt pipelines that decompose long-form documents into structured summaries using intermediate extraction, map-reduce chaining, and quality validation.

---

## 📜 Problem Statement
Attempting to summarize massive long-form texts (research papers, legal contracts, transcript logs) in a single LLM prompt often causes key information loss, attention degradation, or hallucinations. Single-prompt summarization fails to enforce consistent multi-faceted output structures (such as key takeaways, executive summaries, risk factors, and action items).

---

## 🎯 Objectives
1. Design a multi-step sequential prompt pipeline (Extraction -> Map Summarization -> Reduce Aggregation -> Formatting).
2. Implement intermediate validation checks between chain steps.
3. Compare single-prompt summarization vs. chained prompt pipelines across accuracy, coverage, and structure.
4. Build a user-facing dashboard to visualize intermediate chain steps and final outputs.

---

## 💡 Agentic AI Concept Overview
This experiment explores **Prompt Chaining & Modular Task Decomposition**.

Prompt chaining breaks complex tasks into small, deterministic steps where the output of step $N$ becomes the validated input for step $N+1$. This reduces reasoning entropy, improves prompt control, enables per-step error checks, and yields higher quality summaries.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Long Source Text │ ──> │ Step 1: Key Facts    │ ──> │ Step 2: Sectional    │
└──────────────────┘     │ Extraction           │     │ Draft Summaries      │
                         └──────────────────────┘     └──────────────────────┘
                                                                 │
                                                                 ▼
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Final Formatted  │ <── │ Step 4: Refinement & │ <── │ Step 3: Executive    │
│ Summary Report   │     │ Format Enforcer      │     │ Aggregation (Reduce) │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Frameworks:** LangChain Expression Language (LCEL) / LangGraph
* **LLM Engine:** OpenAI GPT-4o-mini / Anthropic Claude / Ollama
* **User Interface:** Streamlit step-by-step viewer UI

---

## 📦 Installation Instructions

```bash
cd experiment-03-prompt-chaining
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run pipeline evaluation benchmark script
python src/chain_runner.py

# Launch interactive step-by-step summarization UI
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> A 15-page annual research report on AI agent architectures.

### Expected Output
> **Executive Summary:** High-level strategic overview.  
> **Key Innovations:** List of technical breakthroughs extracted in Step 1.  
> **Risk & Limitations:** Risk matrix synthesized in Step 3.  

---

## 🖼️ Results & Screenshots
*(Screenshots showing intermediate prompt chain outputs will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: What is the main advantage of prompt chaining over single-prompt zero-shot summarization?**  
   *A:* Prompt chaining breaks a complex task into manageable sub-tasks, reducing context overload, enabling intermediate quality checks, and improving structural consistency.

2. **Q: Explain the Map-Reduce pattern in prompt chaining.**  
   *A:* Map applies summarization independently to small text chunks; Reduce aggregates all chunk summaries into a coherent final document.
