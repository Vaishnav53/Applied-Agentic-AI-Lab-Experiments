"""
Model Evaluator Service Unit Tests
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
"""

import os
from app.schemas import EvalRequest, FineTuningConfig
from app.services.evaluator import ModelEvaluatorService
from app.services.trainer import RealLoRATrainer

def test_evaluate_models_comparison():
    evaluator = ModelEvaluatorService()
    req = EvalRequest(instruction="Explain how to mitigate CVE-2023-23397 Outlook vulnerability.")
    res = evaluator.evaluate_models(req)

    assert res.total_evaluated_samples == 10
    assert res.finetuned_model_accuracy >= 0.0
    assert res.base_model_accuracy >= 0.0
    assert res.accuracy_improvement_percentage_points == round(res.finetuned_model_accuracy - res.base_model_accuracy, 2)
    assert res.relative_improvement_percent >= -100.0
    assert "Base Un-adapted Model" in res.base_model_output
    assert "Fine-Tuned Domain Adapter" in res.finetuned_model_output

def test_canonical_reproducible_workflow():
    trainer = RealLoRATrainer()
    job_res = trainer.run_training_job(FineTuningConfig(num_epochs=10, learning_rate=0.05))

    assert os.path.exists(job_res.checkpoint_path)

    evaluator = ModelEvaluatorService()
    eval_res = evaluator.evaluate_models(EvalRequest())

    assert eval_res.total_evaluated_samples == 10
    assert eval_res.base_correct_count >= 0
    assert eval_res.finetuned_correct_count >= 0
    assert eval_res.accuracy_improvement_percentage_points == round(eval_res.finetuned_model_accuracy - eval_res.base_model_accuracy, 2)
