# EXPERIMENTALIST.md — Experiment Execution Protocol
## SIH 26139 · Hybrid QML Platform

> This agent is responsible for designing and running ML/QML experiments.  
> Every experiment must follow docs/EXPERIMENT_PROTOCOL.md exactly.

---

## Pre-Experiment Checklist

```
[ ] Read docs/EXPERIMENT_PROTOCOL.md (the non-negotiable contract)
[ ] Identify the experiment ID (EXP-NNN — check EXPERIMENT_LOG.md for last used)
[ ] Define the complete experiment config BEFORE running anything
[ ] Save the config to experiments/configs/exp_NNN_<name>.json
[ ] Verify environment is healthy (scripts/health_check.sh)
[ ] Confirm all dependencies (dataset loaded, preprocessing fitted, model classes importable)
```

**The config file must exist before the first model trains. Not after.**

---

## Required Experiment Config Schema

Every experiment config file must contain ALL of these fields:

```json
{
  "experiment_id": "exp_NNN_<name>",
  "timestamp": "ISO8601",
  "description": "Human-readable description of what this experiment tests",
  "dataset": {
    "name": "WDBC",
    "source": "sklearn.datasets.load_breast_cancer",
    "n_instances": 569,
    "n_features_raw": 30,
    "target_encoding": "0=benign, 1=malignant"
  },
  "split": {
    "strategy": "stratified_holdout | stratified_kfold",
    "test_fraction": 0.20,
    "k_folds": null,
    "random_seed": 42
  },
  "preprocessing": {
    "scaler": "StandardScaler",
    "n_pca_components": 8,
    "pca_random_state": 42
  },
  "models": {
    "svm": {"kernel": "rbf", "C": 1.0, "gamma": "scale", "random_state": 42},
    "random_forest": {"n_estimators": 100, "max_features": "sqrt", "random_state": 42},
    "xgboost": {"n_estimators": 100, "learning_rate": 0.1, "max_depth": 6, "random_state": 42},
    "vqc": {
      "enabled": true,
      "framework": "pennylane",
      "n_qubits": 8,
      "encoding": "AngleEmbedding",
      "ansatz": "RealAmplitudes",
      "entanglement": "linear",
      "n_layers": 3,
      "optimizer": "Adam",
      "learning_rate": 0.01,
      "max_iterations": 100,
      "backend": "lightning.qubit",
      "noise_model": null,
      "random_state": 42
    }
  },
  "software_versions": {
    "python": "record at runtime",
    "sklearn": "record at runtime",
    "xgboost": "record at runtime",
    "pennylane": "record at runtime",
    "numpy": "record at runtime"
  },
  "hardware": {
    "platform": "record at runtime",
    "cpu": "record at runtime",
    "ram_gb": "record at runtime"
  }
}
```

---

## Required Results Schema

Results file at `experiments/results/exp_NNN_<name>.json`:

```json
{
  "experiment_id": "exp_NNN_<name>",
  "config_file": "experiments/configs/exp_NNN_<name>.json",
  "completed_at": "ISO8601",
  "models": {
    "<model_name>": {
      "accuracy": 0.0,
      "sensitivity": 0.0,
      "specificity": 0.0,
      "precision": 0.0,
      "f1": 0.0,
      "roc_auc": 0.0,
      "training_time_s": 0.0,
      "inference_time_s": 0.0,
      "confusion_matrix": [[TN, FP], [FN, TP]]
    }
  },
  "verdict": {
    "primary_metric": "f1",
    "best_classical_model": "<name>",
    "best_classical_f1": 0.0,
    "vqc_f1": 0.0,
    "quantum_delta": 0.0,
    "quantum_improved": true,
    "verdict_text": "The VQC [improved / did not improve] the best classical baseline on F1..."
  },
  "reproducibility_note": "Re-run experiment_id with same config to reproduce."
}
```

---

## During the Experiment

- Monitor training loss/convergence for VQC (log to `experiments/logs/exp_NNN.log`).
- If VQC diverges or explodes: DO NOT stop and fabricate results. Log the failure and try the COBYLA fallback config.
- Save intermediate results after each model completes (not only at the end).
- Never overwrite a completed results file. Append new experiments with new IDs.

---

## Post-Experiment Checklist

```
[ ] Results file exists and is valid JSON
[ ] All required metric fields are present
[ ] Confusion matrix sums to n_test_samples
[ ] ROC-AUC was computed from predict_proba (not hard labels)
[ ] Training time and inference time are recorded in seconds
[ ] Verdict is correct (compare vqc_f1 to best_classical_f1)
[ ] Re-run experiment with same config: results match to 4 decimal places
[ ] EXPERIMENT_LOG.md updated with new entry
[ ] Config and results files committed to git
```

---

## Failed Experiment Protocol

If an experiment fails:
1. Save the partial results (whatever was completed) to `experiments/results/exp_NNN_<name>_FAILED.json`.
2. Log the failure in `experiments/logs/exp_NNN.log` with the full traceback.
3. Update EXPERIMENT_LOG.md with status FAILED and notes.
4. Diagnose: is it a barren plateau? OOM? Framework bug? Wrong config?
5. Try the fallback configuration (COBYLA optimizer, fewer layers, fewer qubits).
6. Create a new experiment ID for the retry.

**Never delete a failed experiment record. It is evidence.**

---

## Experiment Directory Layout

```
experiments/
├── configs/
│   ├── exp_001_classical_baseline.json
│   ├── exp_002_vqc_benchmark_8q_3l.json
│   └── exp_003_vqc_benchmark_5q_3l.json
├── results/
│   ├── exp_001_classical_baseline.json
│   ├── exp_002_vqc_benchmark_8q_3l.json
│   └── exp_002_vqc_benchmark_8q_3l_FAILED.json  (if failure occurred)
├── logs/
│   ├── exp_001.log
│   └── exp_002.log
└── artifacts/
    ├── exp_001_roc_curve.png
    └── exp_002_shap_beeswarm.png
```
