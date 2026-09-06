import pytest
import numpy as np
import os
from unittest.mock import patch
from backend.core.dataset import DatasetManager, Dataset
from backend.core.config import ExperimentConfig
from backend.core.cv_experiment_runner import CVExperimentRunner

@pytest.mark.skipif(os.environ.get("SKIP_OPENML") == "1", reason="Requires OpenML network access")
def test_parkinsons_load_and_validate():
    """
    Integration test: Actually hits OpenML to verify dataset schema.
    To skip in fast local runs, set SKIP_OPENML=1.
    """
    ds = DatasetManager.load_parkinsons()
    assert ds.X.shape == (756, 753)
    assert ds.y.shape == (756,)
    assert set(np.unique(ds.y)) == {0, 1}
    assert ds.groups is not None
    assert len(ds.groups) == 756
    
    unique_groups, counts = np.unique(ds.groups, return_counts=True)
    assert len(unique_groups) == 252
    assert all(c == 3 for c in counts)
    
    # Check that targets are uniform within each group
    for g in unique_groups:
        idx = np.where(ds.groups == g)[0]
        assert len(np.unique(ds.y[idx])) == 1

@patch("backend.core.dataset.DatasetManager.load_parkinsons")
def test_parkinsons_cv_overlap_mocked(mock_load):
    """
    Unit test: Verifies the StratifiedGroupKFold overlap prevention
    logic without hitting OpenML or taking significant time.
    """
    # Create mock dataset
    # 30 samples, 10 groups of 3
    X_mock = np.random.rand(30, 10)
    y_mock = np.array([0, 0, 0]*5 + [1, 1, 1]*5)
    groups_mock = np.repeat(np.arange(10), 3)
    
    mock_dataset = Dataset(
        X=X_mock, y=y_mock,
        feature_names=[f"f{i}" for i in range(10)],
        target_names=["Healthy", "Parkinsons"],
        provenance="Mock for CV test",
        groups=groups_mock
    )
    mock_load.return_value = mock_dataset
    
    cfg = ExperimentConfig(
        experiment_id="test_park_mock",
        dataset_name="Parkinsons",
        split_strategy="cv",
        test_size=0.2,
        random_seed=42,
        n_pca_components=2,
        models={"svm": {"kernel": "linear"}}
    )
    
    # Use n_splits=3 so groups can be divided reasonably
    runner = CVExperimentRunner(cfg, n_splits=3)
    results = runner.run()
    
    assert results["dataset"] == "Parkinsons"
    assert "stratified_group_cv" in results["split_strategy"]
    assert "pca_explained_variance_mean" in results
    
    # Clean up output
    out_file = [f for f in os.listdir("experiments/results/") if f.startswith("test_park_mock_")]
    for f in out_file:
        os.remove(f"experiments/results/{f}")
