# TECH_STACK.md
## SIH 26139 — Technology Stack Audit
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Document the current environment, recommended versions, and compatibility concerns for all technologies in the proposed stack.

---

## Environment Snapshot

| Tool | Installed Version | How Detected |
|---|---|---|
| Python | 3.14.4 | `python3 --version` |
| Node.js | 22.22.1 | `node --version` |
| npm | 10.9.4 | `npm --version` |
| Docker | 29.6.2 | `docker --version` |
| git | 2.53.0 | `git --version` |
| numpy | 2.3.5 | `pip show numpy` |

### Not Installed

The following packages from the proposed stack are **NOT currently installed**:
- qiskit
- qiskit-aer
- qiskit-machine-learning
- pennylane
- pennylane-lightning
- scikit-learn
- xgboost
- shap
- fastapi
- uvicorn

---

## CRITICAL RISK: Python 3.14.4

> ⚠️ **Python 3.14 is bleeding-edge and may have package compatibility issues.**

Python 3.14 was released in 2025. As of the research audit date (2026-09-05), the installed version is 3.14.4 (a patch release, which is positive). However:

- **qiskit-machine-learning 0.9.x** officially supports Python 3.10–3.13.
- **PennyLane-Lightning** latest release supports Python 3.11–3.13 (dropped 3.10 in recent release).
- **Most quantum packages** publish wheels for Python 3.10–3.13; Python 3.14 may require compiling from source.

**Resolution options:**
1. Use `pyenv` or virtual environment with Python 3.12 or 3.13 (recommended for maximum compatibility).
2. Test each quantum package with Python 3.14 and fall back if needed.
3. Use a Docker container with Python 3.12 for reproducibility.

**Recommendation:** **Use Python 3.12** in a virtual environment. This is the safest choice for all packages in the stack.

---

## Quantum Frameworks

### Option A: PennyLane

| Property | Value |
|---|---|
| Current latest version | ~0.45.0 (pennylane-lightning 0.45.x) |
| Python support | 3.11, 3.12, 3.13 (3.10 dropped) |
| Python 3.14 support | UNKNOWN — likely not yet officially supported |
| Recommended version | 0.40+ (stable, Python 3.12 compatible) |
| Simulator backend | `lightning.qubit` (C++-accelerated, fast) |
| ML integration | Native: `qml.qnode`, `qml.grad`; supports PyTorch, JAX, NumPy |
| VQC support | Yes — `qml.qnode` + `qml.BasisEmbedding`, `qml.AngleEmbedding`, `qml.RealAmplitudes` |
| QSVM support | Via quantum kernel functions |
| License | Apache 2.0 |
| Maintainer | Xanadu |

**Pros:**
- Most Pythonic ML-friendly interface.
- Native automatic differentiation (parameter-shift rule, backpropagation).
- Tight integration with NumPy, PyTorch, JAX.
- Active maintenance and good documentation.
- `lightning.qubit` is very fast for statevector simulation.

**Cons:**
- PennyLane 3.14 compatibility unconfirmed.
- Fewer pre-built algorithm classes compared to Qiskit ML.

---

### Option B: Qiskit Machine Learning

| Property | Value |
|---|---|
| Qiskit (core) latest | 2.x (migrated from 1.x) |
| qiskit-machine-learning latest | 0.9.x |
| Python support | 3.10–3.13 (3.9 dropped in 0.9.1) |
| Python 3.14 support | UNKNOWN — not officially listed |
| Recommended version | qiskit >= 2.0, qiskit-machine-learning >= 0.9 |
| Simulator backend | Qiskit Aer (separate package: `qiskit-aer`) |
| VQC support | Yes — `qiskit_machine_learning.algorithms.classifiers.VQC` |
| QSVM support | Yes — `qiskit_machine_learning.algorithms.classifiers.QSVC` |
| License | Apache 2.0 |
| Maintainer | IBM / Qiskit Community |

**Pros:**
- Pre-built `VQC` class with configurable feature maps and ansatze.
- `ZZFeatureMap` (from Havlíček et al.) built-in.
- `RealAmplitudes` ansatz built-in.
- Good integration with scikit-learn interface.
- IBM Quantum hardware access when needed.

**Cons:**
- Larger dependency footprint.
- V1 primitives deprecated in 0.9; must use V2 primitives.
- Heavier install compared to PennyLane for basic VQC use.

---

### Framework Decision (TBD)

**Our recommendation (pending Python 3.14 compatibility check):**

Use **PennyLane as the primary framework** for the VQC implementation because:
1. Better ML-native interface (autodiff, torch integration).
2. Lighter dependency footprint.
3. `lightning.qubit` is fast for the scale we need (≤10 qubits).

Use **Qiskit Machine Learning** optionally for:
1. ZZFeatureMap experiments.
2. Cross-validation of PennyLane results.
3. Future QPU access via IBM Quantum.

**Action required before implementation:** Install both in a Python 3.12 environment and verify compatibility.

---

## Classical ML Stack

### scikit-learn

| Property | Value |
|---|---|
| Current latest | ~1.6.x |
| Python support | 3.9–3.14 (broad support) |
| Recommended version | >= 1.4 |
| Usage | SVM, PCA, StandardScaler, cross-validation, metrics |
| License | BSD-3-Clause |

### XGBoost

| Property | Value |
|---|---|
| Current latest | ~2.1.x |
| Python support | 3.10–3.13 (verify 3.14) |
| Recommended version | >= 2.0 |
| Usage | Gradient-boosted trees baseline |
| License | Apache 2.0 |

---

## Explainability

### SHAP

| Property | Value |
|---|---|
| Current latest | ~0.46.x |
| Python support | 3.9–3.13 (verify 3.14) |
| Recommended version | >= 0.44 |
| Usage | `TreeExplainer` (RF, XGBoost), `KernelExplainer` (SVM, VQC black box) |
| License | MIT |

**Note:** `KernelExplainer` is model-agnostic but slow; it will work for SVM and VQC black-box attribution. `TreeExplainer` is fast and exact for RF/XGBoost.

---

## Backend

### FastAPI + Uvicorn

| Property | Value |
|---|---|
| FastAPI current latest | ~0.115.x |
| Uvicorn current latest | ~0.32.x |
| Python support | 3.8+ (broad) |
| Recommended version | FastAPI >= 0.110, Uvicorn >= 0.30 |
| Usage | REST API serving experiment runner and results |
| License | MIT |
| Key features needed | Background tasks (experiment runner), JSON serialization, CORS for React |

---

## Frontend

### Node.js + npm (installed)

| Property | Value |
|---|---|
| Node.js installed | 22.22.1 (LTS) |
| npm installed | 10.9.4 |
| React framework | Vite + React 18 (recommended) |
| UI component library | TBD (Tailwind CSS + shadcn/ui, or Chakra UI) |
| Plotting | Recharts or Plotly.js |
| API client | Axios or fetch |

---

## Deployment

### Docker (installed)

| Property | Value |
|---|---|
| Docker installed | 29.6.2 |
| Strategy | Docker Compose: backend + frontend containers |
| Python base image | python:3.12-slim (recommended, NOT 3.14) |
| Node base image | node:22-alpine |

**Docker Compose services:**
1. `backend` — FastAPI + Python ML stack
2. `frontend` — React + Vite dev/production server
3. `(optional) db` — SQLite volume mount or PostgreSQL for results store

---

## Complete Recommended Requirements

### Python Environment (Python 3.12 via venv or Docker)

```
# Core scientific
numpy>=2.0
scipy>=1.13
pandas>=2.2

# Classical ML
scikit-learn>=1.4
xgboost>=2.0

# Quantum (primary)
pennylane>=0.40
pennylane-lightning>=0.40

# Quantum (secondary / cross-validation)
qiskit>=2.0
qiskit-aer>=0.15
qiskit-machine-learning>=0.9

# Explainability
shap>=0.44
matplotlib>=3.9
seaborn>=0.13

# Backend
fastapi>=0.110
uvicorn>=0.30
pydantic>=2.0

# Utilities
python-dotenv>=1.0
joblib>=1.4
tqdm>=4.66
```

### Frontend (package.json dependencies)

```json
{
  "react": "^18.3",
  "react-dom": "^18.3",
  "@vitejs/plugin-react": "^4.3",
  "axios": "^1.7",
  "recharts": "^2.13",
  "tailwindcss": "^3.4"
}
```

---

## Compatibility Concerns Summary

| Concern | Severity | Resolution |
|---|---|---|
| Python 3.14 + quantum packages | **CRITICAL** | Use Python 3.12 venv or Docker |
| Qiskit V1 primitives deprecated | **MEDIUM** | Use V2 primitives (>=0.8) |
| PennyLane-Lightning 3.10 dropped | **LOW** | Python 3.12 target is fine |
| XGBoost 3.14 wheels | **MEDIUM** | Verify; fallback to compile or Docker |
| SHAP + Python 3.14 | **MEDIUM** | Verify; likely fine but unconfirmed |
| Qiskit Aer + Qiskit 2.x | **LOW** | Qiskit ML 0.9 migrated to Qiskit 2.x |

---

## Implementation Order Recommendation

1. Set up Python 3.12 virtual environment.
2. Install scikit-learn, numpy, pandas, xgboost — verify all work.
3. Install PennyLane + pennylane-lightning — verify VQC example runs.
4. Install qiskit + qiskit-aer + qiskit-machine-learning — verify VQC example runs.
5. Install SHAP — verify TreeExplainer + KernelExplainer.
6. Install FastAPI + uvicorn — verify simple API starts.
7. Set up React + Vite frontend — verify npm install and dev server.
8. Create Docker Compose skeleton — verify both containers start.

Only proceed to writing application code after all packages are verified.
