# SIH 26139 — Ultra-Detailed Execution & Action Plan

# SIH 2026 — PS 26139
## Research & Working Specification

**Problem Statement:** Hybrid Quantum Machine Learning Platform for Early Disease Detection  
**PS ID:** 26139  
**Team:** Chai.EXE  
**Institution:** Barak Valley Engineering College  
**Organization / Department:** Egreen Quanta  
**Category:** Software  
**Theme:** MedTech / BioTech / HealthTech  

---

## 0. Purpose of This Document

This document is the working source of truth for the SIH PPT and the eventual prototype.

Every slide claim, architecture choice, benchmark, limitation, and future-work statement should be traceable to this document.

Because the platform has **not yet been built**, proposed capabilities are written as **design targets**, not achieved results.

### Evidence rule

Every statement should fall into one of three categories:

1. **Published evidence**
2. **Our proposed methodology**
3. **Our measured result**

Published benchmark numbers from papers are never presented as our results.

---

# 1. Problem Statement and Requirements

PS 26139 asks for a hybrid quantum-classical machine-learning platform for early disease detection.

The supplied problem description calls for:

- Classical preprocessing and feature engineering combined with quantum-enhanced models such as QSVM, QNN, or VQC.
- Application to biomedical datasets such as cancer, cardiovascular, or neurological datasets.
- Data ingestion.
- Training.
- Prediction.
- Explainability.
- Evaluation against purely classical baselines.

## Required capabilities

The problem statement requires or strongly implies:

- Hybrid quantum-classical architecture.
- Quantum-enhanced classification or regression.
- Comparison against classical models.
- Evaluation using:
  - Accuracy
  - Sensitivity
  - Specificity
  - Computational efficiency
  - Generalization
- Preprocessing.
- Feature selection.
- Explainability.
- Training and inference workflow.
- Compatibility with near-term quantum hardware or simulators.
- A functional software platform rather than a single isolated model.

---

# 2. Core Thesis

## Do not sell quantum advantage. Build a platform that can test it.

The strongest defensible position is that current evidence does not justify assuming QML will outperform classical ML in digital health.

A 2025 systematic review of QML for digital health found no consistent empirical trend supporting quantum utility over classical methods and highlighted weaknesses in many published comparisons.

This makes rigorous benchmarking itself a meaningful technical contribution.

## Working research hypothesis

> Can a carefully designed hybrid quantum model provide useful predictive behaviour under the same data, preprocessing, and evaluation conditions as strong classical baselines?

The system should be designed so the experiment can answer:

- Yes
- No
- Only under specific conditions

without changing the evaluation protocol.

We are **not claiming the answer in advance**.

---

# 3. Pilot Dataset: WDBC

The proposed pilot dataset is the **Breast Cancer Wisconsin (Diagnostic)** dataset.

It is suitable for rapid experimentation because it is small enough for practical prototyping while retaining a meaningful binary classification task.

UCI lists:

- **569 instances**
- **30 real-valued features**
- Binary target: benign / malignant

The features describe characteristics of cell nuclei computed from digitized fine-needle-aspirate images.

## Dataset specification

| Property | Working specification |
|---|---|
| Dataset | Breast Cancer Wisconsin (Diagnostic), UCI |
| Instances | 569 |
| Predictors | 30 real-valued features |
| Target | Benign / Malignant |
| Role | Pilot benchmark |
| Clinical status | Research benchmark, not clinical validation |
| Source | UCI Machine Learning Repository |

### Important limitation

WDBC alone cannot establish:

- Clinical utility
- Hospital-level generalization
- Clinical diagnostic superiority
- Production readiness

It is a **pilot benchmark**.

---

# 4. Proposed System Architecture

## Primary pipeline

```text
Biomedical Dataset
        ↓
Data Validation
        ↓
Train/Test Split
        ↓
Standardization
        ↓
Feature Selection / PCA
        ↓
Quantum Encoding
        ↓
Variational Quantum Circuit
        ↓
Classifier Output
        ↓
Metrics + Explainability
```

## Expanded architecture

```text
                         ┌─────────────────────────┐
                         │   Biomedical Dataset     │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Data Validation /       │
                         │ Schema Checking         │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Train / Test Split      │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Standardization         │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Feature Selection / PCA │
                         │ 5–10 dimensions         │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Quantum Feature         │
                         │ Encoding                │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Parameterized Quantum   │
                         │ Circuit / VQC           │
                         └────────────┬────────────┘
                                      ↓
                         ┌─────────────────────────┐
                         │ Prediction              │
                         └────────────┬────────────┘
                                      ↓
                  ┌───────────────────┴──────────────────┐
                  ↓                                      ↓
       ┌─────────────────────┐               ┌─────────────────────┐
       │ Evaluation          │               │ Explainability      │
       │ Accuracy            │               │ Feature attribution │
       │ Sensitivity         │               │ Model behaviour     │
       │ Specificity         │               │ Measurement data    │
       │ F1 / ROC-AUC        │               └─────────────────────┘
       │ Runtime             │
       └─────────────────────┘
```

---

# 5. Classical Baseline Architecture

The quantum model must not be evaluated in isolation.

The same underlying dataset and evaluation protocol should be used for strong classical baselines.

## Baseline models

### SVM

Purpose:

- Strong classical classification baseline.
- Tests whether the quantum model provides value over a standard kernel/classification approach.

### Random Forest

Purpose:

- Nonlinear ensemble baseline.
- Captures feature interactions without requiring quantum computation.

### XGBoost

Purpose:

- High-performance classical reference model.
- Provides a stronger comparison than relying on a single simple baseline.

### Optional QSVM / Quantum Kernel

Purpose:

- Tests whether quantum feature spaces provide useful behaviour within a kernel-based framework.

---

# 6. Model Matrix

| Model | Purpose | What it tests |
|---|---|---|
| SVM | Strong classical classifier | Linear/nonlinear classical baseline |
| Random Forest | Tree ensemble | Nonlinear feature interactions |
| XGBoost | Boosted trees | High-performance classical reference |
| VQC | Hybrid quantum-classical model | Quantum feature encoding + variational circuit |
| Optional QSVM/QKernel | Quantum kernel baseline | Quantum feature-space behaviour |

---

# 7. Why Hybrid Rather Than Pure Quantum?

Near-term quantum devices impose constraints on:

- Qubit count
- Circuit depth
- Noise
- Training stability
- Hardware access

A hybrid architecture allows:

- Classical preprocessing.
- Classical dimensionality reduction.
- Quantum feature encoding.
- Quantum computation where appropriate.
- Classical optimization.
- Classical evaluation.

Variational quantum algorithms are explicitly designed around this hybrid pattern.

Cerezo et al. identify trainability, accuracy, and efficiency as important challenges for variational quantum algorithms.

Havlíček et al. established a foundational supervised-learning approach using quantum-enhanced feature spaces and a variational quantum classifier.

These works motivate experimentation with quantum feature maps and VQCs.

They do **not** prove practical superiority for medical datasets.

---

# 8. Proposed Quantum Component

## Candidate approach

Use a **Variational Quantum Classifier (VQC)** as the primary quantum model.

### Proposed operating range

- 5–10 qubits.
- 3–5 circuit layers.
- Simulator-first execution.
- Shallow parameterized circuits.
- Classical optimizer.

These are implementation targets, not completed system capabilities.

## Candidate pipeline

```text
30 WDBC Features
        ↓
Standardization
        ↓
PCA / Feature Selection
        ↓
5–10 Features
        ↓
Quantum Feature Encoding
        ↓
Parameterized Circuit
        ↓
Measurement
        ↓
Classical Optimization
        ↓
Binary Prediction
```

---

# 9. Data Preprocessing

Preprocessing is a critical part of the experiment.

## Required steps

1. Load dataset.
2. Validate schema.
3. Identify target column.
4. Check missing values.
5. Encode target labels.
6. Split data.
7. Standardize features.
8. Apply dimensionality reduction if required.
9. Feed reduced representation to quantum circuit.

## Data leakage rule

Transformations such as:

- Standardization
- PCA
- Feature selection

must be fitted only on the training data.

The validation/test data must only be transformed using parameters learned from the training data.

Otherwise, reported performance can be artificially inflated.

---

# 10. Dimensionality Reduction

Quantum circuits have limited practical input dimensions.

The WDBC dataset contains 30 predictors, while the proposed circuit may use only 5–10 qubits.

Therefore dimensionality reduction is required.

## Candidate methods

### PCA

Advantages:

- Simple.
- Reproducible.
- Easy to integrate.
- Produces compact continuous representations.

### Feature selection

Possible approaches:

- Statistical ranking.
- Model-based feature importance.
- Recursive feature elimination.

## Working approach

Start with PCA.

Test a small number of dimensions such as:

- 5
- 8
- 10

Avoid unnecessarily large hyperparameter searches because the goal is a credible SIH prototype, not an exhaustive research paper.

---

# 11. Quantum Feature Encoding

The reduced classical feature vector must be mapped into quantum states.

Candidate approaches include:

- Angle encoding.
- Amplitude encoding.
- Other explicitly documented feature maps.

For the MVP, choose one simple encoding and keep it reproducible.

## Requirement

The PPT must state the encoding method explicitly once implementation is finalized.

Do not write vague phrases such as:

> Advanced quantum encoding.

Instead state the actual method.

---

# 12. Variational Quantum Circuit

The VQC consists of:

1. Input encoding.
2. Parameterized gates.
3. Entangling operations.
4. Measurement.
5. Classical optimization.

## Proposed constraints

Keep the circuit shallow.

Initial target:

```text
5–10 qubits
3–5 layers
```

The exact configuration should be selected experimentally based on:

- Training stability.
- Runtime.
- Validation performance.
- Circuit complexity.

---

# 13. Experimental Design

This is the most important part of the project.

The experiment must prevent the quantum model from receiving a more favourable evaluation protocol than the classical baselines.

## Fair comparison rules

### Rule 1: Same data

All models use the same dataset.

### Rule 2: Same split

All models use the same train/test split or the same cross-validation folds.

### Rule 3: Same preprocessing

Where possible, models should use the same input representation.

### Rule 4: No leakage

Preprocessing is fitted only on training folds.

### Rule 5: Record configurations

Record:

- Random seed.
- Software versions.
- Dataset version.
- Preprocessing parameters.
- PCA dimensions.
- Qubit count.
- Circuit depth.
- Optimizer.
- Learning rate where applicable.
- Number of iterations.
- Stopping criteria.

### Rule 6: Multiple seeds

If compute allows, repeat experiments across multiple random seeds.

Report:

```text
mean ± standard deviation
```

rather than relying on one lucky run.

### Rule 7: Runtime measurement

Record:

- Training time.
- Inference time.
- Simulator/hardware environment.

Do not claim quantum speedup unless measured under an explicitly fair comparison.

---

# 14. Evaluation Metrics

The problem statement explicitly requires benchmarking.

## Primary metrics

### Accuracy

Overall fraction of correct predictions.

### Sensitivity

Also called recall or true-positive rate.

Important when missing a positive disease case is costly.

### Specificity

True-negative rate.

Important when distinguishing negative cases correctly.

### Precision

Measures the proportion of predicted positive cases that are actually positive.

### F1-score

Balances precision and recall.

### ROC-AUC

Useful for evaluating ranking/discrimination across classification thresholds.

### Confusion matrix

Should be shown for model-level interpretation.

### Computational efficiency

Record:

- Training time.
- Inference time.
- Circuit execution time where meaningful.
- Hardware/simulator configuration.

### Generalization

Use:

- Cross-validation where appropriate.
- Multiple seeds.
- Held-out test evaluation.

---

# 15. Explainability

Explainability is a requirement, but it must be represented honestly.

## Classical models

SHAP can be used to investigate feature contributions for:

- SVM
- Random Forest
- XGBoost

depending on the selected implementation and explainer.

## Quantum model

For the VQC, distinguish between:

1. Input feature contribution.
2. Circuit structure.
3. Measurement outputs.
4. Model prediction.

Do not claim that SHAP automatically explains every internal quantum operation.

## Proposed dashboard

For one selected prediction, show:

```text
Input
  ↓
Prediction
  ↓
Confidence / Score
  ↓
Important input features
  ↓
Quantum measurement information
```

The interface should describe these as model-level explanations, not clinically validated explanations.

---

# 16. Software Architecture

## Proposed stack

### Quantum

- Qiskit
- PennyLane
- Qiskit Aer
- PennyLane-Lightning

### Classical ML

- scikit-learn
- XGBoost

### Explainability

- SHAP
- LIME where useful

### Backend

- FastAPI

### Deployment

- Docker

## Architectural separation

```text
Frontend
   ↓
FastAPI Backend
   ↓
Experiment / Model Service
   ├── Classical Models
   ├── Quantum Models
   ├── Evaluation Engine
   └── Explainability Engine
   ↓
Results / Metrics Store
```

The exact frontend framework can remain lightweight.

The judging value comes primarily from:

- Working pipeline.
- Reproducibility.
- Comparison.
- Explainability.
- Clear experimental evidence.

---

# 17. MVP

The minimum viable prototype should demonstrate:

## Stage 1

Load WDBC dataset.

## Stage 2

Run preprocessing.

## Stage 3

Train one classical baseline.

## Stage 4

Train VQC.

## Stage 5

Compare predictions and metrics.

## Stage 6

Display evaluation dashboard.

## Stage 7

Display explainability for a selected prediction.

---

# 18. Ideal Demo Flow

A judge should be able to understand the system within approximately one minute.

```text
Select Dataset
      ↓
Choose Model
      ↓
Train / Load Experiment
      ↓
Prediction
      ↓
Compare Against Classical Baselines
      ↓
Metrics
      ↓
Explainability
```

The most useful dashboard comparison is:

| Metric | SVM | Random Forest | XGBoost | VQC |
|---|---:|---:|---:|---:|
| Accuracy | measured | measured | measured | measured |
| Sensitivity | measured | measured | measured | measured |
| Specificity | measured | measured | measured | measured |
| F1 | measured | measured | measured | measured |
| ROC-AUC | measured | measured | measured | measured |
| Training Time | measured | measured | measured | measured |
| Inference Time | measured | measured | measured | measured |

Do not fill this table with invented numbers.

---

# 19. Feasibility

## Why the MVP is feasible

The pilot dataset is small.

The initial quantum model is intentionally constrained.

The proposed approach is simulator-first.

No real QPU is required for the first demonstration.

## Proposed feasibility constraints

- Small dataset.
- 5–10 qubits.
- Shallow circuits.
- Limited hyperparameter search.
- Classical preprocessing.
- Cached experiment results.
- Dockerized deployment.

---

# 20. Risks and Mitigations

| Risk | Consequence | Mitigation |
|---|---|---|
| Small dataset | Overfitting / unstable estimates | Stratified CV, regularization, multiple seeds |
| Quantum simulation cost | Slow training | Small circuits, limited search space, cache results |
| Data leakage | Inflated test performance | Fit preprocessing inside training folds |
| No quantum improvement | Weak narrative if framed as superiority | Make rigorous benchmarking the contribution |
| Hardware noise | Different results on QPU | Simulator-first; optional noise-model experiment |
| Clinical overclaim | Scientific/ethical credibility problem | Explicitly label prototype as non-clinical and non-diagnostic |
| Explainability mismatch | Misleading interpretation | Separate input-feature attribution from circuit/measurement information |

---

# 21. Research Positioning

The strongest research story is not:

> Quantum ML is better for disease detection.

That statement would require evidence we do not yet have.

The stronger story is:

> We propose a controlled experimental platform for testing hybrid quantum machine learning against strong classical baselines under transparent, reproducible, and explainable conditions.

A 2025 systematic review of QML for digital health is particularly relevant.

It reviewed thousands of records and concluded that existing empirical evidence does not establish a consistent performance advantage or scalability/robustness advantage for QML over classical methods in digital health.

Therefore the project should position itself around:

- Controlled comparison.
- Reproducibility.
- Honest benchmarking.
- Explainability.
- Near-term feasibility.
- Experimental evidence.

---

# 22. What We Can Claim vs What We Cannot Claim

| Safe to claim now | Do NOT claim before experiments |
|---|---|
| We propose a hybrid QML platform. | The platform achieves higher accuracy. |
| WDBC is the pilot dataset. | The model improves clinical diagnosis. |
| VQC/QSVM are candidate quantum models. | Quantum advantage has been demonstrated. |
| SVM/RF/XGBoost are planned baselines. | Quantum model is faster than classical ML. |
| Simulator-first is the implementation strategy. | The system is clinically validated. |
| Explainability is a design requirement. | SHAP proves clinical interpretability. |
| Published studies motivate the research direction. | Published numbers are our benchmark results. |

This table should govern every PPT edit.

---

# 23. PPT Source of Truth

## Slide 1 — Team Details & Problem Statement

Include:

- SIH 2026.
- PS 26139.
- Problem title.
- Team: Chai.EXE.
- Institution: Barak Valley Engineering College.
- Organization / Department: Egreen Quanta.
- Category: Software.
- Theme: MedTech / BioTech / HealthTech.
- Team members.
- Team leader.

Do not overload the opening slide with technical claims.

---

## Slide 2 — Proposed Solution

Narrative:

```text
Biomedical Data
      ↓
Classical Preprocessing
      ↓
Feature Selection / PCA
      ↓
Quantum Encoding
      ↓
VQC
      ↓
Prediction
      ↓
Evaluation + Explainability
```

Emphasize four pillars:

1. Hybrid architecture.
2. Quantum feature encoding.
3. Honest benchmarking.
4. Explainability.

WDBC should be introduced as the pilot use case.

---

## Slide 3 — Technical Approach

Show:

```text
WDBC
569 × 30
   ↓
Preprocessing
   ↓
Standardization
   ↓
PCA
   ↓
5–10 features
   ↓
Quantum encoding
   ↓
Parameterized quantum circuit
   ↓
VQC
   ↓
Prediction
```

Alongside this, show parallel classical baselines:

- SVM
- Random Forest
- XGBoost

Technology stack:

- Qiskit
- PennyLane
- Qiskit Aer
- scikit-learn
- XGBoost
- SHAP
- FastAPI
- Docker

Clearly label the architecture as proposed if implementation is not complete.

---

## Slide 4 — Feasibility & Viability

Show:

### Constraints

- Limited qubits.
- Circuit depth.
- Simulation cost.
- Noise.
- VQC trainability.
- Small biomedical datasets.

### Mitigations

- Simulator-first.
- 5–10 qubits.
- Shallow circuits.
- PCA.
- Controlled experiments.
- Multiple seeds.
- Strong classical baselines.

### Roadmap

```text
WDBC Prototype
      ↓
Larger Biomedical Datasets
      ↓
External Validation
      ↓
QPU Testing
      ↓
Clinical Validation
```

The final stages are future work, not current capabilities.

---

# 24. Slide 5 — Impact & Benefits

Focus on realistic stakeholders.

## Clinicians

Potentially useful as a research-oriented model comparison and decision-support experimentation environment.

## Patients

Potential long-term value comes from investigating models for early disease classification.

Do not claim improved diagnosis until validated.

## Researchers

Provides:

- Reproducible QML experiments.
- Classical comparison.
- Explainability.
- Benchmarking infrastructure.

## Healthcare AI teams

Provides a controlled environment for investigating whether quantum methods justify their computational and engineering cost.

## Measurable outcomes

The platform should measure:

- Accuracy.
- Sensitivity.
- Specificity.
- F1.
- ROC-AUC.
- Runtime.
- Generalization.
- Explainability.

---

# 25. Slide 6 — Research & References

The final slide should establish that the project is research-driven.

## Core references

### Havlíček et al. 2019

**Supervised learning with quantum-enhanced feature spaces**

Nature 567, 209–212.

DOI:

```text
10.1038/s41586-019-0980-2
```

### Cerezo et al. 2021

**Variational quantum algorithms**

Nature Reviews Physics 3, 625–644.

DOI:

```text
10.1038/s42254-021-00348-9
```

### Gupta et al. 2025

**A systematic review of quantum machine learning for digital health**

npj Digital Medicine.

DOI:

```text
10.1038/s41746-025-01597-z
```

### WDBC Dataset

Wolberg, Mangasarian, Street & Street.

**Breast Cancer Wisconsin (Diagnostic)**

UCI Machine Learning Repository.

DOI:

```text
10.24432/C5DW2B
```

Additional research leads from the supplied concept deck:

- Kundu et al. 2025.
- Prajapati et al. 2025.
- Mpofu & Mthunzi-Kufa 2025.
- Pushpanjali & Adisesha 2025.
- Sammartino 2026.

These should be verified from their original publications before being used for exact numerical claims.

---

# 26. Final Slide 6 Message

The final footer/message should not claim that we already achieved quantum advantage.

Use:

> **EXPLORE QUANTUM ADVANTAGE. PROVE IT AGAINST CLASSICAL ML.**

This works because it is a research challenge rather than an unsupported result.

It directly reflects the central experimental philosophy of PS 26139.

---

# 27. Three-Hour Execution Plan

We have approximately three hours.

## 0–30 minutes

### Lock the research/spec

- Freeze this document.
- Freeze architecture.
- Freeze terminology.
- Freeze model list.
- Freeze claims.

**Deliverable:** research source of truth.

---

## 30–75 minutes

### Build / revise Slides 1–3

Focus on:

- Problem.
- Proposed solution.
- Architecture.
- Dataset.
- Classical + quantum models.

Do not waste time on decorative graphics.

---

## 75–115 minutes

### Build / revise Slides 4–6

Focus on:

- Feasibility.
- Risks.
- Mitigation.
- Impact.
- Research foundation.
- References.

---

## 115–140 minutes

### Consistency audit

Check every slide for:

- Unsupported claims.
- Contradictory numbers.
- Inconsistent terminology.
- Wrong dataset dimensions.
- Confusing proposed vs completed functionality.
- Overloaded text.

---

## 140–165 minutes

### Visual cleanup

In Google Slides:

- Align boxes.
- Fix spacing.
- Fix table overflow.
- Ensure titles are consistent.
- Ensure SIH identity remains consistent.
- Ensure footer is consistent.
- Ensure references remain readable.

---

## 165–180 minutes

### Final judge-read

Ask:

1. Can the problem be understood immediately?
2. Can the proposed solution be understood without narration?
3. Is the quantum component technically credible?
4. Is the classical comparison explicit?
5. Is the experimental methodology fair?
6. Are limitations acknowledged?
7. Are claims defensible?
8. Does the final slide establish research credibility?
9. Can the team actually build the MVP?
10. Is there anything on the slide that we cannot defend?

Then export the final PPT/PDF.

---

# 28. Final Strategic Position

The project should not be presented as:

> “We built a quantum model that beats classical ML.”

We have not.

It should be presented as:

> **A hybrid QML experimentation platform designed to rigorously determine when quantum-enhanced learning is actually useful for biomedical classification.**

The WDBC experiment is the first controlled benchmark.

The classical models establish the baseline.

The VQC tests the quantum hypothesis.

The evaluation engine measures whether there is meaningful improvement.

The explainability layer makes model behaviour inspectable.

The platform can then expand to larger biomedical datasets and, eventually, real quantum hardware.

That is the story we can defend.

---

## References

1. Havlíček, V. et al. (2019). *Supervised learning with quantum-enhanced feature spaces*. Nature, 567, 209–212.
2. Cerezo, M. et al. (2021). *Variational quantum algorithms*. Nature Reviews Physics, 3, 625–644.
3. Gupta, R. S. et al. (2025). *A systematic review of quantum machine learning for digital health*. npj Digital Medicine.
4. Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). *Breast Cancer Wisconsin (Diagnostic)*. UCI Machine Learning Repository.
5. Kundu et al. (2025), as listed in the supplied concept deck.
6. Prajapati et al. (2025), as listed in the supplied concept deck.
7. Mpofu & Mthunzi-Kufa (2025), as listed in the supplied concept deck.
8. Pushpanjali & Adisesha (2025), as listed in the supplied concept deck.
9. Sammartino (2026), as listed in the supplied concept deck.
