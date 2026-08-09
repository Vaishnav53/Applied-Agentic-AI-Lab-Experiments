"""
Pydantic API Request/Response Schemas
Experiment 09 — Reasoning Model Benchmarking (MR23-1CS0436)
"""

from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class BenchmarkTask(BaseModel):
    task_id: str
    title: str
    domain: str
    complexity: str
    problem_statement: str
    ground_truth_key_factors: List[str]

class StrategyMetrics(BaseModel):
    correctness_score: int  # 0-100
    logical_rigor_score: int  # 0-100
    latency_ms: float
    estimated_tokens: int
    tool_invocations_count: int

class StrategyResult(BaseModel):
    strategy_name: str  # "Zero-Shot", "Chain-of-Thought", "ReAct", "Multi-Agent"
    output_summary: str
    reasoning_steps: List[str]
    metrics: StrategyMetrics

class BenchmarkRequest(BaseModel):
    task_id: Optional[str] = Field(default="TASK-CYBER-01", description="Benchmark task ID to execute")
    custom_problem_statement: Optional[str] = Field(default=None, description="Custom problem statement")

class BenchmarkComparisonResponse(BaseModel):
    task_id: str
    task_title: str
    domain: str
    complexity: str
    problem_statement: str
    strategy_results: List[StrategyResult]
    winning_strategy_accuracy: str
    winning_strategy_efficiency: str
    tradeoff_synthesis: str
    benchmark_duration_ms: float
