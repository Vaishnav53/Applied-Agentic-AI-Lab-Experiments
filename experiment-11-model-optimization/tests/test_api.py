"""
FastAPI Integration Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api_benchmark_endpoint():
    response = client.post("/api/optimization/benchmark", json={
        "base_model_name": "Llama-3-70B-Instruct",
        "target_hardware": "NVIDIA A100 (80GB VRAM)"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["base_model_name"] == "Llama-3-70B-Instruct"
    assert len(data["profiles"]) == 4
    assert data["evaluation_duration_ms"] >= 0
