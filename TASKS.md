# TASKS.md — Task Registry
## SIH 26139 · Hybrid QML Platform

> Priorities: P0=blocking, P1=critical path, P2=important, P3=polish  
> Statuses: DISCOVERED → PLANNED → IMPLEMENTING → IMPLEMENTED → TESTING → VERIFIED → ACCEPTED

---

## Phase 0 — Workspace & Infrastructure

### T-000: Agentic workspace setup
- **Priority:** P0
- **Status:** IMPLEMENTING
- **Owner:** Session 2 (this session)
- **Dependencies:** none
- **Output:** AGENTS.md, PROJECT_STATE.md, TASKS.md, DECISIONS.md, EXPERIMENT_LOG.md, agent files, .gitignore, README.md, scripts/health_check.sh, initial git commit
- **Verification:** All files exist + git log shows initial commit + fresh agent can orient from AGENTS.md alone

### T-001: .gitignore + README.md
- **Priority:** P0
- **Status:** VERIFIED
- **Dependencies:** git init (done)
- **Output:** .gitignore (Python + Node + IDE patterns), README.md (project overview)
- **Verification:** `git status` shows no junk files; README renders correctly

---

## Phase 1 — Environment & Dependencies

### T-010: Python environment resolution
- **Priority:** P0 (blocks everything)
- **Status:** VERIFIED
- **Dependencies:** T-001
- **Expected output:**
  - Python 3.12 virtual environment at `.venv/` (managed by `uv`)
  - All packages successfully installed (scikit-learn, xgboost, shap, fastapi, uvicorn, pennylane, pennylane-lightning) via `pyproject.toml`
  - `docs/TECH_STACK.md` updated with `uv` strategy
- **Verification criteria:**
  - `scripts/health_check.sh` passes environment section
  - Minimal VQC test circuit runs to completion without error
- **Notes:** Python 3.14 is installed system-wide. Quantum packages (PennyLane, Qiskit ML) officially support 3.10–3.13. Attempt 3.14 first; fallback to Python 3.12 via pyenv or Docker.

### T-011: Backend project skeleton
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-010
- **Expected output:** `backend/` directory with module structure matching `docs/SOFTWARE_ARCHITECTURE.md`; empty `__init__.py` files; importable from root
- **Verification:** `python -c "from backend.core import dataset_manager"` exits 0

### T-012: Frontend project skeleton
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-010
- **Expected output:** `frontend/` directory with Vite + React 18 scaffold; `npm install` succeeds; `npm run dev` starts
- **Verification:** `npm run build` exits 0

---

## Phase 2 — Data & Preprocessing

### T-020: DatasetManager — WDBC loader
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-011
- **Expected output:**
  - `backend/core/dataset_manager.py` — `DatasetManager` class
  - `DatasetManager().load_wdbc()` returns `(X, y)` with shape `(569, 30)` and binary target
  - `DatasetManager().validate(X, y, 'wdbc')` raises on invalid data; returns report on valid data
- **Verification criteria:**
  - Unit test: `assert X.shape == (569, 30)`
  - Unit test: `assert sorted(set(y)) == [0, 1]`
  - Unit test: `assert y.sum() == 212` (212 malignant)
  - Unit test: `assert np.isnan(X).sum() == 0`

### T-021: PreprocessingEngine — leakage-safe scaler + PCA
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-020
- **Expected output:**
  - `backend/core/preprocessing_engine.py` — `PreprocessingEngine` class
  - `fit(X_train)` → `transform(X_test)` pattern, no leakage
  - `transform()` raises `PreprocessingNotFittedError` if `fit()` not called first
  - `get_config()` returns reproducibility dict
- **Verification criteria:**
  - Unit test: transform before fit raises error
  - Unit test: X_train_pca and X_test_pca have shape `(n_samples, n_pca_components)`
  - Unit test: StandardScaler mean vector fitted on train; verify test column mean is NOT zero (proves no leakage)
  - Unit test: same config → same PCA result with same seed

---

## Phase 3 — Classical ML

### T-030: ClassicalModelEngine — SVM, RF, XGBoost
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-021
- **Expected output:**
  - `backend/core/classical_engine.py` — `ClassicalModelEngine` class
  - `train(model_name, X_train, y_train, config, seed)` returns `(model, training_time)`
  - `evaluate(model, X_test, y_test)` returns metrics dict
- **Verification criteria:**
  - All 3 models train without error
  - Returned metrics dict has keys: accuracy, sensitivity, specificity, precision, f1, roc_auc, training_time, inference_time, confusion_matrix
  - Accuracy for SVM on WDBC (seed=42, 80/20 split, 8 PCA dims) is plausible (>0.85)
  - Results are deterministic: same seed → same result

### T-031: EvaluationEngine — metrics computation
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-030
- **Expected output:**
  - `backend/core/evaluation_engine.py` — `EvaluationEngine` class
  - Computes all 8 required metrics from `docs/EXPERIMENT_PROTOCOL.md §6`
  - Includes specificity (not in sklearn by default)
  - VerdictLogic: compares VQC vs best classical on primary metric (F1)
- **Verification criteria:**
  - Unit test: known y_true/y_pred → verify every metric manually
  - Specificity test: all-benign predictions → specificity = 1.0, sensitivity = 0.0

### T-032: First classical baseline experiment
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-030, T-031
- **Expected output:**
  - Experiment config saved to `experiments/configs/exp_001_classical_baseline.json`
  - Results saved to `experiments/results/exp_001_classical_baseline.json`
  - Contains: all metadata + all 3 models × all 8 metrics
  - Reproducible: re-running with same config produces same numbers
- **Verification criteria:**
  - Config file exists and is valid JSON
  - Results file exists and contains all required metrics
  - Re-run with same seed → numbers match to 4 decimal places
  - `EXPERIMENT_LOG.md` updated

---

## Phase 4 — Quantum ML

### T-040: QuantumModelEngine abstract interface
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-011
- **Expected output:**
  - `backend/core/quantum_engine.py` — `QuantumModelEngine` ABC
  - `backend/quantum/base.py` — shared utilities
  - Abstract methods: `build_circuit`, `train`, `predict`, `predict_proba`, `get_config`
- **Verification:** `from backend.core.quantum_engine import QuantumModelEngine` imports cleanly

### T-041: PennyLane VQC implementation
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-040, T-010 (PennyLane installed and working)
- **Expected output:**
  - `backend/quantum/pennylane_vqc.py` — `PennyLaneVQC(QuantumModelEngine)`
  - Supports: AngleEmbedding, ZZFeatureMap (optional), RealAmplitudes ansatz
  - Optimizer: Adam (default), COBYLA (fallback)
  - Backend: `lightning.qubit`
  - `get_config()` returns complete reproducibility record
- **Verification criteria:**
  - VQC trains on WDBC (8 qubits, 3 layers, 100 iters) without error
  - Returns binary predictions
  - Returns probability scores (for ROC-AUC)
  - Same seed → same predictions (deterministic)
  - `get_config()` dict can be round-tripped to JSON

### T-042: VQC experiment — first benchmark
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-041, T-032 (classical baseline must exist)
- **Expected output:**
  - Experiment config saved to `experiments/configs/exp_002_vqc_benchmark.json`
  - Results saved to `experiments/results/exp_002_vqc_benchmark.json`
  - Contains: VQC metrics + all classical metrics (same split, same preprocessing)
  - Verdict computed and stored
  - `EXPERIMENT_LOG.md` updated
- **Verification criteria:**
  - Results file exists and is valid JSON
  - Same experiment_id config → same results (reproducible)
  - VQC accuracy is plausible (does not need to beat classical)
  - Verdict field correctly reflects measured comparison

---

## Phase 5 — Explainability

### T-050: ExplainabilityEngine — SHAP for classical
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-030
- **Expected output:**
  - `backend/core/explainability_engine.py` — `ExplainabilityEngine`
  - `explain_classical(model_name, model, X_bg, X_explain)` returns SHAP values + expected value
  - TreeExplainer for RF/XGBoost; KernelExplainer for SVM
- **Verification:** SHAP values sum approximately to prediction - expected_value (within tolerance)

### T-051: ExplainabilityEngine — input attribution for VQC
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-050, T-041
- **Expected output:**
  - `explain_quantum(model, X_bg, X_explain)` using KernelExplainer (black-box)
  - `get_circuit_info(model)` returns circuit metadata dict
  - Disclaimer string included in return dict
- **Verification:** Returns attribution values with shape matching n_pca_components

---

## Phase 6 — Experiment Runner + Results Store

### T-060: ExperimentRunner — orchestration
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-021, T-031, T-041, T-050
- **Expected output:**
  - `backend/core/experiment_runner.py` — `ExperimentRunner`
  - Atomically records full config before any model trains
  - Runs all selected models in sequence
  - Stores results after each model
  - Computes verdict
- **Verification:** Re-running same config ID → identical results

### T-061: ResultsStore — JSON persistence
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-060
- **Expected output:**
  - `backend/core/results_store.py` — `ResultsStore`
  - `save(result)` → creates `experiments/results/<exp_id>.json`
  - `load(exp_id)` → returns result dict
  - `list_experiments()` → summary list
  - Never overwrites existing files

---

## Phase 7 — API

### T-070: FastAPI application
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-060, T-061
- **Expected output:**
  - `backend/api/main.py` with all endpoints from `docs/SOFTWARE_ARCHITECTURE.md §3.9`
  - Endpoints: POST /api/experiments, GET /api/experiments/{id}, GET /api/experiments, GET /api/datasets
  - `uvicorn backend.api.main:app` starts without error
  - OpenAPI docs accessible at /docs
- **Verification:** `curl http://localhost:8000/api/datasets` returns WDBC info

---

## Phase 8 — Frontend Dashboard

### T-080: React dashboard scaffold
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-070, T-012
- **Expected output:** Basic dashboard that calls API and displays experiment list
- **Verification:** Page loads; API call returns data; no console errors

### T-081: Results comparison table
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-080
- **Output:** Side-by-side metrics for all models; correct highlighting; honest VerdictPanel

### T-082: ROC curve + confusion matrix visualizations
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-081
- **Output:** ROC overlay chart; per-model confusion matrices

### T-083: SHAP plots + explainability panel
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-082, T-051
- **Output:** SHAP beeswarm/waterfall; circuit info card for VQC

### T-084: Experiment metadata + reproducibility panel
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-081
- **Output:** Full config displayed; "Copy metadata" button

---

## Phase 9 — Integration & Demo

### T-090: Docker Compose setup
- **Priority:** P2
- **Status:** VERIFIED
- **Dependencies:** T-070, T-083
- **Output:** `docker-compose.yml` starts backend + frontend with one command

### T-091: End-to-end integration test
- **Priority:** P1
- **Status:** VERIFIED
- **Dependencies:** T-090
- **Verification:** Full demo flow from Step 1 to Step 11 works; VerdictPanel shows real result

### T-092: Demo pre-training + cache
- **Priority:** P1 (for demo day)
- **Status:** VERIFIED
- **Dependencies:** T-042, T-091
- **Output:** Pre-trained results cached in `experiments/results/`; UI loads instantly

---

## Phase 10 — Quality & Documentation

### T-100: Unit test suite
- **Priority:** P2
- **Status:** VERIFIED
- **Output:** `pytest` runs; all core modules have tests; CI-ready

### T-101: Integration test suite
- **Priority:** P2
- **Status:** VERIFIED
- **Output:** Full experiment pipeline tested end-to-end with known inputs

### T-102: Multi-seed experiment + mean/std reporting
- **Priority:** P3
- **Status:** DISCOVERED
- **Output:** Experiment results reported as mean ± std across 5 seeds

### T-103: QSVM / Quantum Kernel fallback implementation
- **Priority:** P3
- **Status:** DISCOVERED
- **Output:** QSVM as alternative if VQC training diverges

---

## Deferred / Future Work

| ID | Title | Notes |
|---|---|---|
| F-001 | Noise model experiment | Depolarizing noise on VQC; defer post-MVP |
| F-002 | Real QPU testing | IBM Quantum access required; Phase 6 roadmap |
| F-003 | Additional datasets (Heart Disease, Parkinson's) | Post-MVP extensibility |
| F-004 | Clinical validation pathway | Out of scope for SIH prototype |
| F-005 | Sammartino 2026 reference | Locate or remove; do not cite until verified |
| F-006 | Prajapati year fix | Verify 2023 vs 2025 before any PPT submission |

---

## MILESTONE 04: Quantum Suitability & Complexity Benchmarking

### T-060: Complexity-Regime Benchmark Engine
- **Status:** VERIFIED
- **Description:** Canonical synthetic complexity validation. Established an association between R3_CORRELATED and improved VQC performance.

### T-061: Real PS-Relevant Biomedical Complexity Benchmark
- **Status:** NEXT
- **Goal:** Test whether the relative behaviour of classical and quantum learning changes across real biomedical disease-classification problems with different measurable data characteristics.
- **Datasets:** WDBC (569 samples, diagnostic classification), UCI Parkinson's (high-dimensional, ~754 features).
- **Protocol:** Strict validation, leakage-safe preprocessing, strong classical baselines vs canonical VQC.

### T-062: Evidence-driven quantum pathway selection
- **Status:** PLANNED
- **Description:** Do not automatically implement before T-061 provides sufficient evidence.

### T-063: Potential specialist/residual/uncertainty-aware hybrid architecture
- **Status:** PLANNED

### T-064: SIH prototype integration + visual demonstration
- **Status:** PLANNED

### T-065: Hostile judge evaluation + final scientific audit
- **Status:** PLANNED
