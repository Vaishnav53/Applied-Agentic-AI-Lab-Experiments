# Experiment 10: Fine-Tuning for Domain Adaptation

**Course Code:** MR23-1CS0436  
**Course Name:** Applied Agentic AI  
**Laboratory:** Applied Agentic AI Laboratory  
**Status:** ⬜ Pending  

---

## 🎯 Aim
To fine-tune a small base Large Language Model on a domain-specific dataset using Parameter-Efficient Fine-Tuning (PEFT / LoRA) techniques, evaluate training loss trajectories, and compare base vs. adapted model output quality.

---

## 📜 Problem Statement
General-purpose LLMs lack specialized domain knowledge (e.g., specific medical diagnoses, internal proprietary code formats, or legal terminology). Prompt engineering and RAG have limits when enforcing exact formatting rules or specific domain tone. Fine-tuning adapts model weights to internalize specific domain semantics, terminology, and structural formatting without incurring full model retraining costs.

---

## 🎯 Objectives
1. Prepare and format an instruction-tuning dataset (Alpaca / ShareGPT format).
2. Configure Low-Rank Adaptation (LoRA / QLoRA) parameters ($r, \alpha$, target modules).
3. Train the model adapter using Hugging Face `TRL` (Transformer Reinforcement Learning) & `SFTTrainer`.
4. Evaluate training/validation loss curves and test domain adaptation using quantitative BLEU/ROUGE/LLM-as-a-judge metrics.

---

## 💡 Agentic AI Concept Overview
This experiment introduces **Parameter-Efficient Fine-Tuning (PEFT) & LoRA Adaptation**.

Instead of updating all billions of parameters in a base model, Low-Rank Adaptation (LoRA) freezes base weights and injects trainable rank decomposition matrices into transformer attention layers:
$$W = W_0 + \Delta W = W_0 + B \cdot A$$
where $B \in \mathbb{R}^{d \times r}$ and $A \in \mathbb{R}^{r \times k}$ with rank $r \ll \min(d, k)$. This drastically reduces memory overhead while retaining adaptation performance.

---

## 🏗️ System Architecture & Workflow

```
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Instruction Data │ ──> │ Dataset Tokenizer &  │ ──> │ Base Model (Frozen)  │
│ (JSONL Format)   │     │ Format Cleaner       │     │ + LoRA Adapters      │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
                                                                 │
                                                                 ▼
┌──────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Domain Adapted   │ <── │ Model Adapter Merge  │ <── │ SFT Training Loop &  │
│ Model Inference  │     │ & Quantized Export   │     │ Loss Evaluation      │
└──────────────────┘     └──────────────────────┘     └──────────────────────┘
```

---

## 🛠️ Technologies Used
* **Programming Language:** Python 3.10+
* **Frameworks:** Hugging Face `transformers`, `peft`, `trl`, `datasets`, `accelerate`
* **Optimization:** `bitsandbytes` (QLoRA 4-bit quantization)
* **Hardware Target:** NVIDIA CUDA GPU / Apple Silicon MPS / Google Colab
* **User Interface:** Streamlit Base vs Fine-Tuned Comparison Playground

---

## 📦 Installation Instructions

```bash
cd experiment-10-fine-tuning
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

---

## 🚀 Execution Instructions

```bash
# Run fine-tuning training script
python src/train.py --config configs/lora_config.yaml

# Launch side-by-side comparison playground
streamlit run app.py
```

---

## 📥 Example Inputs & 📤 Expected Outputs

### Example Input
> Prompt: *"Translate the following medical complaint into ICD-10 medical coding format: Patient reports acute right-side abdominal pain."*

### Expected Output
> **Base LLM:** *"The patient is experiencing appendicitis symptoms, which should be checked by a doctor..."* (General response)  
> **Fine-Tuned LLM:** `R10.31 - Right lower quadrant abdominal pain.` (Exact domain coding output)

---

## 🖼️ Results & Screenshots
*(Loss curves and comparison playground screenshots will be added upon implementation.)*

---

## 📊 Result
*(To be populated after execution verification.)*

---

## 📝 Conclusion
*(To be populated after lab implementation completion.)*

---

## ❓ Viva Voce Questions & Key Concepts

1. **Q: What is the primary benefit of LoRA over full fine-tuning?**  
   *A:* LoRA freezes base model weights and trains low-rank decomposition matrices, reducing trainable parameters by >99% and GPU VRAM requirements drastically.

2. **Q: Explain QLoRA and how it further reduces memory footprint.**  
   *A:* QLoRA quantizes the frozen base model to 4-bit NormalFloat (NF4) while maintaining full precision for LoRA adapters, allowing 7B+ parameter models to be fine-tuned on single consumer GPUs.
