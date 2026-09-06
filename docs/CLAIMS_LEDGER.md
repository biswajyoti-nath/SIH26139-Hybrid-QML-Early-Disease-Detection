# CLAIMS_LEDGER.md

## SCIENTIFIC LANGUAGE RULES
Every important research statement must belong to one of:
- VERIFIED FACT
- OUR EXPERIMENT
- RESEARCH HYPOTHESIS
- FUTURE WORK
- DO NOT CLAIM

Never silently promote a hypothesis into a result.
Especially DO NOT claim:
- quantum advantage, speedup, or superiority
- clinical benefit
- early-detection validation from WDBC
- hardware advantage when using simulation
- optimal quantum configuration unless the experimental design actually supports optimality
- dataset linear separability unless mathematically established
- synthetic benchmark results before running the benchmark

**Examples:**
- BAD: "Quantum advantage does not exist for WDBC."
- GOOD: "No quantum advantage was observed for the tested VQC configuration under our WDBC evaluation protocol."
- BAD: "This dataset proves quantum ML is useless for tabular biomedical data."
- GOOD: "This benchmark shows that the tested VQC was substantially weaker and more computationally expensive than the tested classical baselines on WDBC."

## SIH 26139 — Research Claims Classification Ledger
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Classify every claim that may appear in our PPT, demo, or documentation. Governs all written and spoken communication about this project.

---

## Classification System

Every claim MUST be assigned one of the following classes:

- **EXTERNAL FACT**: Verified external claims backed by peer-reviewed literature.
- **OUR EXPERIMENT**: Internally generated claims backed by a reproducible experiment artifact.
- **HYPOTHESIS**: Testable claims we intend to evaluate during the project.
- **FUTURE WORK**: Out-of-scope claims or speculations reserved for future research.

> **CRITICAL RULE:** Never classify internally generated numbers as "Verified Fact". Use "OUR EXPERIMENT". Never call a baseline performance a "ceiling" — it is a "reference baseline under current protocol."

---

## Section 1 — Dataset Claims

| Claim | Category | Notes |
|---|---|---|
| "WDBC contains 569 instances" | **A. VERIFIED FACT** | UCI ML Repository, DOI 10.24432/C5DW2B |
| "WDBC contains 30 real-valued features" | **A. VERIFIED FACT** | UCI ML Repository |
| "WDBC target is binary: benign / malignant" | **A. VERIFIED FACT** | UCI ML Repository |
| "WDBC has 357 benign and 212 malignant instances" | **A. VERIFIED FACT** | UCI ML Repository (load_breast_cancer in sklearn) |
| "WDBC features are computed from FNA images" | **A. VERIFIED FACT** | Wolberg et al. 1993 |
| "WDBC has no missing values (standard version)" | **A. VERIFIED FACT** | Standard dataset documentation |
| "WDBC is an early-detection dataset" | **E. UNSUPPORTED / DO NOT CLAIM** | WDBC is a diagnostic benchmark; FNA is not a screening modality |
| "Our model detects breast cancer early" | **E. UNSUPPORTED / DO NOT CLAIM** | No clinical or early-detection evidence |
| "WDBC generalizes to clinical settings" | **E. UNSUPPORTED / DO NOT CLAIM** | Single institution, retrospective benchmark |

---

## Section 2 — Architecture and Design Claims

| Claim | Category | Notes |
|---|---|---|
| "We propose a hybrid quantum-classical platform" | **A. VERIFIED FACT** (design intent) | Documented in both project spec files |
| "VQC and QSVM are our candidate quantum models" | **A. VERIFIED FACT** (design intent) | Specified in project docs |
| "SVM, Random Forest, XGBoost are our classical baselines" | **A. VERIFIED FACT** (design intent) | Specified in project docs |
| "The architecture uses classical preprocessing before quantum encoding" | **A. VERIFIED FACT** (design intent) | Core pipeline in both docs |
| "Explainability is a design requirement of the system" | **A. VERIFIED FACT** (design intent) | Explicitly required by PS 26139 |
| "The platform uses simulator-first execution" | **A. VERIFIED FACT** (design intent) | Explicitly stated in feasibility section |
| "PCA reduces 30 WDBC features to 5-10 dimensions for quantum circuits" | **A. VERIFIED FACT** (design intent) | Proposed approach in both docs |
| "The quantum layer is replaceable in the architecture" | **A. VERIFIED FACT** (design intent) | Architectural requirement in both docs |
| "The system is production-ready" | **E. UNSUPPORTED / DO NOT CLAIM** | Prototype status only |
| "The system is deployable in clinical environments" | **E. UNSUPPORTED / DO NOT CLAIM** | No clinical validation conducted |

---

## Section 3 — Quantum Model Claims

| Claim | Category | Notes |
|---|---|---|
| "VQC is a variational quantum-classical algorithm" | **A. VERIFIED FACT** | Cerezo et al. 2021 |
| "VQC uses parameterized quantum gates optimized with classical optimizer" | **A. VERIFIED FACT** | Standard VQA design |
| "ZZFeatureMap is a quantum feature map introduced by Havlíček et al. 2019" | **A. VERIFIED FACT** | Havlíček et al. Nature 2019 |
| "Barren plateaus can impede VQC training at scale" | **A. VERIFIED FACT** | Cerezo et al. 2021 |
| "We will use [specific encoding] in our VQC" | **B. OUR EXPERIMENTAL RESULT** | Only after architecture is finalized and fixed |
| "Our VQC achieves X% accuracy on WDBC" | **B. OUR EXPERIMENTAL RESULT** | Only after running the experiment |
| "Our VQC has N qubits and D layers" | **B. OUR EXPERIMENTAL RESULT** | Only after implementation is finalized |
| "Quantum feature maps generate classically intractable feature spaces" | **C. RESEARCH HYPOTHESIS** | Theoretically motivated by Havlíček et al.; not proven for our dataset |
| "Quantum feature encoding captures patterns classical methods miss" | **C. RESEARCH HYPOTHESIS** | Requires experimental validation |
| "The VQC learns meaningful representations from WDBC" | **C. RESEARCH HYPOTHESIS** | Must be tested |
| "Quantum model may outperform classical under certain conditions" | **C. RESEARCH HYPOTHESIS** | Our working hypothesis — pending experiment |

---

## Section 4 — Performance Claims

| Claim | Category | Notes |
|---|---|---|
| "XGBoost achieves >98% accuracy on WDBC" | **E. UNSUPPORTED / DO NOT CLAIM** | This is a number from published literature, not our result |
| "SVM achieves high accuracy on WDBC in published literature" | **A. VERIFIED FACT** (about the literature) | Many published works; cite the source |
| "Our SVM achieves X% accuracy on WDBC" | **B. OUR EXPERIMENTAL RESULT** | Only after we run our experiment |
| "Our XGBoost achieves X% accuracy on WDBC" | **B. OUR EXPERIMENTAL RESULT** | Only after we run our experiment |
| "Our VQC achieves X% sensitivity on WDBC" | **B. OUR EXPERIMENTAL RESULT** | Only after we run our experiment |
| "Quantum model is more accurate than classical models" | **E. UNSUPPORTED / DO NOT CLAIM** | Not demonstrated by us; contradicted by Gupta et al. 2025 systematic review |
| "Quantum model improves clinical diagnosis" | **E. UNSUPPORTED / DO NOT CLAIM** | No clinical validation conducted |
| "Our system outperforms state-of-the-art" | **E. UNSUPPORTED / DO NOT CLAIM** | No such comparison conducted |
| "Our platform achieves higher accuracy than prior work" | **E. UNSUPPORTED / DO NOT CLAIM** | Prior results are not our results |

---

## Section 5 — Speed and Efficiency Claims

| Claim | Category | Notes |
|---|---|---|
| "Training time for our VQC is X seconds" | **B. OUR EXPERIMENTAL RESULT** | Only after measuring during our experiment |
| "Training time for our SVM is X seconds" | **B. OUR EXPERIMENTAL RESULT** | Only after measuring during our experiment |
| "Quantum model trains faster than classical ML" | **E. UNSUPPORTED / DO NOT CLAIM** | False for NISQ simulators; simulators are far slower than classical |
| "Simulator execution provides quantum speedup" | **E. UNSUPPORTED / DO NOT CLAIM** | Fundamentally false — simulators scale exponentially worse |
| "Real QPU execution would be faster" | **D. FUTURE WORK** | No QPU testing conducted; may or may not be true |
| "Quantum algorithm has polynomial speedup over classical" | **E. UNSUPPORTED / DO NOT CLAIM** | Not demonstrated for VQC on medical data |

---

## Section 6 — Explainability Claims

| Claim | Category | Notes |
|---|---|---|
| "SHAP provides feature attribution for our classical models" | **B. OUR EXPERIMENTAL RESULT** | After implementing SHAP and verifying it runs |
| "Explainability is a core requirement of the platform" | **A. VERIFIED FACT** (design intent) | Required by PS 26139 |
| "SHAP explains internal quantum operations" | **E. UNSUPPORTED / DO NOT CLAIM** | SHAP does not operate at gate level in quantum circuits |
| "SHAP proves our model is clinically interpretable" | **E. UNSUPPORTED / DO NOT CLAIM** | SHAP provides model-level attribution only |
| "Our explainability layer provides clinical decision support" | **E. UNSUPPORTED / DO NOT CLAIM** | Not validated; prototype only |
| "Our explainability layer shows which input features influence predictions" | **B. OUR EXPERIMENTAL RESULT** | After implementing and validating |

---

## Section 7 — Research Positioning Claims

| Claim | Category | Notes |
|---|---|---|
| "No consistent QML advantage over classical methods in digital health has been demonstrated (Gupta et al. 2025)" | **A. VERIFIED FACT** | Directly from verified systematic review |
| "Havlíček et al. 2019 introduced quantum-enhanced feature spaces" | **A. VERIFIED FACT** | Verified |
| "Cerezo et al. 2021 identified barren plateaus as a key VQA challenge" | **A. VERIFIED FACT** | Verified |
| "Rigorous benchmarking of QML vs classical ML is a meaningful contribution" | **C. RESEARCH HYPOTHESIS** | Our framing, supported by Gupta et al. 2025 |
| "Our platform enables fair comparison of quantum and classical ML" | **A. VERIFIED FACT** (design intent) | Once implemented |
| "Quantum advantage in medical AI has been demonstrated" | **E. UNSUPPORTED / DO NOT CLAIM** | Directly contradicted by Gupta et al. 2025 |
| "Quantum ML is the future of medical diagnosis" | **E. UNSUPPORTED / DO NOT CLAIM** | Speculative marketing language |
| "WDBC results will generalize to clinical deployment" | **E. UNSUPPORTED / DO NOT CLAIM** | No clinical generalization evidence |

---

## Section 8 — Clinical and Safety Claims

| Claim | Category | Notes |
|---|---|---|
| "The system is a research prototype and not a medical device" | **A. VERIFIED FACT** | Must be stated in all demos and documentation |
| "Results on WDBC do not constitute clinical validation" | **A. VERIFIED FACT** | Must be stated in all demos and documentation |
| "The system has been clinically validated" | **E. UNSUPPORTED / DO NOT CLAIM** | No clinical trial conducted |
| "The system is FDA/CE/CDSCO approved" | **E. UNSUPPORTED / DO NOT CLAIM** | No regulatory submission made |
| "The system can replace clinical diagnosis" | **E. UNSUPPORTED / DO NOT CLAIM** | Ethically and factually unjustifiable |

---

## Critical Warning: Numbers

> **ZERO experimental numbers should appear in any presentation until the experiment has been run.**
> 
> When we do run experiments:
> - Numbers must be labelled as "our result under [exact experimental conditions]."
> - The experimental conditions (seed, split, versions, preprocessing, circuit config) must be recorded.
> - Numbers from published papers must never be presented as our results.
> - Numbers should ideally be mean ± std across multiple seeds.

---

## Approved Language Examples

### Safe framing (before experiments)
- "We propose to evaluate..."
- "Our design target is..."
- "We hypothesize that..."
- "The platform is designed to measure..."
- "Published literature motivates..."

### Safe framing (after experiments)
- "Under our experimental conditions [seed=X, split=Y, n_qubits=Z, encoding=W, framework=V, version=U], our VQC achieved..."
- "Our classical baseline SVM achieved..."
- "The quantum model [improved / did not improve / showed mixed results on] the [metric] metric compared to the best classical baseline."

### Forbidden framing (at all times without verification)
- "Quantum beats classical..."
- "Our model achieves state-of-the-art..."
- "This will improve cancer diagnosis..."
- "Quantum is faster..."
- "X% accuracy" (without our own experimental data)

### CLAIM_002: Classical Baselines are Extremely Strong on WDBC
- **Claim:** Standard classical models (SVM, RF, XGBoost) achieve >95% accuracy and F1 on WDBC (8 PCA components).
- **Source:** OUR EXPERIMENT (exp_002_cv_baseline)
- **Evidence:** 5-fold CV shows SVM achieves 97.3% mean accuracy, 96.4% mean F1, and 99.4% mean ROC-AUC.
- **Classification:** OUR EXPERIMENT
- **Constraint:** This sets a reference baseline under the current experimental protocol. VQC must be benchmarked against this exact 97.3% accuracy baseline to claim "improvement".

### CLAIM_003: VQC Core Engine is Functional
- **Claim:** A PennyLane-based Variational Quantum Circuit can natively integrate with standard classical scikit-learn pipelines on WDBC.
- **Source:** OUR EXPERIMENT (exp_003_vqc_smoke)
- **Evidence:** End-to-end simulation of an 8-qubit circuit trained via parameter shift / adjoint gradients with identical preprocessing to the classical baselines.
- **Classification:** OUR EXPERIMENT
- **Constraint:** This merely establishes the software architecture. It does NOT establish quantum advantage.

### CLAIM_004: VQC Performance and Advantage (FIREWALL)
- **Claim:** Quantum computing provides speedup, hardware advantage, or clinical benefit for WDBC.
- **Source:** N/A
- **Evidence:** None yet.
- **Classification:** FUTURE WORK
- **Constraint:** DO NOT CLAIM. Current metrics represent untuned smoke tests or classical simulations. Real advantage requires detailed benchmarks against the CLAIM_002 reference baseline (97.3%).

### CLAIM_005: Untuned VQC Underperforms Strong Classical Baselines
- **Claim:** A standard un-tuned PennyLane VQC (8-qubits, 3 layers, 50 iterations) achieves only ~60.8% ROC-AUC on WDBC, heavily trailing classical SVM (99.7% ROC-AUC).
- **Source:** OUR EXPERIMENT (exp_004_vqc_baseline)
- **Evidence:** 80/20 stratified holdout comparison using identical PCA components.
- **Classification:** OUR EXPERIMENT
- **Constraint:** This establishes that raw injection of data into a variational circuit does not yield automatic advantages. Extensive hyperparameter tuning, loss function redesign (e.g., cross-entropy), or advanced feature maps are necessary to close the gap.

### CLAIM_006: Optimized VQC Underperforms Classical ML on WDBC
- **Claim:** Even after structural ablation (PCA dimensions, circuit depth, loss functions, iterations), a PennyLane VQC (6-qubits, 3 layers) achieves only ~62.0% mean 5-fold CV ROC-AUC on WDBC.
- **Source:** OUR EXPERIMENT (exp_005_ablation_final_cv)
- **Evidence:** Strict 5-fold cross-validation showing a -37.3% ROC-AUC delta against a classical linear SVM.
- **Classification:** OUR EXPERIMENT
- **Constraint:** DO NOT CLAIM that quantum machine learning currently provides any predictive advantage for breast cancer diagnosis using standard tabular data and standard VQC architectures.

### CLAIM_007: VQC Dimensionality Trade-off (Barren Plateaus)
- **Claim:** Increasing qubit count from 6 to 8 on WDBC tabular data hurts VQC performance, likely due to optimization difficulty (barren plateaus), despite retaining more dataset variance.
- **Source:** OUR EXPERIMENT (exp_005_ablation_final_cv Stage A)
- **Evidence:** 6 qubits achieved 0.689 ROC-AUC in holdout, while 8 qubits dropped to 0.599.
- **Classification:** OUR EXPERIMENT

### NOT YET PROVEN (STRICTLY PROHIBITED)
- correlation causes quantum suitability
- correlation alone predicts VQC performance
- quantum entanglement exploits correlated biomedical features
- quantum advantage / quantum speedup / clinical benefit / clinical validation
- early detection performance from WDBC
- generalization of the synthetic result to real biomedical datasets

### CURRENT VERIFIED CLAIM
"Under the tested synthetic regimes and canonical VQC configuration, R3_CORRELATED produced substantially higher VQC ROC-AUC than R1_SIMPLE, and this association persisted at the canonical 100-iteration training budget."

### CLAIM_008: Dataset-Dependent Hybrid Quantum Performance
- **Claim:** VQC performance relative to classical baselines is dataset-dependent and heavily modulated by complexity characteristics like the severity of the PCA dimensionality bottleneck and native feature correlation.
- **Source:** OUR EXPERIMENT (T-061: WDBC vs Parkinson's)
- **Evidence:** 5-fold CV comparisons showing VQC maintained learning on WDBC (AUC 0.620) but collapsed to random guessing on Parkinson's (AUC 0.519), while classical SVM extracted signal from both (0.993 and 0.793, respectively).
- **Classification:** OUR EXPERIMENT
- **Constraint:** Do not claim that correlation *causes* quantum suitability alone. Claim only that dataset complexity characteristics empirically modulate the relative advantage/disadvantage of the quantum pathway.

### CLAIM_009: The Choice of Quantum Learning Paradigm Matters
- **Claim:** Quantum suitability depends on both the dataset characteristics and the choice of the quantum learning paradigm (e.g., VQC vs Quantum Kernel).
- **Source:** OUR EXPERIMENT (T-103: Quantum Shootout)
- **Evidence:** On WDBC (8 PCA components, 92.7% retained variance), QSVM vastly outperformed canonical VQC (AUC 0.842 vs 0.665) under identical dataset conditions.
- **Classification:** OUR EXPERIMENT
- **Constraint:** Do not claim that "quantum methods" generally fail or succeed based on testing only a VQC. Different paradigms behave differently. Do not claim quantum advantage; both still trailed the classical SVM (AUC 0.995).

### CLAIM_010: PCA Representation Bottleneck is Fatal to Current Quantum Models
- **Claim:** Severe PCA information loss starves current small-scale quantum models of necessary predictive signal, even when classical models operating on the exact same low-dimensional subspace can extract it.
- **Source:** OUR EXPERIMENT (T-103: Quantum Shootout)
- **Evidence:** On Parkinson's (47.0% variance retained), classical SVM achieved 0.815 AUC, while VQC (0.549) and QSVM (0.504) completely collapsed. QSVM defaulted to majority-class prediction.
- **Classification:** OUR EXPERIMENT
- **Constraint:** Do not state that PCA mathematically destroys all information (as proven by SVM's 0.815 AUC). State that the bottleneck is fatal specifically to the evaluated 8-qubit quantum architectures.
