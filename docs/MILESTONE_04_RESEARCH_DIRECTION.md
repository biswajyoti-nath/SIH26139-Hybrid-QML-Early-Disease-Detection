# MILESTONE 04: Research Direction Pivot

## 1. Current Architecture
The architecture is a hybrid classical/quantum benchmarking pipeline featuring:
- A biomedical dataset manager (`DatasetManager`) that enforces strict test/train splits.
- A leakage-safe `PreprocessingEngine` utilizing Scikit-Learn Pipelines.
- A `ModelFactory` providing identical standard interfaces for classical ML (SVM, RF, XGBoost) and QML (PennyLane VQC).
- A reproducible `CVExperimentRunner` orchestrating 5-fold cross-validation and rigorous metric collection.

## 2. Current Experiments
- **WDBC Baseline (Classical):** Verified 97-99% ROC-AUC across SVM, RF, and XGBoost.
- **Quantum Ablation Protocol:** Systematic VQC evaluation manipulating dimensionality (PCA), circuit depth, loss functions, and iterations using a rapid-search holdout method followed by a 5-fold CV confirmation.
- **WDBC VQC Final:** The optimal VQC (6 qubits, 3 layers, MSE loss, 100 iterations) evaluated under strict fair-comparison rules.

## 3. Current Authoritative Results
- **SVM:** ~99.35% ROC-AUC, 95.61% Accuracy, 0.02s training time per fold.
- **VQC:** ~62.01% ROC-AUC, 61.68% Accuracy, 286.08s training time per fold.
- **Authoritative JSON:** `experiments/results/exp_005_ablation_final_cv_*.json`.

## 4. Current Scientific Claims
- Standard VQCs drastically underperform classical models on easily separable tabular data (like WDBC).
- Increasing VQC parameters (e.g., jumping from 6 to 8 qubits) degrades performance due to barren plateaus in NISQ-era representations.
- Quantum Advantage **does not** exist for standard tabular WDBC classification.

## 5. Current Limitations
- The VQC acts as a global replacement for classical models, which is inefficient and inaccurate.
- The pipeline lacks a mechanism to evaluate *when* a quantum circuit should be invoked.
- We have not explored nonlinear, highly correlated, or synthetic complex datasets where quantum state spaces might offer a theoretical advantage.

## 6. What Must Remain Unchanged
- The strict, leakage-safe cross-validation protocol.
- The objective reproducibility and metadata serialization (JSON artifacts).
- The "WDBC Negative Control" baseline proving that we do not fabricate quantum advantage.
- The Claims Firewall protecting scientific integrity.

## 7. What Should Be Extended
- The project scope moves from "Does QML win?" to "When is QML worth testing?"
- The evaluation criteria should extend beyond raw accuracy to include "Quantum Utility Scores" (robustness, noise sensitivity, classical baseline difficulty).
- The dataset module must support diverse, tunable complexity-regimes (synthetic data).

## 8. Proposed Architecture for the New Research Direction
1. **Quantum Suitability Engine:** A dataset profiler (analyzing dimensionality, non-linearity, class imbalance, classical SVM margins) to estimate a *Quantum Viability Score* prior to training.
2. **Adaptive Quantum Pathway:** A router that dynamically constructs the VQC configuration (Ansatz, Qubits, Layers) constrained by the Suitability Engine's profile.
3. **Hybrid Decision Specialist / Residual Correction:** Architectural modifications where classical models clear high-confidence samples and the VQC is trained strictly on classical residuals or low-confidence ambiguous boundaries.

## 9. Proposed Experiment Roadmap
1. **Experiment A (Complexity Regimes):** Generate datasets with increasing non-linearity and dimensionality. Map where SVM performance decays and track if VQC performance decays at a slower rate.
2. **Experiment B (Residual QML):** Train SVM on WDBC, isolate the misclassified/low-margin support vectors, and train a specialized VQC strictly on that subset.
3. **Experiment C (Utility Scoring):** Define a weighted equation factoring in `Δ ROC-AUC`, `Train Time Ratio`, and `Dataset Complexity` to empirically grade quantum utility.

## 10. Risks of Scientific Leakage / Biased Evaluation
- **Hyperparameter Cheating:** Tuning the VQC heavily on the complex dataset while leaving the classical model with default parameters. *(Mitigation: Automated GridSearchCV must be applied equally to classical models).*
- **False Specialist Advantage:** Claiming the VQC "fixes" classical errors when a secondary classical model (e.g., Gradient Boosting) would have fixed them faster. *(Mitigation: Always test against a Classical-Classical stacking ensemble).*
- **Selection Bias:** Inventing a Utility Score formula that artificially inflates the value of quantum execution despite poor accuracy. *(Mitigation: The Utility Score must penalize runtime exponentially and require a strict ROC-AUC floor).*

## 11. Exact Next Implementation Milestone
**MILESTONE 04: Complexity-Regime Benchmarking & Quantum Suitability Engine**
- Implement synthetic dataset generators with tunable decision-boundary complexity.
- Build the dataset profiler to extract statistical classical-difficulty markers.
- Run the Classical vs. Quantum suite across 3 distinct complexity regimes (Simple, Non-linear, Noise-heavy).
- Establish the correlation between dataset complexity and VQC relative performance.
