"""
Real Model & Autograd LoRA Unit Tests
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
"""

import os
import tempfile
from app.services.model_engine import CyberSecurityLoRAModel

def test_trainable_and_frozen_parameter_counts():
    model = CyberSecurityLoRAModel(in_dim=16, out_dim=4, lora_rank=8, lora_alpha=16)
    assert model.get_frozen_parameter_count() == 68
    assert model.get_trainable_parameter_count() == 160

def test_real_training_parameter_change():
    model = CyberSecurityLoRAModel(in_dim=16, out_dim=4, lora_rank=8, lora_alpha=16)
    snapshot_before = model.get_parameter_snapshot()

    x = [0.5] * 16
    y = [1.0, 0.0, 0.0, 0.0]

    loss1 = model.train_step(x, y, lr=0.05)
    loss2 = model.train_step(x, y, lr=0.05)

    diff_norm = model.compute_parameter_change_norm(snapshot_before)
    assert diff_norm > 0.0, "Trainable parameters must numerically change after training steps"

def test_checkpoint_save_and_reload():
    model = CyberSecurityLoRAModel(in_dim=16, out_dim=4, lora_rank=8, lora_alpha=16)
    x = [0.2] * 16
    y = [0.0, 1.0, 0.0, 0.0]
    model.train_step(x, y, lr=0.05)

    with tempfile.TemporaryDirectory() as tmpdir:
        ckpt_path = os.path.join(tmpdir, "lora_adapter.pt")
        model.save_checkpoint(ckpt_path)
        assert os.path.exists(ckpt_path)

        new_model = CyberSecurityLoRAModel(in_dim=16, out_dim=4, lora_rank=8, lora_alpha=16)
        new_model.load_checkpoint(ckpt_path)

        assert new_model.A == model.A
        assert new_model.B == model.B
