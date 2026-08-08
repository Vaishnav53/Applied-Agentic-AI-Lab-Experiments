# Experiment 11: Model Optimization Experiment

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To apply post-training model optimization techniques (quantization to INT8/INT4 and GGUF format conversion) to evaluate trade-offs between model memory footprint, inference throughput (tokens/sec), and semantic quality loss.

---

## 📜 Problem Statement
Deploying large open-source LLMs (e.g., Llama, Mistral, Qwen) in edge environments or low-cost production infrastructure is constrained by GPU VRAM memory and memory bandwidth limitations. Unoptimized 16-bit FP16 models require massive VRAM. Model optimization techniques compress model weights to 8-bit or 4-bit representation, enabling fast CPU/GPU inference while minimizing accuracy degradation.

---

## 🎯 Objectives
1. Quantize a base FP16 model to INT8 and INT4 (via `bitsandbytes`, AWQ, or `llama.cpp` GGUF).
2. Measure VRAM and RAM memory usage across FP16, INT8, and INT4 variants.
3. Benchmark inference throughput in tokens per second (tok/s) and time-to-first-token (TTFT).
4. Evaluate semantic quality loss using perplexity benchmarks and LLM-as-a-judge scoring.

---

## 💡 Agentic AI Concept Overview
This experiment introduces **Model Quantization & Inference Speedup Optimization**.

Quantization converts high-precision floating point numbers (FP16/FP32) into lower-precision representation (INT8/INT4):
$$\mathbf{Q} = \text{round}\left( \frac{\mathbf{X}}{\text{scale}} \right) + \text{zero\_point}$$
This reduces memory consumption by 50% to 75% and accelerates vector-matrix multiplications on hardware supporting tensor cores.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Base FP16 Model  │ ──> │ Quantization Engine  │ ──> │ Quantized Artifacts  │
│ (Weights & Graph)│     │ (GGUF / AWQ / INT4)  │     │ (INT8 / INT4 / GGUF) │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                 │
                                                                 ▼
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Profiling Report │ <── │ Quality & Perplexity │ <── │ Latency & VRAM       │
│ & UI Benchmark   │     │ Evaluator            │     │ Benchmark Suite      │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+ / C++ (`llama.cpp`)
* **Optimization Libraries:** `bitsandbytes`, `autoawq`, `optimum`, `llama-cpp-python`
* **Benchmarking Tools:** PyTorch Profiler / Custom Latency Harness
* **User Interface:** Streamlit Optimization Benchmark Dashboard

---

## 📦 Installation Instructions

```bash
cd experiment-11-model-optimization
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run model quantization and benchmark runner
python src/benchmark_quant.py --model llama3-8b --precisions fp16,int8,int4

# Launch interactive optimization dashboard
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> Model: Llama-3-8B-Instruct | Target Benchmarks: VRAM (GB), Tokens/sec, Perplexity

### Expected Output
| Model Variant | VRAM (GB) | Throughput (tok/s) | Perplexity | Degradation |
| :--- | :---: | :---: | :---: | :---: |
| **FP16** | 16.2 GB | 22.4 tok/s | 5.82 | Baseline |
| **INT8** | 8.4 GB | 38.1 tok/s | 5.86 | +0.68% |
| **INT4 (GGUF Q4_K_M)** | 4.8 GB | 54.2 tok/s | 6.01 | +3.26% |

---

## 🖼️ Results & Screenshots
*(Optimization benchmark charts will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: What is the main difference between Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT)?**  
   *A:* PTQ quantizes weights after training without retraining. QAT simulates quantization during model training, allowing weights to adapt and minimize precision loss.

2. **Q: What is GGUF format and why is it widely used for local LLM inference?**  
   *A:* GGUF is a single-file binary format optimized for `llama.cpp` that stores model metadata and quantized weights for efficient CPU/GPU offloading.
