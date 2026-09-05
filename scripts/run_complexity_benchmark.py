import json
import time
import os
import numpy as np
from sklearn.model_selection import StratifiedKFold
from backend.core.synthetic_generator import SyntheticGenerator
from backend.core.complexity_profiler import ComplexityProfiler
from backend.core.experiment_runner import ModelFactory
from backend.core.preprocessing import PreprocessingEngine
from backend.core.evaluation import EvaluationEngine

def run_benchmark(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
    
    regimes = config["regimes"]
    seeds = config["seeds"]
    models = config["models"]
    n_samples = config["n_samples"]
    vqc_config = config["quantum_config"]
    
    results = {
        "metadata": config,
        "regime_profiles": {},
        "benchmark": {}
    }
    
    for regime in regimes:
        results["benchmark"][regime] = {}
        for model in models:
            results["benchmark"][regime][model] = {}
            for seed in seeds:
                results["benchmark"][regime][model][str(seed)] = {}

    for seed in seeds:
        print(f"\n{'='*40}\nRunning SEED {seed}\n{'='*40}")
        for regime in regimes:
            print(f"\n--- Regime: {regime} ---")
            
            # Generate dataset
            X, y = SyntheticGenerator.generate(regime, n_samples=n_samples, random_state=seed)
            
            # Profile complexity (only save once per regime/seed)
            profile = ComplexityProfiler.profile(X, y, random_state=seed)
            if regime not in results["regime_profiles"]:
                results["regime_profiles"][regime] = {}
            results["regime_profiles"][regime][str(seed)] = profile
            
            print(f"Profile: n={profile['n_samples']}, dims={profile['n_features']}, LR_acc={profile['linear_separability_score']:.4f}")
            
            for model_name in models:
                print(f"Evaluating {model_name}...")
                skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
                
                fold_metrics = []
                fold_times = []
                
                for train_idx, test_idx in skf.split(X, y):
                    X_train, X_test = X[train_idx], X[test_idx]
                    y_train, y_test = y[train_idx], y[test_idx]
                    
                    # Preprocess (PCA to 6 dimensions to match qubit budget, like WDBC)
                    n_components = vqc_config["n_qubits"]
                    processor = PreprocessingEngine.build_pipeline(n_pca_components=n_components, random_seed=seed)
                    X_train_proc = processor.fit_transform(X_train)
                    X_test_proc = processor.transform(X_test)
                    
                    # Instantiate model
                    if model_name == "vqc":
                        model = ModelFactory.create_classical_model("vqc", {
                            "random_state": seed,
                            "n_qubits": vqc_config["n_qubits"],
                            "n_layers": vqc_config["n_layers"],
                            "loss_fn": vqc_config["loss_fn"],
                            "iterations": vqc_config["iterations"],
                            "learning_rate": vqc_config["learning_rate"]
                        })
                    else:
                        model = ModelFactory.create_classical_model(model_name, {"random_state": seed})
                        
                    start_time = time.time()
                    model.fit(X_train_proc, y_train)
                    train_time = time.time() - start_time
                    
                    y_pred = model.predict(X_test_proc)
                    y_prob = model.predict_proba(X_test_proc)
                    
                    metrics = EvaluationEngine.evaluate(y_test, y_pred, y_prob)
                    fold_metrics.append(metrics)
                    fold_times.append(train_time)
                
                # Aggregate metrics for this seed across folds
                agg = {
                    "accuracy": np.mean([m["accuracy"] for m in fold_metrics]),
                    "roc_auc": np.mean([m["roc_auc"] for m in fold_metrics]),
                    "f1": np.mean([m["f1"] for m in fold_metrics]),
                    "training_time_s": np.mean(fold_times)
                }
                
                results["benchmark"][regime][model_name][str(seed)] = agg
                print(f"  -> ROC-AUC: {agg['roc_auc']:.4f} (Time: {agg['training_time_s']:.2f}s)")

    # Save final results
    os.makedirs("experiments/results", exist_ok=True)
    timestamp = int(time.time())
    out_file = f"experiments/results/complexity_benchmark_{timestamp}.json"
    with open(out_file, "w") as f:
        json.dump(results, f, indent=4) # wait, json doesn't have prompt_dump, fixing below
        
    print(f"\nSaved benchmark results to {out_file}")

if __name__ == "__main__":
    import sys; run_benchmark(sys.argv[1] if len(sys.argv) > 1 else "experiments/configs/complexity_regimes_v1.json")
