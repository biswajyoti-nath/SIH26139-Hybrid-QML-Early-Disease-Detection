# T-062 Quantum Suitability Protocol

## 1. Objective
Design an evidence-driven, mathematical routing framework capable of determining whether to allocate computational resources to classical machine learning, quantum machine learning, or a hybrid combination. The primary objective is to avoid wasting quantum resources when evidence strongly indicates the quantum pathway is unsuitable, while identifying specific data regimes where quantum models offer competitive utility.

## 2. Research Question
“Does the relative performance and utility of quantum versus classical learning change systematically across biomedical data-complexity regimes relevant to disease detection?”

## 3. Scientific Assumptions
- **No Universal Quantum Superiority:** We do not assume quantum models will categorically outperform classical models.
- **Empiricism Over Heuristics:** We rely on measurable evidence, not arbitrary thresholds (e.g., hardcoded PCA cutoffs).
- **Correlation is Observational:** Feature correlation and linear separability are candidate variables that correlate with observed model performance; they are not assumed to possess a causal relationship with quantum suitability.
- **Dimensionality Bottleneck:** Aggressive data compression (PCA) required to fit biomedical datasets into near-term quantum architectures physically destroys information, directly impacting downstream predictive utility.

## 4. Complexity Feature Vector
Before model training, a dataset can be described by an unsupervised/supervised descriptive feature vector:
$$\vec{v} = [R_k, L_k, C, S, \rho]$$
Where $R_k$ and $L_k$ measure information retention, $C$ measures required compression, $S$ measures separability, and $\rho$ measures feature correlation. 

## 5. Mathematical Definitions
**1. PCA Information Retention ($R_k$)**
For a dataset requiring reduction to $k$ quantum dimensions:
$$R_k = \sum_{i=1}^{k} \text{explained\_variance\_ratio}_i$$

**2. Information Loss ($L_k$)**
$$L_k = 1 - R_k$$
*What it measures:* The proportion of dataset variance irretrievably lost before state preparation.
*What it does NOT measure:* It does not guarantee that the lost variance contained the decision boundary, only that global structural information was discarded.

**3. Compression Ratio ($C$)**
$$C = \frac{d_{raw}}{k}$$
where $d_{raw}$ is the original raw feature dimension and $k$ is the quantum representation dimension.

**4. Linear Separability ($S$)**
Measured via existing classical proxy (e.g., logistic regression baseline margin or intra/inter-class distance). It contributes to routing by profiling whether the dataset inherently requires highly non-linear entanglement.

**5. Feature Correlation ($\rho$)**
The mean absolute pairwise Pearson correlation of the features. It is strictly an observed descriptive variable, not a proven predictor of quantum suitability.

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
A positive $\Delta_Q$ indicates predictive advantage. However, overall utility must incorporate resource cost. 

## 9. Uncertainty Handling
Every evaluation produces a variance across the folds (e.g., standard deviation of ROC-AUC).
Uncertainty $\sigma_{\Delta}$ is incorporated into the routing decision:
$$\sigma_{\Delta} = \sqrt{\sigma_{quantum}^2 + \sigma_{classical}^2}$$
Wide variance intervals across folds prevent the system from falsely routing based on statistical noise.

## 10. Evidence States
The decision function must output one of four states. It must **not** force a binary classical/quantum choice.
1. **Classical Preferred:** $B_{classical}$ heavily outperforms $B_{quantum}$ outside the margin of error, or $L_k$ is so extreme that $B_{quantum}$ collapses to random guessing.
2. **Quantum Pathway Promising:** $\Delta_Q > 0$ and is statistically significant across folds.
3. **Statistically Comparable:** $|\Delta_Q| \approx 0$ (within $\sigma_{\Delta}$). Both pathways offer similar predictive power.
4. **Inconclusive:** High variance ($\sigma > \text{threshold}$) or contradicting metric indicators (e.g., high AUC but low F1 due to imbalance instability) prevents a confident routing decision.

## 11. Two-Stage Routing Architecture
**Stage 1: Dataset Complexity Profiling**
Extract $\vec{v} = [R_k, L_k, C, S, \rho]$.
*Output:* Unsupervised and supervised complexity characteristics.

**Stage 2: Classical Reference Benchmark**
Run $B_{classical}$ using leakage-safe CV.
*Output:* Ceiling of predictive task difficulty.

**Stage 3: Quantum Pilot Evaluation**
Run $B_{quantum}$ on a minimal subset/budget if $L_k$ does not trivially guarantee model collapse.

**Stage 4: Evidence Comparison & Decision**
Compute $\Delta_Q$ and variance. Route to one of the four Evidence States.

## 12. Resource-Aware Routing
A conceptual utility function guides the final routing recommendation:
$$Utility = (\text{Predictive Benefit}) - (\text{Computational Cost}) - (\text{Uncertainty Penalty})$$
*Computational Cost* factors in simulator runtime, qubit scaling, and iteration budget. No arbitrary numerical weights are hardcoded. Future iterations of this framework will calibrate the weights via multi-dataset benchmark evidence.

## 13. Leakage Prevention
**Unsupervised vs Supervised Features:**
- Unsupervised characteristics ($R_k, C, \rho$) can be computed globally on the dataset feature matrix *only if* target labels are ignored.
- Supervised metrics ($S$, $B_{classical}$, $B_{quantum}$) strictly require a CV loop. The profiler must fit its preprocessing pipelines entirely within the training folds.
- Target information must never bleed into the global complexity profiler.

## 14. Validation Protocol
T-062 itself will be validated on a matrix of *unseen* biomedical datasets spanning different:
- Dimensionality ($d_{raw} \in [30, \sim 10000]$)
- Imbalance ratios
- Feature correlation regimes
- PCA variance retention characteristics
*Evaluation Criteria:* Does the routing protocol reliably predict relative quantum/classical utility out-of-sample?

## 15. Failure Modes
1. **Dimensionality Curse:** Extremely high $d_{raw}$ (e.g., genomics) forces $C \gg 1$, yielding near 100% information loss ($L_k \to 1$).
2. **Simulator Exhaustion:** Exceeding 20-24 qubits on local classical hardware causes RAM exhaustion, blocking evaluation.
3. **Classical Over-optimization:** Imbalanced hyperparameter tuning where classical models are aggressively optimized while the quantum model is restricted to its canonical baseline.

## 16. Current Evidence from T-060/T-061
- **T-060:** A reproducible association was found on synthetic data between highly correlated regimes (R3) and improved relative VQC performance.
- **T-061 (WDBC):** $R_6 \approx 88.8\%$. $B_{quantum} \approx 0.620$ vs $B_{classical} \approx 0.993$.
- **T-061 (Parkinson's):** $R_6 \approx 41.7\%$. $B_{quantum} \approx 0.519$ vs $B_{classical} \approx 0.793$. The PCA bottleneck severely starves the state preparation, leading to model collapse near random guessing.

## 17. What is NOT yet proven
- It is NOT proven that high feature correlation *causes* quantum suitability.
- It is NOT proven that there exists a universal PCA variance cutoff (e.g., exactly 50%) below which quantum models will always fail.

## 18. Future Benchmark Requirements
To graduate this framework from theoretical to validated, we require a diverse benchmark repository containing text, tabular, and signal biomedical data of varying dimensionalities.

## 19. Proposed T-062 Acceptance Criteria
- No arbitrary routing threshold is presented as scientifically validated.
- No causal claim is made about feature correlation.
- PCA information retention is treated as a measurable information/compression variable, not proof of quantum suitability.
- Classical performance is explicitly included.
- Quantum performance is explicitly included.
- Uncertainty is explicitly represented.
- INCONCLUSIVE is a valid output.
- Resource cost is considered.
- Validation on unseen biomedical datasets is specified.
- Leakage prevention is explicitly defined.
- The protocol remains strictly aligned with SIH PS 26139.
- The design does not assume quantum superiority.
- No code is implemented.
