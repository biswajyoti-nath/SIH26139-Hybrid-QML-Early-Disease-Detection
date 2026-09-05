import os
import json
from backend.core.config import ExperimentConfig
from backend.core.experiment_runner import ExperimentRunner

def test_experiment_runner_smoke():
    # Use a minimal config for smoke test
    cfg_dict = {
        "experiment_id": "smoke_test_001",
        "dataset_name": "WDBC",
        "split_strategy": "stratified_holdout",
        "test_size": 0.20,
        "random_seed": 42,
        "n_pca_components": 2,
        "models": {
            "svm": {"kernel": "linear", "random_state": 42}
        }
    }
    
    with open("experiments/configs/smoke_cfg.json", "w") as f:
        json.dump(cfg_dict, f)
        
    cfg = ExperimentConfig.load_from_json("experiments/configs/smoke_cfg.json")
    runner = ExperimentRunner(cfg)
    runner.run()
    
    # Check that output file is generated
    results_dir = "experiments/results/"
    files = [f for f in os.listdir(results_dir) if f.startswith("smoke_test_001")]
    assert len(files) >= 1
    
    # Check contents
    with open(os.path.join(results_dir, files[-1]), "r") as f:
        res = json.load(f)
        
    assert res["experiment_id"] == "smoke_test_001"
    assert "svm" in res["results"]
    assert "metrics" in res["results"]["svm"]
    assert "f1" in res["results"]["svm"]["metrics"]
    
    # Cleanup
    os.remove("experiments/configs/smoke_cfg.json")
    for file in files:
        os.remove(os.path.join(results_dir, file))
