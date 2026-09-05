# SIH 26139 — Hybrid Quantum Machine Learning Platform for Early Disease Detection

**Team:** Chai.EXE · Barak Valley Engineering College  
**Organization:** Egreen Quanta  
**Theme:** MedTech / BioTech / HealthTech  
**Category:** Software  

---

## Project Framing

> We are not building a system that assumes quantum wins.  
> We are building a platform that can rigorously measure when the quantum component provides value over classical ML.

Current evidence (Gupta et al. 2025, *npj Digital Medicine*, 4,915 papers reviewed) shows **no consistent empirical advantage** for quantum ML over classical methods in digital health. Our contribution is a reproducible, honest, explainable experimental framework that can test this hypothesis fairly.

**Pilot dataset:** Breast Cancer Wisconsin (Diagnostic) — WDBC, 569 samples, 30 features, binary classification.  
**Status:** Pre-implementation. Research and architecture audit complete.

---

## Quick Start (for a fresh agent or developer)

### 1. Read the operating system
```bash
cat AGENTS.md          # mandatory first read
cat PROJECT_STATE.md   # current status
cat TASKS.md           # task queue
```

### 2. Set up environment
```bash
# Python 3.12 required (not 3.14 — quantum package compatibility)
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt  # once backend/ is created
```

### 3. Check health
```bash
./scripts/health_check.sh
```

### 4. Run tests
```bash
pytest backend/tests/ -v  # once tests exist
```

---

## Directory Structure

```
core-program/
├── AGENTS.md               ← Read first. Agent operating system.
├── PROJECT_STATE.md        ← Current phase and next action.
├── TASKS.md                ← Prioritized task list.
├── DECISIONS.md            ← Architecture decisions log.
├── EXPERIMENT_LOG.md       ← Record of every experiment run.
│
├── agents/                 ← Agent protocols
│   ├── EVALUATOR.md
│   ├── RESEARCHER.md
│   ├── ENGINEER.md
│   ├── EXPERIMENTALIST.md
│   ├── JUDGE.md
│   └── SESSION_PROTOCOL.md
│
├── docs/                   ← Research and architecture (source of truth)
│   ├── PROJECT_KNOWLEDGE.md
│   ├── RESEARCH_LOG.md
│   ├── CLAIMS_LEDGER.md
│   ├── TECH_STACK.md
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── SOFTWARE_ARCHITECTURE.md
│   ├── DEMO_SPECIFICATION.md
│   └── OPEN_QUESTIONS.md
│
├── experiments/            ← Experiment artifacts (configs, results, logs)
├── scripts/                ← Utility scripts
│   └── health_check.sh
│
├── backend/                ← [TODO] FastAPI + ML core (Python 3.12)
└── frontend/               ← [TODO] React 18 + Vite dashboard
```

---

## Core Architecture (Proposed)

```
Frontend (React)  →  FastAPI Backend  →  ExperimentRunner
                                            ├── ClassicalModelEngine (SVM, RF, XGBoost)
                                            ├── QuantumModelEngine (PennyLane VQC)
                                            ├── EvaluationEngine (all 8 metrics)
                                            └── ExplainabilityEngine (SHAP + VQC attribution)
                                            ↓
                                        ResultsStore (JSON)  →  experiments/results/
```

---

## Scientific Claims Policy

All claims are governed by `docs/CLAIMS_LEDGER.md`. Key prohibitions:

| ❌ Never claim | ✅ Safe to claim |
|---|---|
| Quantum provides faster diagnosis | We are testing whether quantum adds value |
| X% accuracy (before experiments run) | The platform will measure and compare |
| WDBC is an early-detection dataset | WDBC is a research diagnostic benchmark |
| Simulator execution = quantum speedup | Simulator-first is our development strategy |
| Clinically validated | Research prototype only |

---

## Literature Foundation

| Paper | Role |
|---|---|
| Havlíček et al. (2019). Nature 567. DOI: 10.1038/s41586-019-0980-2 | Motivates VQC + ZZFeatureMap |
| Cerezo et al. (2021). Nat Rev Phys 3. DOI: 10.1038/s42254-021-00348-9 | Justifies shallow circuits (barren plateaus) |
| Gupta et al. (2025). npj Dig Med 8. DOI: 10.1038/s41746-025-01597-z | Core framing: no consistent QML advantage |
| WDBC Dataset. DOI: 10.24432/C5DW2B | Pilot dataset |

---

## Disclaimer

This is a **research prototype** developed for SIH 2026 PS 26139.  
It is NOT a medical device, NOT clinically validated, and NOT intended for clinical use.  
Results on WDBC do not constitute evidence of clinical diagnostic improvement.
