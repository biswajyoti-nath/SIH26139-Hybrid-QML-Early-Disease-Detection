# OPEN_QUESTIONS.md
## SIH 26139 — Open Questions and Unresolved Decisions
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Explicitly list every unresolved technical, experimental, and strategic question. Do NOT arbitrarily resolve these to eliminate uncertainty. Flag which ones require experimentation.

---

## Priority Levels

| Level | Meaning |
|---|---|
| 🔴 CRITICAL | Must be resolved before any implementation begins |
| 🟡 HIGH | Must be resolved before VQC implementation begins |
| 🟢 MEDIUM | Should be resolved before demo; can be deferred |
| ⚪ LOW | Can be deferred to future work |

---

## Category 1 — Environment and Infrastructure

### Q1.1 — Python 3.14 Package Compatibility
**Priority:** 🔴 CRITICAL

The installed Python version is 3.14.4. Key quantum packages (PennyLane, Qiskit, qiskit-machine-learning) officially support Python 3.10–3.13. Python 3.14 support is unknown or unconfirmed.

**Resolution required:**
- Attempt `pip install pennylane` in a Python 3.14 environment.
- Attempt `pip install qiskit qiskit-aer qiskit-machine-learning` in a Python 3.14 environment.
- If either fails: create a Python 3.12 virtual environment and use that.
- **If Python 3.14 is incompatible**, use Python 3.12 via `python3.12 -m venv` or Docker.

**Decision gate:** Cannot write any quantum code until this is resolved.

---

### Q1.2 — Virtual Environment Strategy
**Priority:** 🔴 CRITICAL

Options:
1. Native Python 3.14 venv (risky, see Q1.1)
2. Python 3.12 venv via pyenv or system Python 3.12
3. Docker container with Python 3.12-slim as base

**Recommendation:** Use Python 3.12 venv. If pyenv is not installed, use Docker.

---

### Q1.3 — Results Persistence: JSON vs SQLite
**Priority:** 🟢 MEDIUM

The `ResultsStore` needs a backend. Options:
1. **JSON files** — simple, human-readable, easy to inspect. Suitable for MVP.
2. **SQLite** — structured queries, better for list/filter. Slightly more complex.

**Recommendation:** Start with JSON. Migrate to SQLite if query needs arise.

---

## Category 2 — Quantum Framework

### Q2.1 — Primary Quantum Framework: PennyLane vs Qiskit ML
**Priority:** 🟡 HIGH

Must choose one primary framework for the VQC implementation.

| Factor | PennyLane | Qiskit ML |
|---|---|---|
| ML integration | Native autodiff (JAX/torch) | sklearn-like API |
| VQC class | Manual (`qml.qnode`) | Pre-built `VQC` class |
| ZZFeatureMap | Manual or via conversion | Built-in |
| Simulator | `lightning.qubit` (fast C++) | `qiskit-aer` |
| Python 3.14 | UNKNOWN | UNKNOWN |
| Dependency size | Lighter | Heavier |

**Recommended decision criterion:** Whichever installs successfully on our environment. If both install: use PennyLane as primary.

**Resolution:** Install and run a minimal VQC example on WDBC data with each framework. Record runtime and ease of use.

---

## Category 3 — Quantum Circuit Design

### Q3.1 — Feature Encoding Method
**Priority:** 🟡 HIGH

Must select ONE encoding and fix it before the experiment.

| Encoding | Method | Qubits needed | Notes |
|---|---|---|---|
| AngleEmbedding (Rx) | Feature → rotation angle on single qubit | n = n_features | Simple; standard practice |
| AngleEmbedding (Ry) | Feature → Ry rotation | n = n_features | Very common; used as default |
| ZZFeatureMap | Second-order Pauli feature map | n = n_features | From Havlíček et al.; more complex |
| Amplitude encoding | Features as quantum state amplitudes | log2(n_features) | More qubits efficient; harder to implement |

**Recommendation:** Start with `AngleEmbedding` (Ry) for simplicity and reproducibility. Experiment with ZZFeatureMap as a second configuration.

**Resolution:** Empirical — run a small-scale experiment with both encodings and compare.

---

### Q3.2 — Ansatz Design
**Priority:** 🟡 HIGH

| Ansatz | Structure | Trainability |
|---|---|---|
| RealAmplitudes | Ry + CNOT entangling layers | Generally good; fewer parameters |
| TwoLocal | Configurable gates + entanglement | More flexible; more parameters |
| StronglyEntanglingLayers | Ry,Rz + CNOT | More expressive; may have barren plateaus |

**Recommendation:** Start with `RealAmplitudes` (linear entanglement). This is the standard default and avoids excessive parameter count.

**Resolution:** Use RealAmplitudes as the baseline ansatz. If training fails (barren plateaus), investigate alternatives.

---

### Q3.3 — Number of Qubits
**Priority:** 🟡 HIGH (linked to Q3.4 — PCA dimensionality)

The number of qubits equals the PCA dimensionality.

| n_qubits | PCA dims | Circuit complexity | Training speed |
|---|---|---|---|
| 5 | 5 | Low | Fast |
| 8 | 8 | Medium | Moderate |
| 10 | 10 | Higher | Slow |

**Decision gate:** Choose n_qubits = n_pca_dims. Determined by Q3.4.

**Recommendation:** Start with n=8. Provides more information than n=5 while remaining computationally manageable.

---

### Q3.4 — PCA Dimensionality
**Priority:** 🟡 HIGH

| n_components | PCA variance retained (estimate) | Quantum circuit size |
|---|---|---|
| 5 | ~80-85% | 5 qubits |
| 8 | ~90-92% | 8 qubits |
| 10 | ~93-95% | 10 qubits |

**Exact variance retained must be computed on the actual WDBC data after fitting PCA.**

**Recommendation:** Run PCA with n=5, 8, 10; compute `pca.explained_variance_ratio_.cumsum()` for each; select based on variance retained vs circuit complexity trade-off.

**Resolution:** Empirical — compute on WDBC data during environment setup.

---

### Q3.5 — Number of VQC Layers
**Priority:** 🟡 HIGH

| n_layers | Parameters (8 qubits, RealAmplitudes) | Training stability |
|---|---|---|
| 1 | 16 | Very stable; may underfit |
| 3 | 48 | Good balance |
| 5 | 80 | May approach barren plateau territory |

**Recommendation:** Start with 3 layers. Monitor loss curve for barren plateau signs (flat, near-zero gradients).

**Resolution:** Empirical — train with 1, 3, 5 layers; compare validation loss curves.

---

### Q3.6 — Classical Optimizer for VQC
**Priority:** 🟡 HIGH

| Optimizer | Type | Notes |
|---|---|---|
| COBYLA | Gradient-free | Robust but slow; good for noisy circuits |
| SPSA | Gradient-based (stochastic) | Designed for noisy simulators; IBM standard |
| Adam | Gradient-based | Fast but requires gradient computation |
| L-BFGS-B | Gradient-based | Good for smooth objectives |

**Recommendation for PennyLane:** Adam with parameter-shift gradients. Fast and well-tested.

**Recommendation for Qiskit ML VQC:** COBYLA or SPSA (defaults in the VQC class).

**Resolution:** Use Adam as default. Switch to COBYLA if training diverges.

---

### Q3.7 — Maximum Optimizer Iterations
**Priority:** 🟢 MEDIUM

| Max iters | Training time (estimate, 8q, 3L, 455 train) | Convergence |
|---|---|---|
| 50 | Fast | May not converge |
| 100 | Moderate | Reasonable starting point |
| 200 | Slow | Better convergence chance |

**Recommendation:** 100 iterations initially. Check convergence curve. If not converged, try 200.

---

## Category 4 — Experimental Design

### Q4.1 — Cross-Validation Strategy
**Priority:** 🟢 MEDIUM

Options:
1. **Stratified holdout (80/20)** — fast, simple, suitable for rapid prototyping.
2. **5-fold stratified CV** — more reliable estimates; preprocessing must be re-fitted inside each fold.
3. **Both** — holdout for prototyping, K-fold for final reported results.

**Recommendation:** Use holdout for MVP; add K-fold for final demo results.

**Resolution:** Implement holdout first. Add K-fold support in the `ExperimentRunner`.

---

### Q4.2 — Multiple Seeds
**Priority:** 🟢 MEDIUM

Running with seeds [42, 123, 2025, 7, 999] provides stability estimates (mean ± std). This is scientifically preferable to a single seed.

**Constraint:** VQC training is slow (minutes per run); 5 seeds × 1 VQC run = 5× training time.

**Recommendation:** Implement multi-seed support; use it for final reported results. Cache results so re-running the demo doesn't require re-training.

---

### Q4.3 — Noise Model Experiment
**Priority:** ⚪ LOW

Should we include an optional noise model experiment (add depolarizing noise to the VQC)?

**Arguments for:**
- More realistic NISQ simulation.
- Demonstrates the platform's extensibility.
- Shows VQC robustness under noise.

**Arguments against:**
- Significant additional implementation complexity.
- Dramatically slower simulation.
- Not required for MVP.

**Resolution:** Defer to Phase 6 (future work). Document as a planned extension.

---

## Category 5 — Explainability

### Q5.1 — SHAP KernelExplainer for VQC
**Priority:** 🟢 MEDIUM

`KernelExplainer` requires a background dataset (sample of training data) and is slow for large samples.

**Question:** How many background samples for `KernelExplainer` on VQC?

- Too few (N=10): unstable SHAP estimates.
- Too many (N=100+): very slow.

**Recommendation:** Use N=50 background samples from X_train_pca. This balances stability and speed.

**Resolution:** Empirical — test SHAP runtime with N=25, 50, 100 background samples.

---

### Q5.2 — Circuit Visualization
**Priority:** 🟢 MEDIUM

Should the UI display the quantum circuit diagram?

- PennyLane: `qml.draw(circuit)` provides text or matplotlib circuit diagram.
- Qiskit: `circuit.draw()` provides multiple formats.

**Recommendation:** Include a text representation of the circuit in the metadata panel. A visual diagram would be nice-to-have.

---

## Category 6 — Strategic Questions

### Q6.1 — What if VQC Fails to Train?
**Priority:** 🔴 CRITICAL (contingency plan)

If VQC training diverges (barren plateau, numerically unstable):
1. Reduce n_layers.
2. Reduce n_qubits.
3. Switch optimizer (Adam → COBYLA).
4. Switch encoding (ZZFeatureMap → AngleEmbedding).
5. As a last resort: replace VQC with QSVM (quantum kernel SVC).

**QSVM fallback:** `qiskit_machine_learning.algorithms.QSVC` or quantum kernel + sklearn `SVC`. This is simpler to train and may be more stable.

**Resolution:** Have QSVM implemented as a backup from the start.

---

### Q6.2 — Demo Caching Strategy
**Priority:** 🟡 HIGH

VQC training takes minutes. The SIH demo may have strict time limits.

**Strategy:** Pre-train all models before the demo. Cache results in `ResultsStore`. During the demo, load cached results rather than re-training.

**UI requirement:** Show "Load cached results" option alongside "Run Experiment" button.

**Risk:** If cached results don't load, need a fallback. Solution: keep pre-trained model artifacts as files that can be loaded.

---

### Q6.3 — Sammartino 2026 Reference
**Priority:** 🟡 HIGH (for PPT/documentation)

The project documents cite "Sammartino 2026" but no verifiable publication was found. This reference must be resolved before the PPT or any submission is finalized.

**Action required:**
1. Check with team members who added this reference.
2. Locate the actual publication.
3. If no publication found: remove from reference list entirely.
4. Do NOT cite an unverifiable reference in any SIH submission.

---

### Q6.4 — Prajapati et al. Publication Year
**Priority:** 🟡 HIGH (for PPT/documentation)

The project documents list "Prajapati et al. 2025" but the source appears to be a 2023 Springer book chapter.

**Action required:**
1. Verify the actual publication year.
2. If it is 2023, correct the reference year in all documents.
3. Use the correct year in any PPT or submission.

---

## Resolved Questions (Record Decisions Here)

| Question | Decision | Date | Rationale |
|---|---|---|---|
| (None yet) | | | |

*This section should be updated as decisions are made during implementation.*
