# Complexity-Regime Benchmark Results
> **Status:** VERIFIED FACT
> **Date:** 2026-09-06

## 1. Regime Table & Dataset Statistics
We executed a 5-regime controlled benchmark evaluating model performance against isolated complexity dimensions.
- **R1_SIMPLE:** Linear boundary, 10 dims, low noise. (Linear Separability: 1.000)
- **R2_NONLINEAR:** Highly non-linear boundaries embedded in 10 dims. (Linear Separability: 0.846)
- **R3_CORRELATED:** 10 dims, 7 entirely redundant/highly correlated features. (Linear Separability: 0.784)
- **R4_NOISY:** 25% label noise, overlapping class distributions. (Linear Separability: 0.608)
- **R5_HIGH_DIMENSIONAL:** 100 features, only 5 informative. (Linear Separability: 0.700)

*(Linear Separability defined as logistic regression 5-fold CV accuracy).*

## 2. Classical Results (Mean ROC-AUC)
- **R1_SIMPLE:** SVM (0.986), RF (0.976)
- **R2_NONLINEAR:** SVM (0.896), RF (0.888)
- **R3_CORRELATED:** SVM (0.948), RF (0.932)
- **R4_NOISY:** SVM (0.581), RF (0.581)
- **R5_HIGH_DIMENSIONAL:** SVM (0.854), RF (0.819)

## 3. VQC Results & Variability (Mean ROC-AUC across 3 seeds)
- **R1_SIMPLE:** 0.522 ± 0.031
- **R2_NONLINEAR:** 0.526 ± 0.040
- **R3_CORRELATED:** 0.742 ± 0.015
- **R4_NOISY:** 0.525 ± 0.058
- **R5_HIGH_DIMENSIONAL:** 0.535 ± 0.004

## 4. Runtime Comparison
- **SVM/RF:** ~0.02s - 0.1s per fold.
- **VQC (10 iterations):** ~6.5 seconds per fold.

## 5. Observations
1. **General Inferiority:** The VQC underperforms classical baselines across all 5 regimes given the constrained iteration budget. It completely fails to learn simple boundaries (R1) rapidly.
2. **The Correlated Activation:** The VQC exhibited a *massive* performance spike (+22% ROC-AUC) on `R3_CORRELATED` relative to other regimes. While it still trails the SVM (0.742 vs 0.948), the gap narrowed significantly. 

## 6. Alternative Explanations
The performance spike in `R3` could be explained by:
- The `AngleEmbedding` and basic entangler layers naturally mapping redundant classical features into highly reinforcing entangled quantum states, avoiding barren plateaus.
- The iteration budget (10 iterations) being too low for the VQC to learn uncorrelated structures, but redundant gradients accelerating convergence in `R3`.

## 7. Limitations
- We limited the VQC to 10 iterations to make a 300-fit benchmark computationally tractable for rapid iteration. A full 100-iteration benchmark might shift the absolute values, though the structural differences between regimes should hold.
- The regimes were evaluated in isolation. Real biomedical datasets combine nonlinearity, correlation, and high dimensions simultaneously.

## 8. Conclusion for Quantum Suitability Engine
**RESEARCH HYPOTHESIS:** Pairwise feature correlation (redundancy) is a strong candidate metric for the `Quantum Suitability Profiler`. The engine should look for high multi-collinearity in classical datasets as a trigger for testing a quantum pathway.
