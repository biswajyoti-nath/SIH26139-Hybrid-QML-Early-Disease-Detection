# Quantum Stack Decision

## Framework: PennyLane
**Version:** 0.45.1 (with `pennylane-lightning` 0.45.0)
**Decision Date:** 2026-09-05

### Why Selected
We require a stack that enables reproducible, differentiable Variational Quantum Circuits (VQCs) capable of plugging directly into a scikit-learn-style classical evaluation pipeline. 

PennyLane provides a native, seamless interface with NumPy (`autograd`), PyTorch, and JAX, making gradient-based optimization of quantum circuits feel identical to classical deep learning. Its `lightning.qubit` statevector simulator (written in C++) provides extremely fast execution for typical shallow QML models.

### Alternative Considered: Qiskit
- **Qiskit** (via `qiskit-machine-learning`) was strongly considered, especially given IBM's dominance in hardware.
- **Why Rejected for Core Experimentation:** Qiskit underwent significant API churn between 1.x and 2.x. While excellent for low-level hardware transpilation, building arbitrary parameterized quantum circuits (VQCs) and hooking them into custom gradient loops is generally more verbose and slower to iterate upon than PennyLane. PennyLane abstracts the measurement and differentiation (via parameter-shift rules or adjoint differentiation) elegantly.

### Advantages of PennyLane
1. **API Stability:** Highly stable `qml.qnode` paradigm.
2. **Gradient Support:** Built-in differentiation (e.g. adjoint, parameter-shift) allowing seamless use of `qml.AdamOptimizer`.
3. **Scikit-Learn Interoperability:** Can be easily wrapped into a class that implements `.fit()`, `.predict()`, and `.predict_proba()`.
4. **Simulator Support:** `lightning.qubit` is exceptionally fast for the 8-12 qubit range we require.

### Limitations
1. **Portability to Real Hardware:** While PennyLane *can* dispatch to IBM Q hardware (via PennyLane-Qiskit plugin), executing thousands of parameter-shift gradient evaluations on real hardware is prohibitively expensive and noisy. (We mitigate this by strictly utilizing simulators for the prototype phase).
2. **Advanced Noise Simulation:** PennyLane's noise models (`default.mixed`) are computationally heavier than Qiskit Aer. We will restrict initial milestones to ideal simulation.

### Evidence
- Our current UV environment successfully locked and resolved `pennylane==0.45.1` on Python 3.12 without the heavy dependency tree conflicts sometimes seen with older QML toolkits.
