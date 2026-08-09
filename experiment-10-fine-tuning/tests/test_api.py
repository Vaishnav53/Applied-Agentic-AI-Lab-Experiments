"""
FastAPI Integration Tests
Experiment 10 — Fine-Tuning for Domain Adaptation (MR23-1CS0436)
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_stats_endpoint():
    response = client.get("/api/dataset/stats")
    assert response.status_code == 200
    stats = response.json()
    assert stats["train_samples_count"] >= 3

def test_api_train_endpoint():
    response = client.post("/api/train/run", json={
        "lora_rank": 8,
        "lora_alpha": 16,
        "learning_rate": 0.0002,
        "num_epochs": 2,
        "batch_size": 4
    })
    assert response.status_code == 200
    data = response.json()
    assert data["training_status"] == "COMPLETED"
    assert len(data["epoch_metrics"]) == 2

def test_api_eval_endpoint():
    response = client.post("/api/eval/run", json={
        "instruction": "What is the recommended NIST PQC key exchange algorithm?"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["finetuned_model_accuracy"] >= 90
