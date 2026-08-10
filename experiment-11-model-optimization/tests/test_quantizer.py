"""
Quantization Engine Unit Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

import os
from app.services.quantizer import RealQuantizationEngineService

def test_quantization_profiles_and_artifacts():
    quantizer = RealQuantizationEngineService()
    fp32 = quantizer.get_fp32_profile()
    int8 = quantizer.get_int8_profile()
    int4 = quantizer.get_int4_profile()

    assert os.path.exists(fp32.artifact_path)
    assert os.path.exists(int8.artifact_path)
    assert os.path.exists(int4.artifact_path)

    assert int8.metrics.serialized_file_size_mb < fp32.metrics.serialized_file_size_mb
    assert int4.metrics.serialized_file_size_mb < int8.metrics.serialized_file_size_mb
    assert int8.metrics.compression_ratio_percent > 0.0
    assert int4.metrics.compression_ratio_percent > int8.metrics.compression_ratio_percent
    assert int8.metrics.measured_latency_ms > 0.0
