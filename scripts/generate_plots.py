import json
import glob
import os
import matplotlib.pyplot as plt

os.makedirs("experiments/artifacts", exist_ok=True)
files = glob.glob("experiments/results/exp_005_ablation_final_cv_*.json")
files.sort()
latest_file = files[-1]

with open(latest_file, "r") as f:
    data = json.load(f)

res = data["results"]
models = ["SVM", "Random Forest", "XGBoost", "VQC"]
keys = ["svm", "random_forest", "xgboost", "vqc"]

# 1. Accuracy & ROC-AUC Bar Chart
accs = [res[k]["metrics_mean"]["accuracy"] for k in keys]
aucs = [res[k]["metrics_mean"]["roc_auc"] for k in keys]

x = range(len(models))
plt.figure(figsize=(10, 6))
plt.bar([i - 0.2 for i in x], accs, width=0.4, label="Accuracy", color="#1f77b4")
plt.bar([i + 0.2 for i in x], aucs, width=0.4, label="ROC-AUC", color="#ff7f0e")
plt.xticks(x, models)
plt.ylabel("Score")
plt.title("Classical vs Quantum Performance (WDBC 5-Fold CV)")
plt.legend()
plt.ylim(0, 1.1)
plt.savefig("experiments/artifacts/performance_comparison.png")
plt.close()

# 2. VQC Loss Curve (from the last fold)
if "history" in res["vqc"]["folds"][-1]:
    history = res["vqc"]["folds"][-1]["history"]
    plt.figure(figsize=(8, 5))
    plt.plot(history, label="MSE Loss", color="purple", linewidth=2)
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.title("VQC Training Loss Curve (Fold 5)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig("experiments/artifacts/vqc_loss_curve.png")
    plt.close()

print("Visual artifacts generated in experiments/artifacts/")
