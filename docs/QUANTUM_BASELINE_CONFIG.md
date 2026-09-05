# Canonical Quantum Baseline Configuration

## 1. Environment Specifications
- **Framework:** PennyLane
- **Framework Version:** 0.45.1
- **Python Version:** 3.12.13 (Managed via `uv`)
- **Simulator:** `lightning.qubit` (C++ statevector simulation)

## 2. Dataset & Preprocessing
- **Dataset:** WDBC (569 samples, 30 features)
- **Split Strategy:** Stratified 80/20 holdout or 5-fold CV
- **Preprocessing:** `StandardScaler` (fitted on train only) followed by `PCA`
- **Number of PCA Components:** 8 (This explicitly determines the number of qubits)

## 3. VQC Architecture
- **Number of Qubits:** 8
- **Feature Encoding (Data Loader):** `qml.AngleEmbedding`
  - **Rotation Axis:** $R_x$ (standard rotation for continuous variables)
- **Ansatz (Parameterized Circuit):** 
  - **Concept:** `RealAmplitudes` (Linear entanglement with parameterized $R_y$ rotations)
  - **PennyLane Implementation:** `qml.BasicEntanglerLayers(weights, wires, rotation=qml.RY)`
  - **Entanglement Pattern:** Ring (each qubit targets the next, standard in PennyLane)
- **Number of Layers (Depth):** 3
- **Measurement Observable:** Expectation value of Pauli-Z on qubit 0 (`qml.expval(qml.PauliZ(0))`)
- **Output-to-Probability Mapping:** `Probability(y=1) = (expval + 1.0) / 2.0`

## 4. Training Hyperparameters
- **Loss Function:** Mean Squared Error (MSE) against shifted binary targets
- **Optimizer:** Adam (`qml.AdamOptimizer`)
- **Learning Rate:** 0.05
- **Maximum Iterations:** 50
- **Batch Strategy:** Full-batch gradient descent (for absolute stability during simulation)
- **Initialization Strategy:** Uniform random $[0, 2\pi)$
- **Random Seed:** 42

## 5. Noise and Hardware (Future Variables)
- **Noise Model:** None (Ideal simulator baseline). Noise injection is explicitly separated as a future experiment variable.
- **Hardware Execution:** None for this baseline.

---

> **Note on Ansatz Naming:** Project requirements often refer to `RealAmplitudes`. In Qiskit, this is a built-in template. In PennyLane, the exact mathematical equivalent is `qml.BasicEntanglerLayers` using the $R_y$ rotation. Throughout this codebase, "RealAmplitudes" conceptually refers to this PennyLane implementation.
