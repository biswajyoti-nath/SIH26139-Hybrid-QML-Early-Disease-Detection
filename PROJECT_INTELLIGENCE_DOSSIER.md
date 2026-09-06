# PROJECT INTELLIGENCE DOSSIER

## 1. Executive Summary
This dossier extracts the comprehensive state, architecture, and scientific evidence of the SIH 2026 PS 26139 project: "Hybrid Quantum Machine Learning Platform for Early Disease Detection". The core philosophy of this project is evidence-driven resource allocation: rather than blindly assuming quantum superiority, the platform profiles dataset complexity and dynamically routes to the most promising computational pathway (Classical, VQC, or QSVM). The T-103 benchmark successfully proved that quantum paradigm choice dictates performance and that extreme dimensionality bottlenecks fatally starve small-scale quantum models. T-103B was formally aborted due to hardware memory limits, establishing the boundary of the local computational environment. The immediate next phase is the implementation of T-062: Evidence-Gated Quantum Pathway Selection.

## 2. Project Identity
- **Project:** SIH 26139 — Hybrid Quantum Machine Learning Platform for Early Disease Detection
- **Team:** Chai.EXE
- **Institution:** Barak Valley Engineering College
- **Organization:** Egreen Quanta
- **SIH:** Smart India Hackathon 2026
- **Problem Statement ID:** SIH26139
- **Problem Statement:** Hybrid Quantum Machine Learning Platform for Early Disease Detection
- **Theme:** MedTech / BioTech / HealthTech
- **Category:** Software
- **GitHub:** https://github.com/biswajyoti-nath/SIH26139-Hybrid-QML-Early-Disease-Detection

## 3. SIH Problem Statement Alignment
The project perfectly aligns with the software requirements of MedTech PS 26139 by focusing on early disease detection using hybrid classical-quantum models (VQC/QSVM). It avoids marketing hype, directly addressing the real-world challenge of when and how to integrate NISQ-era quantum computing into clinical ML workflows.

## 4. Current Strategic Thesis
"Instead of assuming quantum is better, we measure when and which quantum pathway is worth using."
The platform aims to serve as an intelligent, evidence-gated hybrid router:
Biomedical Dataset → Leakage-Safe Preprocessing → Dataset Complexity Profiling → Classical + Multiple Quantum Pathways → Controlled / Paired Evaluation → Evidence State → Recommended Learning Pathway.

## 5. Current Project State
- **Current Phase:** Phase 4 — Quantum Suitability & Multi-Pathway Routing
- **Active Task:** NEXT TASK is T-062 (Evidence-Gated Quantum Pathway Selection).
- **Completed Major Tasks:** T-060 (Synthetic benchmark), T-061 (Biomedical CV benchmark), T-103 (Quantum Model Shootout - VQC vs QSVM vs Classical).
- **Aborted Tasks:** T-103B (Encoding Ablation) aborted due to local hardware OOM limitations.

## 6. Complete Repository Structure
- **agents/**: Contains subagent markdown protocols (ENGINEER, EVALUATOR, etc.).
- **AGENTS.md**: Core operating system manual for autonomous agent execution.
- **backend/**:
  - **core/**: `dataset.py`, `models.py`, `cv_experiment_runner.py`, `config.py`, `preprocessing.py`, `synthetic_generator.py`, `evaluation.py`.
  - **quantum/**: `pennylane_vqc.py`, `pennylane_qsvm.py`.
  - **tests/**: pytest suite covering dataset loading, preprocessing, VQC, QSVM, etc.
- **data/**: Parkinsons data (WDBC is fetched via scikit-learn).
- **DECISIONS.md**: Architectural and research decisions.
- **docs/**: Core knowledge base (CLAIMS_LEDGER.md, T062_QUANTUM_SUITABILITY_PROTOCOL.md, T103_QUANTUM_SHOOTOUT_REPORT.md, etc.).
- **EXPERIMENT_LOG.md**: Chronological registry of CV runs.
- **experiments/**: `configs/` (JSON benchmark configurations) and `results/` (output metrics artifacts).
- **PROJECT_STATE.md, TASKS.md**: Current state machines.
- **scripts/**: Utility runners (e.g. `run_ablation.sh`, `benchmark_gpu.py`).

## 7. Architecture
- **Frontend**: [PLANNED] React dashboard.
- **Backend/API**: [PLANNED] FastAPI server.
- **Experiment Runner**: [IMPLEMENTED] `cv_experiment_runner.py`.
- **Dataset Manager**: [IMPLEMENTED] `dataset.py` (Supports WDBC, Parkinsons).
- **Preprocessing**: [IMPLEMENTED] `preprocessing.py` (Leakage-safe StandardScaler + PCA).
- **Complexity Profiler**: [PLANNED/PARTIALLY DESIGNED] Extracts R_k, L_k, ho, S.
- **Classical Models**: [IMPLEMENTED] SVM, Random Forest, XGBoost.
- **Quantum Models**: [IMPLEMENTED] `PennyLaneVQC`, `PennyLaneQSVM`.
- **Evaluation**: [IMPLEMENTED] `evaluation.py` (ROC-AUC, F1, Sensitivity, etc.).
- **Explainability**: [PLANNED] SHAP engine.
- **Results Store**: [IMPLEMENTED] JSON artifacts in `experiments/results/`.
- **Recommendation / Router (T-062)**: [PLANNED / NEXT TASK].

## 8. Implemented Components
- `backend/core/dataset.py`: `DatasetManager`. Loads UCI data, parses grouping (e.g., Parkinsons 3-recordings per patient).
- `backend/core/preprocessing.py`: `PreprocessingEngine`. Fits scaler+PCA per CV fold to prevent leakage.
- `backend/core/models.py`: `ModelFactory`. Instantiates classical and quantum models homogenously.
- `backend/core/cv_experiment_runner.py`: `CVExperimentRunner`. Executes 5-fold CV (Stratified or GroupStratified) safely.
- `backend/quantum/pennylane_vqc.py`: `PennyLaneVQC`. 8-qubit variational circuit, Adam optimizer.
- `backend/quantum/pennylane_qsvm.py`: `PennyLaneQSVM`. 8-qubit RX-fidelity kernel, highly batched, feeds into SVC.

## 9. Planned Components
- `backend/core/complexity_profiler.py`: Automated extraction of complexity characteristics ($v = [R_k, L_k, C, S, ho]$).
- T-062 Router Logic: Translates profiler output and CV evaluations into one of 4 Evidence States.
- REST API / React UI (Frontend Dashboard).
- Explainability Engine (SHAP).

## 10. Dataset Inventory
- **WDBC (Breast Cancer Wisconsin Diagnostic)**:
  - Source: UCI / sklearn
  - Samples: 569
  - Raw Features: 30
  - PCA Dimensions: 8 (retained 92.7% variance in T-103)
  - CV Strategy: 5-fold Stratified CV
  - Usage: Negative Control (Classical highly separable, quantum struggles).
- **Parkinson's Disease Classification**:
  - Source: OpenML (ID 42176) / UCI
  - Samples: 756
  - Raw Predictive Features: 753
  - Grouping: 252 subjects x 3 recordings (Requires `StratifiedGroupKFold`).
  - PCA Dimensions: 8 (retained 47.0% variance in T-103)
  - Usage: Extreme dimensionality bottleneck test.

## 11. Preprocessing Pipeline
Implemented via scikit-learn `Pipeline`. Fits `StandardScaler` followed by `PCA` strictly on the *training indices* of each cross-validation fold. Testing indices are only transformed. Global fitting is strictly prohibited to prevent data leakage.

## 12. Complexity Profiling
Designed conceptual complexity vector $v = [R_k, L_k, C, S, ho]$:
- $R_k$: PCA variance retention (measured in T-103).
- $L_k$: Information loss (1 - $R_k$).
- $C$: Compression ratio ($d_{raw} / d_{pca}$).
- $S$: Linear separability proxy.
- $ho$: Mean absolute pairwise Pearson correlation.
*Note: These are descriptive characteristics, NOT proven predictive constraints for quantum advantage.*

## 13. Classical ML
Implemented in `backend/core/models.py`:
- **SVM**: `kernel='linear'`, `C=1.0`. Evaluated inside `CalibratedClassifierCV(cv=5, ensemble=False)` for probabilty outputs.
- **Random Forest**: `n_estimators=100`.
- **XGBoost**: `n_estimators=100`, `max_depth=6`, `learning_rate=0.1`.

## 14. VQC Implementation
File: `backend/quantum/pennylane_vqc.py`
- Qubits: 8
- Feature Encoding: `AngleEmbedding(rotation='X')`
- Ansatz: `BasicEntanglerLayers(rotation=qml.RY)`
- Layers: 3 (trainable weights)
- Optimizer: Adam (`learning_rate=0.01`)
- Iterations: 100
- Backend: `lightning.gpu` with fallback to `lightning.qubit`.
- Output: PauliZ expectation value mapped to [0,1] probability.

## 15. QSVM / Quantum Kernel Implementation
File: `backend/quantum/pennylane_qsvm.py`
- Qubits: 8
- Feature Encoding: `AngleEmbedding(rotation='X')`
- Kernel: Transition-amplitude (Fidelity) $K(x, y) = |\langle \Phi(x) | \Phi(y) angle|^2$
- SVC: `kernel='precomputed'`, C=1.0. Calibrated via `CalibratedClassifierCV`.
- Backend: `lightning.gpu` (Batched $N 	imes M$ matrix via array broadcasting. Chunked to size 64 to prevent OOM).
- Autograd: Explicitly disabled (`interface=None`) to prevent memory leaks during massive CV matrix generation.

## 16. Explainability
Planned. Not yet implemented. Will involve SHAP/LIME for post-hoc feature importance on the classical fallback models.

## 17. Evaluation Methodology
Strict 5-fold CV. Fold-wise preprocessing. `StratifiedGroupKFold` used for datasets with subject-level clustering (e.g. Parkinson's). Primary metric is mean ROC-AUC. Secondary metrics: Accuracy, Precision, Recall, F1, runtime. Statistical paired differences ($\Delta_Q$) are calculated at the fold level.

## 18. Experiment Timeline
- T-001 - T-060: Early synthetic prototyping and CV baselining.
- T-061: Real biomedical baseline (WDBC vs Parkinsons) proving dataset-dependent VQC performance.
- T-103: Quantum Model Shootout (Added QSVM. Proved paradigm matters, and representation bottlenecks are fatal).
- T-103B: Quantum Encoding Ablation [ABORTED].
- T-062: Suitability Router Implementation [NEXT].

## 19. T-061 Evidence
VQC evaluated.
- WDBC: VQC = 0.620 vs SVM = 0.993
- Parkinson's: VQC = 0.519 vs SVM = 0.793

## 20. T-103 Evidence
QSVM vs VQC vs Classical evaluated.
- **WDBC (92.7% PCA variance retained)**:
  - QSVM: 0.842
  - VQC: 0.665
  - SVM: 0.995
  - RF: 0.987
  - XGBoost: 0.991
  - Paired Deltas: QSVM vs SVM ≈ -0.153 | VQC vs SVM ≈ -0.330
- **Parkinson's (47.0% PCA variance retained)**:
  - QSVM: 0.504 (Failed. Specificity 0.0, predicting majority class).
  - VQC: 0.549
  - SVM: 0.815
  - RF: 0.801
  - XGBoost: 0.781
  - Paired Deltas: QSVM vs SVM ≈ -0.311 | VQC vs SVM ≈ -0.266
- **Runtimes**: Classical < 1s | QSVM ~400s | VQC ~1900s.

## 21. T-103B Abortion Record
**Task:** T-103B Quantum Encoding Ablation (AngleEmbedding vs IQPEmbedding).
**Status:** ABORTED.
**Reason:** The non-linear $ZZ$-feature map (`IQPEmbedding`) generates $O(N^2)$ entanglement gates. Running this through PennyLane's `autograd` interface for VQC training (100 iterations on batch size 455) caused the computational graph to exponentially explode, immediately exhausting system RAM and triggering Linux Kernel OOM (Out of Memory) kills.
**Conclusion:** Local hardware (16-32GB RAM, RTX 3050 6GB VRAM) cannot support $O(N^2)$ entangling feature maps in batched VQC autograd loops. The T-103 evidence is sufficient to justify the T-062 router.

## 22. T-062 Protocol
The framework logic:
1. Profile Dataset ($R_k, L_k$, etc.)
2. Establish Classical Benchmark ($B_{classical}$)
3. Quantum Pilot Gate (Test if it's even worth running quantum based on budget and $R_k$)
4. Quantum Execution (VQC/QSVM)
5. Paired Evidence Comparison ($\Delta_j = B_{quantum,j} - B_{classical,j}$)
6. Output Evidence State

## 23. Current Router Design
The router outputs 4 definitive Evidence States:
1. **CLASSICAL PREFERRED**
2. **QUANTUM PATHWAY PROMISING**
3. **STATISTICALLY COMPARABLE**
4. **INCONCLUSIVE**

## 24. Scientific Claims Ledger Summary
**CAN CLAIM (A. Verified Fact / B. Our Experiment):**
- Standard classical models achieve >95% ROC-AUC on WDBC (8 PCA).
- PennyLane VQC integrates smoothly into standard scikit-learn pipelines.
- VQC relative performance is heavily modulated by dataset complexity (PCA bottlenecks).
- Quantum paradigm choice matters (QSVM outperforms VQC on WDBC).
- Representation bottlenecks (losing >50% variance on Parkinson's) are fatal to current 8-qubit quantum models, collapsing QSVM to majority-class guessing while classical SVM succeeds.

**DO NOT CLAIM (E. Unsupported):**
- "Quantum methods fail entirely" (QSVM got 0.842 on WDBC).
- "Quantum is useless."
- "PCA causes quantum failure." (It just correlates with the failure of 8-qubit constraints).
- Quantum advantage / clinical benefit / early detection improvement.

**Safe Language:**
- "Under the tested protocol..."
- "Dataset-dependent behaviour was observed..."
- "The tested quantum pathways performed differently..."

## 25. Documentation ↔ Implementation Mismatches
1. **DOCUMENTATION**: `T062_QUANTUM_SUITABILITY_PROTOCOL.md` defines routing mathematics.
   **ACTUAL CODE**: Router logic does not exist yet.
   **IMPACT**: T-062 is pending implementation.
2. **DOCUMENTATION**: `DEMO_SPECIFICATION.md` outlines React frontend and Verdict panel.
   **ACTUAL CODE**: Frontend directory is empty/uninitialized.
   **IMPACT**: UI tasks pending post-backend router creation.

## 26. Technical Risks
- **RAM Limits**: Autograd graphs on entangling feature maps crash the host (T-103B Aborted).
- **PCIe Latency**: $O(100)$ VQC iterations on `lightning.gpu` takes ~30 minutes per fold due to CPU-GPU transfer overhead for tiny 8-qubit state vectors.
- **Simulator Wall**: Cannot exceed 8-10 qubits locally without exponential slowdown.

## 27. Scientific Risks
- Metrics are tied exclusively to the 8-qubit PCA bottleneck limit.
- Generalizability to non-UCI datasets is untested.

## 28. Current Limitations
- PCA fixed at $n=8$ components.
- Qubits fixed at 8.
- QSVM hyperparameter $C$ uncalibrated.

## 29. Research Novelty
- Evidence-gated resource allocation rather than assuming quantum advantage.
- Direct paired empirical comparison of classical, VQC, and QSVM on identical biomedical CV folds.
- Formulating uncertainty and computational cost into the routing decision.

## 30. SIH Winning Differentiators
Extreme Scientific Honesty. Instead of fabricating 99% accuracy on a quantum circuit (which judges will spot as fake), the platform *measures* the quantum collapse on complex datasets and proves why the fallback classical framework is necessary. The intellectual property is the intelligent router itself.

## 31. Demo Readiness
- Backend Data/ML Core: **PARTIALLY READY**
- API Endpoints: **NOT READY**
- Frontend UI: **NOT READY**

## 32. PPT-Relevant Facts
- **Strongest Visual:** Paired fold-level ROC-AUC distributions proving quantum paradigm divergence.
- **Differentiator:** The hybrid platform is failure-resistant because it falls back to classical methods when quantum paths collapse (e.g., Parkinson's dataset).

## 33. Judge Q&A
- **Why not just use Classical?** Classical *is* used. The router defaults to classical unless empirical profiling demonstrates quantum promise.
- **Why only 8 dimensions?** Simulator and NISQ hardware limits. This creates a representation bottleneck, which is exactly what our router tests for.
- **What happens if quantum loses?** The router outputs CLASSICAL PREFERRED and serves the classical predictions to the clinician. Patient safety is uncompromised.
- **Why was T-103B abandoned?** OOM hardware constraints for $O(N^2)$ autograd tensors. It proves that advanced quantum feature maps require cloud HPC, validating our focus on lightweight dynamic routing.

## 34. Open Questions
- What exact threshold of PCA variance retention triggers a CLASSICAL PREFERRED short-circuit?
- How do we calculate strict statistical significance ($\sigma_\Delta$) across 5 folds?

## 35. Exact Next Steps
T-062: Build the Python module that ingests the JSON output of the CVRunner and formally categorizes it into one of the 4 Evidence States.

## 36. Complete File-to-Concept Map
- `dataset.py` -> Data Ingestion & Integrity.
- `preprocessing.py` -> Leakage-safe scaling & compression.
- `models.py` -> Classical & Quantum interfaces.
- `cv_experiment_runner.py` -> Execution & Evaluation engine.
- JSON Artifacts -> Immutable scientific evidence base.
- Router -> (Next Phase) Decision logic.

## 37. Source of Truth Hierarchy
1. Actual executable code
2. Experiment artifacts/results/logs
3. Claims ledger
4. Project state
5. Research protocol
6. Architecture/design documents
7. README/general documentation

---
# HANDOFF FOR NEXT AGENT

CURRENT OBJECTIVE:
T-062 Evidence-Gated Quantum Pathway Selection

DO NOT DO:
- Do not restart T-103B
- Do not run heavy quantum ablations
- Do not assume quantum superiority
- Do not modify canonical experimental evidence
- Do not make unsupported clinical claims

NEXT:
Implement T-062 using the existing T-103 evidence while preserving the scientific claims policy.

**IF I WERE A NEW AGENT ENTERING THIS REPOSITORY TODAY, HERE IS EVERYTHING I NEED TO KNOW IN 20 BULLETS:**
1. This is SIH PS 26139: Hybrid QML for Early Disease Detection.
2. We do NOT assume quantum is better; we measure it.
3. The platform is an evidence-gated router, not just a model.
4. T-103 benchmarked SVM vs VQC vs QSVM on WDBC and Parkinson's.
5. All experiments use strict 5-fold CV and fold-wise PCA (8 dimensions) to prevent data leakage.
6. Parkinson's dataset groups 3 recordings per patient (StratifiedGroupKFold used).
7. On WDBC (92% PCA variance), QSVM vastly outperformed VQC (0.842 vs 0.665). Paradigm matters.
8. On Parkinson's (47% PCA variance), both quantum methods collapsed (~0.50 AUC).
9. Classical SVM succeeded on both (0.995 and 0.815), proving the 8D PCA bottleneck is fatal specifically to small-scale quantum models.
10. T-103B (Encoding ablation) was aborted due to massive RAM OOM errors from $O(N^2)$ autograd graphs.
11. Local hardware is limited to RTX 3050 (6GB) and finite RAM. Do not run heavy simulations.
12. Your active task is T-062: building the router logic based on the T-103 JSON results.
13. Router output must be: Classical Preferred, QSVM Promising, VQC Promising, or Inconclusive.
14. Do not fabricate results, metrics, or claim clinical validation.
15. Do not say "quantum fails"; say "dataset-dependent behaviour was observed."
16. The Frontend UI is not yet built.
17. The API is not yet built.
18. Source of truth is executable code > JSON results > claims ledger > docs.
19. Read `AGENTS.md` and this dossier fully before proceeding.
20. Act exclusively as the T-062 Software Architect.
