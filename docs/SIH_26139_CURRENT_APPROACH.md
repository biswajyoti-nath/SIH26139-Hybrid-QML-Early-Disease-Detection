# SIH 2026 PS 26139: Current Research & Implementation Approach

## Project

**Problem Statement:** SIH 26139  
**Title:** Hybrid Quantum Machine Learning Platform for Early Disease Detection  
**Organization:** Egreen Quanta  
**Category:** Software  
**Theme:** MedTech / BioTech / HealthTech  
**Team:** Chai.EXE  
**Institution:** Barak Valley Engineering College

---

## 1. Strategic Objective

Our primary objective is to build a solution that is both:

1. **Highly competitive for SIH 2026**, and
2. **Genuinely novel and scientifically defensible**.

The solution must remain strictly aligned with PS 26139.

### Winning hierarchy

Every proposed feature, experiment, or research direction should be evaluated in this order:

1. **PS Fit**
2. **SIH Value**
3. **Technical Novelty**
4. **Demo Value**
5. **Scientific Validity**

A technically interesting idea that does not materially serve PS 26139 should be rejected or deferred.

We should prefer **one strong, demonstrable novel contribution implemented deeply** over many superficial innovations.

---

## 2. Core Interpretation of the Problem Statement

The PS asks for a hybrid quantum-classical platform for early disease detection.

The platform is expected to support:

- Biomedical data ingestion
- Classical preprocessing and feature engineering
- Quantum-enhanced learning
- Disease prediction
- Comparison against classical baselines
- Explainability
- Performance evaluation
- Compatibility with simulators and near-term quantum hardware
- Assessment of accuracy, sensitivity, specificity, computational efficiency, and generalization

### Our interpretation

We are **not assuming that quantum machine learning is automatically better**.

Instead, the platform investigates:

> **When is a quantum learning pathway actually useful for biomedical disease detection compared with strong classical alternatives?**

This is the central research direction.

---

## 3. Central Research Hypothesis

### Primary hypothesis

> The utility of a quantum learning pathway may depend on the structure and complexity of the biomedical problem.

Therefore, rather than evaluating one quantum model on one dataset and declaring it successful, we compare classical and quantum pathways under controlled and real biomedical conditions.

The platform should be able to conclude:

- Quantum pathway is useful
- Quantum pathway is not useful
- Evidence is inconclusive
- Classical learning is preferable

A negative result is scientifically valid.

---

## 4. Key Differentiation

The proposed differentiation is an **evidence-driven hybrid learning platform**.

Instead of:

> "Quantum ML is better than classical ML."

we investigate:

> **"Under which biomedical data conditions, if any, does quantum-enhanced learning provide useful predictive value?"**

This creates a stronger system-level contribution:

**Biomedical Data → Complexity Analysis → Classical Baseline → Quantum Pathway → Unified Evaluation → Evidence-Based Recommendation**

The eventual system may therefore recommend a classical pathway when quantum learning does not provide sufficient value.

---

## 5. Current Experimental Strategy

The research is being developed in stages.

### Stage A: Controlled complexity experiments

We created synthetic biomedical-like classification regimes to study how model behaviour changes as data characteristics change.

Current regimes include:

- **R1_SIMPLE**
- **R2_NONLINEAR**
- **R3_CORRELATED**
- **R4_NOISY**
- **R5_HIGH_DIMENSIONAL**

These experiments are intended to provide controlled evidence before introducing more complicated real biomedical datasets.

### Important limitation

The current synthetic regimes are not perfectly one-factor-isolated experiments.

For example:

- R3 changes correlation/redundancy characteristics alongside other `make_classification` parameters.
- R2 contains nonlinear structure plus additional noise dimensions.
- R5 changes dimensionality and informative/redundant feature structure.

Therefore, observed differences should initially be described as **associations**, not causal proof that a single complexity factor causes quantum suitability.

---

## 6. T-060 Complexity Benchmark

### Initial benchmark

The first benchmark compared:

- SVM
- Random Forest
- XGBoost
- VQC

across five synthetic regimes.

Initial runs used:

- Stratified 5-fold CV
- Multiple random seeds
- Reduced VQC iteration budget for tractability

Representative initial results:

| Regime | SVM ROC-AUC | VQC ROC-AUC |
|---|---:|---:|
| R1_SIMPLE | ~0.986 | ~0.522 |
| R2_NONLINEAR | ~0.896 | ~0.526 |
| R3_CORRELATED | ~0.948 | ~0.742 |
| R4_NOISY | ~0.581 | ~0.525 |
| R5_HIGH_DIMENSIONAL | ~0.854 | ~0.535 |

These results are **exploratory**, not final evidence.

The apparent improvement in R3 is particularly important but must not be interpreted as proof of quantum advantage.

Possible explanations include:

- Optimization behaviour
- Training budget
- Parameterization
- Data-generation effects
- Interaction between correlation and the selected quantum feature map
- Statistical variation

The canonical validation run is required before drawing stronger conclusions.

---

## 7. Canonical T-060 Validation

A targeted canonical validation was prepared to test the most interesting observed contrast.

### Configuration

- Benchmark: `complexity_regimes_v2_canonical`
- Seeds: `42`, `123`
- Samples: `150`
- Regimes: `R1_SIMPLE`, `R3_CORRELATED`
- Models: SVM, VQC
- VQC qubits: `6`
- VQC layers: `3`
- Loss: MSE
- Iterations: `100`
- Learning rate: `0.05`

### Status

The canonical run must be completed and audited before T-061 is accepted.

No subsequent research task should treat the R3 result as established evidence until this validation is complete.

---

## 8. Real Biomedical Data Strategy

Synthetic experiments alone are insufficient for a strong SIH solution.

The next stage is to test the hypothesis on **real biomedical disease-classification data relevant to PS 26139**.

### Current data ladder

#### Dataset 1: WDBC

Wisconsin Diagnostic Breast Cancer.

Purpose:

- Controlled diagnostic benchmark
- Reproducible classical baseline
- Initial quantum baseline
- Method validation

WDBC has:

- 569 samples
- 30 real-valued features
- Binary benign/malignant classification

### Critical framing

WDBC is a **diagnostic classification benchmark**.

It must **not** be presented as evidence of clinical early detection.

---

#### Dataset 2: Parkinson's disease classification

The UCI Parkinson's Disease Classification dataset provides a substantially higher-dimensional neurological disease-classification problem.

Key characteristics:

- 756 instances
- 754 features
- Data from Parkinson's disease and healthy-control subjects
- Features derived from multiple voice/signal-processing methods

Purpose:

- Test whether model behaviour changes in a real, high-dimensional neurological disease classification problem.
- Determine whether complexity-related observations from synthetic data remain relevant in real biomedical data.

### Critical framing

The dataset is being used as a **real high-dimensional neurological disease-classification regime relevant to the PS**, not merely because it is "the hardest dataset."

---

#### Potential Dataset 3: High-dimensional omics

A later stage may evaluate an appropriate disease-related omics dataset with very high dimensionality.

This is only justified if:

- The disease-detection task remains clearly within PS 26139.
- Data can be processed reproducibly.
- The dataset is legally and technically usable.
- The added complexity provides meaningful experimental value.
- The resulting experiment can be completed within SIH constraints.

We should not add genomics merely to increase feature count.

---

## 9. Real Research Question

The refined research question is:

> **Does the relative performance and utility of quantum versus classical learning change systematically across biomedical data-complexity regimes relevant to disease detection?**

This is more defensible than asking whether quantum ML is simply "better."

---

## 10. Classical Baseline

Classical ML is the reference path.

Current models include:

- SVM
- Random Forest
- XGBoost

The purpose is to establish strong baselines before evaluating quantum models.

### Why this matters

A quantum result has little meaning without a credible classical comparison.

The system therefore must never optimize only for quantum performance.

---

## 11. Quantum Baseline

The current quantum model is a variational quantum classifier implemented with PennyLane.

### Current canonical design

- AngleEmbedding
- BasicEntanglerLayers
- 3 layers
- Pauli-Z expectation measurement
- MSE loss
- Adam optimizer
- Learning rate: `0.05`
- Controlled qubit count
- Simulator-based execution

The quantum pathway is intended to test whether quantum feature representations and variational circuits provide useful predictive behaviour.

### Current evidence

On the WDBC benchmark, the tested VQC configuration substantially underperformed the classical baselines.

This is an important result, not a failure of the project.

It demonstrates why the platform needs:

- Controlled comparison
- Complexity analysis
- Reproducible experiments
- Evidence-based model selection
- Honest reporting

---

## 12. WDBC Experimental Results

A canonical classical evaluation produced strong performance.

Representative 5-fold CV results with 8 PCA components and seed 42:

| Model | Accuracy | Sensitivity | Specificity | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| SVM | 97.36% | 96.23% | 98.03% | 96.45% | 99.39% |
| Random Forest | ~95.2% | ~91.9% | ~97.2% | ~93.4% | ~98.6% |
| XGBoost | ~96.1% | ~93.8% | ~97.5% | ~94.7% | ~99.1% |

The VQC baseline was substantially weaker under the tested configuration.

An earlier WDBC holdout experiment produced approximately:

- VQC Accuracy: 57.9%
- VQC Sensitivity: 40.5%
- VQC Specificity: 68.1%
- VQC ROC-AUC: 60.8%

versus approximately:

- SVM Accuracy: 98.2%
- SVM ROC-AUC: 99.7%

The holdout and later CV experiments use different evaluation protocols and must not be mixed as though they were one experiment.

---

## 13. Quantum Ablation Strategy

A controlled ablation study was introduced to investigate whether VQC configuration materially affects performance.

Variables included:

- Qubit count
- Circuit depth
- Loss function
- Training iterations

### Selected configuration

The current selection identified:

- 6 qubits
- 3 layers
- MSE
- 100 iterations

as the strongest tested configuration under the selection protocol.

### Important methodological caveat

The configuration was selected using a stratified holdout and subsequently evaluated on the same overall WDBC dataset.

Therefore, this is **not equivalent to unbiased nested cross-validation**.

Preferred wording:

> "The VQC configuration was selected through a controlled ablation study and subsequently evaluated using stratified cross-validation."

Avoid calling it globally optimal.

---

## 14. Complexity Profiler

A complexity profiler is being developed to characterize biomedical datasets before model routing.

Current indicators include:

- Feature dimensionality
- Class balance
- Mean absolute feature correlation
- Logistic-regression-based linear separability proxy

These metrics should be treated as **descriptive complexity indicators**, not formal measures of dataset complexity.

The profiler's eventual role is to support evidence-driven pathway selection.

---

## 15. Planned System Architecture

```text
                    Biomedical Dataset
                           |
                           v
                    Data Validation
                           |
                           v
                  Train/Test Split or CV
                           |
                           v
                Leakage-Safe Preprocessing
                           |
                 +---------+---------+
                 |                   |
                 v                   v
        Complexity Profiler     Feature Selection
                 |                   |
                 +---------+---------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
       Classical Path              Quantum Path
       SVM / RF / XGB          Feature Map + VQC/PQC
             |                           |
             +-------------+-------------+
                           |
                           v
                   Unified Evaluation
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          Metrics     Explainability  Runtime
             |             |             |
             +-------------+-------------+
                           |
                           v
                  Evidence Report
                           |
                           v
             Pathway Recommendation
```

---

## 16. Planned Platform Modules

### Data Manager

Handles:

- Dataset ingestion
- Dataset validation
- Metadata
- Dataset versioning

### Preprocessor

Handles:

- Scaling
- PCA
- Feature selection
- Leakage prevention

### Complexity Profiler

Computes measurable dataset characteristics.

### Classical Models

Supports:

- SVM
- Random Forest
- XGBoost

### Quantum Models

Supports:

- Quantum feature maps
- VQC / PQC
- Simulator execution
- Future hardware-compatible execution

### Experiment Runner

Controls:

- Seeds
- Cross-validation
- Hyperparameters
- Repeated experiments

### Metrics Engine

Computes:

- Accuracy
- Sensitivity
- Specificity
- Precision
- Recall
- F1
- ROC-AUC
- Confusion matrix
- Runtime

### Explainability Engine

Provides interpretable information about model behaviour and feature contribution where technically appropriate.

### Results Store

Stores experiment metadata and results.

Each result should record, where applicable:

- Dataset
- Dataset version
- Seed
- Model
- Preprocessing
- PCA components
- Feature map
- Qubit count
- Circuit depth
- Optimizer
- Learning rate
- Iterations
- Metrics
- Runtime
- Execution environment

---

## 17. Evidence-Driven Quantum Routing

This is the main candidate for the novel system contribution.

The platform should eventually be able to evaluate whether a quantum pathway is worth using based on measured evidence.

Conceptually:

```text
Dataset
   |
   v
Profile Complexity
   |
   v
Run / Retrieve Classical Baselines
   |
   v
Evaluate Quantum Pathway
   |
   v
Compare Predictive + Computational Utility
   |
   v
Evidence-Based Recommendation
```

Possible outcomes:

- **Use classical pathway**
- **Use quantum-enhanced pathway**
- **Run quantum specialist pathway**
- **Evidence inconclusive**

The recommendation must be derived from experiments, not hard-coded assumptions.

---

## 18. Potential Future Research Directions

These are candidates, not yet accepted features.

### A. Complexity-aware pathway selection

Investigate whether measurable dataset characteristics can predict when a quantum pathway is worth testing.

### B. Quantum specialist/residual pathway

Instead of forcing the entire prediction problem through a quantum model, investigate whether a quantum model can act as a specialist on difficult or residual cases.

### C. Multi-objective quantum utility

Evaluate quantum pathways across:

- Predictive performance
- Sensitivity
- Specificity
- Runtime
- Training cost
- Generalization
- Robustness

This avoids treating accuracy as the only objective.

### D. Noise-aware evaluation

Evaluate whether conclusions remain stable under realistic noise models before making hardware-related claims.

### E. Real hardware compatibility

Where resources permit, execute selected experiments on actual quantum hardware.

No hardware result should be claimed before actual execution.

---

## 19. Scientific Guardrails

The following claims are prohibited unless directly demonstrated by valid experiments.

### Never claim

- Quantum speedup
- Quantum advantage
- Superior quantum accuracy without fair comparison
- Clinical validation
- Clinical deployment readiness
- Proven early detection using WDBC
- Real-world patient benefit
- Hardware validation without hardware execution
- Optimality without appropriate search/validation
- Causal complexity effects from observational synthetic comparisons
- General quantum superiority

### Required language

Prefer:

- "tested"
- "observed"
- "under the evaluated configuration"
- "under the stated evaluation protocol"
- "suggests"
- "association"
- "evidence is inconclusive"
- "classical pathway performed better"
- "requires further validation"

---

## 20. Reproducibility Requirements

Every major experiment should be reproducible.

Minimum requirements:

- Fixed seeds
- Explicit dataset version
- Explicit preprocessing pipeline
- Train/test or CV protocol
- Model configuration
- Environment information
- Saved metrics
- Confusion matrices
- Runtime
- Experiment configuration
- Git commit

Reproducibility tests should confirm repeated runs produce equivalent metrics within an explicitly defined tolerance.

---

## 21. Current Engineering State

Implemented components include:

- WDBC dataset management
- Leakage-safe preprocessing
- Classical model factories
- SVM / Random Forest / XGBoost baselines
- PennyLane VQC baseline
- Quantum ablation framework
- Synthetic complexity generator
- Complexity profiler
- Complexity benchmark runner
- Experiment configurations
- Mathematical metric tests
- Reproducibility checks
- Research documentation

The project repository is:

`biswajyoti-nath/SIH26139-Hybrid-QML-Early-Disease-Detection`

---

## 22. Current Task Order

The research must proceed in this order.

### T-060

**Canonical complexity validation**

- Finish R1 vs R3 canonical run
- Audit metrics
- Audit reproducibility
- Check whether the observed R3 behaviour survives the larger training budget
- Do not claim quantum suitability from the result automatically

### T-061

**Real PS-relevant biomedical complexity benchmark**

- Profile WDBC
- Profile Parkinson's
- Establish comparable classical baselines
- Establish comparable quantum experiments
- Measure complexity characteristics
- Compare relative quantum/classical behaviour

### T-062

**Evidence-driven pathway selection**

Only after sufficient evidence exists.

Potentially investigate:

- Complexity-aware routing
- Classical-first / quantum-specialist pathways
- Quantum residual correction
- Uncertainty-aware routing

### T-063

**Utility and decision framework**

Potentially combine:

- Predictive performance
- Robustness
- Runtime
- Complexity
- Reproducibility
- Quantum resource requirements

into an evidence-based pathway recommendation.

---

## 23. SIH Demonstration Strategy

The final prototype should make the research contribution visible.

A judge should be able to:

1. Select a biomedical dataset.
2. Inspect dataset characteristics.
3. Run classical baselines.
4. Run the quantum pathway.
5. Compare metrics.
6. Inspect explainability outputs.
7. View computational cost.
8. See whether quantum added measurable value.
9. Receive an evidence-based pathway recommendation.

The strongest demonstration is not:

> "Look, our quantum model has a high score."

It is:

> **"Give us a biomedical problem. We measure its characteristics, test both learning paradigms, and show you whether the quantum pathway actually adds value."**

---

## 24. Final Product Positioning

The platform should be positioned as:

> **An evidence-driven hybrid quantum-classical biomedical learning platform that evaluates when quantum-enhanced learning is worth using for disease detection.**

This satisfies the core PS requirements while providing a meaningful research contribution.

The central philosophy is:

> **Do not assume quantum wins. Measure when it is worth using.**
