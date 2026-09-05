import numpy as np
import pytest
from backend.quantum.pennylane_vqc import PennyLaneVQC

def test_vqc_initialization_and_forward():
    vqc = PennyLaneVQC(n_qubits=3, n_layers=2, random_state=42)
    assert vqc.weights.shape == (2, 3)
    x = np.array([0.1, 0.5, 0.9])
    prob = vqc._forward(vqc.weights, x)
    assert 0.0 <= prob <= 1.0

def test_vqc_fit_predict():
    vqc = PennyLaneVQC(n_qubits=2, n_layers=1, iterations=5, learning_rate=0.1, random_state=42)
    X = np.array([[0.0, 0.1], [np.pi, np.pi/2], [0.1, 0.2], [np.pi/2, np.pi]])
    y = np.array([0, 1, 0, 1])
    
    # Store old weights to check if they change
    old_weights = vqc.weights.copy()
    
    vqc.fit(X, y)
    
    # Check weights actually changed
    assert not np.allclose(old_weights, vqc.weights)
    
    # Check history populated
    assert len(vqc.history_) == 5
    
    # Check probabilities shape
    probas = vqc.predict_proba(X)
    assert probas.shape == (4, 2)
    np.testing.assert_array_almost_equal(np.sum(probas, axis=1), np.ones(4))
    assert np.all((probas >= 0.0) & (probas <= 1.0))
    
    # Check predictions shape and type
    preds = vqc.predict(X)
    assert preds.shape == (4,)
    assert set(np.unique(preds)).issubset({0, 1})

def test_vqc_determinism():
    X = np.array([[0.1, 0.2]])
    vqc1 = PennyLaneVQC(n_qubits=2, n_layers=1, random_state=42)
    vqc2 = PennyLaneVQC(n_qubits=2, n_layers=1, random_state=42)
    
    prob1 = vqc1.predict_proba(X)
    prob2 = vqc2.predict_proba(X)
    np.testing.assert_array_almost_equal(prob1, prob2)

def test_vqc_bce_loss():
    vqc = PennyLaneVQC(n_qubits=2, n_layers=1, iterations=2, learning_rate=0.1, random_state=42, loss_fn="bce")
    X = np.array([[0.0, 0.1], [np.pi, np.pi/2], [0.1, 0.2], [np.pi/2, np.pi]])
    y = np.array([0, 1, 0, 1])
    
    old_weights = vqc.weights.copy()
    vqc.fit(X, y)
    
    assert not np.allclose(old_weights, vqc.weights)
    assert len(vqc.history_) == 2
