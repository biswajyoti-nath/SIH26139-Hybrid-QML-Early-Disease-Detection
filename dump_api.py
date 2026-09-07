import json
import os
from backend.core.dataset import DatasetManager
from backend.core.complexity_profiler import profile_dataset
from backend.core.suitability_router import SuitabilityRouter

def load_results(dataset_name: str):
    if dataset_name == "wdbc":
        filename = "experiments/results/exp_t103_shootout_wdbc_1788680280.json"
    elif dataset_name == "parkinsons":
        filename = "experiments/results/exp_t103_shootout_parkinsons_1788682249.json"
    else:
        raise ValueError("Unknown")
    with open(filename, 'r') as f:
        return json.load(f)

def run():
    os.makedirs("frontend/public/api/dataset/wdbc", exist_ok=True)
    os.makedirs("frontend/public/api/dataset/parkinsons", exist_ok=True)
    os.makedirs("frontend/public/api/route", exist_ok=True)
    
    for name in ["wdbc", "parkinsons"]:
        # Profile
        if name == "wdbc":
            ds = DatasetManager.load_wdbc()
        else:
            ds = DatasetManager.load_parkinsons()
        
        profile = profile_dataset(ds.X, ds.y, n_components=8)
        results = load_results(name)
        
        if "pca_explained_variance_mean" in results:
            profile["variance_retained"] = results["pca_explained_variance_mean"]
            profile["information_loss"] = 1.0 - profile["variance_retained"]
            
        with open(f"frontend/public/api/dataset/{name}/profile.json", "w") as f:
            json.dump(profile, f)
            
        # Results
        with open(f"frontend/public/api/dataset/{name}/results.json", "w") as f:
            json.dump(results, f)
            
        # Route
        c_metrics = {}
        q_metrics = {}
        runtimes = {}
        models = results.get("results", {})
        for m_name, m_data in models.items():
            metrics = m_data.get("metrics_mean", {})
            runtimes[m_name] = metrics.get("training_time_s", 0.0) + metrics.get("inference_time_s", 0.0)
            if m_name in ["svm", "random_forest", "xgboost"]:
                c_metrics[m_name] = metrics
            else:
                q_metrics[m_name] = metrics
        classical_base = c_metrics.get("svm", {})
        
        routing = SuitabilityRouter.route(profile, classical_base, q_metrics, runtimes)
        with open(f"frontend/public/api/route/{name}.json", "w") as f:
            json.dump(routing, f)

if __name__ == "__main__":
    run()
