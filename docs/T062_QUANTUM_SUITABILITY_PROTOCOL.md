# T-062 Quantum Suitability Protocol

## 1. Objective
Design an evidence-driven, mathematical routing framework capable of determining whether to allocate computational resources to classical machine learning, quantum machine learning, or a hybrid combination. The primary objective is to avoid wasting quantum resources when evidence strongly indicates the quantum pathway is unsuitable, while identifying specific data regimes where quantum models offer competitive utility.

## 2. Research Question
“Does the relative performance and utility of quantum versus classical learning change systematically across biomedical data-complexity regimes relevant to disease detection?”

## 3. Scientific Assumptions
- **No Universal Quantum Superiority:** We do not assume quantum models will categorically outperform classical models.
- **Empiricism Over Heuristics:** We rely on measurable evidence, not arbitrary thresholds (e.g., hardcoded PCA cutoffs).
- **Correlation is Observational:** Feature correlation and linear separability are candidate variables that correlate with observed model performance; they are not assumed to possess a causal relationship with quantum suitability.
- **Dimensionality Bottleneck:** PCA reduces the representation to a lower-dimensional subspace and discards variance outside that subspace. High information loss may indicate a representation bottleneck, but explained variance is NOT equivalent to predictive information.

## 4. Complexity Feature Vector
Before model training, a dataset can be described by an unsupervised/supervised descriptive feature vector:
$$\vec{v} = [R_k, L_k, C, S, \rho]$$
Where $R_k$ and $L_k$ measure information retention, $C$ measures required compression, $S$ measures separability, and $\rho$ measures feature correlation. 

## 5. Mathematical Definitions
**1. PCA Information Retention ($R_k$)**
For a dataset requiring reduction to $k$ quantum dimensions:
$$R_k = \sum_{i=1}^{k} \text{explained\_variance\_ratio}_i$$
*What it measures:* $R_k$ measures retained global variance. Neither directly measures retained class-discriminative information.

**2. Information Loss ($L_k$)**
$$L_k = 1 - R_k$$
*What it measures:* $L_k$ measures discarded global variance. Neither directly measures discarded class-discriminative information.

**3. Compression Ratio ($C$)**
$$C = \frac{d_{raw}}{k}$$
where $d_{raw}$ is the original raw feature dimension and $k$ is the quantum representation dimension.

**4. Linear Separability ($S$)**
Linear separability is a descriptive proxy for the difficulty of a linear decision boundary. It may characterize dataset structure, but it does not establish that a quantum model or entanglement is required.

**5. Feature Correlation ($\rho$)**
The mean absolute pairwise Pearson correlation of the features. It is strictly an observed descriptive variable, not a proven predictor of quantum suitability. No complexity variable establishes a specific quantum mechanism.

## 6. Classical Reference Model
The predictive baseline strength, $B_{classical}$, is defined by a highly optimized classical model (e.g., SVM or XGBoost). Routing depends on **relative** utility; hence, evaluating intrinsic quantum performance is meaningless without $B_{classical}$ evaluated strictly under identical cross-validation folds and leakage-safe preprocessing.

## 7. Quantum Reference Model
The quantum baseline performance, $B_{quantum}$, is derived from the canonical VQC:
- 8 qubits
- AngleEmbedding using RY
- RealAmplitudes ansatz (linear entanglement, 3 layers)
- Adam Optimizer (lr=0.01, 100 iterations)
- `lightning.qubit` statevector simulator

## 8. Relative Utility Formulation
The primary metric for comparative analysis is the predictive delta:
$$\Delta_Q = B_{quantum} - B_{classical}$$
A positive $\Delta_Q$ indicates predictive advantage under the evaluated protocol. However, overall utility must incorporate resource cost. 

## 9. Uncertainty Handling
A simplified approximation of uncertainty assumes independent models:
$$\sigma_{\Delta} \approx \sqrt{\sigma_{quantum}^2 + \sigma_{classical}^2}$$
However, because quantum and classical models are evaluated on the same folds, their fold-level estimates are paired and may be correlated. The framework requires a more rigorous future formulation based on fold-wise paired differences:

For fold $j$:
$$\Delta_j = B_{quantum,j} - B_{classical,j}$$

Then:
$$\text{mean}(\Delta) = \frac{1}{n} \sum \Delta_j$$

And estimate uncertainty directly from the distribution of $\Delta_j$:
$$s_{\Delta} = \sqrt{ \frac{1}{n-1} \sum_j (\Delta_j - \text{mean}(\Delta))^2 }$$

The eventual routing decision should use the paired distribution of model differences rather than assuming independent model estimates. Do NOT claim statistical significance until an appropriate statistical test and confidence interval procedure are actually implemented.

## 10. Evidence States
The decision function must output one of four states.
1. **CLASSICAL PREFERRED:** Strong evidence that the classical reference is better under the evaluated protocol and quantum pilot does not justify additional quantum allocation.
2. **QUANTUM PATHWAY PROMISING:** Quantum performance is better than the classical reference under the evaluated protocol with uncertainty sufficiently supporting the observed advantage.
3. **STATISTICALLY COMPARABLE:** Observed difference is small relative to uncertainty and there is no sufficient evidence to prefer either pathway. This conceptually requires a pre-specified practical equivalence margin in a future validated implementation.
4. **INCONCLUSIVE:** Evidence is insufficient because of high variance, unstable metrics, inadequate quantum training, conflicting metrics, insufficient sample size, or other methodological limitations.

## 11. Evidence-Gated Quantum Pathway Selection
**Stage 1: Dataset Complexity Profiling**
Compute descriptive characteristics before supervised benchmarking: $R_k$, $L_k$, $C$, $\rho$, $S$ (where valid).

**Stage 2: Classical Reference Benchmark**
Evaluate strong classical baselines under leakage-safe CV.

**Stage 3: Quantum Pilot Gate**
Use complexity characteristics and available computational budget only to determine whether a quantum pilot is WORTH TESTING. Low PCA retention may provide an early warning of a severe representation bottleneck and can therefore be investigated as a resource-allocation signal. That is an experimentally testable hypothesis, not a validated rule. *CRITICAL: This gate must NOT claim that it can already predict quantum suitability. It is an EXPERIMENTAL ALLOCATION GATE.*

**Stage 4: Quantum Pilot**
Evaluate the canonical VQC under matched preprocessing and evaluation conditions.

**Stage 5: Paired Evidence Comparison**
Compare fold-level quantum and classical results using paired distributions.

**Stage 6: Evidence State**
Determine state: CLASSICAL PREFERRED, QUANTUM PATHWAY PROMISING, STATISTICALLY COMPARABLE, or INCONCLUSIVE. This distinction is central to the research contribution.

## 12. Resource-Aware Routing
A conceptual utility framework guides the final routing recommendation:
$$Utility = (\text{Predictive Benefit}) - (\text{Computational Cost}) - (\text{Uncertainty Penalty})$$
*Computational Cost* factors in simulator runtime, qubit scaling, and iteration budget. This is explicitly classified as a conceptual framework. No weights should be selected yet. Future calibration requires multi-dataset empirical evidence.

## 13. Leakage Prevention
**Unsupervised vs Supervised Features:**
- Unsupervised characteristics ($R_k, C, \rho$) can be computed globally on the dataset feature matrix *only if* target labels are ignored.
- Supervised metrics ($S$, $B_{classical}$, $B_{quantum}$) strictly require a CV loop. The profiler must fit its preprocessing pipelines entirely within the training folds.
- Target information must never bleed into the global complexity profiler.

## 14. Validation Protocol
T-062 should eventually be evaluated using:
**TRAINING / CALIBRATION DATASETS** versus **HELD-OUT TEST DATASETS.**

The router must not be judged on the same datasets used to discover its thresholds or weighting. The final scientific question becomes:
*“Can the routing protocol generalize to previously unseen biomedical datasets?”*
This requires a future benchmark matrix containing multiple biomedical datasets with different dimensionality, PCA retention, feature correlation, separability, sample size, class imbalance, and quantum compression requirements.

## 15. Failure Modes
1. **Dimensionality Curse:** Extremely high $d_{raw}$ (e.g., genomics) forces $C \gg 1$, yielding near 100% information loss ($L_k \to 1$).
2. **Simulator Exhaustion:** Exceeding 20-24 qubits on local classical hardware causes RAM exhaustion, blocking evaluation.
3. **Classical Over-optimization:** Imbalanced hyperparameter tuning where classical models are aggressively optimized while the quantum model is restricted to its canonical baseline.

## 16. Current Evidence from T-060/T-061
**WDBC:**
$R_6 \approx 88.8\%$
$VQC \approx 0.620$ ROC-AUC
$SVM \approx 0.993$ ROC-AUC

**Parkinson's (PCA=6):**
$R_6 \approx 41.7\%$
$VQC \approx 0.519$ ROC-AUC
$SVM \approx 0.793$ ROC-AUC

**Parkinson's (PCA=8):**
$R_8 \approx 46.3\%$
$VQC \approx 0.517$ ROC-AUC
$SVM \approx 0.815$ ROC-AUC

T-061 demonstrates dataset-dependent differences in the observed performance of the tested VQC relative to classical baselines. Parkinson's also exhibits substantially lower PCA variance retention than WDBC under the tested quantum dimensionality. These observations motivate investigation of representation bottlenecks as candidate resource-allocation variables.

## 17. Research Novelty
The proposed contribution is an evidence-gated framework that integrates biomedical complexity profiling, classical reference benchmarking, quantum pilot evaluation, paired comparative evidence, uncertainty handling, and resource-aware pathway selection within a single hybrid QML platform. Novelty relative to prior literature requires a dedicated literature review.

## 18. Proposed T-062 Acceptance Criteria
- No causal interpretation of PCA retention.
- No causal interpretation of feature correlation.
- No claim that any complexity variable is already a validated quantum-suitability predictor.
- Fold-level paired comparison is specified.
- Statistical significance is not claimed before a valid statistical procedure is implemented.
- Practical equivalence margins are to be empirically calibrated.
- Router validation uses unseen datasets.
- Quantum pilot allocation is distinguished from quantum suitability prediction.
- INCONCLUSIVE remains a first-class outcome.
- Resource cost is included.
- The framework remains aligned with PS 26139.
- No quantum advantage is assumed.

