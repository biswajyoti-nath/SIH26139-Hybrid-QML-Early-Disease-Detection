import time
import json
import os
import datetime
import sys
import sklearn
import xgboost
from backend.core.config import ExperimentConfig
from backend.core.dataset import DatasetManager
from backend.core.preprocessing import PreprocessingEngine
from backend.core.models import ModelFactory
from backend.core.evaluation import EvaluationEngine

class ExperimentRunner:
    def __init__(self, config: ExperimentConfig):
        self.config = config
        
    def run(self):
        print(f"Starting Experiment: {self.config.experiment_id}")
        
        # 1. Dataset
        dataset = DatasetManager.load_wdbc()
        
        # 2. Preprocessing & Split
        prep_result = PreprocessingEngine.run_pipeline(
            X=dataset.X,
            y=dataset.y,
            test_size=self.config.test_size,
            random_seed=self.config.random_seed,
            n_pca_components=self.config.n_pca_components
        )
        
        results_out = {
            "experiment_id": self.config.experiment_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "dataset": "WDBC",
            "dataset_source": dataset.provenance,
            "split_strategy": self.config.split_strategy,
            "test_fraction": self.config.test_size,
            "random_seed": self.config.random_seed,
            "n_pca_components": self.config.n_pca_components,
            "preprocessing": "StandardScaler+PCA",
            "models_tested": list(self.config.models.keys()),
            "results": {},
            "software_versions": {
                "python": sys.version.split()[0],
                "sklearn": sklearn.__version__,
                "xgboost": xgboost.__version__
            }
        }
        
        # 3. Model execution
        for model_name, model_params in self.config.models.items():
            print(f"  -> Running {model_name}...")
            model = ModelFactory.create_classical_model(model_name, model_params)
            
            # Training
            t_start_train = time.perf_counter()
            model.fit(prep_result.X_train, prep_result.y_train)
            training_time = time.perf_counter() - t_start_train
            
            # Inference
            t_start_inf = time.perf_counter()
            y_pred = model.predict(prep_result.X_test)
            inference_time = time.perf_counter() - t_start_inf
            
            # Probabilities (if available)
            if hasattr(model, "predict_proba"):
                y_pred_proba = model.predict_proba(prep_result.X_test)
            else:
                y_pred_proba = None
                
            # Evaluation
            metrics = EvaluationEngine.evaluate(prep_result.y_test, y_pred, y_pred_proba)
            metrics["training_time_s"] = training_time
            metrics["inference_time_s"] = inference_time
            if hasattr(model, "history_"):
                metrics["history"] = model.history_
            
            results_out["results"][model_name] = {
                "hyperparameters": model_params,
                "metrics": metrics
            }
            
        self._store_results(results_out)
        self._update_log(results_out)
        
    def _store_results(self, results_out):
        os.makedirs("experiments/results", exist_ok=True)
        out_file = f"experiments/results/{self.config.experiment_id}_{int(time.time())}.json"
        with open(out_file, 'w') as f:
            json.dump(results_out, f, indent=2)
        print(f"Results stored to {out_file}")
        
    def _update_log(self, results_out):
        log_file = "EXPERIMENT_LOG.md"
        with open(log_file, 'a') as f:
            timestamp = results_out["timestamp"]
            exp_id = results_out["experiment_id"]
            seed = results_out["random_seed"]
            models = ", ".join(results_out["models_tested"])
            f.write(f"| {timestamp[:10]} | {exp_id} | {models} | seed={seed} | See {exp_id}_*.json |\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m backend.core.experiment_runner <path_to_config.json>")
        sys.exit(1)
    
    cfg = ExperimentConfig.load_from_json(sys.argv[1])
    runner = ExperimentRunner(cfg)
    runner.run()
