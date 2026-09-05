# EXPERIMENT_LOG.md — Experiment Registry
## SIH 26139 · Hybrid QML Platform

> Every experiment that runs must be logged here.  
> Never delete entries. Failed experiments are evidence too.  
> Results files live in `experiments/results/`. Config files in `experiments/configs/`.

---

## Log Format

```
### EXP-NNN: <short title>
- **Date:** YYYY-MM-DD HH:MM
- **Status:** RUNNING | COMPLETED | FAILED | ABORTED
- **Config file:** experiments/configs/exp_NNN_<name>.json
- **Results file:** experiments/results/exp_NNN_<name>.json
- **Seed:** N
- **Split:** holdout 80/20 | 5-fold CV
- **PCA dims:** N
- **Models run:** SVM, RF, XGBoost, VQC (n_qubits=N, n_layers=N, encoding=X)
- **Key results:**
  | Model | Accuracy | F1 | Sensitivity | Specificity | ROC-AUC | Train time |
  |---|---|---|---|---|---|---|
  | SVM | ? | ? | ? | ? | ? | ? |
- **Verdict:** (quantum improved / did not improve / matched)
- **Notes:** Observations, anomalies, decisions made based on results.
```

---

## Experiments

*(No experiments have run yet. This log is empty.)*

---

## Summary Table

| Exp ID | Date | Models | Best F1 | VQC F1 | Verdict | Status |
|---|---|---|---|---|---|---|
| (none yet) | — | — | — | — | — | — |
| 2026-09-05 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-05 | exp_001_controlled_pilot | svm, random_forest, xgboost | seed=42 | See exp_001_controlled_pilot_*.json |
| 2026-09-05 | exp_002_cv_baseline | svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_002_cv_baseline_*.json |
| 2026-09-05 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-05 | exp_002_cv_baseline | svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_002_cv_baseline_*.json |
| 2026-09-05 | exp_002_cv_baseline | svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_002_cv_baseline_*.json |
| 2026-09-05 | exp_002_cv_baseline | svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_002_cv_baseline_*.json |
| 2026-09-05 | exp_002_cv_baseline | svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_002_cv_baseline_*.json |
| 2026-09-05 | exp_003_vqc_smoke | vqc, svm | seed=42 | See exp_003_vqc_smoke_*.json |
| 2026-09-05 | exp_004_vqc_baseline | svm, random_forest, xgboost, vqc | seed=42 | See exp_004_vqc_baseline_*.json |
| 2026-09-05 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-05 | ablation_A_dim4 | vqc | seed=42 | See ablation_A_dim4_*.json |
| 2026-09-05 | ablation_A_dim4 | vqc | seed=42 | See ablation_A_dim4_*.json |
| 2026-09-05 | ablation_A_dim6 | vqc | seed=42 | See ablation_A_dim6_*.json |
| 2026-09-05 | ablation_A_dim8 | vqc | seed=42 | See ablation_A_dim8_*.json |
| 2026-09-05 | ablation_B_depth1 | vqc | seed=42 | See ablation_B_depth1_*.json |
| 2026-09-05 | ablation_B_depth2 | vqc | seed=42 | See ablation_B_depth2_*.json |
| 2026-09-05 | ablation_B_depth3 | vqc | seed=42 | See ablation_B_depth3_*.json |
| 2026-09-05 | ablation_C_loss_mse | vqc | seed=42 | See ablation_C_loss_mse_*.json |
| 2026-09-05 | ablation_C_loss_bce | vqc | seed=42 | See ablation_C_loss_bce_*.json |
| 2026-09-05 | ablation_D_iters_25 | vqc | seed=42 | See ablation_D_iters_25_*.json |
| 2026-09-05 | ablation_D_iters_50 | vqc | seed=42 | See ablation_D_iters_50_*.json |
| 2026-09-05 | ablation_D_iters_100 | vqc | seed=42 | See ablation_D_iters_100_*.json |
| 2026-09-05 | exp_005_ablation_final_cv | vqc, svm, random_forest, xgboost | seed=42 (5-fold CV) | See exp_005_ablation_final_cv_*.json |
