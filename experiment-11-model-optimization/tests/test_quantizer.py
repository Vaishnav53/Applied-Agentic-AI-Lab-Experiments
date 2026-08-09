"""
Quantization Engine Unit Tests
Experiment 11 — Model Optimization Experiment (MR23-1CS0436)
"""

from app.services.quantizer import QuantizationEngineService

def test_quantization_profiles():
    quantizer = QuantizationEngineService()
    fp16 = quantizer.get_fp16_profile()
    int8 = quantizer.get_int8_profile()
    int4 = quantizer.get_int4_profile()

    assert fp16.metrics.file_size_gb == 16.0
    assert int8.metrics.vram_usage_gb < fp16.metrics.vram_usage_gb
    assert int4.metrics.vram_usage_gb < int8.metrics.vram_usage_gb
    assert int4.metrics.throughput_tokens_sec > fp16.metrics.throughput_tokens_sec
