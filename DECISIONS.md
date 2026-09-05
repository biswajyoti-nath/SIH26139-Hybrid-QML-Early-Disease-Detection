# DECISIONS.md — Architecture & Research Decision Log
## SIH 26139 · Hybrid QML Platform

> Record every important decision here. Settled decisions should NOT be revisited unless new evidence appears.  
> Format: see template below.

---

## Decision Template

```
## Decision: <name>
- **Date:** YYYY-MM-DD
- **Decision:** What was decided.
- **Reason:** Why this choice was made.
- **Alternatives considered:** What else was evaluated.
- **Evidence:** Data, benchmarks, or references that informed the choice.
- **Consequences:** What this choice requires or prevents.
- **Status:** SETTLED | REVISABLE | SUPERSEDED
```

---

## Decision: Scientific Framing

- **Date:** 2026-09-05
- **Decision:** The project frames itself as "a platform for testing whether quantum ML adds value" — NOT as a system that assumes or demonstrates quantum advantage.
- **Reason:** Gupta et al. 2025 (npj Digital Medicine) reviewed 4,915 QML-health papers and found no consistent empirical evidence of quantum utility over classical methods in digital health. Claiming quantum advantage without evidence would be scientifically dishonest and easily challenged by SIH judges.
- **Alternatives considered:** Claiming superiority of quantum approach (rejected — no evidence); positioning as purely classical with quantum as add-on (rejected — doesn't meet PS 26139).
- **Evidence:** Gupta et al. (2025). DOI: 10.1038/s41746-025-01597-z. Verified via Tavily.
- **Consequences:** All claims must pass the Claims Ledger. UI VerdictPanel must display honest comparison. If quantum loses, that is still a valid research result.
- **Status:** SETTLED

---

## Decision: Python Version — 3.12 (not 3.14)

- **Date:** 2026-09-05
- **Decision:** Use Python 3.12 for all backend code, virtual environment, and Docker images.
- **Reason:** System Python is 3.14.4. PennyLane, Qiskit Machine Learning, and related packages officially support Python 3.10–3.13. Python 3.14 compatibility is unknown/unconfirmed. Using 3.14 risks installation failures at a critical juncture.
- **Alternatives considered:** Python 3.14 (risky), Python 3.11 (slightly older LTS).
- **Evidence:** Tavily research: qiskit-machine-learning 0.9.x supports 3.10–3.13; pennylane-lightning dropped 3.10, supports 3.11–3.13.
- **Consequences:** Must install Python 3.12 via pyenv or use Docker python:3.12-slim. `.venv` must be created with `python3.12`.
- **Status:** SETTLED

---

## Decision: Primary Quantum Framework — PennyLane

- **Date:** 2026-09-05
- **Decision:** PennyLane is the primary framework for VQC implementation. Qiskit Machine Learning is secondary (used for ZZFeatureMap experiments and optional cross-validation).
- **Reason:** PennyLane has a more ML-native interface (native autodiff via parameter-shift rule, PyTorch/JAX integration), lighter dependency footprint, and `lightning.qubit` for fast simulation. It is easier to write leakage-safe, reproducible code with PennyLane.
- **Alternatives considered:** Qiskit ML only (heavier dependencies; VQC class is pre-built but less flexible); both equally (creates maintenance overhead).
- **Evidence:** TECH_STACK.md; PennyLane documentation; Qiskit ML 0.9 release notes.
- **Consequences:** VQC implementation uses `qml.qnode`, `qml.AngleEmbedding`, `qml.RealAmplitudes`. Qiskit ML kept as optional second implementation for ZZFeatureMap experiments.
- **Status:** SETTLED (revisable if PennyLane fails Python 3.12 install)

---

## Decision: Initial VQC Configuration

- **Date:** 2026-09-05
- **Decision:** Default VQC config: n_qubits=8, encoding=AngleEmbedding(Ry), ansatz=RealAmplitudes(linear), n_layers=3, optimizer=Adam(lr=0.01), backend=lightning.qubit, max_iter=100.
- **Reason:** 8 qubits = 8 PCA components retaining ~90% variance. AngleEmbedding is simplest reproducible encoding. RealAmplitudes is the standard NISQ ansatz. Adam is fast with parameter-shift gradients. 3 layers avoids barren plateau territory while providing expressibility.
- **Alternatives considered:** n_qubits=5 (too lossy), n_qubits=10 (slower), ZZFeatureMap (more complex, second experiment), COBYLA (gradient-free, slower).
- **Evidence:** OPEN_QUESTIONS.md Q3.1–Q3.6; Cerezo et al. 2021 (barren plateau guidance).
- **Consequences:** These are the default config. The ExperimentRunner must record them exactly. PCA n_components must equal n_qubits. Alternative configs (n=5, n=10, ZZFeatureMap) are separate experiments, not replacements.
- **Status:** SETTLED (initial configuration; results may prompt follow-up experiments)

---

## Decision: Data Split Strategy

- **Date:** 2026-09-05
- **Decision:** 80/20 stratified holdout split (seed=42) for prototyping; 5-fold stratified CV for final reported results.
- **Reason:** Holdout is fast for iteration. CV provides stable estimates for the demo. Both use stratification to maintain class ratio (62.7% benign / 37.3% malignant).
- **Alternatives considered:** 70/30 split (smaller train), leave-one-out (too slow for quantum).
- **Evidence:** EXPERIMENT_PROTOCOL.md §3; OPEN_QUESTIONS.md Q4.1.
- **Consequences:** ExperimentRunner must support both split strategies. Holdout for T-032; CV for T-042 final results.
- **Status:** SETTLED

---

## Decision: Preprocessing Leakage Prevention

- **Date:** 2026-09-05
- **Decision:** All preprocessing (StandardScaler, PCA) MUST be fitted on training data only. This is enforced architecturally by `PreprocessingEngine.fit(X_train)` → `transform(X)`.
- **Reason:** Fitting scaler/PCA on all data before splitting leaks test-set statistics into the training signal, artificially inflating reported performance. This is a common and career-damaging mistake in ML papers.
- **Alternatives considered:** Fit on all data (explicitly rejected — data leakage).
- **Evidence:** EXPERIMENT_PROTOCOL.md §2 (Preprocessing); standard ML best practice.
- **Consequences:** `PreprocessingEngine.transform()` must raise `PreprocessingNotFittedError` if `fit()` has not been called. This is a hard architectural constraint.
- **Status:** SETTLED — NON-NEGOTIABLE

---

## Decision: Results Persistence — JSON files

- **Date:** 2026-09-05
- **Decision:** Experiment results are stored as JSON files in `experiments/results/<exp_id>.json`. No database for MVP.
- **Reason:** JSON is human-readable, version-controllable, debuggable, and requires no ORM. Sufficient for MVP scale (tens of experiments).
- **Alternatives considered:** SQLite (more queryable), PostgreSQL (overkill for MVP).
- **Evidence:** OPEN_QUESTIONS.md Q1.3.
- **Consequences:** `ResultsStore` reads/writes JSON. Never overwrites an existing file. Experiment IDs must be unique (timestamp-based). Migration to SQLite is straightforward if query needs arise.
- **Status:** SETTLED (revisable if query complexity increases)

---

## Decision: WDBC as Pilot Dataset

- **Date:** 2026-09-05
- **Decision:** Breast Cancer Wisconsin (Diagnostic) is the sole pilot dataset for the MVP.
- **Reason:** Small enough for quantum simulation (569 samples); well-established benchmark; sklearn built-in; binary classification; meaningful real-world domain.
- **Alternatives considered:** Heart Disease (UCI — different problem type), Parkinson's (smaller), synthetic data (no clinical relevance).
- **Evidence:** docs/PROJECT_KNOWLEDGE.md §9; UCI DOI: 10.24432/C5DW2B.
- **Consequences:** WDBC must be loaded via `sklearn.datasets.load_breast_cancer()`. Target encoding: 0=benign (sklearn label 1), 1=malignant (sklearn label 0) — NOTE: sklearn's default labels are inverted. Must verify and correct encoding so malignant=1.
- **Status:** SETTLED

---

## Decision: Claims Firewall

- **Date:** 2026-09-05
- **Decision:** All claims must be classified per `docs/CLAIMS_LEDGER.md` before appearing in any PPT, demo, or documentation. Category E claims (UNSUPPORTED / DO NOT CLAIM) are permanently prohibited.
- **Reason:** Scientific integrity; SIH judge credibility; avoid contradicted-by-evidence claims.
- **Alternatives considered:** None — this is non-negotiable.
- **Status:** SETTLED — NON-NEGOTIABLE

---

## Pending Decisions

| Question | Options | Decision gate |
|---|---|---|
| Q1.1: Python 3.14 compatibility | Test 3.14; fallback to 3.12 | T-010 |
| Q3.1: Feature encoding (ZZFeatureMap vs Angle) | Empirical comparison | T-041, T-042 |
| Q3.5: n_layers (1, 3, 5) | Empirical (loss curve analysis) | T-041 |
| Q4.1: CV vs holdout for final results | Both: holdout for proto, CV for final | T-032 → T-042 |
| Q5.1: SHAP background sample size | N=50 initial; tune if too slow | T-050 |

### 09. Graphify Tool Integration
- **Context:** Evaluated `graphify` for building a project context graph over our Markdown-heavy research repository.
- **Decision:** Do NOT force Graphify into the automated pipeline.
- **Rationale:** The repository currently consists of 23+ Markdown/document files. Graphify relies on a semantic LLM pass to build relations between non-code text files, which requires setting an explicit `GEMINI_API_KEY` (or similar). Mandating external API keys for a simple health check or graph build violates our reproducible, offline-first development ethos. 
- **Alternative:** We manually maintain `docs/PROJECT_HIERARCHY.md` as the definitive structural map of the project.

### Decision 10: Quantum Framework Selection
- **Context:** We need a framework to implement the VQC that handles quantum gradients efficiently and integrates natively with our Python `scikit-learn` testing pipeline.
- **Decision:** PennyLane (0.45.1) with `lightning.qubit`.
- **Alternatives:** Qiskit (qiskit-machine-learning).
- **Reasoning:** PennyLane abstracts the gradient calculation securely and integrates effortlessly with standard NumPy optimizers, enabling a VQC class that perfectly matches our `ModelFactory` interface. The C++ `lightning.qubit` statevector simulator provides extreme speed improvements over standard simulators for prototype workloads (like our 8-qubit WDBC run).
- **Consequences:** We depend strictly on PennyLane. If we eventually want hardware execution, we can use PennyLane plugins (e.g., `pennylane-qiskit`) rather than rewriting the circuit from scratch.
