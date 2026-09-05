# PROJECT_KNOWLEDGE.md
## SIH 26139 — Hybrid Quantum Machine Learning Platform for Early Disease Detection
### Team Chai.EXE · Barak Valley Engineering College · Egreen Quanta

> **Last Updated:** 2026-09-05  
> **Status:** Pre-implementation — research and architecture phase  

---

## 1. Problem Statement

**PS ID:** 26139  
**Title:** Hybrid Quantum Machine Learning Platform for Early Disease Detection  
**Organization:** Egreen Quanta  

The problem statement calls for a **hybrid quantum-classical machine-learning platform** that:

- Combines classical preprocessing and feature engineering with quantum-enhanced models (QSVM, QNN, or VQC).
- Is applicable to biomedical datasets (cancer, cardiovascular, or neurological).
- Provides data ingestion, training, prediction, and explainability.
- Evaluates quantum models against purely classical baselines.
- Assesses: Accuracy, Sensitivity, Specificity, Computational efficiency, Generalization.
- Is compatible with near-term quantum hardware or simulators.
- Constitutes a functional **software platform**, not an isolated model.

---

## 2. Project Objective

Build a **controlled experimental platform** that can rigorously determine when a quantum-enhanced component provides meaningful value over strong classical baselines under the same data, preprocessing, split, and evaluation conditions.

> "A hybrid QML experimentation platform designed to rigorously determine when quantum-enhanced learning is actually useful for biomedical classification."

**What this is NOT:**
- A claim that quantum ML beats classical ML.
- A clinically validated diagnostic system.
- A production medical device.

---

## 3. Core Hypothesis

> Can a carefully designed hybrid quantum model (VQC or QSVM) provide useful predictive behaviour under the same data, preprocessing, and evaluation conditions as strong classical baselines?

The system must be designed so the experiment can answer:
- **Yes** — quantum model provides meaningful improvement under specific conditions.
- **No** — classical baselines match or exceed quantum model.
- **Only under specific conditions** — advantage on particular metrics or subsets.

**We are not pre-claiming the answer.**

---

## 4. Proposed Solution

A **four-pillar hybrid platform:**

1. **Hybrid Architecture** — classical preprocessing feeds quantum circuits.
2. **Quantum Feature Encoding + VQC** — parameterized quantum circuits as quantum learner.
3. **Honest Benchmarking** — same data, same split, same preprocessing, same metrics for ALL models.
4. **Explainability** — SHAP-based feature attribution for classical models; input-feature attribution for quantum models.

**Pilot use case:** Breast Cancer Wisconsin (Diagnostic) — WDBC dataset.

---

## 5. System Architecture

### Primary Pipeline

```
Biomedical Dataset
        ↓
Data Validation / Schema Check
        ↓
Train / Test Split (stratified)
        ↓
Standardization (fit on train only)
        ↓
Feature Selection / PCA (fit on train only)
        ↓
+---------------------+    +---------------------------+
|  Classical Path     |    |     Quantum Path           |
|  SVM                |    |  Quantum Feature Encoding  |
|  Random Forest      |    |  Parameterized VQC         |
|  XGBoost            |    |  Classical Optimizer       |
|  (optional QSVM)    |    |  Binary Prediction         |
+----------+----------+    +-------------+--------------+
           +------------------+----------+
                              ↓
               +--------------------------+
               |   Common Evaluation      |
               |   Acc / Sens / Spec      |
               |   F1 / ROC-AUC           |
               |   Runtime                |
               +------------+-------------+
                            ↓
               +--------------------------+
               |   Explainability         |
               |   Feature Attribution    |
               |   Model Inspection       |
               +--------------------------+
```

### Software Stack Layers

```
Frontend (React)
        ↓
FastAPI Backend
        ↓
Experiment / Model Service
   ├── Classical Engine (sklearn, XGBoost)
   ├── Quantum Engine (PennyLane / Qiskit ML)
   ├── Evaluation Engine
   └── Explainability Engine (SHAP)
        ↓
Results / Experiment Store (JSON/SQLite)
```

---

## 6. Classical ML Pipeline

### Models

| Model | Purpose |
|---|---|
| SVM (RBF kernel) | Strong classical classifier; linear/nonlinear baseline |
| Random Forest | Nonlinear ensemble; captures feature interactions |
| XGBoost | High-performance boosted-tree reference |
| QSVM / Quantum Kernel | Optional; tests quantum feature-space utility in SVM framework |

### Preprocessing Steps (mandatory order)

1. Load dataset (WDBC via sklearn or UCI download).
2. Validate schema and feature count.
3. Identify target column; encode labels (B=0, M=1).
4. Check and handle missing values.
5. Stratified train/test split (80/20 or 5-fold CV).
6. Fit StandardScaler on **training data only**.
7. Apply PCA on **training data only** (initially n=5, 8, or 10 components).
8. Transform test data using fitted scaler and PCA.

**Data leakage rule (non-negotiable):** No information from the test set may influence any preprocessing parameter.

---

## 7. Quantum ML Pipeline

### VQC Architecture

```
PCA-reduced features (5-10 dims)
        ↓
Angle Encoding (RY rotations) or ZZFeatureMap
        ↓
Parameterized Entangling Layers (RealAmplitudes ansatz or custom)
        ↓
Pauli-Z measurement (expectation value)
        ↓
Sigmoid -> Binary prediction
        ↓
Classical optimizer updates parameters
```

### Design Targets (NOT yet implemented)

- 5-10 qubits
- 3-5 circuit layers
- Simulator-first execution (Qiskit Aer / PennyLane lightning.qubit)
- Classical optimizer: COBYLA, SPSA, or Adam

### Encoding Candidates

| Encoding | Description | Source |
|---|---|---|
| Angle encoding | Feature values mapped to RY rotation angles | Standard practice |
| ZZFeatureMap | Second-order Pauli feature map | Havlíček et al. 2019 |

**The encoding must be selected, fixed, and explicitly stated before implementation.**

### Framework Choice (Unresolved — see Open Questions)

- **PennyLane** preferred: native ML integration, supports PyTorch/JAX autodiff.
- **Qiskit Machine Learning** (≥0.8, requires Qiskit ≥1.0): VQC class available, migrated to Qiskit 2.x.
- **Python 3.12 has been enforced via uv to avoid 3.14 incompatibility** — must be verified before framework choice is finalized.

---

## 8. Evaluation Protocol

### Metrics (Required)

| Metric | Definition | Note |
|---|---|---|
| Accuracy | (TP+TN)/(total) | Can be misleading with class imbalance |
| Sensitivity/Recall | TP/(TP+FN) | Critical for disease detection |
| Specificity | TN/(TN+FP) | Correct negative identification |
| Precision | TP/(TP+FP) | Quality of positive predictions |
| F1-score | 2*(P*R)/(P+R) | Balance of precision and recall |
| ROC-AUC | Area under ROC curve | Threshold-independent ranking |
| Training time | Wall-clock seconds | Computational efficiency |
| Inference time | Wall-clock seconds | Deployment relevance |

### Fair Comparison Rules (Non-Negotiable)

1. **Same dataset** for all models.
2. **Same train/test split** (same random seed) for all models.
3. **Same preprocessing** pipeline where possible.
4. **No leakage** — preprocessing fit on training folds only.
5. **Record all configurations** — seed, package versions, params.
6. **Multiple seeds** where compute allows — report mean ± std.
7. **Runtime measurement** — measured under identical hardware, not assumed.

---

## 9. Dataset Strategy

### Pilot: WDBC

| Property | Value |
|---|---|
| Full name | Breast Cancer Wisconsin (Diagnostic) |
| Source | UCI Machine Learning Repository |
| DOI | 10.24432/C5DW2B |
| Instances | 569 |
| Features | 30 real-valued |
| Target | Binary (357 benign, 212 malignant) |
| Clinical status | **Research benchmark ONLY — NOT clinical validation** |
| Role | Pilot controlled experiment |

**WDBC cannot establish:** clinical utility, hospital-level generalization, diagnostic superiority, or production readiness.

### Future Datasets (Post-MVP Roadmap)

- Cardiovascular datasets (Heart Disease, etc.)
- Neurological datasets (Parkinson's, Alzheimer's)
- Larger multi-modal biomedical datasets

---

## 10. Explainability Strategy

### Classical Models: SHAP
- `TreeExplainer` for RF and XGBoost.
- `KernelExplainer` for SVM.
- Show SHAP waterfall or beeswarm plots for selected predictions.

### Quantum Model: Input-Level Attribution Only
- Apply `KernelExplainer` treating VQC as a black box w.r.t. PCA-reduced features.
- **Do NOT claim SHAP explains internal quantum gate operations.**
- Display circuit structure (ansatz + feature map) as model transparency.
- Display measurement expectation values as output information.

**Label all explainability outputs:** "Model-level explanation. Not clinically validated."

---

## 11. Software Architecture

### Core Modules

| Module | Responsibility |
|---|---|
| `DatasetManager` | Load, validate, cache datasets |
| `PreprocessingEngine` | Standardize, PCA — leakage-safe, train-only fitting |
| `ClassicalModelEngine` | Train/evaluate SVM, RF, XGBoost |
| `QuantumModelEngine` | Train/evaluate VQC, QSVM — replaceable interface |
| `ExperimentRunner` | Orchestrate full experiment, record configuration atomically |
| `EvaluationEngine` | Compute all metrics, confusion matrix, ROC |
| `ExplainabilityEngine` | SHAP + circuit inspection |
| `ResultsStore` | Persist experiment configs and results (JSON/SQLite) |
| `APILayer` | FastAPI endpoints serving frontend |
| `Dashboard` | React UI for experiment control and results display |

### Design Principles

- **Replaceable quantum layer** — `QuantumModelEngine` interface can swap PennyLane for Qiskit.
- **Classical layer always available** — never removed; always serves as baseline.
- **Reproducibility enforced** — `ExperimentRunner` records all config before running.
- **Extensible datasets** — `DatasetManager` supports additional datasets without redesign.
- **Cached results** — experiments are stored and can be replayed without re-running.

---

## 12. Demo Flow

```
Step 1: Select Dataset (WDBC)
Step 2: Configure Preprocessing (PCA dims, split ratio, seed)
Step 3: Select Classical Models (SVM, RF, XGBoost)
Step 4: Select Quantum Model (VQC: qubits, layers, encoding, optimizer)
Step 5: Run Experiment
Step 6: Display Comparison Table (Acc / F1 / Sens / Spec / ROC-AUC / Runtime)
Step 7: Display Confusion Matrices
Step 8: Display ROC Curves
Step 9: Display Explainability (SHAP / feature attribution)
Step 10: Experiment configuration metadata (reproducibility panel)
Step 11: Verdict — did quantum improve the primary metric?
```

**UI Honesty Rule:** If quantum performs worse, the UI displays that result without manipulation.

---

## 13. Research Evidence

### Primary Literature (Verified)

| Reference | Verified | What it establishes |
|---|---|---|
| Havlíček et al. (2019). Nature 567, 209-212. DOI: 10.1038/s41586-019-0980-2 | VERIFIED | QSVM and ZZFeatureMap as supervised-learning approach; 4,043 citations |
| Cerezo et al. (2021). Nature Reviews Physics 3, 625-644. DOI: 10.1038/s42254-021-00348-9 | VERIFIED | VQA challenges: barren plateaus, trainability, accuracy |
| Gupta et al. (2025). npj Digital Medicine 8, 237. DOI: 10.1038/s41746-025-01597-z | VERIFIED | Systematic review; 4,915 papers; NO consistent QML advantage in digital health |
| WDBC. DOI: 10.24432/C5DW2B | VERIFIED | 569 instances, 30 features, binary target |

### Secondary Literature (Partially Verified)

| Reference | Status | Notes |
|---|---|---|
| Mpofu & Mthunzi-Kufa (2025). MATEC Web of Conferences 417, 02001. | PARTIALLY VERIFIED | Conference paper comparing ANN vs VQC on WDBC exists; low-impact venue |
| Kundu, Muhuri & Kumar (2025). IEEE QCNC. | PARTIALLY VERIFIED | Paper exists; quantum-classical techniques for breast cancer prediction |
| Pushpanjali & Adisesha (2025). IJSAT 16(3). | PARTIALLY VERIFIED | Paper exists in IJSAT; QML vs classical benchmarking on breast cancer |
| Prajapati et al. ("2025") | UNVERIFIED as 2025 | Appears to be 2023 Springer book chapter, not a 2025 paper |
| Sammartino (2026) | UNVERIFIED | No verifiable publication found |

---

## 14. Known Limitations

| Limitation | Implication |
|---|---|
| WDBC is small (n=569) | Unstable estimates; use CV and multiple seeds |
| Simulator-only execution | No evidence of real QPU performance |
| PCA reduces features | Quantum circuit sees reduced, not full, feature space |
| Barren plateaus in VQC | Training may be unstable, especially with more qubits |
| SHAP limitation for quantum | Attribution only at input level |
| No clinical validation | Cannot claim diagnostic improvement |
| WDBC class imbalance (62.7% benign) | Accuracy alone is misleading |
| Python 3.12 environment | Critical: quantum packages may not support Python 3.14 |

---

## 15. Open Questions

See `docs/OPEN_QUESTIONS.md` for full list.

Key unresolved items:
1. Python 3.14 compatibility for quantum packages (CRITICAL).
2. Primary quantum framework: PennyLane vs Qiskit ML.
3. Feature encoding: ZZFeatureMap vs angle encoding.
4. PCA dimensionality: 5, 8, or 10.
5. Optimizer: COBYLA vs SPSA vs Adam.
6. Cross-validation: holdout vs k-fold.
7. Noise model experiment: include or defer.

---

## 16. Unsupported Claims — Must NOT Make

| Claim | Reason |
|---|---|
| "Quantum provides faster diagnosis" | Simulators are slower than classical; no QPU tested |
| "The system achieves X% accuracy" | No results exist yet — platform not yet built |
| "Quantum model outperforms classical ML" | Not demonstrated |
| "WDBC is an early-detection dataset" | WDBC is a diagnostic benchmark, not early-detection |
| "Simulator execution provides quantum speedup" | FALSE — simulators are exponentially slower |
| "SHAP proves clinical interpretability" | SHAP provides model-level attribution only |
| "The system is clinically validated" | No clinical trial or regulatory review conducted |
| "Published numbers are our results" | Published benchmarks from papers are NOT our results |
| "Quantum advantage has been demonstrated" | A research hypothesis, not a result |

---

## 17. Implementation Roadmap

### Phase 0 — Research Audit (DONE)
- Read project documents, verify literature, audit tech stack, design experimental contract.

### Phase 1 — Environment + Data + Classical Baseline
- Resolve Python 3.14 + quantum package compatibility.
- Implement DatasetManager (WDBC).
- Implement PreprocessingEngine (leakage-safe).
- Implement ClassicalModelEngine (SVM, RF, XGBoost).
- Implement EvaluationEngine.
- Run and record classical baseline experiment.

### Phase 2 — Quantum Component
- Implement QuantumModelEngine (VQC via chosen framework).
- Fix: encoding, ansatz, qubits, layers, optimizer.
- Train VQC on same split as classical models.

### Phase 3 — Explainability
- SHAP for classical models.
- Input-feature attribution for VQC.
- Circuit visualization.

### Phase 4 — API + Dashboard
- ResultsStore (JSON/SQLite).
- FastAPI endpoints.
- React dashboard: comparison table, ROC, SHAP plots.

### Phase 5 — Integration, Demo, Docker
- Docker-compose setup.
- End-to-end demo run.
- Reproducibility validation.

### Phase 6 — Future Work (Post-SIH)
- Additional biomedical datasets.
- Noise model experiment.
- Real QPU testing.
- Clinical validation pathway.
