# Experiment 9: Reasoning Model Benchmarking

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To build a systematic evaluation testbed to benchmark LLM performance across diverse prompting strategies (Zero-Shot, Few-Shot, Chain-of-Thought, Tree-of-Thoughts) and compare model reasoning accuracy, token consumption, and execution latency.

---

## 📜 Problem Statement
Deploying AI agents requires selecting optimal prompting paradigms and model tiers based on quantitative trade-offs between accuracy, reasoning depth, latency, and token cost. Without a standardized benchmarking engine, prompting choices remain anecdotal. A structured benchmarking suite systematically evaluates models on mathematical, logical, and code reasoning datasets under identical prompt conditions.

---

## 🎯 Objectives
1. Implement standard prompting strategy adapters: Zero-Shot, Few-Shot, Chain-of-Thought (CoT), and Tree-of-Thoughts (ToT).
2. Create an automated test harness to run benchmarks over mathematical (GSM8K) and logical reasoning datasets.
3. Compute quantitative metrics: Accuracy (%), Reasoning Token Consumption, Execution Latency (ms), and Cost per Query.
4. Develop an interactive benchmarking dashboard featuring comparative plots and latency-accuracy radar charts.

---

## 💡 Agentic AI Concept Overview
This experiment explores **Reasoning Paradigms & Systematic Model Benchmarking**.

Prompting strategies alter how models navigate complex problem spaces:
* **Zero-Shot / Few-Shot:** Direct inference without explicit step-by-step reasoning.
* **Chain-of-Thought (CoT):** Encourages sequential intermediate step generation ($A \rightarrow B \rightarrow C$).
* **Tree-of-Thoughts (ToT):** Explores multiple parallel reasoning branches with search/backtracking algorithms (BFS/DFS).

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌─────────────────────────────────────────────────────────┐
│ Benchmark Dataset│ ──> │               Prompting Engine Adapters                 │
│ (GSM8K / Logic)  │     │  [Zero-Shot] [Few-Shot] [Chain-of-Thought] [Tree-of-T] │
└──────────────────┘     └────────────────────────────┬────────────────────────────┘
                                                      │ Parallel Test Runner
                                                      ▼
┌──────────────────┐     ┌─────────────────────────────────────────────────────────┐
│ Analytics Dashboard│ <─ │ Evaluation Metrics Collector                            │
│ & Radar Charts   │     │ (Accuracy %, Latency ms, Token Usage, Cost ($))        │
└──────────────────┘     └─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Benchmarking Suite:** Custom Test Harness / Ragas / DeepEval
* **Data & Visualization:** Pandas, Plotly, Streamlit
* **Models Tested:** OpenAI GPT-4o, Claude 3.5, Local Ollama models (DeepSeek-R1 / Llama 3)

---

## 📦 Installation Instructions

```bash
cd experiment-09-reasoning-benchmark
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run benchmark evaluation suite
python src/run_benchmark.py --dataset gsm8k --models gpt-4o,llama3

# Launch interactive benchmarking analytics dashboard
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> Dataset: Logical Reasoning Suite (50 questions) | Prompt Strategies: CoT vs Zero-Shot

### Expected Output
> **Zero-Shot Accuracy:** 64.0% | Avg Latency: 1.2s  
> **Chain-of-Thought Accuracy:** 88.0% | Avg Latency: 3.4s  
> **Tree-of-Thoughts Accuracy:** 94.0% | Avg Latency: 8.9s  
> **Trade-off Analysis:** CoT provides a 24% accuracy boost at 2.8x token overhead.

---

## 🖼️ Results & Screenshots
*(Benchmarking dashboard plots and comparison charts will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: How does Chain-of-Thought (CoT) prompting improve multi-step mathematical reasoning?**  
   *A:* By decomposing complex calculations into step-by-step intermediate tokens, giving the model additional compute budget per token step.

2. **Q: What is the primary trade-off of Tree-of-Thoughts (ToT) compared to standard CoT?**  
   *A:* ToT achieves higher accuracy on combinatorial tasks through search and evaluation, but at significantly higher token consumption and latency cost.
