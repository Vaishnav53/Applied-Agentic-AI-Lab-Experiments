"""
Fine-Tuning Trainer Simulator
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
Simulates LoRA rank adaptation training epochs, tracking loss curves, perplexity, and duration.
"""

import time
import math
from typing import List, Dict, Any
from app.schemas import FineTuningConfig, TrainingJobResponse, EpochMetric
from app.services.dataset_curator import load_jsonl_dataset, settings

class LoRATrainerSimulator:
    def __init__(self):
        self.service_name = "LoRA PEFT Fine-Tuning Simulator v1.0"

    def run_training_job(self, config: FineTuningConfig) -> TrainingJobResponse:
        start_time = time.time()
        train_samples = load_jsonl_dataset(settings.TRAIN_DATASET_PATH)
        val_samples = load_jsonl_dataset(settings.VAL_DATASET_PATH)

        num_epochs = config.num_epochs
        rank = config.lora_rank
        alpha = config.lora_alpha

        epoch_metrics: List[EpochMetric] = []

        # Initial baseline loss
        current_train_loss = 2.85
        current_val_loss = 3.10

        # Higher LoRA rank accelerates loss reduction
        decay_factor = 0.45 + (rank / 100.0)

        for epoch in range(1, num_epochs + 1):
            ep_start = time.time()
            
            # Loss decay curve simulation
            current_train_loss = max(0.15, current_train_loss * (1.0 - decay_factor * (1.0 / math.sqrt(epoch))))
            current_val_loss = max(0.25, current_val_loss * (1.0 - (decay_factor - 0.05) * (1.0 / math.sqrt(epoch))))
            perplexity = round(math.exp(current_val_loss), 2)
            
            ep_duration = round((time.time() - ep_start) * 1000 + 45.0, 2)

            epoch_metrics.append(EpochMetric(
                epoch=epoch,
                train_loss=round(current_train_loss, 4),
                val_loss=round(current_val_loss, 4),
                perplexity=perplexity,
                duration_ms=ep_duration
            ))

        total_duration = round((time.time() - start_time) * 1000, 2)

        return TrainingJobResponse(
            job_id=f"JOB-LORA-R{rank}-A{alpha}",
            model_name=f"Llama-3-8B-LoRA-Cyber-r{rank}",
            lora_rank=rank,
            lora_alpha=alpha,
            total_train_samples=len(train_samples),
            total_val_samples=len(val_samples),
            epoch_metrics=epoch_metrics,
            final_train_loss=epoch_metrics[-1].train_loss,
            final_val_loss=epoch_metrics[-1].val_loss,
            final_perplexity=epoch_metrics[-1].perplexity,
            training_status="COMPLETED",
            total_training_duration_ms=total_duration
        )
