# PROJECT_STATE.md
## SIH 26139 — Hybrid QML Platform

> **Last Updated:** 2026-09-06
> **Current Phase:** Phase 4 — Quantum Suitability & Multi-Pathway Routing

---

## Active Task

**T-061:** VERIFIED
**Summary:** Benchmark on real biomedical data (WDBC & Parkinson's) showed dataset-dependent VQC performance, heavily modulated by PCA bottlenecks and feature correlation.

**T-103 (Quantum Model Shootout):** VERIFIED
**Summary:** Expanded the benchmark to include QSVM (Quantum Kernel). Proved that quantum learning paradigms behave fundamentally differently. QSVM outperformed VQC on WDBC, but both quantum methods catastrophically collapsed on the heavily bottlenecked Parkinson's dataset, while classical SVM maintained high predictive performance.

**NEXT TASK: T-062 — Evidence-Gated Quantum Pathway Selection (Implementation)**
**PURPOSE:** The mathematical framework for T-062 is designed (`docs/T062_QUANTUM_SUITABILITY_PROTOCOL.md`). The implementation must now build the actual routing component capable of distinguishing between Classical Preferred, QSVM Promising, VQC Promising, or Inconclusive based on dataset complexity metrics (like PCA variance retention).

---

## Blocked Tasks
- None.

---

## Session Handoff (Next Agent Instructions)
- Read `AGENTS.md` before doing anything.
- Understand the evidence gathered in T-103 (`docs/T103_QUANTUM_SHOOTOUT_REPORT.md`). 
- Do NOT assume "quantum is better". Do NOT assume any single complexity metric is a perfect predictor.
- The next step is implementing the T-062 routing logic based on the approved multi-stage protocol.
