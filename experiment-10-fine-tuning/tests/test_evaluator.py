"""
Model Evaluator Service Unit Tests
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
"""

from app.schemas import EvalRequest
from app.services.evaluator import ModelEvaluatorService

def test_evaluate_models_comparison():
    evaluator = ModelEvaluatorService()
    req = EvalRequest(instruction="Explain how to mitigate CVE-2023-23397 Outlook vulnerability.")
    res = evaluator.evaluate_models(req)

    assert res.finetuned_model_accuracy > res.base_model_accuracy
    assert res.finetuned_model_hallucination_rate < res.base_model_hallucination_rate
    assert res.accuracy_improvement_percent > 50
    assert "KB5023151" in res.finetuned_model_output
