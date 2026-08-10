"""
Distillation Engine Unit Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

import os
from app.services.distiller import RealKnowledgeDistillationService

def test_distillation_profile():
    distiller = RealKnowledgeDistillationService()
    profile = distiller.get_distillation_profile()

    assert os.path.exists(profile.artifact_path)
    assert profile.metrics.serialized_file_size_mb > 0
    assert profile.metrics.compression_ratio_percent > 0.0
    assert profile.metrics.throughput_tokens_sec > 100.0
