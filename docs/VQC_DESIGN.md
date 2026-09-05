# VQC Design Specification

## Research Objective
Evaluate whether a quantum-enhanced feature representation (via a Variational Quantum Circuit) provides measurable predictive value on the WDBC dataset when compared to strong classical baselines (SVM, RF, XGBoost).

## Architecture

### 1. Dimensionality Reduction
- **Problem:** WDBC has 30 features. A 30-qubit simulator is extremely slow for training, and 30 qubits is too deep for current NISQ devices without severe barren plateau issues.
- **Solution:** Principal Component Analysis (PCA).
- **Dimension Chosen:** 8 components. 8 qubits allow for fast simulation, capture the vast majority of variance in the WDBC dataset, and perfectly match the baseline classical protocol. 

### 2. Feature Encoding (Quantum Data Loader)
- **Method:** `qml.AngleEmbedding`
- **Why:** Maps the 8 classical continuous features into the rotation angles (e.g., $R_y$) of 8 qubits. This is minimal in depth (depth=1) and avoids the complexity of amplitude encoding while still embedding the features non-linearly into the quantum state.

### 3. Ansatz (Parameterized Variational Circuit)
- **Method:** `qml.BasicEntanglerLayers`
- **Why:** It applies single-qubit rotations (parameterized) followed by a ring of CNOT gates. It is highly expressive for its depth.
- **Layers:** Default to 3. This provides a balance between expressibility and trainability.

### 4. Measurement & Classification
- **Measurement:** Expectation value of the Pauli-Z operator on the first qubit: `qml.expval(qml.PauliZ(0))`.
- **Mapping:** The expectation value spans `[-1, 1]`. We map this to a probability `[0, 1]` using the linear transformation: `prob = (expval + 1) / 2`.
- **Classification:** Threshold at 0.5. `Prediction = 1 if prob >= 0.5 else 0`.

### 5. Training Protocol
- **Optimizer:** `qml.AdamOptimizer` (or `qml.NesterovMomentumOptimizer`). Adam is robust for VQC landscapes.
- **Loss Function:** Binary Cross-Entropy (or Mean Squared Error against binary targets). We will use a standard Square Loss `(y_true - prob)**2` for simplicity and stability in quantum landscapes.
- **Batches:** Full-batch or large mini-batch to ensure stable gradient updates.

## Common Interface Integration
The VQC will be wrapped in a `PennyLaneVQC` class that implements:
- `fit(X, y)`
- `predict(X)`
- `predict_proba(X)`

This ensures the `ExperimentRunner` and `EvaluationEngine` can treat the VQC exactly like an XGBoost or SVM model, guaranteeing a 100% fair evaluation pipeline.
