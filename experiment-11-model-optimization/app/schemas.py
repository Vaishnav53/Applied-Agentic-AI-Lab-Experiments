"""
Pydantic API Request/Response Schemas
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class OptimizationMetrics(BaseModel):
    file_size_gb: float
    vram_usage_gb: float
    latency_ms: float
    throughput_tokens_sec: float
    quality_retention_percent: float

class OptimizationProfile(BaseModel):
    level_name: str  # "FP16 Baseline", "INT8 Quantization", "INT4 Block Quantization", "3B Student Distillation"
    technique: str
    description: str
    metrics: OptimizationMetrics

class OptimizationRequest(BaseModel):
    base_model_name: Optional[str] = Field(default="Llama-3-8B-Instruct", description="Base foundation model name")
    target_hardware: Optional[str] = Field(default="NVIDIA RTX 4090 (24GB VRAM)", description="Target deployment hardware")

class OptimizationComparisonResponse(BaseModel):
    base_model_name: str
    target_hardware: str
    profiles: List[OptimizationProfile]
    vram_reduction_champion: str
    throughput_champion: str
    optimization_synthesis: str
    evaluation_duration_ms: float
