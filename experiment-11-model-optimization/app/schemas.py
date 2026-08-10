"""
Pydantic API Request/Response Schemas
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class OptimizationMetrics(BaseModel):
    serialized_file_size_mb: float
    compression_ratio_percent: float
    vram_usage_gb: float
    measured_latency_ms: float
    throughput_tokens_sec: float
    quality_retention_percent: float

class OptimizationProfile(BaseModel):
    level_name: str  # "FP32 Baseline", "Dynamic INT8 Post-Training Quantization", "Packed INT4 Uniform Quantization", "Distilled 2-Layer Student Model"
    technique: str
    description: str
    artifact_path: str
    metrics: OptimizationMetrics

class OptimizationRequest(BaseModel):
    base_model_name: Optional[str] = Field(default="CyberSecurity-FP32-8B-Base", description="Base foundation model name")
    target_hardware: Optional[str] = Field(default="Intel Core i7 CPU / Edge Workstation", description="Target deployment hardware")

class OptimizationComparisonResponse(BaseModel):
    base_model_name: str
    target_hardware: str
    profiles: List[OptimizationProfile]
    file_size_reduction_champion: str
    throughput_champion: str
    optimization_synthesis: str
    evaluation_duration_ms: float
