from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from backend.core.dataset import DatasetManager
from backend.core.complexity_profiler import profile_dataset
from backend.core.suitability_router import SuitabilityRouter

app = FastAPI(title="Hybrid QML Platform API (Demo Mode)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RouteRequest(BaseModel):
    dataset_name: str

def load_results(dataset_name: str):
    if dataset_name == "wdbc":
        filename = "experiments/results/exp_t103_shootout_wdbc_1788680280.json"
    elif dataset_name == "parkinsons":
        filename = "experiments/results/exp_t103_shootout_parkinsons_1788682249.json"
    else:
        raise HTTPException(status_code=404, detail="Dataset results not found")
        
    if not os.path.exists(filename):
        raise HTTPException(status_code=500, detail="Missing cached T-103 artifact")
        
    with open(filename, 'r') as f:
        return json.load(f)

@app.get("/api/health")
def health():
    return {"status": "ok", "demo_mode": True}

@app.get("/api/datasets")
def get_datasets():
    return [
        {"name": "wdbc", "label": "Breast Cancer (WDBC)", "samples": 569, "features": 30},
        {"name": "parkinsons", "label": "Parkinson's Disease", "samples": 756, "features": 753}
    ]

@app.get("/api/dataset/{name}/profile")
def get_profile(name: str):
    if name == "wdbc":
        ds = DatasetManager.load_wdbc()
    elif name == "parkinsons":
        ds = DatasetManager.load_parkinsons()
    else:
        raise HTTPException(status_code=404, detail="Dataset not found")
    
    return profile_dataset(ds.X, ds.y, n_components=8)

@app.get("/api/dataset/{name}/results")
def get_results(name: str):
    return load_results(name)

@app.post("/api/route")
def route_pathway(req: RouteRequest):
    name = req.dataset_name
    
    # Load data for profile
    if name == "wdbc":
        ds = DatasetManager.load_wdbc()
    elif name == "parkinsons":
        ds = DatasetManager.load_parkinsons()
    else:
        raise HTTPException(status_code=404, detail="Dataset not found")
        
    profile = profile_dataset(ds.X, ds.y, n_components=8)
    results = load_results(name)
    
    # OVERWRITE dynamic variance with the official cached T-103 variance to guarantee consistency
    if "pca_explained_variance_mean" in results:
        profile["variance_retained"] = results["pca_explained_variance_mean"]
        profile["information_loss"] = 1.0 - profile["variance_retained"]
    elif "pca_explained_variance" in results and len(results["pca_explained_variance"]) > 0:
        profile["variance_retained"] = sum(results["pca_explained_variance"]) / len(results["pca_explained_variance"])
        profile["information_loss"] = 1.0 - profile["variance_retained"]
    
    c_metrics = {}
    q_metrics = {}
    runtimes = {}
    
    try:
        models = results.get("results", {})
        
        for m_name, m_data in models.items():
            metrics = m_data.get("metrics_mean", {})
            runtimes[m_name] = metrics.get("training_time_s", 0.0) + metrics.get("inference_time_s", 0.0)
            
            if m_name in ["svm", "random_forest", "xgboost"]:
                c_metrics[m_name] = metrics
            else:
                q_metrics[m_name] = metrics
                
        # SVM is the canonical baseline
        classical_base = c_metrics.get("svm", {})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Invalid result format in T-103 artifact")
        
    return SuitabilityRouter.route(profile, classical_base, q_metrics, runtimes)

