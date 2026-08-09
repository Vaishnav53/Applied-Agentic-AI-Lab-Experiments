"""
LoRA Trainer Simulator Unit Tests
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
"""

from app.schemas import FineTuningConfig
from app.services.trainer import LoRATrainerSimulator

def test_run_training_job():
    trainer = LoRATrainerSimulator()
    config = FineTuningConfig(lora_rank=16, lora_alpha=32, num_epochs=3)
    res = trainer.run_training_job(config)

    assert res.training_status == "COMPLETED"
    assert len(res.epoch_metrics) == 3
    assert res.final_train_loss < res.epoch_metrics[0].train_loss
    assert res.final_val_loss < res.epoch_metrics[0].val_loss
    assert res.final_perplexity > 0
