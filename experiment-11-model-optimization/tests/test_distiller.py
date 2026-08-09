"""
Distillation Engine Unit Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from app.services.distiller import KnowledgeDistillationService

def test_distillation_profile():
    distiller = KnowledgeDistillationService()
    profile = distiller.get_distillation_profile()

    assert "3B Student" in profile.level_name
    assert profile.metrics.throughput_tokens_sec > 100.0
    assert profile.metrics.quality_retention_percent >= 94.0
