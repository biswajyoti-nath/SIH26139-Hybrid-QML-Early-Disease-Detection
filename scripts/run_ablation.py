import os
import json
import time
import numpy as np
from backend.core.dataset import DatasetManager
from backend.core.config import ExperimentConfig
from backend.core.experiment_runner import ExperimentRunner

def run_config(config_dict, stage_name):
    cfg = ExperimentConfig(**config_dict)
    runner = ExperimentRunner(cfg)
    
    # Hijack store_results to return data
    original_store = runner._store_results
    def mock_store(results_out):
        runner.last_results = results_out
        original_store(results_out)
    runner._store_results = mock_store
    
    t0 = time.time()
    runner.run()
    t1 = time.time()
    
    res = runner.last_results["results"]["vqc"]["metrics"]
    print(f"\n[{stage_name}] Config: {config_dict['models']['vqc']}")
    print(f"[{stage_name}] Time: {t1-t0:.1f}s | ROC-AUC: {res['roc_auc']:.4f} | Accuracy: {res['accuracy']:.4f}\n")
    return res['roc_auc'], runner.last_results

def stage_a():
    print("=== STAGE A: QUBIT DIMENSION ===")
    results = {}
    for dim in [4, 6, 8]:
        cfg = {
            "experiment_id": f"ablation_A_dim{dim}",
            "dataset_name": "WDBC",
            "split_strategy": "stratified_holdout",
            "test_size": 0.2,
            "random_seed": 42,
            "n_pca_components": dim,
            "models": {
                "vqc": {
                    "n_qubits": dim, "n_layers": 3, "learning_rate": 0.05, 
                    "iterations": 25, "random_state": 42, "loss_fn": "mse"
                }
            }
        }
        auc, res = run_config(cfg, f"Stage A dim={dim}")
        results[dim] = auc
        
    best_dim = max(results.keys(), key=lambda d: results[d])
    print(f"WINNER STAGE A: {best_dim} qubits\n")
    return best_dim

def stage_b(best_dim):
    print("=== STAGE B: CIRCUIT DEPTH ===")
    results = {}
    for depth in [1, 2, 3]:
        cfg = {
            "experiment_id": f"ablation_B_depth{depth}",
            "dataset_name": "WDBC",
            "split_strategy": "stratified_holdout",
            "test_size": 0.2,
            "random_seed": 42,
            "n_pca_components": best_dim,
            "models": {
                "vqc": {
                    "n_qubits": best_dim, "n_layers": depth, "learning_rate": 0.05, 
                    "iterations": 25, "random_state": 42, "loss_fn": "mse"
                }
            }
        }
        auc, res = run_config(cfg, f"Stage B depth={depth}")
        results[depth] = auc
        
    best_depth = max(results.keys(), key=lambda d: results[d])
    print(f"WINNER STAGE B: {best_depth} layers\n")
    return best_depth

def stage_c(best_dim, best_depth):
    print("=== STAGE C: LOSS FUNCTION ===")
    results = {}
    for loss in ["mse", "bce"]:
        cfg = {
            "experiment_id": f"ablation_C_loss_{loss}",
            "dataset_name": "WDBC",
            "split_strategy": "stratified_holdout",
            "test_size": 0.2,
            "random_seed": 42,
            "n_pca_components": best_dim,
            "models": {
                "vqc": {
                    "n_qubits": best_dim, "n_layers": best_depth, "learning_rate": 0.05, 
                    "iterations": 25, "random_state": 42, "loss_fn": loss
                }
            }
        }
        auc, res = run_config(cfg, f"Stage C loss={loss}")
        results[loss] = auc
        
    best_loss = max(results.keys(), key=lambda d: results[d])
    print(f"WINNER STAGE C: {best_loss}\n")
    return best_loss
    
def stage_d(best_dim, best_depth, best_loss):
    print("=== STAGE D: ITERATIONS ===")
    results = {}
    for iters in [25, 50, 100]:
        cfg = {
            "experiment_id": f"ablation_D_iters_{iters}",
            "dataset_name": "WDBC",
            "split_strategy": "stratified_holdout",
            "test_size": 0.2,
            "random_seed": 42,
            "n_pca_components": best_dim,
            "models": {
                "vqc": {
                    "n_qubits": best_dim, "n_layers": best_depth, "learning_rate": 0.05, 
                    "iterations": iters, "random_state": 42, "loss_fn": best_loss
                }
            }
        }
        auc, res = run_config(cfg, f"Stage D iters={iters}")
        results[iters] = auc
        
    best_iters = max(results.keys(), key=lambda d: results[d])
    print(f"WINNER STAGE D: {best_iters}\n")
    return best_iters

if __name__ == "__main__":
    best_dim = stage_a()
    best_depth = stage_b(best_dim)
    best_loss = stage_c(best_dim, best_depth)
    best_iters = stage_d(best_dim, best_depth, best_loss)
    
    print("=======================================")
    print(f"OPTIMAL CONFIG: PCA={best_dim}, Depth={best_depth}, Loss={best_loss}, Iters={best_iters}")
    with open("experiments/configs/exp_005_ablation_best.json", "w") as f:
        json.dump({
            "experiment_id": "exp_005_ablation_final_cv",
            "dataset_name": "WDBC",
            "split_strategy": "stratified_cv_5fold",
            "test_size": 0.2,
            "random_seed": 42,
            "n_pca_components": best_dim,
            "models": {
                "vqc": {
                    "n_qubits": best_dim, "n_layers": best_depth, "learning_rate": 0.05, 
                    "iterations": best_iters, "random_state": 42, "loss_fn": best_loss
                },
                "svm": {"kernel": "linear", "random_state": 42},
                "random_forest": {"n_estimators": 100, "max_features": "sqrt", "random_state": 42},
                "xgboost": {"n_estimators": 100, "learning_rate": 0.1, "max_depth": 6, "eval_metric": "logloss", "random_state": 42}
            }
        }, f, indent=2)
