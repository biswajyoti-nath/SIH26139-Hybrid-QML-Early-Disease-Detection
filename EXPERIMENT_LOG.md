# EXPERIMENT_LOG.md

## WDBC ROLE
WDBC remains a critical control experiment. Current result: classical models substantially outperform the VQC.
This is our NEGATIVE CONTROL. Never hide it from the UI, report, PPT, or judge.

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
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |

## Experiment: Complexity-Regime Benchmark (T-060)
- **Date:** 2026-09-06
- **Config:** `experiments/configs/complexity_regimes_v1.json`
- **Result Artifact:** `experiments/results/complexity_benchmark_1788638141.json`
- **Summary:** Evaluated VQC (6 qubits, 10 iters) against SVM/RF across 5 structural regimes (SIMPLE, NONLINEAR, CORRELATED, NOISY, HIGH_DIMENSIONAL) using 3 predefined seeds and 5-fold CV.
- **Key Finding:** VQC performance is strongly dependent on data structure, not just hyperparameter tuning. While it failed to match classical models on simple/nonlinear boundaries in this low-iteration limit (AUC ~0.52), it jumped significantly (+22% AUC) on `R3_CORRELATED`. This suggests redundancy/collinearity as a candidate variable for further suitability analysis. The experiment does not establish causality or validate feature correlation as a quantum-routing criterion.
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | test_park (Parkinsons) | svm | seed=42 (3-fold) | See test_park_*.json |
| 2026-09-06 | smoke_test_001 | svm | seed=42 | See smoke_test_001_*.json |
| 2026-09-06 | test_park_mock (Parkinsons) | svm | seed=42 (3-fold) | See test_park_mock_*.json |
| 2026-09-06 | exp_061_wdbc_control (WDBC) | vqc, svm, random_forest, xgboost | seed=42 (5-fold) | See exp_061_wdbc_control_*.json |
| 2026-09-06 | exp_061_parkinsons (Parkinsons) | vqc, svm, random_forest, xgboost | seed=42 (5-fold) | See exp_061_parkinsons_*.json |
| 2026-09-06 | exp_061_parkinsons_sensitivity_pca8 (Parkinsons) | vqc, svm | seed=42 (5-fold) | See exp_061_parkinsons_sensitivity_pca8_*.json |


## T-061: Real PS-Relevant Biomedical Complexity Benchmark

**Goal:** Determine if the relative performance of classical vs quantum models changes systematically across real biomedical complexity regimes.

**Datasets & Characteristics:**
- **WDBC (Control):** 569 samples, 30 raw features -> PCA 6.
  - Mean feature correlation: 0.382
  - Linear separability: 0.953
- **Parkinson's (High-Dim):** 756 samples, 753 predictive features -> PCA 6.
  - Subject Grouping: 252 subjects, 3 recordings each. Validated strictly with `StratifiedGroupKFold`.
  - Mean feature correlation: 0.116
  - Linear separability: 0.774

**Results (5-Fold CV Mean ROC-AUC):**
- **WDBC (Canonical VQC vs SVM):** VQC = 0.620 | SVM = 0.993
- **Parkinson's (Canonical VQC vs SVM):** VQC = 0.519 | SVM = 0.793

**PCA Compression & Sensitivity:**
- WDBC Explained Variance (6 comps): 88.9%
- Parkinson's Explained Variance (6 comps): 42.2%
- Parkinson's Sensitivity (8 comps): VQC AUC = 0.517, Explained Var = 47.0%

**OBSERVATION:** 
The real biomedical datasets exhibit distinctly different complexity profiles. Parkinson's requires extreme PCA compression (losing >50% of dataset variance to fit into 6-8 qubits) and has natively low feature correlation compared to WDBC. Under these constraints, classical models (SVM) continue to extract predictive signal (AUC ~0.79-0.81), while the canonical VQC collapses entirely (AUC ~0.51, near random guessing).

**SCIENTIFIC CONCLUSION:**
The evidence confirms dataset-dependent behaviour. VQC performance relative to classical baselines is heavily modulated by dataset complexity characteristics (such as the severity of the PCA information bottleneck and native feature correlation).
