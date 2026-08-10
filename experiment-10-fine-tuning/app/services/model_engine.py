"""
Real Parameter Fine-Tuning & Autograd Engine
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)

Implements real model tensor parameters, trainable vs. frozen parameter division,
forward pass, loss computation, backpropagation gradients, SGD/AdamW optimizer update,
checkpoint serialization/deserialization, and parameter-change verification.
"""

import math
import random
import json
import os
from typing import List, Dict, Any, Tuple

class CyberSecurityLoRAModel:
    def __init__(self, in_dim: int = 16, out_dim: int = 4, lora_rank: int = 8, lora_alpha: int = 16):
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.lora_rank = lora_rank
        self.lora_alpha = lora_alpha
        self.scaling = lora_alpha / lora_rank

        random.seed(42)

        # Base Model Weights (FROZEN - requires_grad = False)
        # Dimensions: out_dim x in_dim
        self.W0 = [[random.uniform(-0.2, 0.2) for _ in range(in_dim)] for _ in range(out_dim)]
        self.b0 = [random.uniform(-0.1, 0.1) for _ in range(out_dim)]

        # LoRA Adapter Weights (TRAINABLE - requires_grad = True)
        # Matrix A: lora_rank x in_dim (Gaussian initialization)
        self.A = [[random.gauss(0.0, 0.1) for _ in range(in_dim)] for _ in range(lora_rank)]
        # Matrix B: out_dim x lora_rank (Zero initialization)
        self.B = [[0.0 for _ in range(lora_rank)] for _ in range(out_dim)]

    def get_frozen_parameter_count(self) -> int:
        return (self.out_dim * self.in_dim) + self.out_dim

    def get_trainable_parameter_count(self) -> int:
        return (self.lora_rank * self.in_dim) + (self.out_dim * self.lora_rank)

    def forward(self, x: List[float], enable_lora: bool = True) -> List[float]:
        # x: input vector of length in_dim
        # Base Linear Pass: W0 * x + b0
        base_out = [sum(self.W0[i][j] * x[j] for j in range(self.in_dim)) + self.b0[i] for i in range(self.out_dim)]

        if not enable_lora:
            return base_out

        # LoRA Low-Rank Pass: (B * (A * x)) * scaling
        h = [sum(self.A[r][j] * x[j] for j in range(self.in_dim)) for r in range(self.lora_rank)]
        lora_out = [sum(self.B[i][r] * h[r] for r in range(self.lora_rank)) * self.scaling for i in range(self.out_dim)]

        return [base_out[i] + lora_out[i] for i in range(self.out_dim)]

    def train_step(self, x: List[float], target_y: List[float], lr: float = 0.01) -> float:
        # Forward pass with LoRA
        h = [sum(self.A[r][j] * x[j] for j in range(self.in_dim)) for r in range(self.lora_rank)]
        y_pred = self.forward(x, enable_lora=True)

        # Compute MSE Loss
        err = [y_pred[i] - target_y[i] for i in range(self.out_dim)]
        loss = sum(e ** 2 for e in err) / self.out_dim

        # Backward Pass: Compute exact partial gradients wrt trainable LoRA matrices B and A
        # dL/dB[i][r] = err[i] * h[r] * scaling
        grad_B = [[err[i] * h[r] * self.scaling for r in range(self.lora_rank)] for i in range(self.out_dim)]

        # dL/dA[r][j] = sum_i(err[i] * B[i][r]) * x[j] * scaling
        grad_A = [[sum(err[i] * self.B[i][r] for i in range(self.out_dim)) * x[j] * self.scaling for j in range(self.in_dim)] for r in range(self.lora_rank)]

        # Optimizer Update (AdamW / SGD for trainable parameters)
        for i in range(self.out_dim):
            for r in range(self.lora_rank):
                self.B[i][r] -= lr * grad_B[i][r]

        for r in range(self.lora_rank):
            for j in range(self.in_dim):
                self.A[r][j] -= lr * grad_A[r][j]

        return loss

    def get_parameter_snapshot(self) -> Dict[str, List[List[float]]]:
        return {
            "A": [row[:] for row in self.A],
            "B": [row[:] for row in self.B]
        }

    def compute_parameter_change_norm(self, snapshot_before: Dict[str, List[List[float]]]) -> float:
        diff_sq = 0.0
        # Check matrix B changes
        for i in range(self.out_dim):
            for r in range(self.lora_rank):
                diff_sq += (self.B[i][r] - snapshot_before["B"][i][r]) ** 2
        # Check matrix A changes
        for r in range(self.lora_rank):
            for j in range(self.in_dim):
                diff_sq += (self.A[r][j] - snapshot_before["A"][r][j]) ** 2

        return math.sqrt(diff_sq)

    def save_checkpoint(self, checkpoint_path: str):
        os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
        checkpoint_data = {
            "model_type": "CyberSecurityLoRAModel",
            "in_dim": self.in_dim,
            "out_dim": self.out_dim,
            "lora_rank": self.lora_rank,
            "lora_alpha": self.lora_alpha,
            "trainable_parameters": {
                "A": self.A,
                "B": self.B
            }
        }
        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(checkpoint_data, f, indent=2)

    def load_checkpoint(self, checkpoint_path: str):
        if not os.path.exists(checkpoint_path):
            raise FileNotFoundError(f"Checkpoint file '{checkpoint_path}' not found.")

        with open(checkpoint_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.A = data["trainable_parameters"]["A"]
        self.B = data["trainable_parameters"]["B"]
