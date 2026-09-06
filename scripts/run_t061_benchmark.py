import argparse
import os
import json
from backend.core.config import ExperimentConfig
from backend.core.dataset import DatasetManager
from backend.core.complexity_profiler import ComplexityProfiler
from backend.core.cv_experiment_runner import CVExperimentRunner

def run_benchmark(config_path: str):
    print(f"\n==========================================")
    print(f"Running Experiment: {config_path}")
    print(f"==========================================\n")
    
    cfg = ExperimentConfig.load_from_json(config_path)
    
    # 1. Profile Complexity
    if cfg.dataset_name.lower() == "parkinsons":
        dataset = DatasetManager.load_parkinsons()
    else:
        dataset = DatasetManager.load_wdbc()
        
    print(f"--- Complexity Profile for {cfg.dataset_name} ---")
    profile = ComplexityProfiler.profile(dataset.X, dataset.y, random_state=cfg.random_seed)
    for k, v in profile.items():
        print(f"  {k}: {v}")
    print(f"-----------------------------------------\n")
    
    # 2. Run Validation with injected profile
    runner = CVExperimentRunner(cfg, n_splits=5)
    results = runner.run(complexity_profile=profile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="T-061 Real PS-Relevant Biomedical Complexity Benchmark")
    parser.add_argument("--dataset", type=str, choices=["WDBC", "Parkinsons", "all"], default="all")
    parser.add_argument("--sensitivity", action="store_true", help="Run PCA sensitivity experiment for Parkinson's")
    args = parser.parse_args()
    
    if args.dataset in ["WDBC", "all"]:
        run_benchmark("experiments/configs/exp_061_wdbc_control.json")
        
    if args.dataset in ["Parkinsons", "all"]:
        run_benchmark("experiments/configs/exp_061_parkinsons.json")
        
    if args.sensitivity:
        run_benchmark("experiments/configs/exp_061_parkinsons_sensitivity.json")
