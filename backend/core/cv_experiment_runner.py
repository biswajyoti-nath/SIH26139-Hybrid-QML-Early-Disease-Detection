import time
import json
import os
import datetime
import sys
import numpy as np
import sklearn
import xgboost
from sklearn.model_selection import StratifiedKFold, StratifiedGroupKFold
from backend.core.config import ExperimentConfig
from backend.core.dataset import DatasetManager
from backend.core.preprocessing import PreprocessingEngine
from backend.core.models import ModelFactory
from backend.core.evaluation import EvaluationEngine

class CVExperimentRunner:
    def __init__(self, config: ExperimentConfig, n_splits: int = 5):
        self.config = config
        self.n_splits = n_splits
        
    def run(self, complexity_profile: dict = None):
        print(f"Starting CV Experiment: {self.config.experiment_id} ({self.n_splits}-fold)")
        
        # 1. Dataset
        if self.config.dataset_name.lower() == "parkinsons":
            dataset = DatasetManager.load_parkinsons()
        else:
            dataset = DatasetManager.load_wdbc()
            
        # Determine CV strategy and validate subject leakage constraints
        if dataset.groups is not None:
            skf = StratifiedGroupKFold(n_splits=self.n_splits, shuffle=True, random_state=self.config.random_seed)
            split_gen = list(skf.split(dataset.X, dataset.y, groups=dataset.groups))
            split_strategy = f"{self.n_splits}-fold_stratified_group_cv"
            grouping_info = "Sequential 3-recording subject grouping based on dataset provenance"
        else:
            skf = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=self.config.random_seed)
            split_gen = list(skf.split(dataset.X, dataset.y))
            split_strategy = f"{self.n_splits}-fold_stratified_cv"
            grouping_info = "None"
            
        results_out = {
            "experiment_id": self.config.experiment_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "dataset": self.config.dataset_name,
            "dataset_source": dataset.provenance,
            "n_samples": dataset.X.shape[0],
            "raw_features": dataset.X.shape[1],
            "class_distribution": {str(k): int(v) for k, v in zip(*np.unique(dataset.y, return_counts=True))},
            "split_strategy": split_strategy,
            "validation_protocol": split_strategy,
            "n_splits": self.n_splits,
            "grouping_information": grouping_info,
            "random_seed": self.config.random_seed,
            "preprocessing_configuration": "StandardScaler+PCA",
            "pca_configuration": self.config.n_pca_components,
            "pca_explained_variance": [],
            "compression_ratio": float(dataset.X.shape[1]) / float(self.config.n_pca_components) if self.config.n_pca_components else 1.0,
            "complexity_characteristics": complexity_profile or {},
            "models_tested": list(self.config.models.keys()),
            "classical_model_configuration": {k: v for k, v in self.config.models.items() if k != "vqc"},
            "vqc_configuration": self.config.models.get("vqc", {}),
            "results": {},
            "software_versions": {
                "python": sys.version.split()[0],
                "sklearn": sklearn.__version__,
                "xgboost": xgboost.__version__
            }
        }
        
        for model_name in self.config.models.keys():
            results_out["results"][model_name] = {
                "hyperparameters": self.config.models[model_name],
                "folds": [],
                "metrics_mean": {},
                "metrics_std": {},
                "pooled_confusion_matrix": {"tn": 0, "fp": 0, "fn": 0, "tp": 0}
            }
            
        for fold, (train_idx, test_idx) in enumerate(split_gen):
            print(f"--- Fold {fold+1}/{self.n_splits} ---")
            
            # Subject leakage validation
            if dataset.groups is not None:
                train_groups = dataset.groups[train_idx]
                val_groups = dataset.groups[test_idx]
                overlap = set(train_groups).intersection(set(val_groups))
                if overlap:
                    raise ValueError(f"Subject leakage detected in fold {fold+1}! Overlapping groups: {overlap}")
            
            X_train_raw, X_test_raw = dataset.X[train_idx], dataset.X[test_idx]
            y_train, y_test = dataset.y[train_idx], dataset.y[test_idx]
            
            # Preprocess (Leakage safe) via Pipeline
            pipeline = PreprocessingEngine.build_pipeline(self.config.n_pca_components, self.config.random_seed)
            X_train = pipeline.fit_transform(X_train_raw, y_train)
            X_test = pipeline.transform(X_test_raw)
            
            # Record PCA explained variance
            pca_step = pipeline.named_steps.get("pca")
            if pca_step is not None:
                evr = float(np.sum(pca_step.explained_variance_ratio_))
                results_out["pca_explained_variance"].append(evr)
                
            for model_name, model_params in self.config.models.items():
                model = ModelFactory.create_classical_model(model_name, model_params)
                
                t_start = time.perf_counter()
                model.fit(X_train, y_train)
                train_time = time.perf_counter() - t_start
                
                t_start = time.perf_counter()
                y_pred = model.predict(X_test)
                inf_time = time.perf_counter() - t_start
                
                if hasattr(model, "predict_proba"):
                    try:
                        y_pred_proba = model.predict_proba(X_test)
                    except:
                        y_pred_proba = None
                else:
                    y_pred_proba = None
                    
                metrics = EvaluationEngine.evaluate(y_test, y_pred, y_pred_proba)
                metrics["training_time_s"] = train_time
                metrics["inference_time_s"] = inf_time
                if hasattr(model, "history_"):
                    metrics["history"] = model.history_
                
                results_out["results"][model_name]["folds"].append(metrics)
                
                # Accumulate pooled confusion matrix
                cm = metrics["confusion_matrix"]
                results_out["results"][model_name]["pooled_confusion_matrix"]["tn"] += cm["tn"]
                results_out["results"][model_name]["pooled_confusion_matrix"]["fp"] += cm["fp"]
                results_out["results"][model_name]["pooled_confusion_matrix"]["fn"] += cm["fn"]
                results_out["results"][model_name]["pooled_confusion_matrix"]["tp"] += cm["tp"]
                
        # Compute means and stds for PCA EVR
        if results_out["pca_explained_variance"]:
            results_out["pca_explained_variance_mean"] = float(np.mean(results_out["pca_explained_variance"]))
            results_out["pca_explained_variance_std"] = float(np.std(results_out["pca_explained_variance"]))
            results_out["pca_explained_variance_min"] = float(np.min(results_out["pca_explained_variance"]))
            results_out["pca_explained_variance_max"] = float(np.max(results_out["pca_explained_variance"]))

        # Compute means and stds for models
        for model_name in self.config.models.keys():
            folds = results_out["results"][model_name]["folds"]
            keys = folds[0].keys()
            for k in keys:
                if k == "confusion_matrix": continue
                vals = [f[k] for f in folds if f[k] is not None]
                if vals:
                    results_out["results"][model_name]["metrics_mean"][k] = float(np.mean(vals))
                    results_out["results"][model_name]["metrics_std"][k] = float(np.std(vals))

        self.store_results(results_out)
        self.update_log(results_out)
        return results_out
        
    def store_results(self, results_out):
        os.makedirs("experiments/results", exist_ok=True)
        out_file = f"experiments/results/{self.config.experiment_id}_{int(time.time())}.json"
        with open(out_file, 'w') as f:
            json.dump(results_out, f, indent=2)
        print(f"Results stored to {out_file}")
        
    def update_log(self, results_out):
        log_file = "EXPERIMENT_LOG.md"
        with open(log_file, 'a') as f:
            timestamp = results_out["timestamp"]
            exp_id = results_out["experiment_id"]
            seed = results_out["random_seed"]
            models = ", ".join(results_out["models_tested"])
            f.write(f"| {timestamp[:10]} | {exp_id} ({results_out['dataset']}) | {models} | seed={seed} ({self.n_splits}-fold) | See {exp_id}_*.json |\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.core.cv_experiment_runner <path_to_config.json>")
        sys.exit(1)
    
    cfg = ExperimentConfig.load_from_json(sys.argv[1])
    runner = CVExperimentRunner(cfg, n_splits=5)
    runner.run()
