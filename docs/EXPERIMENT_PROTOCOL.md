# EXPERIMENT_PROTOCOL.md
## SIH 26139 — Experimental Contract and Protocol
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Define the precise, non-negotiable experimental contract that governs ALL model comparisons. This document must be followed exactly before any result is recorded or reported.

---

## Governing Principle

> **Every comparison between classical and quantum models must use the same dataset, the same split, the same preprocessing parameters, and the same evaluation metrics. No exceptions.**

Any result reported without following this protocol is invalid and must not be included in the project.

---

## 1. Dataset

### Primary Dataset: WDBC

| Property | Specification |
|---|---|
| Dataset | Breast Cancer Wisconsin (Diagnostic) |
| Source | `sklearn.datasets.load_breast_cancer()` or UCI DOI 10.24432/C5DW2B |
| Instances | 569 |
| Features | 30 real-valued |
| Target | 0 = benign, 1 = malignant |
| Class distribution | 357 benign (62.7%), 212 malignant (37.3%) |
| Version | Standard sklearn version or UCI original |
| Checksum | Record SHA-256 or sklearn version when loading |

### Validation Step (run before any experiment)

Before training any model, verify:
```python
assert X.shape == (569, 30), "WDBC feature matrix shape mismatch"
assert len(set(y)) == 2, "WDBC should have exactly 2 classes"
assert y.sum() == 212, "WDBC malignant count mismatch"
assert X.isnull().sum().sum() == 0 if isinstance(X, pd.DataFrame) else np.isnan(X).sum() == 0
```

---

## 2. Preprocessing Pipeline

### Step-by-Step (must be followed in this exact order)

```
Step 1: Load dataset
Step 2: Validate schema (shape, classes, missing values)
Step 3: Encode target (B=0, M=1) — verify encoding
Step 4: Stratified Train/Test Split (BEFORE any scaling or PCA)
Step 5: Fit StandardScaler on X_train ONLY
Step 6: Transform X_train and X_test with fitted scaler
Step 7: Fit PCA on scaled X_train ONLY
Step 8: Transform scaled X_train and X_test with fitted PCA
Step 9: Feed preprocessed data to each model
```

### Data Leakage Rule (Non-Negotiable)

```
MUST:   StandardScaler.fit(X_train) → StandardScaler.transform(X_train, X_test)
MUST:   PCA.fit(X_train_scaled) → PCA.transform(X_train_scaled, X_test_scaled)

NEVER:  StandardScaler.fit(X_all) before split
NEVER:  PCA.fit(X_all) before split
NEVER:  Any parameter estimated from test data
```

Violation of this rule will invalidate all results and must be treated as a bug.

### StandardScaler Parameters

| Parameter | Value |
|---|---|
| with_mean | True |
| with_std | True |
| Implementation | `sklearn.preprocessing.StandardScaler` |

### PCA Parameters (Experiment Variable)

| Parameter | Candidates | Default |
|---|---|---|
| n_components | 5, 8, 10 | 8 |
| Implementation | `sklearn.decomposition.PCA` |
| random_state | Fixed (see Section 3) |

The PCA dimensionality is an **experiment variable**. Run experiments at n=5, n=8, n=10 to assess sensitivity.

---

## 3. Data Split

### Validation Strategy A: Stratified Holdout Split

| Parameter | Value |
|---|---|
| Test fraction | 0.20 (20%) |
| Train fraction | 0.80 (80%) |
| Stratification | By target class (maintain class ratio) |
| Implementation | `sklearn.model_selection.train_test_split(stratify=y)` |
| Random state | Fixed (see Section 4) |

**Resulting sizes (approximate):**
- Train: ~455 instances (285 B, 170 M)
- Test: ~114 instances (72 B, 42 M)

### Validation Strategy B: Stratified K-Fold Cross-Validation

| Parameter | Value |
|---|---|
| K | 5 |
| Stratification | By target class |
| Implementation | `sklearn.model_selection.StratifiedKFold` |
| Shuffle | True |
| Random state | Fixed (see Section 4) |

**When to use K-Fold:** For final reported results and stability estimation. Preprocessing must be re-fitted inside each fold.

**Recommendation:** Use Strategy A for rapid prototyping and Strategy B for final reported results.

---

## 4. Reproducibility Parameters

### Random Seed Policy

All random operations must be seeded. Primary seed: **42**.

For multiple-seed experiments: use seeds [42, 123, 2025, 7, 999].

```python
RANDOM_SEED = 42  # Primary
ADDITIONAL_SEEDS = [42, 123, 2025, 7, 999]  # For multi-seed experiments
```

Seeds must be applied to:
- `numpy.random.seed(RANDOM_SEED)`
- `random.seed(RANDOM_SEED)` (Python stdlib)
- `sklearn.utils.check_random_state(RANDOM_SEED)` (where required)
- `torch.manual_seed(RANDOM_SEED)` (if PyTorch used in quantum model)
- Train/test split `random_state=RANDOM_SEED`
- PCA `random_state=RANDOM_SEED`
- Each model `random_state=RANDOM_SEED` (where supported)

### Software Version Recording

Record at the start of every experiment run:

```python
import sys, sklearn, xgboost, shap
experiment_metadata["python_version"] = sys.version
experiment_metadata["sklearn_version"] = sklearn.__version__
experiment_metadata["xgboost_version"] = xgboost.__version__
experiment_metadata["shap_version"] = shap.__version__
# Add pennylane or qiskit versions as appropriate
```

---

## 5. Model Configurations

### Classical Model Configurations

#### SVM

| Parameter | Value |
|---|---|
| Kernel | RBF |
| C | 1.0 (default; may tune via CV) |
| gamma | 'scale' |
| Implementation | `sklearn.svm.SVC(probability=True)` |
| Random state | RANDOM_SEED |

#### Random Forest

| Parameter | Value |
|---|---|
| n_estimators | 100 |
| max_features | 'sqrt' |
| random_state | RANDOM_SEED |
| Implementation | `sklearn.ensemble.RandomForestClassifier` |

#### XGBoost

| Parameter | Value |
|---|---|
| n_estimators | 100 |
| learning_rate | 0.1 |
| max_depth | 6 |
| use_label_encoder | False |
| eval_metric | 'logloss' |
| random_state | RANDOM_SEED |
| Implementation | `xgboost.XGBClassifier` |

### Quantum Model Configuration (VQC)

The following parameters are **experiment variables** — they must be selected before the experiment runs and then fixed.

| Parameter | Candidates | Must be fixed before run |
|---|---|---|
| Framework | PennyLane / Qiskit ML | Yes |
| n_qubits | 5, 8, 10 | Yes (equals PCA n_components) |
| Feature encoding | AngleEmbedding / ZZFeatureMap | Yes |
| Ansatz | RealAmplitudes (via BasicEntanglerLayers) | Yes |
| n_layers | 3, 5 | Yes |
| Optimizer | COBYLA / SPSA / Adam | Yes |
| Learning rate | 0.01, 0.1 (if Adam) | Yes |
| Max iterations | 100, 200 | Yes |
| Backend/device | lightning.qubit / aer_simulator_statevector | Yes |
| Noise | None (noiseless simulator) | Yes (for MVP) |
| Random state | RANDOM_SEED | Yes |

**Recording rule:** ALL parameter values for the VQC run must be recorded in the experiment metadata before the experiment starts. The output record must contain every parameter value so the experiment is fully reproducible.

---

## 6. Evaluation Metrics

### Implementation

All metrics computed using `sklearn.metrics`. Applied to **held-out test set only** (or test fold in CV).

```python
from sklearn.metrics import (
    accuracy_score,
    recall_score,            # = Sensitivity
    precision_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
)

def compute_specificity(y_true, y_pred):
    """TN / (TN + FP) — specificity for binary classification."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    return tn / (tn + fp)
```

### Required Metrics Table

For each model, record:

| Metric | Function | Note |
|---|---|---|
| Accuracy | `accuracy_score(y_test, y_pred)` | |
| Sensitivity / Recall | `recall_score(y_test, y_pred, pos_label=1)` | Malignant = positive class |
| Specificity | `compute_specificity(y_test, y_pred)` | Custom function above |
| Precision | `precision_score(y_test, y_pred, pos_label=1)` | |
| F1-score | `f1_score(y_test, y_pred, pos_label=1)` | |
| ROC-AUC | `roc_auc_score(y_test, y_pred_proba)` | Requires probability output |
| Training time (s) | `time.perf_counter()` delta | Wall-clock, start before `model.fit()`, end after |
| Inference time (s) | `time.perf_counter()` delta | Wall-clock, start before `model.predict()`, end after |
| Confusion matrix | `confusion_matrix(y_test, y_pred)` | Record as [TP, FP, FN, TN] |

### Positive Class Convention

For WDBC: `pos_label = 1` (malignant). Sensitivity measures how well we detect cancer. This is the clinically meaningful direction.

---

## 7. Runtime Measurement

```python
import time

# Training time
t_start = time.perf_counter()
model.fit(X_train_pca, y_train)
training_time = time.perf_counter() - t_start

# Inference time (on test set)
t_start = time.perf_counter()
y_pred = model.predict(X_test_pca)
inference_time = time.perf_counter() - t_start
```

### Runtime Reporting Rules

- Record hardware: CPU model, RAM, whether GPU was used.
- For quantum simulators: record backend name and whether any parallelization was used.
- Do NOT compare quantum simulator time vs classical CPU time as evidence of "quantum speedup" or "quantum slowdown" — they are fundamentally different computational mechanisms.
- Report runtime as a **resource cost metric**, not as evidence of quantum advantage or disadvantage.

---

## 8. Experiment Metadata Schema

Every experiment run must produce a metadata record. Minimum schema:

```json
{
  "experiment_id": "exp_001",
  "timestamp": "2026-09-05T22:00:00+05:30",
  "dataset": "WDBC",
  "dataset_source": "sklearn.datasets.load_breast_cancer",
  "n_instances": 569,
  "n_features_raw": 30,
  "split_strategy": "stratified_holdout",
  "test_fraction": 0.20,
  "random_seed": 42,
  "n_pca_components": 8,
  "scaler": "StandardScaler",
  "models": {
    "svm": {"kernel": "rbf", "C": 1.0, "gamma": "scale"},
    "random_forest": {"n_estimators": 100, "max_features": "sqrt"},
    "xgboost": {"n_estimators": 100, "learning_rate": 0.1, "max_depth": 6},
    "vqc": {
      "framework": "pennylane",
      "pennylane_version": "0.40.0",
      "n_qubits": 8,
      "encoding": "AngleEmbedding",
      "ansatz": "RealAmplitudes (qml.RY)",
      "n_layers": 3,
      "optimizer": "Adam",
      "learning_rate": 0.01,
      "max_iterations": 100,
      "backend": "lightning.qubit",
      "noise_model": null
    }
  },
  "software_versions": {
    "python": "3.12.x",
    "sklearn": "1.x.x",
    "xgboost": "2.x.x",
    "pennylane": "0.x.x",
    "numpy": "2.x.x"
  },
  "hardware": {
    "cpu": "describe",
    "ram_gb": "describe",
    "gpu": null
  }
}
```

---

## 9. Result Reporting Rules

### Single Seed Run

Report as:

```
Model: VQC (seed=42, n_qubits=8, encoding=AngleEmbedding, ...)
Accuracy: 0.XXX
Sensitivity: 0.XXX
Specificity: 0.XXX
F1: 0.XXX
ROC-AUC: 0.XXX
Training time: X.XXX s
Inference time: X.XXX s
```

### Multi-Seed Run (preferred for final results)

Report as:

```
Model: VQC (seeds=[42, 123, 2025, 7, 999], n_qubits=8, ...)
Accuracy: mean ± std = 0.XXX ± 0.XXX
Sensitivity: 0.XXX ± 0.XXX
...
```

### Forbidden Patterns

- Do NOT report a result without specifying the exact experimental conditions.
- Do NOT round numbers to make them look better.
- Do NOT cherry-pick the best seed.
- Do NOT omit the standard deviation in multi-seed runs.
- Do NOT mix our results with published benchmark numbers.

---

## 10. Verdict Logic

At the end of each experiment, record a structured verdict:

```json
{
  "primary_metric": "F1",
  "best_classical_F1": 0.XXX,
  "best_classical_model": "XGBoost",
  "vqc_F1": 0.XXX,
  "quantum_improved_primary_metric": true/false,
  "quantum_delta": "+/-0.XXX",
  "verdict": "Quantum model [improved / did not improve / matched] the best classical baseline on F1 under these experimental conditions."
}
```

The UI must display the verdict text honestly, including if quantum performs worse.

---

## 11. Experiment Flow Diagram

```
Load WDBC
      ↓
Validate schema (assert)
      ↓
Stratified train/test split (seed=42)
      ↓
Fit StandardScaler on X_train
Transform X_train, X_test
      ↓
Fit PCA(n=8) on X_train_scaled
Transform X_train_scaled, X_test_scaled
      ↓
  +---------------------------+
  |  For each model:          |
  |  1. Record start time     |
  |  2. model.fit(X_train_pca)|
  |  3. Record training time  |
  |  4. Record start time     |
  |  5. model.predict(X_test) |
  |  6. Record inference time |
  |  7. Compute all metrics   |
  |  8. Record metadata       |
  +---------------------------+
      ↓
Save results to ResultsStore
      ↓
Compute verdict
      ↓
Display in dashboard
```

---

## 12. Dataset Provenance Decision

The project explicitly uses `sklearn.datasets.load_breast_cancer()` as the canonical source for the WDBC dataset.

**Justification:**
1. **Verifiable Identity:** The sklearn dataset is a direct, unmodified copy of the UCI Machine Learning Repository's Breast Cancer Wisconsin (Diagnostic) dataset (WDBC).
2. **Reproducibility:** Distributing or caching a raw CSV requires managing file paths and parsing logic across environments. Relying on `sklearn` guarantees that every researcher running this code receives the exact same 569 instances and 30 features.
3. **Target Standardisation:** The sklearn dataset defaults to 0 for Malignant and 1 for Benign. Our `DatasetManager` explicitly intercepts and flips this so that Malignant = 1, ensuring sensitivity metrics map correctly to clinical disease detection.

## 13. FAIR COMPARISON & SELECTION BIAS RULE
- Classical and quantum models must receive comparable experimental treatment. A classical model must NOT be intentionally left at poor defaults while the VQC receives extensive tuning.
- NO POST-HOC BENCHMARK DESIGN: The dataset generator must be independent of the quantum model. Do not tune synthetic-data parameters after seeing VQC results to manufacture a favorable regime.
- Do not use the same data repeatedly for selecting the best quantum configuration and claiming unbiased final generalization. Prefer nested cross-validation or preregistered predefined holdouts.
