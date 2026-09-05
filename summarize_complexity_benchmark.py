import json
import glob
import numpy as np
import matplotlib.pyplot as plt

files = glob.glob("experiments/results/complexity_benchmark_*.json")
files.sort()
latest = files[-1]

with open(latest, "r") as f:
    data = json.load(f)

regimes = data["metadata"]["regimes"]
models = data["metadata"]["models"]
seeds = data["metadata"]["seeds"]

print("| Regime | LR Separability | SVM AUC | RF AUC | VQC AUC | VQC Time |")
print("|---|---|---|---|---|---|")

auc_data = {r: {m: [] for m in models} for r in regimes}

for r in regimes:
    lr_acc = np.mean([data["regime_profiles"][r][str(s)]["linear_separability_score"] for s in seeds])
    svm_auc = np.mean([data["benchmark"][r]["svm"][str(s)]["roc_auc"] for s in seeds])
    rf_auc = np.mean([data["benchmark"][r]["random_forest"][str(s)]["roc_auc"] for s in seeds])
    vqc_auc = np.mean([data["benchmark"][r]["vqc"][str(s)]["roc_auc"] for s in seeds])
    vqc_std = np.std([data["benchmark"][r]["vqc"][str(s)]["roc_auc"] for s in seeds])
    vqc_time = np.mean([data["benchmark"][r]["vqc"][str(s)]["training_time_s"] for s in seeds])
    
    print(f"| {r} | {lr_acc:.4f} | {svm_auc:.4f} | {rf_auc:.4f} | {vqc_auc:.4f} ± {vqc_std:.4f} | {vqc_time:.2f}s |")
    
    for m in models:
        auc_data[r][m] = np.mean([data["benchmark"][r][m][str(s)]["roc_auc"] for s in seeds])

# Plotting
x = np.arange(len(regimes))
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))
for i, m in enumerate(["svm", "random_forest", "vqc"]):
    vals = [auc_data[r][m] for r in regimes]
    ax.bar(x + (i-1)*width, vals, width, label=m.upper())

ax.set_ylabel('Mean ROC-AUC')
ax.set_title('Model Performance Across Complexity Regimes')
ax.set_xticks(x)
ax.set_xticklabels(regimes, rotation=15)
ax.legend()
plt.tight_layout()
plt.savefig("experiments/artifacts/complexity_regimes_performance.png")
