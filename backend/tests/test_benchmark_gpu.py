import pytest
from unittest.mock import patch, MagicMock

# The module is scripts.benchmark_gpu
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import scripts.benchmark_gpu as bgpu

@patch("scripts.benchmark_gpu.qml.device")
def test_sanity_check_mocked(mock_device):
    # Mock CPU and GPU devices to just return dummy objects that don't fail initialization
    mock_dev_cpu = MagicMock()
    mock_dev_cpu.name = "Mock CPU"
    mock_dev_gpu = MagicMock()
    mock_dev_gpu.name = "Mock GPU"
    
    # We don't actually want to run QNodes in a unit test since that hits the Pennylane engine.
    # Instead, we just patch the QNode execution to return identical arrays.
    with patch("scripts.benchmark_gpu.qml.QNode", return_value=lambda weights, inputs: 0.42):
        with patch("scripts.benchmark_gpu.time.perf_counter", side_effect=[0, 1, 0, 0.1]):
            # This should pass without raising an error
            res = bgpu.sanity_check()
            assert res is True

@patch("scripts.benchmark_gpu.sanity_check", return_value=True)
def test_benchmark_runner(mock_sanity):
    # Just ensure we can import and it has the right structure
    assert hasattr(bgpu, "benchmark_realistic_workload")
