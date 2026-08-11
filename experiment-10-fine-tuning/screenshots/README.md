# Experiment 10 — Screenshots & Visual Artifacts Directory

**Course Code:** MR23-1CS0436
**Experiment Name:** Fine-Tuning for Domain Adaptation

---

## 📌 Overview

This directory stores verified visual evidence and runtime application screenshots demonstrating the **Fine-Tuning for Domain Adaptation** web application running on port `8009`.

---

## 📷 Verified Screenshots & Cryptographic Hashes

| View | Filename | SHA-256 Hash | Byte Size |
| :--- | :--- | :--- | :--- |
| **01. Initial Home Interface** | `01-home-interface.png` | `B98541F16395913EC02950A6382684A40A163FCA74450042D3DE8C8619E3A89A` | 285,486 B |
| **02. PyTorch Training Loss Curves** | `02-training-loss-curves.png` | `5B15FA36F092E6687C6CDB8F95FEF5A905F10F5E06D9891937A02E186718E170` | 296,447 B |
| **03. Base vs Fine-Tuned Evaluation** | `03-base-vs-finetuned-eval.png` | `9D05685BFE6930D28761DBE7EC59B3AF8411DA1065D75B3319B3ED29C37829BD` | 282,634 B |
| **04. Accuracy Improvement Gauge** | `04-accuracy-improvement-gauge.png` | `9D05685BFE6930D28761DBE7EC59B3AF8411DA1065D75B3319B3ED29C37829BD` | 282,634 B |

### Verified View Contents:
1. **`01-home-interface.png`**: Initial Web UI studio setup showing canonical LoRA hyperparameter controls (Rank $r=8$, $\alpha=16$, Epochs=5, LR=0.05), dataset statistics, and empty training workbench.
2. **`02-training-loss-curves.png`**: Training job execution summary (`Trainable Params: 160`, `Frozen Base Params: 68`, `Delta Trainable: +0.788014 > 0.0`, `Delta Frozen: 0.000000`) and epoch loss trajectory table across 5 epochs.
3. **`03-base-vs-finetuned-eval.png`**: Base Model (LoRA Disabled, 20% accuracy) vs. Fine-Tuned Model (LoRA Adapted, 40% accuracy) side-by-side comparison cards displaying +20 percentage points gain (+100% relative).
4. **`04-accuracy-improvement-gauge.png`**: Benchmark evaluation cards displaying domain adaptation output, +20 percentage points gain, and +100% relative performance improvement.
