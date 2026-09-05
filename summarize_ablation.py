import json
import glob

# Find the latest ablation final cv result
files = glob.glob("experiments/results/exp_005_ablation_final_cv_*.json")
files.sort()
latest_file = files[-1]

with open(latest_file, "r") as f:
    data = json.load(f)
    
res = data["results"]
vqc = res["vqc"]["metrics_mean"]
svm = res["svm"]["metrics_mean"]
rf = res["random_forest"]["metrics_mean"]
xgb = res["xgboost"]["metrics_mean"]

def print_model(name, d, d_std):
    print(f"| {name} | {d['accuracy']:.4f} ± {d_std['accuracy']:.4f} | {d['sensitivity']:.4f} ± {d_std['sensitivity']:.4f} | {d['specificity']:.4f} ± {d_std['specificity']:.4f} | {d['f1']:.4f} ± {d_std['f1']:.4f} | {d['roc_auc']:.4f} ± {d_std['roc_auc']:.4f} | {d['training_time_s']:.2f}s |")

print("| Model | Accuracy | Sensitivity | Specificity | F1 | ROC-AUC | Train Time |")
print("|---|---|---|---|---|---|---|")
print_model("VQC (Optimized)", vqc, res["vqc"]["metrics_std"])
print_model("SVM", svm, res["svm"]["metrics_std"])
print_model("Random Forest", rf, res["random_forest"]["metrics_std"])
print_model("XGBoost", xgb, res["xgboost"]["metrics_std"])
print("\nDeltas vs SVM:")
print(f"Δ Accuracy: {vqc['accuracy'] - svm['accuracy']:.4f}")
print(f"Δ ROC-AUC: {vqc['roc_auc'] - svm['roc_auc']:.4f}")
print(f"Δ F1: {vqc['f1'] - svm['f1']:.4f}")
