# DEMO_SPECIFICATION.md
## SIH 26139 — Demo Specification
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Define the exact demo flow, UI behavior, and honesty requirements for the SIH presentation.

---

## Core Principle

> **The demo must be scientifically honest. If quantum performs worse, the UI must show that result clearly. There must be no manipulation of display logic to make quantum appear superior.**

---

## 1. Demo Flow (11 Steps)

### Step 1: Dataset Selection

**User action:** Select dataset from dropdown.

**Options:**
- Breast Cancer Wisconsin (Diagnostic) — WDBC [pilot, available]
- (Future: Heart Disease, Parkinson's — shown as "coming soon")

**Display:**
- Dataset name
- Instance count: 569
- Feature count: 30
- Target: Binary (Benign / Malignant)
- Class distribution: 357 B (62.7%) / 212 M (37.3%)
- Clinical status label: **"Research benchmark. Not a clinical dataset."**

---

### Step 2: Configure Preprocessing

**User action:** Set preprocessing parameters via form controls.

| Parameter | Control | Default | Range |
|---|---|---|---|
| PCA dimensions | Slider or number input | 8 | 5, 8, 10 |
| Train/test split | Slider | 80/20 | 70/30, 80/20 |
| Random seed | Number input | 42 | Any integer |
| Stratify | Checkbox | Checked | — |

**Display:** Live preview of resulting train/test sizes given selected split.

---

### Step 3: Select Classical Models

**User action:** Checkbox selection of classical models to include.

| Model | Default | Config shown |
|---|---|---|
| SVM (RBF) | Checked | kernel, C, gamma |
| Random Forest | Checked | n_estimators |
| XGBoost | Checked | n_estimators, learning_rate |

**All selected models will run in the experiment and be included in the comparison.**

---

### Step 4: Select and Configure Quantum Model

**User action:** Enable VQC toggle; configure parameters.

| Parameter | Control | Default |
|---|---|---|
| Framework | Dropdown | PennyLane |
| Qubits (= PCA dims) | Read-only | Matches PCA dims |
| Feature encoding | Dropdown | AngleEmbedding |
| Ansatz | Dropdown | RealAmplitudes |
| Number of layers | Number input | 3 |
| Optimizer | Dropdown | Adam |
| Learning rate | Number input | 0.01 |
| Max iterations | Number input | 100 |
| Backend | Read-only | lightning.qubit (noiseless) |

**Label displayed prominently:** "Runs on quantum simulator. NOT real quantum hardware."

---

### Step 5: Run Experiment

**User action:** Click "Run Experiment" button.

**System behavior:**
1. Validate all parameters (show errors if invalid).
2. Display progress indicator with steps:
   - "Loading dataset..."
   - "Preprocessing..."
   - "Training SVM..."
   - "Training Random Forest..."
   - "Training XGBoost..."
   - "Training VQC... (may take several minutes)"
   - "Computing explainability..."
   - "Complete."

**VQC training note:** Display "Quantum circuit training is computationally intensive. Estimated time: X minutes." if prior estimate is available.

**Cancel button:** Available during training.

---

### Step 6: Results Comparison Table

**Display:** Side-by-side metric comparison for all models.

| Metric | SVM | Random Forest | XGBoost | VQC |
|---|---|---|---|---|
| Accuracy | measured | measured | measured | measured |
| Sensitivity | measured | measured | measured | measured |
| Specificity | measured | measured | measured | measured |
| Precision | measured | measured | measured | measured |
| F1-score | measured | measured | measured | measured |
| ROC-AUC | measured | measured | measured | measured |
| Training Time | measured | measured | measured | measured |
| Inference Time | measured | measured | measured | measured |

**Highlighting:** Automatically highlight the best value per metric row. Do NOT force VQC to always appear highlighted.

**Label:** "Results measured under identical experimental conditions. Seed: [N]. PCA: [N] dims."

---

### Step 7: Confusion Matrix Panel

**Display:** 2×2 confusion matrix for each model. All four matrices shown side by side.

Layout per matrix:
```
          Predicted B  Predicted M
Actual B:    TN           FP
Actual M:    FN           TP
```

Label axes clearly. Include: sensitivity = TP/(TP+FN), specificity = TN/(TN+FP).

---

### Step 8: ROC Curve Panel

**Display:** All ROC curves on the same axes. Different color per model.

Include:
- AUC value in legend per model.
- Diagonal reference line (random classifier).
- Axes labeled: True Positive Rate (Sensitivity) vs False Positive Rate (1 - Specificity).

---

### Step 9: Explainability Panel

**Sub-panel A: Classical Models (SHAP)**

For a user-selected instance from the test set:
- SHAP waterfall plot showing feature contributions for the selected classical model.
- Display original feature values alongside.
- Label: "SHAP values show how each input feature contributed to this prediction."
- Label: "This is a model-level explanation, not clinical validation."

**Sub-panel B: Quantum Model (VQC)**

For the same selected instance:
- Input feature attribution (SHAP KernelExplainer treating VQC as black box).
- Circuit information card:
  - Number of qubits
  - Number of layers
  - Encoding method
  - Ansatz
  - Number of trainable parameters
  - Measurement expectation value for this instance
- Label: **"Attribution is at the input-feature level. SHAP does not explain internal quantum gate operations."**

---

### Step 10: Experiment Metadata Panel (Reproducibility)

**Display:** Full reproducibility record for this experiment run.

Show:
- Experiment ID
- Timestamp
- Dataset name and source
- Random seed
- Split strategy and fraction
- PCA dimensions
- StandardScaler parameters
- All model configurations (classical and quantum)
- Software versions (Python, sklearn, xgboost, pennylane/qiskit, numpy)

**Include:** "Copy metadata" button for judges to record.

**Label:** "Re-running with this configuration and these software versions should produce identical results."

---

### Step 11: Verdict Panel

**Display:** Explicit, honest verdict comparing quantum vs best classical.

Template:
```
Primary metric: F1-score
Best classical model: [XGBoost / SVM / RF]
Best classical F1: [value]
VQC F1: [value]
Delta: [+/-delta]

Verdict: The VQC [improved / did not improve / matched] the best classical 
         baseline on F1-score under these experimental conditions.

Note: This result is specific to the WDBC dataset, the chosen experimental 
configuration, and the noiseless simulator. Results on real quantum hardware 
or other datasets may differ.
```

**Verdict Panel must NOT:**
- Show "quantum wins" if it didn't.
- Show a vague message that avoids the comparison.
- Hide the delta value.
- Recommend clinical use regardless of result.

---

## 2. Judge Q&A Preparation

### Q: "Why didn't your quantum model beat classical ML?"

**A:** This is a research platform, not a marketing platform. Current evidence — including the Gupta et al. 2025 systematic review of 4,915 papers — shows no consistent QML advantage in digital health. Our contribution is a rigorous, reproducible framework that can test this hypothesis fairly. The result itself is the scientific contribution.

### Q: "Can this system be used for actual cancer diagnosis?"

**A:** No. WDBC is a retrospective research benchmark, not a clinical validation dataset. This system is a research prototype. Clinical deployment would require prospective clinical validation, regulatory approval, and substantial additional work.

### Q: "Why are you using a simulator instead of real quantum hardware?"

**A:** Near-term quantum hardware (NISQ devices) has noise, limited qubits, and restricted access. Simulator-first execution allows us to demonstrate the architecture, pipeline, and comparison framework. Real QPU testing is on our roadmap as Phase 6 future work.

### Q: "How do you ensure the comparison is fair?"

**A:** All models use the same WDBC dataset, the same stratified train/test split (seed=42), the same StandardScaler, the same PCA transformation (fitted on training data only), and the same evaluation metrics. We explicitly prevent data leakage by fitting all preprocessing parameters on the training set only. The ExperimentRunner records every configuration parameter before any experiment runs.

### Q: "What is your contribution if quantum doesn't win?"

**A:** Rigorous benchmarking itself is the contribution — the Gupta et al. 2025 review specifically identifies the lack of fair comparative platforms as a weakness of existing QML health research. Our platform can generate reproducible, honest comparisons. That is valuable regardless of the quantum model's performance.

### Q: "Can you scale this to larger datasets?"

**A:** The architecture is designed to be dataset-extensible. Adding new datasets requires only implementing a new loader in `DatasetManager`. The rest of the pipeline (preprocessing, training, evaluation, UI) works unchanged. Quantum simulation cost will scale with dataset size and qubit count, which is a known limitation addressed in our feasibility analysis.

---

## 3. What Must Be True Before Demo Day

- [ ] All classical models trained and results stored.
- [ ] VQC trained and results stored.
- [ ] SHAP working for at least one classical model.
- [ ] Input-level attribution working for VQC.
- [ ] Reproducibility validation: re-run experiment with same seed → same results.
- [ ] All UI panels displaying correct data from backend.
- [ ] VerdictPanel correctly showing actual quantum vs classical comparison.
- [ ] Experiment metadata panel showing complete configuration.
- [ ] Clinical status label visible on every relevant screen.
- [ ] "Simulator, not real QPU" label visible on quantum model panels.
- [ ] Docker-compose starts entire system with one command.

---

## 4. Demo Script (2-Minute Version)

1. (10s) "This is our Hybrid QML Platform for SIH 26139. We are not claiming quantum beats classical — we're building the platform that can rigorously test that question."
2. (20s) Select WDBC, show dataset info, note clinical status label.
3. (20s) Set preprocessing: PCA=8, split=80/20, seed=42.
4. (20s) Select all classical models; enable VQC with AngleEmbedding, 8 qubits, 3 layers.
5. (10s) Show results table with pre-loaded results (training takes minutes; load cached).
6. (20s) Highlight confusion matrices and ROC curves. Point out sensitivity metric.
7. (20s) Show SHAP explanation for one prediction.
8. (10s) Show VerdictPanel. Read the verdict as measured.
9. (10s) "The platform is reproducible — here is the exact experimental configuration that produced these results."

**Total: ~2 minutes. Leave 3 minutes for judge questions.**
