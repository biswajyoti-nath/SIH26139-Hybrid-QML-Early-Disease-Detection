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
