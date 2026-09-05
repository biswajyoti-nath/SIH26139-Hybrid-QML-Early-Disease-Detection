# SOFTWARE_ARCHITECTURE.md
## SIH 26139 — Software Architecture Design
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Status:** Design document — NOT yet implemented  
> **Purpose:** Define the modular software architecture before any code is written.

---

## 1. Design Principles

1. **Modularity** — each engine has a single responsibility and clean interface.
2. **Replaceability** — the quantum layer can be swapped without touching classical code.
3. **Classical layer mandatory** — classical baselines are permanent, never optional.
4. **Reproducibility enforced** — `ExperimentRunner` records all configuration before execution.
5. **Extensibility** — adding new datasets or models requires implementing an interface, not modifying core logic.
6. **Honesty** — results are displayed as measured; the UI has no "make quantum look good" mode.
7. **Separation of concerns** — frontend, API, experiment logic, and data storage are separate layers.

---

## 2. Module Map

```
core-program/
├── backend/
│   ├── api/                        # FastAPI application
│   │   ├── main.py                 # App entry point
│   │   ├── routes/
│   │   │   ├── experiments.py      # POST /experiments, GET /experiments/{id}
│   │   │   ├── datasets.py         # GET /datasets
│   │   │   └── results.py          # GET /results/{id}
│   │   └── schemas.py              # Pydantic request/response models
│   │
│   ├── core/                       # Business logic (no HTTP dependency)
│   │   ├── dataset_manager.py      # DatasetManager
│   │   ├── preprocessing_engine.py # PreprocessingEngine
│   │   ├── classical_engine.py     # ClassicalModelEngine
│   │   ├── quantum_engine.py       # QuantumModelEngine (abstract interface)
│   │   ├── experiment_runner.py    # ExperimentRunner
│   │   ├── evaluation_engine.py    # EvaluationEngine
│   │   ├── explainability_engine.py# ExplainabilityEngine
│   │   └── results_store.py        # ResultsStore
│   │
│   ├── quantum/                    # Quantum implementations (replaceable)
│   │   ├── base.py                 # Abstract QuantumModel interface
│   │   ├── pennylane_vqc.py        # PennyLane VQC implementation
│   │   └── qiskit_vqc.py           # Qiskit ML VQC implementation (optional)
│   │
│   ├── config.py                   # Configuration constants, seeds
│   ├── requirements.txt            # Python dependencies (Python 3.12)
│   └── Dockerfile                  # Backend container
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── DatasetSelector.jsx
│   │   │   ├── PreprocessingConfig.jsx
│   │   │   ├── ModelSelector.jsx
│   │   │   ├── ExperimentRunner.jsx
│   │   │   ├── ResultsTable.jsx
│   │   │   ├── ConfusionMatrix.jsx
│   │   │   ├── ROCCurve.jsx
│   │   │   ├── SHAPPlot.jsx
│   │   │   ├── ExperimentMetadata.jsx
│   │   │   └── VerdictPanel.jsx
│   │   ├── api/
│   │   │   └── client.js           # Axios API client
│   │   └── pages/
│   │       ├── Dashboard.jsx
│   │       └── ExperimentDetail.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── Dockerfile
│
├── results/                        # Persistent experiment results (mounted volume)
│   └── experiments.json            # or SQLite db
│
├── docs/                           # This directory — all architecture docs
│   ├── PROJECT_KNOWLEDGE.md
│   ├── RESEARCH_LOG.md
│   ├── CLAIMS_LEDGER.md
│   ├── TECH_STACK.md
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── SOFTWARE_ARCHITECTURE.md
│   ├── DEMO_SPECIFICATION.md
│   └── OPEN_QUESTIONS.md
│
└── docker-compose.yml
```

---

## 3. Module Specifications

### 3.1 DatasetManager

**File:** `backend/core/dataset_manager.py`

**Responsibility:** Load, validate, and cache datasets.

```python
class DatasetManager:
    def load_wdbc(self) -> tuple[np.ndarray, np.ndarray]:
        """Load WDBC from sklearn.datasets. Returns (X, y) where y: 0=benign, 1=malignant."""
        
    def validate(self, X: np.ndarray, y: np.ndarray, dataset_name: str) -> dict:
        """
        Validate dataset schema. Returns validation report.
        Asserts: correct shape, no missing values, correct class count.
        Raises DatasetValidationError on failure.
        """
        
    def list_available(self) -> list[str]:
        """Return list of available dataset names."""
```

**Design notes:**
- WDBC is loaded via `sklearn.datasets.load_breast_cancer()`.
- Target encoding: benign=0, malignant=1 (sklearn default is reversed; must be checked).
- Future datasets added by implementing `load_<name>` method.

---

### 3.2 PreprocessingEngine

**File:** `backend/core/preprocessing_engine.py`

**Responsibility:** Perform all preprocessing, strictly preventing data leakage.

```python
class PreprocessingEngine:
    def fit(self, X_train: np.ndarray, n_pca_components: int) -> None:
        """
        Fit StandardScaler and PCA on X_train ONLY.
        Must be called BEFORE any transform. Never call on test data.
        """
        
    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transform X using ALREADY FITTED scaler and PCA.
        Raises if fit() has not been called.
        """
        
    def fit_transform(self, X_train: np.ndarray, n_pca_components: int) -> np.ndarray:
        """Fit on X_train and return transformed X_train. Convenience method."""
        
    def get_config(self) -> dict:
        """Return preprocessing configuration for reproducibility recording."""
```

**Design notes:**
- Internal state: `_scaler` (StandardScaler), `_pca` (PCA), `_is_fitted` (bool).
- `transform()` raises `PreprocessingNotFittedError` if called before `fit()`.
- This class is the primary guard against data leakage.

---

### 3.3 ClassicalModelEngine

**File:** `backend/core/classical_engine.py`

**Responsibility:** Train and evaluate classical ML models.

```python
class ClassicalModelEngine:
    SUPPORTED_MODELS = ['svm', 'random_forest', 'xgboost']
    
    def train(
        self, 
        model_name: str,
        X_train: np.ndarray,
        y_train: np.ndarray,
        config: dict,
        random_state: int
    ) -> tuple[object, float]:
        """
        Train the specified model. Returns (fitted_model, training_time_seconds).
        """
        
    def evaluate(
        self,
        model: object,
        X_test: np.ndarray,
        y_test: np.ndarray
    ) -> dict:
        """
        Evaluate model on test set. Returns dict of all required metrics.
        Includes: accuracy, sensitivity, specificity, precision, f1, roc_auc,
                  inference_time, confusion_matrix.
        """
        
    def get_probability_scores(self, model: object, X: np.ndarray) -> np.ndarray:
        """Return probability scores for ROC-AUC computation."""
```

---

### 3.4 QuantumModelEngine (Abstract Interface)

**File:** `backend/core/quantum_engine.py`

**Responsibility:** Define the interface that all quantum model implementations must satisfy.

```python
from abc import ABC, abstractmethod

class QuantumModelEngine(ABC):
    @abstractmethod
    def build_circuit(self, config: dict) -> None:
        """Build the quantum circuit with the given configuration."""
        
    @abstractmethod
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        config: dict,
        random_state: int
    ) -> tuple[dict, float]:
        """
        Train quantum model. Returns (trained_params, training_time_seconds).
        """
        
    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Return binary predictions."""
        
    @abstractmethod
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Return probability scores (for ROC-AUC)."""
        
    @abstractmethod
    def get_config(self) -> dict:
        """Return complete configuration for reproducibility recording."""
```

**Concrete implementations:**
- `backend/quantum/pennylane_vqc.py` — PennyLane VQC
- `backend/quantum/qiskit_vqc.py` — Qiskit ML VQC (optional)

---

### 3.5 ExperimentRunner

**File:** `backend/core/experiment_runner.py`

**Responsibility:** Orchestrate a complete experiment run, enforce the experimental protocol.

```python
class ExperimentRunner:
    def run(self, experiment_config: ExperimentConfig) -> ExperimentResult:
        """
        Execute a full experiment following EXPERIMENT_PROTOCOL.md.
        
        Steps:
        1. Record all configuration and software versions.
        2. Load and validate dataset.
        3. Create stratified train/test split with fixed seed.
        4. Fit preprocessing on train only.
        5. For each selected model: train, evaluate, record.
        6. Compute explainability (if requested).
        7. Compute verdict.
        8. Persist result to ResultsStore.
        9. Return ExperimentResult.
        """
        
    def _record_metadata(self, config: ExperimentConfig) -> dict:
        """Record all software versions, seeds, parameters."""
```

**Key design note:** The `ExperimentRunner` creates a snapshot of all configuration parameters BEFORE starting execution. This snapshot is the reproducibility record.

---

### 3.6 EvaluationEngine

**File:** `backend/core/evaluation_engine.py`

**Responsibility:** Compute all required metrics uniformly for any model.

```python
class EvaluationEngine:
    def evaluate(
        self,
        y_true: np.ndarray,
        y_pred: np.ndarray,
        y_proba: np.ndarray | None = None
    ) -> EvaluationResult:
        """
        Compute all required metrics. Returns structured EvaluationResult.
        Includes: accuracy, sensitivity, specificity, precision, f1, 
                  roc_auc (if y_proba provided), confusion_matrix.
        """
        
    def compute_specificity(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """Compute TN / (TN + FP)."""
```

---

### 3.7 ExplainabilityEngine

**File:** `backend/core/explainability_engine.py`

**Responsibility:** Generate SHAP feature attributions for classical models and input-level attribution for quantum models.

```python
class ExplainabilityEngine:
    def explain_classical(
        self,
        model_name: str,
        model: object,
        X_background: np.ndarray,
        X_explain: np.ndarray
    ) -> dict:
        """
        Generate SHAP values for a classical model.
        - Uses TreeExplainer for RF, XGBoost.
        - Uses KernelExplainer for SVM.
        Returns SHAP values and expected value.
        """
        
    def explain_quantum(
        self,
        model: QuantumModelEngine,
        X_background: np.ndarray,
        X_explain: np.ndarray
    ) -> dict:
        """
        Generate input-level attribution for quantum model (black-box SHAP).
        NOTE: This explains input features, NOT internal circuit operations.
        Returns attribution values and explicit disclaimer text.
        """
        
    def get_circuit_info(self, model: QuantumModelEngine) -> dict:
        """
        Return circuit structure information for display.
        Includes: n_qubits, n_layers, encoding_type, ansatz_type,
                  n_parameters, measurement_type.
        """
```

---

### 3.8 ResultsStore

**File:** `backend/core/results_store.py`

**Responsibility:** Persist and retrieve experiment results.

```python
class ResultsStore:
    def save(self, result: ExperimentResult) -> str:
        """Persist experiment result. Returns experiment_id."""
        
    def load(self, experiment_id: str) -> ExperimentResult:
        """Load experiment result by ID."""
        
    def list_experiments(self) -> list[ExperimentSummary]:
        """List all stored experiments with summary metadata."""
        
    def export_json(self, experiment_id: str) -> str:
        """Export experiment as JSON string."""
```

**Storage backend:** JSON file initially; SQLite optionally for structured querying.

---

### 3.9 API Layer

**File:** `backend/api/`

**Framework:** FastAPI

**Endpoints:**

```
POST   /api/experiments          — start a new experiment
GET    /api/experiments/{id}     — get experiment result
GET    /api/experiments          — list all experiments
GET    /api/datasets             — list available datasets
GET    /api/experiments/{id}/explainability — get SHAP/attribution data
GET    /api/experiments/{id}/export         — export as JSON
```

**Design notes:**
- Long-running experiments use FastAPI `BackgroundTasks`.
- CORS configured for React frontend.
- All responses use Pydantic models (type-safe, serializable).
- Experiment status: `pending`, `running`, `completed`, `failed`.

---

### 3.10 Frontend Dashboard

**Framework:** React 18 + Vite  
**Styling:** Tailwind CSS  
**Plotting:** Recharts (comparison tables, ROC curves) or Plotly.js

**Key components:**

| Component | Purpose |
|---|---|
| `DatasetSelector` | Choose dataset (WDBC; future datasets) |
| `PreprocessingConfig` | Set PCA dims, split ratio, seed |
| `ModelSelector` | Toggle classical models; configure VQC params |
| `ExperimentRunner` | Start experiment; show progress indicator |
| `ResultsTable` | Side-by-side metrics for all models |
| `ConfusionMatrix` | Confusion matrix visualization per model |
| `ROCCurve` | ROC curves for all models on same plot |
| `SHAPPlot` | SHAP beeswarm/waterfall for selected prediction |
| `ExperimentMetadata` | Full reproducibility panel |
| `VerdictPanel` | "Did quantum improve the primary metric?" |

**UI Honesty principle:** `VerdictPanel` shows the actual result. It does NOT have conditional display logic that makes quantum look better. If `quantum_delta < 0`, show that clearly.

---

## 4. Data Flow Diagram

```
Browser (React)
     |
     | POST /api/experiments  (experiment config)
     |
     v
FastAPI (api/main.py)
     |
     | Validates request (Pydantic)
     | Launches BackgroundTask
     |
     v
ExperimentRunner.run(config)
     |
     +-- DatasetManager.load_wdbc()
     |         |
     |         +-- validate()
     |
     +-- train_test_split(stratify=y, random_state=seed)
     |
     +-- PreprocessingEngine.fit(X_train, n_pca)
     +-- PreprocessingEngine.transform(X_train) -> X_train_pca
     +-- PreprocessingEngine.transform(X_test)  -> X_test_pca
     |
     +-- For each classical model:
     |         ClassicalModelEngine.train(X_train_pca, y_train)
     |         EvaluationEngine.evaluate(y_test, y_pred, y_proba)
     |         ExplainabilityEngine.explain_classical(model, X_train_pca, X_test_pca)
     |
     +-- For VQC (if selected):
     |         QuantumModelEngine.train(X_train_pca, y_train)
     |         EvaluationEngine.evaluate(y_test, y_pred, y_proba)
     |         ExplainabilityEngine.explain_quantum(model, X_train_pca, X_test_pca)
     |
     +-- Compute verdict
     +-- ResultsStore.save(result)
     |
     v
FastAPI returns experiment_id

Browser polls GET /api/experiments/{id}
     |
     v
Display: ResultsTable, ConfusionMatrix, ROCCurve, SHAPPlot, VerdictPanel
```

---

## 5. Quantum Layer Replaceability

The `QuantumModelEngine` abstract class ensures the quantum layer can be swapped:

```python
# In ExperimentRunner:
if config.quantum_framework == "pennylane":
    quantum_engine = PennyLaneVQC()
elif config.quantum_framework == "qiskit":
    quantum_engine = QiskitVQC()
# Future: other frameworks
```

The rest of the system (evaluation, explainability, results store, API, frontend) is completely independent of which quantum framework is used.

---

## 6. Extensibility for New Datasets

Adding a new dataset requires only:
1. Adding `load_<dataset_name>(self)` method to `DatasetManager`.
2. Adding the dataset name to `DatasetManager.SUPPORTED_DATASETS`.
3. The rest of the pipeline (preprocessing, training, evaluation, explainability, API, UI) works unchanged.

---

## 7. Reproducibility Guarantee

An experiment is reproducible if and only if:
1. The same `ExperimentConfig` (including seed, all hyperparameters) is provided.
2. The same software versions are installed.
3. The dataset has not changed.

The `ExperimentMetadata` record stored with every result contains all of the above. The `ExperimentMetadata` panel in the frontend displays this record so judges can verify.
