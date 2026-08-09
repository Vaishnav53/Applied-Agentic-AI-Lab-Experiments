"""
Optimization Engine Unit Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from app.schemas import OptimizationRequest
from app.services.optimization_engine import ModelOptimizationEngine

def test_run_optimization_benchmark():
    engine = ModelOptimizationEngine()
    req = OptimizationRequest(base_model_name="Llama-3-8B-Instruct", target_hardware="NVIDIA RTX 4090")
    res = engine.run_optimization_benchmark(req)

    assert len(res.profiles) == 4
    assert res.vram_reduction_champion == "3B Student Model Distillation"
    assert res.throughput_champion == "3B Student Model Distillation"
    assert "Optimization Synthesis" in res.optimization_synthesis
