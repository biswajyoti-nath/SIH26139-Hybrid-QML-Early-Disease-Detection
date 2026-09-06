import pytest
from backend.core.suitability_router import SuitabilityRouter

def test_router_classical_preferred_wdbc():
    profile = {"variance_retained": 0.927}
    c_metrics = {"roc_auc": 0.995}
    q_metrics = {"qsvm": {"roc_auc": 0.842}, "vqc": {"roc_auc": 0.665}}
    runtimes = {"classical": 0.25, "qsvm": 400, "vqc": 1900}
    
    res = SuitabilityRouter.route(profile, c_metrics, q_metrics, runtimes)
    assert res["recommendation"] == "CLASSICAL PREFERRED"
    assert res["best_quantum_pathway"] == "qsvm"

def test_router_classical_preferred_parkinsons():
    profile = {"variance_retained": 0.470}
    c_metrics = {"roc_auc": 0.815}
    q_metrics = {"qsvm": {"roc_auc": 0.504}, "vqc": {"roc_auc": 0.549}}
    runtimes = {"classical": 1.0, "qsvm": 400, "vqc": 1900}
    
    res = SuitabilityRouter.route(profile, c_metrics, q_metrics, runtimes)
    assert res["recommendation"] == "CLASSICAL PREFERRED"
    assert "bottleneck" in res["reason"].lower()

def test_router_inconclusive_missing_quantum():
    profile = {"variance_retained": 0.90}
    c_metrics = {"roc_auc": 0.80}
    q_metrics = {}
    runtimes = {}
    
    res = SuitabilityRouter.route(profile, c_metrics, q_metrics, runtimes)
    assert res["recommendation"] == "INCONCLUSIVE"
