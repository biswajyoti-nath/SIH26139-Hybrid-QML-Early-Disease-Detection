# Quantum Optimization & Ablation Findings

## 1. Does VQC outperform SVM on WDBC?
**No.** The optimized VQC achieved a mean ROC-AUC of 0.6201 (±0.0624), significantly trailing the classical SVM at 0.9935 (±0.0047). Accuracy was similarly impacted (0.6168 vs 0.9561).

## 2. Does VQC approach classical performance?
**No.** Despite testing various depths, dimensionalities, and loss functions, the VQC struggled to capture the complex tabular structure of WDBC effectively. It remained ~37% worse in ROC-AUC than the linear SVM.

## 3. Which variables affect VQC performance?
- **Iterations:** Had the strongest positive effect; moving from 25 to 100 iterations increased ROC-AUC by approximately 4%.
- **Dimensionality:** Crucially, 6 qubits drastically outperformed 8 qubits. This suggests that injecting too many continuous parameters into the NISQ-era `AngleEmbedding` leads to harder optimization landscapes (likely barren plateaus) overriding any information gain from retaining 2 extra PCA components.
- **Circuit Depth:** 3 layers significantly outperformed 1 or 2 layers, indicating that entanglement expressivity is required to model the feature interactions.

## 4. Does increased circuit depth help?
**Yes.** Depth 3 (ROC-AUC ~0.689 in holdout) outperformed Depth 1 (~0.538) by over 15% absolute. Expressivity is a bottleneck in shallower circuits.

## 5. Does increased qubit count help?
**No.** Qubit count demonstrated a non-linear relationship. 6 qubits was the optimal configuration. Increasing to 8 qubits dropped performance severely (~0.689 -> ~0.599 in holdout). This is a textbook example of the trainability vs. expressivity trade-off in QML.

## 6. Does BCE improve training compared with MSE?
**No.** In our ablation study, BCE achieved comparable but marginally worse ROC-AUC (0.6878 vs 0.6895 for MSE). Given the linear mapping of expectation values to probabilities, MSE proved slightly more stable.

## 7. What is the computational cost?
Astronomical compared to classical ML. Training the 6-qubit VQC for 100 iterations took **~286 seconds per fold** using an advanced C++ statevector simulator (`lightning.qubit`). The classical SVM took **0.02 seconds** per fold.

## 8. Is there evidence of quantum advantage?
**None.** The VQC requires vastly more compute, achieves substantially lower predictive validity, and provides no specific representational advantage on this tabular dataset.

## 9. What can legitimately be claimed?
We can claim that we successfully engineered a highly optimized, reproducible Hybrid QML architecture capable of executing variational circuits natively alongside classical baselines. We can also claim the scientifically rigorous finding that standard VQCs do *not* offer automatic advantages on classical tabular data like WDBC, acting as a critical correction to hype in the digital health sector.

## 10. What remains unresolved?
Whether alternative feature maps (like ZZFeatureMap or trainable data re-uploading) or alternative target functions (like Quantum Support Vector Classification - QSVM) can bridge the 37% ROC-AUC gap.
