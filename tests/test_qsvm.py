import pytest
import numpy as np
from backend.quantum.pennylane_qsvm import PennyLaneQSVM

def test_qsvm_kernel_dimensions():
    model = PennyLaneQSVM(n_qubits=4)
    X1 = np.random.random((10, 4))
    X2 = np.random.random((5, 4))
    K = model.kernel_matrix(X1, X2)
    assert K.shape == (10, 5), f"Expected (10, 5), got {K.shape}"

def test_qsvm_kernel_symmetry():
    model = PennyLaneQSVM(n_qubits=4)
    X = np.random.random((10, 4))
    K = model.kernel_matrix(X, X)
    assert np.allclose(K, K.T), "Kernel matrix should be symmetric"
    assert np.allclose(np.diag(K), 1.0), "Kernel matrix diagonal should be 1.0 for identical samples"

def test_qsvm_fit_predict():
    model = PennyLaneQSVM(n_qubits=4)
    X = np.random.random((20, 4))
    y = np.random.randint(0, 2, 20)
    model.fit(X, y)
    preds = model.predict(X)
    assert preds.shape == (20,), "Predict shape mismatch"
    probas = model.predict_proba(X)
    assert probas.shape == (20, 2), "Predict proba shape mismatch"
