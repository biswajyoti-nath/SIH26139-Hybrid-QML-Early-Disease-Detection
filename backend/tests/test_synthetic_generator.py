import pytest
import numpy as np
from backend.core.synthetic_generator import SyntheticGenerator
from backend.core.complexity_profiler import ComplexityProfiler

def test_synthetic_generator_determinism():
    X1, y1 = SyntheticGenerator.generate("R1_SIMPLE", n_samples=100, random_state=42)
    X2, y2 = SyntheticGenerator.generate("R1_SIMPLE", n_samples=100, random_state=42)
    np.testing.assert_array_equal(X1, X2)
    np.testing.assert_array_equal(y1, y2)

def test_synthetic_generator_dimensions():
    X_simple, _ = SyntheticGenerator.generate("R1_SIMPLE", n_samples=100)
    assert X_simple.shape == (100, 10)
    
    X_hd, _ = SyntheticGenerator.generate("R5_HIGH_DIMENSIONAL", n_samples=100)
    assert X_hd.shape == (100, 100)
    
    X_nonlinear, _ = SyntheticGenerator.generate("R2_NONLINEAR", n_samples=100)
    assert X_nonlinear.shape == (100, 10)

def test_complexity_profiler_output():
    X, y = SyntheticGenerator.generate("R1_SIMPLE", n_samples=100)
    profile = ComplexityProfiler.profile(X, y)
    
    assert "n_samples" in profile
    assert profile["n_samples"] == 100
    assert "n_features" in profile
    assert profile["n_features"] == 10
    assert "class_balance_pos_ratio" in profile
    assert 0.0 <= profile["class_balance_pos_ratio"] <= 1.0
    assert "mean_abs_feature_correlation" in profile
    assert "linear_separability_score" in profile
    # R1_SIMPLE should be highly linearly separable
    assert profile["linear_separability_score"] > 0.8
