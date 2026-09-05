# Quantum Ablation Protocol

## Objective
Identify how dimensionality, circuit depth, loss function, and training budget affect VQC performance on WDBC without manual cherry-picking or data leakage.

## Selection Rule
At the conclusion of each stage, the "winning" configuration is the one that achieves the highest ROC-AUC on a 20% stratified holdout. 
**Tie-breaker:** If two configurations are within 1.0% absolute ROC-AUC of each other, the computationally cheaper configuration (fewer qubits, fewer layers, or fewer iterations) will be strictly selected.

## Stage A: PCA / Qubit Dimension
- **Fixed Variables:** Layers = 3, Loss = MSE, Iterations = 50, Seed = 42
- **Test Variables (Qubits / PCA components):** 
  - `dim_4`: 4
  - `dim_6`: 6
  - `dim_8`: 8

## Stage B: Circuit Depth
- **Fixed Variables:** Qubits = [Best from Stage A], Loss = MSE, Iterations = 50, Seed = 42
- **Test Variables (Layers):**
  - `depth_1`: 1 layer
  - `depth_2`: 2 layers
  - `depth_3`: 3 layers

## Stage C: Loss Function
- **Fixed Variables:** Qubits = [Best A], Layers = [Best B], Iterations = 50, Seed = 42
- **Test Variables (Loss):**
  - `loss_mse`: Mean Squared Error
  - `loss_bce`: Binary Cross-Entropy

## Stage D: Training Budget
- **Fixed Variables:** Qubits = [Best A], Layers = [Best B], Loss = [Best C], Seed = 42
- **Test Variables (Iterations):**
  - `iter_50`: 50
  - `iter_100`: 100
  - `iter_200`: 200

## Stage E: Classical Comparison
- The final VQC configuration (Best from Stage D) will be compared against the existing classical baseline reference (SVM, RF, XGBoost) using the exact same metrics and 5-fold CV protocol.
