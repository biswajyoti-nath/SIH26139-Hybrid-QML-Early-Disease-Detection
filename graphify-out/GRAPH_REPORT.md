# Graph Report - core-program  (2026-09-06)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 852 nodes · 939 edges · 97 communities (81 shown, 7 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0d47a30d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- experiment_runner.py
- PROJECT_KNOWLEDGE.md
- EXPERIMENT_PROTOCOL.md
- Complexity-Regime Benchmark Results
- OPEN_QUESTIONS.md
- CLAIMS_LEDGER.md
- TECH_STACK.md
- 1. Demo Flow (11 Steps)
- DECISIONS.md — Architecture & Research Decision Log
- 3. Module Specifications
- AGENTS.md — Agentic Development Operating System
- SIH_26139_Research_Work_Document.md
- SIH 2026 PS 26139: Current Research & Implementation Approach
- SIH_26139_ULTRA_DETAILED_ACTION_PLAN.md
- PennyLaneVQC
- MILESTONE 04: Research Direction Pivot
- 27. Three-Hour Execution Plan
- 27. Three-Hour Execution Plan
- SIH 26139 — Hybrid Quantum Machine Learning Platform for Early Disease Detection
- Quantum Optimization & Ablation Findings
- Primary metrics
- Primary metrics
- 16. Planned Platform Modules
- Architecture
- Quantum Ablation Protocol
- Fair comparison rules
- Fair comparison rules
- SESSION_PROTOCOL.md — Session Start/End Checklist
- Framework: PennyLane
- Proposed stack
- 17. MVP
- 23. PPT Source of Truth
- Proposed stack
- 17. MVP
- 23. PPT Source of Truth
- TASKS.md — Task Registry
- Canonical Quantum Baseline Configuration
- MILESTONE 04: Quantum Suitability & Complexity Benchmarking
- 18. Potential Future Research Directions
- 8. Real Biomedical Data Strategy
- 24. Slide 5 — Impact & Benefits
- Core references
- Baseline models
- 24. Slide 5 — Impact & Benefits
- Core references
- Baseline models
- health_check.sh
- Phase 8 — Frontend Dashboard
- Variational Quantum Classifier (VQC)
- 22. Current Task Order
- 10. Dimensionality Reduction
- 10. Dimensionality Reduction
- Phase 10 — Quality & Documentation
- WDBC Dataset
- SIH 2026 — PS 26139
- 15. Explainability
- 8. Proposed Quantum Component
- SIH 2026 — PS 26139
- 15. Explainability
- 8. Proposed Quantum Component
- Phase 1 — Environment & Dependencies
- Phase 3 — Classical ML
- Phase 4 — Quantum ML
- Phase 9 — Integration & Demo
- 11. Quantum Baseline
- 13. Quantum Ablation Strategy
- 19. Scientific Guardrails
- 5. Current Experimental Strategy
- 7. Canonical T-060 Validation
- 2. Core Thesis
- 3. Pilot Dataset: WDBC
- 4. Proposed System Architecture
- 9. Data Preprocessing
- 19. Feasibility
- 2. Core Thesis
- 3. Pilot Dataset: WDBC
- 4. Proposed System Architecture
- 9. Data Preprocessing
- Phase 0 — Workspace & Infrastructure
- Phase 2 — Data & Preprocessing
- Phase 6 — Experiment Runner + Results Store
- JUDGE_QA_QUANTUM.md
- 1. Strategic Objective
- 3. Central Research Hypothesis
- 6. T-060 Complexity Benchmark
- Pushpanjali & Adisesha 2025
- Sammartino 2026
- core-program

## God Nodes (most connected - your core abstractions)
1. `SIH 2026 PS 26139: Current Research & Implementation Approach` - 26 edges
2. `PennyLaneVQC` - 16 edges
3. `TASKS.md — Task Registry` - 15 edges
4. `ExperimentRunner` - 14 edges
5. `ExperimentConfig` - 13 edges
6. `DECISIONS.md — Architecture & Research Decision Log` - 13 edges
7. `DatasetManager` - 12 edges
8. `PreprocessingEngine` - 12 edges
9. `MILESTONE 04: Research Direction Pivot` - 12 edges
10. `Approved Language Examples` - 12 edges

## Surprising Connections (you probably didn't know these)
- `run_benchmark()` --uses--> `ComplexityProfiler`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/complexity_profiler.py
- `run_benchmark()` --uses--> `EvaluationEngine`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/evaluation.py
- `run_benchmark()` --uses--> `PreprocessingEngine`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/preprocessing.py
- `run_benchmark()` --uses--> `SyntheticGenerator`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/synthetic_generator.py
- `run_config()` --calls--> `ExperimentConfig`  [EXTRACTED]
  scripts/run_ablation.py → backend/core/config.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Breast Cancer QML Benchmarking Literature** — docs_research_log_mpofu_2025, docs_research_log_kundu_2025, docs_research_log_pushpanjali_2025, wdbc_dataset [EXTRACTED 0.90]
- **QML Theoretical Foundations and Challenges** — docs_research_log_havlicek_2019, docs_research_log_cerezo_2021, docs_research_log_gupta_2025 [EXTRACTED 0.95]
- **Scientific Integrity Framework** — docs_claims_ledger, docs_experiment_protocol, decisions [EXTRACTED 1.00]

## Communities (97 total, 7 thin omitted)

### Community 0 - "experiment_runner.py"
Cohesion: 0.06
Nodes (41): ComplexityProfiler, ndarray, Computes observable statistical descriptors of a dataset. These are purely…, ExperimentConfig, CVExperimentRunner, Dataset, DatasetManager, Manages loading and validation of the WDBC dataset. (+33 more)

### Community 1 - "PROJECT_KNOWLEDGE.md"
Cohesion: 0.04
Nodes (45): 10. Explainability Strategy, 11. Software Architecture, 12. Demo Flow, 13. Research Evidence, 14. Known Limitations, 15. Open Questions, 16. Unsupported Claims — Must NOT Make, 17. Implementation Roadmap (+37 more)

### Community 2 - "EXPERIMENT_PROTOCOL.md"
Cohesion: 0.05
Nodes (38): 10. Verdict Logic, 11. Experiment Flow Diagram, 12. Dataset Provenance Decision, 13. FAIR COMPARISON & SELECTION BIAS RULE, 1. Dataset, 2. Preprocessing Pipeline, 3. Data Split, 4. Reproducibility Parameters (+30 more)

### Community 3 - "Complexity-Regime Benchmark Results"
Cohesion: 0.06
Nodes (27): ENGINEER AGENT PROTOCOL, EVALUATOR AGENT PROTOCOL, EXPERIMENTALIST AGENT PROTOCOL, JUDGE AGENT PROTOCOL, RESEARCHER AGENT PROTOCOL, 1. Regime Table & Dataset Statistics, 2. Classical Results (Mean ROC-AUC), 3. VQC Results & Variability (Mean ROC-AUC across 3 seeds) (+19 more)

### Community 4 - "OPEN_QUESTIONS.md"
Cohesion: 0.06
Nodes (30): Category 1 — Environment and Infrastructure, Category 2 — Quantum Framework, Category 3 — Quantum Circuit Design, Category 4 — Experimental Design, Category 5 — Explainability, Category 6 — Strategic Questions, Priority Levels, Q1.1 — Python 3.14 Package Compatibility (+22 more)

### Community 5 - "CLAIMS_LEDGER.md"
Cohesion: 0.08
Nodes (25): Approved Language Examples, CLAIM_002: Classical Baselines are Extremely Strong on WDBC, CLAIM_003: VQC Core Engine is Functional, CLAIM_004: VQC Performance and Advantage (FIREWALL), CLAIM_005: Untuned VQC Underperforms Strong Classical Baselines, CLAIM_006: Optimized VQC Underperforms Classical ML on WDBC, CLAIM_007: VQC Dimensionality Trade-off (Barren Plateaus), Classification System (+17 more)

### Community 6 - "TECH_STACK.md"
Cohesion: 0.08
Nodes (25): Backend, Classical ML Stack, Compatibility Concerns Summary, Complete Recommended Requirements, Dependencies (via `uv`), Deployment, Docker (installed), Environment Management Strategy: `uv` (+17 more)

### Community 7 - "1. Demo Flow (11 Steps)"
Cohesion: 0.08
Nodes (24): 1. Demo Flow (11 Steps), 2. Judge Q&A Preparation, 3. What Must Be True Before Demo Day, 4. Demo Script (2-Minute Version), Core Principle, Q: "Can this system be used for actual cancer diagnosis?", Q: "Can you scale this to larger datasets?", Q: "How do you ensure the comparison is fair?" (+16 more)

### Community 8 - "DECISIONS.md — Architecture & Research Decision Log"
Cohesion: 0.09
Nodes (20): circuit(), 09. Graphify Tool Integration, Decision 10: Quantum Framework Selection, Decision 11: Pivot to Hybrid Quantum Suitability Engine, Decision 12: SIH Strategic Alignment & Scientific Gating, Decision: Claims Firewall, Decision: Data Split Strategy, Decision: Initial VQC Configuration (+12 more)

### Community 9 - "3. Module Specifications"
Cohesion: 0.10
Nodes (19): 1. Design Principles, 2. Module Map, 3.10 Frontend Dashboard, 3.1 DatasetManager, 3.2 PreprocessingEngine, 3.3 ClassicalModelEngine, 3.4 QuantumModelEngine (Abstract Interface), 3.5 ExperimentRunner (+11 more)

### Community 10 - "AGENTS.md — Agentic Development Operating System"
Cohesion: 0.11
Nodes (16): 0. Project Identity (30-second brief), 0. STRATEGIC OBJECTIVE & WINNING FILTER, 1. Mandatory Session Protocol, 2. Task Lifecycle State Machine, 3. Git Commit Convention, 4. Directory Layout, 5. Specialized Agent Invocation, 6. Critical Scientific Rules (Non-Negotiable) (+8 more)

### Community 11 - "SIH_26139_Research_Work_Document.md"
Cohesion: 0.11
Nodes (18): 11. Quantum Feature Encoding, 12. Variational Quantum Circuit, 18. Ideal Demo Flow, 19. Feasibility, 1. Problem Statement and Requirements, 20. Risks and Mitigations, 21. Research Positioning, 22. What We Can Claim vs What We Cannot Claim (+10 more)

### Community 12 - "SIH 2026 PS 26139: Current Research & Implementation Approach"
Cohesion: 0.12
Nodes (16): 10. Classical Baseline, 12. WDBC Experimental Results, 14. Complexity Profiler, 15. Planned System Architecture, 17. Evidence-Driven Quantum Routing, 20. Reproducibility Requirements, 21. Current Engineering State, 23. SIH Demonstration Strategy (+8 more)

### Community 13 - "SIH_26139_ULTRA_DETAILED_ACTION_PLAN.md"
Cohesion: 0.12
Nodes (16): 11. Quantum Feature Encoding, 12. Variational Quantum Circuit, 18. Ideal Demo Flow, 1. Problem Statement and Requirements, 20. Risks and Mitigations, 21. Research Positioning, 22. What We Can Claim vs What We Cannot Claim, 26. Final Slide 6 Message (+8 more)

### Community 14 - "PennyLaneVQC"
Cohesion: 0.23
Nodes (7): PennyLaneVQC, ndarray, A Variational Quantum Classifier (VQC) using PennyLane. Implements a standard…, test_vqc_bce_loss(), test_vqc_determinism(), test_vqc_fit_predict(), test_vqc_initialization_and_forward()

### Community 15 - "MILESTONE 04: Research Direction Pivot"
Cohesion: 0.15
Nodes (12): 10. Risks of Scientific Leakage / Biased Evaluation, 11. Exact Next Implementation Milestone, 1. Current Architecture, 2. Current Experiments, 3. Current Authoritative Results, 4. Current Scientific Claims, 5. Current Limitations, 6. What Must Remain Unchanged (+4 more)

### Community 16 - "27. Three-Hour Execution Plan"
Cohesion: 0.15
Nodes (13): 0–30 minutes, 115–140 minutes, 140–165 minutes, 165–180 minutes, 27. Three-Hour Execution Plan, 30–75 minutes, 75–115 minutes, Build / revise Slides 1–3 (+5 more)

### Community 17 - "27. Three-Hour Execution Plan"
Cohesion: 0.15
Nodes (13): 0–30 minutes, 115–140 minutes, 140–165 minutes, 165–180 minutes, 27. Three-Hour Execution Plan, 30–75 minutes, 75–115 minutes, Build / revise Slides 1–3 (+5 more)

### Community 18 - "SIH 26139 — Hybrid Quantum Machine Learning Platform for Early Disease Detection"
Cohesion: 0.15
Nodes (12): 1. Read the operating system, 2. Set up environment, 3. Check health, 4. Run tests, Core Architecture (Proposed), Directory Structure, Disclaimer, Literature Foundation (+4 more)

### Community 19 - "Quantum Optimization & Ablation Findings"
Cohesion: 0.17
Nodes (11): 10. What remains unresolved?, 1. Does VQC outperform SVM on WDBC?, 2. Does VQC approach classical performance?, 3. Which variables affect VQC performance?, 4. Does increased circuit depth help?, 5. Does increased qubit count help?, 6. Does BCE improve training compared with MSE?, 7. What is the computational cost? (+3 more)

### Community 20 - "Primary metrics"
Cohesion: 0.18
Nodes (11): 14. Evaluation Metrics, Accuracy, Computational efficiency, Confusion matrix, F1-score, Generalization, Precision, Primary metrics (+3 more)

### Community 21 - "Primary metrics"
Cohesion: 0.18
Nodes (11): 14. Evaluation Metrics, Accuracy, Computational efficiency, Confusion matrix, F1-score, Generalization, Precision, Primary metrics (+3 more)

### Community 22 - "16. Planned Platform Modules"
Cohesion: 0.20
Nodes (10): 16. Planned Platform Modules, Classical Models, Complexity Profiler, Data Manager, Experiment Runner, Explainability Engine, Metrics Engine, Preprocessor (+2 more)

### Community 23 - "Architecture"
Cohesion: 0.20
Nodes (9): 1. Dimensionality Reduction, 2. Feature Encoding (Quantum Data Loader), 3. Ansatz (Parameterized Variational Circuit), 4. Measurement & Classification, 5. Training Protocol, Architecture, Common Interface Integration, Research Objective (+1 more)

### Community 24 - "Quantum Ablation Protocol"
Cohesion: 0.22
Nodes (8): Objective, Quantum Ablation Protocol, Selection Rule, Stage A: PCA / Qubit Dimension, Stage B: Circuit Depth, Stage C: Loss Function, Stage D: Training Budget, Stage E: Classical Comparison

### Community 25 - "Fair comparison rules"
Cohesion: 0.22
Nodes (9): 13. Experimental Design, Fair comparison rules, Rule 1: Same data, Rule 2: Same split, Rule 3: Same preprocessing, Rule 4: No leakage, Rule 5: Record configurations, Rule 6: Multiple seeds (+1 more)

### Community 26 - "Fair comparison rules"
Cohesion: 0.22
Nodes (9): 13. Experimental Design, Fair comparison rules, Rule 1: Same data, Rule 2: Same split, Rule 3: Same preprocessing, Rule 4: No leakage, Rule 5: Record configurations, Rule 6: Multiple seeds (+1 more)

### Community 27 - "SESSION_PROTOCOL.md — Session Start/End Checklist"
Cohesion: 0.25
Nodes (7): Environment Quick Reference, Handoff Template, SESSION END CHECKLIST, SESSION_PROTOCOL.md — Session Start/End Checklist, SESSION START CHECKLIST, SIH 26139 · Hybrid QML Platform, Task ID Quick Reference

### Community 28 - "Framework: PennyLane"
Cohesion: 0.25
Nodes (7): Advantages of PennyLane, Alternative Considered: Qiskit, Evidence, Framework: PennyLane, Limitations, Quantum Stack Decision, Why Selected

### Community 29 - "Proposed stack"
Cohesion: 0.25
Nodes (8): 16. Software Architecture, Architectural separation, Backend, Classical ML, Deployment, Explainability, Proposed stack, Quantum

### Community 30 - "17. MVP"
Cohesion: 0.25
Nodes (8): 17. MVP, Stage 1, Stage 2, Stage 3, Stage 4, Stage 5, Stage 6, Stage 7

### Community 31 - "23. PPT Source of Truth"
Cohesion: 0.25
Nodes (8): 23. PPT Source of Truth, Constraints, Mitigations, Roadmap, Slide 1 — Team Details & Problem Statement, Slide 2 — Proposed Solution, Slide 3 — Technical Approach, Slide 4 — Feasibility & Viability

### Community 32 - "Proposed stack"
Cohesion: 0.25
Nodes (8): 16. Software Architecture, Architectural separation, Backend, Classical ML, Deployment, Explainability, Proposed stack, Quantum

### Community 33 - "17. MVP"
Cohesion: 0.25
Nodes (8): 17. MVP, Stage 1, Stage 2, Stage 3, Stage 4, Stage 5, Stage 6, Stage 7

### Community 34 - "23. PPT Source of Truth"
Cohesion: 0.25
Nodes (8): 23. PPT Source of Truth, Constraints, Mitigations, Roadmap, Slide 1 — Team Details & Problem Statement, Slide 2 — Proposed Solution, Slide 3 — Technical Approach, Slide 4 — Feasibility & Viability

### Community 35 - "TASKS.md — Task Registry"
Cohesion: 0.25
Nodes (8): Deferred / Future Work, Phase 5 — Explainability, Phase 7 — API, SIH 26139 · Hybrid QML Platform, T-050: ExplainabilityEngine — SHAP for classical, T-051: ExplainabilityEngine — input attribution for VQC, T-070: FastAPI application, TASKS.md — Task Registry

### Community 36 - "Canonical Quantum Baseline Configuration"
Cohesion: 0.29
Nodes (6): 1. Environment Specifications, 2. Dataset & Preprocessing, 3. VQC Architecture, 4. Training Hyperparameters, 5. Noise and Hardware (Future Variables), Canonical Quantum Baseline Configuration

### Community 37 - "MILESTONE 04: Quantum Suitability & Complexity Benchmarking"
Cohesion: 0.29
Nodes (7): MILESTONE 04: Quantum Suitability & Complexity Benchmarking, T-060: Complexity-Regime Benchmark Engine, T-061: Real PS-Relevant Biomedical Complexity Benchmark, T-062: Evidence-driven quantum pathway selection, T-063: Potential specialist/residual/uncertainty-aware hybrid architecture, T-064: SIH prototype integration + visual demonstration, T-065: Hostile judge evaluation + final scientific audit

### Community 38 - "18. Potential Future Research Directions"
Cohesion: 0.33
Nodes (6): 18. Potential Future Research Directions, A. Complexity-aware pathway selection, B. Quantum specialist/residual pathway, C. Multi-objective quantum utility, D. Noise-aware evaluation, E. Real hardware compatibility

### Community 39 - "8. Real Biomedical Data Strategy"
Cohesion: 0.33
Nodes (6): 8. Real Biomedical Data Strategy, Critical framing, Current data ladder, Dataset 1: WDBC, Dataset 2: Parkinson's disease classification, Potential Dataset 3: High-dimensional omics

### Community 40 - "24. Slide 5 — Impact & Benefits"
Cohesion: 0.33
Nodes (6): 24. Slide 5 — Impact & Benefits, Clinicians, Healthcare AI teams, Measurable outcomes, Patients, Researchers

### Community 41 - "Core references"
Cohesion: 0.33
Nodes (6): 25. Slide 6 — Research & References, Cerezo et al. 2021, Core references, Gupta et al. 2025, Havlíček et al. 2019, WDBC Dataset

### Community 42 - "Baseline models"
Cohesion: 0.33
Nodes (6): 5. Classical Baseline Architecture, Baseline models, Optional QSVM / Quantum Kernel, Random Forest, SVM, XGBoost

### Community 43 - "24. Slide 5 — Impact & Benefits"
Cohesion: 0.33
Nodes (6): 24. Slide 5 — Impact & Benefits, Clinicians, Healthcare AI teams, Measurable outcomes, Patients, Researchers

### Community 44 - "Core references"
Cohesion: 0.33
Nodes (6): 25. Slide 6 — Research & References, Cerezo et al. 2021, Core references, Gupta et al. 2025, Havlíček et al. 2019, WDBC Dataset

### Community 45 - "Baseline models"
Cohesion: 0.33
Nodes (6): 5. Classical Baseline Architecture, Baseline models, Optional QSVM / Quantum Kernel, Random Forest, SVM, XGBoost

### Community 46 - "health_check.sh"
Cohesion: 0.60
Nodes (5): fail(), header(), pass(), health_check.sh script, warn()

### Community 47 - "Phase 8 — Frontend Dashboard"
Cohesion: 0.33
Nodes (6): Phase 8 — Frontend Dashboard, T-080: React dashboard scaffold, T-081: Results comparison table, T-082: ROC curve + confusion matrix visualizations, T-083: SHAP plots + explainability panel, T-084: Experiment metadata + reproducibility panel

### Community 48 - "Variational Quantum Classifier (VQC)"
Cohesion: 0.40
Nodes (5): Cerezo et al. 2021, Gupta et al. 2025, Havlíček et al. 2019, Variational Quantum Classifier (VQC), ZZFeatureMap

### Community 49 - "22. Current Task Order"
Cohesion: 0.40
Nodes (5): 22. Current Task Order, T-060, T-061, T-062, T-063

### Community 50 - "10. Dimensionality Reduction"
Cohesion: 0.40
Nodes (5): 10. Dimensionality Reduction, Candidate methods, Feature selection, PCA, Working approach

### Community 51 - "10. Dimensionality Reduction"
Cohesion: 0.40
Nodes (5): 10. Dimensionality Reduction, Candidate methods, Feature selection, PCA, Working approach

### Community 52 - "Phase 10 — Quality & Documentation"
Cohesion: 0.40
Nodes (5): Phase 10 — Quality & Documentation, T-100: Unit test suite, T-101: Integration test suite, T-102: Multi-seed experiment + mean/std reporting, T-103: QSVM / Quantum Kernel fallback implementation

### Community 53 - "WDBC Dataset"
Cohesion: 0.50
Nodes (4): Kundu, Muhuri & Kumar 2025, Mpofu & Mthunzi-Kufa 2025, Prajapati et al. 2025, WDBC Dataset

### Community 54 - "SIH 2026 — PS 26139"
Cohesion: 0.50
Nodes (4): 0. Purpose of This Document, Evidence rule, Research & Working Specification, SIH 2026 — PS 26139

### Community 55 - "15. Explainability"
Cohesion: 0.50
Nodes (4): 15. Explainability, Classical models, Proposed dashboard, Quantum model

### Community 56 - "8. Proposed Quantum Component"
Cohesion: 0.50
Nodes (4): 8. Proposed Quantum Component, Candidate approach, Candidate pipeline, Proposed operating range

### Community 57 - "SIH 2026 — PS 26139"
Cohesion: 0.50
Nodes (4): 0. Purpose of This Document, Evidence rule, Research & Working Specification, SIH 2026 — PS 26139

### Community 58 - "15. Explainability"
Cohesion: 0.50
Nodes (4): 15. Explainability, Classical models, Proposed dashboard, Quantum model

### Community 59 - "8. Proposed Quantum Component"
Cohesion: 0.50
Nodes (4): 8. Proposed Quantum Component, Candidate approach, Candidate pipeline, Proposed operating range

### Community 60 - "Phase 1 — Environment & Dependencies"
Cohesion: 0.50
Nodes (4): Phase 1 — Environment & Dependencies, T-010: Python environment resolution, T-011: Backend project skeleton, T-012: Frontend project skeleton

### Community 61 - "Phase 3 — Classical ML"
Cohesion: 0.50
Nodes (4): Phase 3 — Classical ML, T-030: ClassicalModelEngine — SVM, RF, XGBoost, T-031: EvaluationEngine — metrics computation, T-032: First classical baseline experiment

### Community 62 - "Phase 4 — Quantum ML"
Cohesion: 0.50
Nodes (4): Phase 4 — Quantum ML, T-040: QuantumModelEngine abstract interface, T-041: PennyLane VQC implementation, T-042: VQC experiment — first benchmark

### Community 63 - "Phase 9 — Integration & Demo"
Cohesion: 0.50
Nodes (4): Phase 9 — Integration & Demo, T-090: Docker Compose setup, T-091: End-to-end integration test, T-092: Demo pre-training + cache

### Community 64 - "11. Quantum Baseline"
Cohesion: 0.67
Nodes (3): 11. Quantum Baseline, Current canonical design, Current evidence

### Community 65 - "13. Quantum Ablation Strategy"
Cohesion: 0.67
Nodes (3): 13. Quantum Ablation Strategy, Important methodological caveat, Selected configuration

### Community 66 - "19. Scientific Guardrails"
Cohesion: 0.67
Nodes (3): 19. Scientific Guardrails, Never claim, Required language

### Community 67 - "5. Current Experimental Strategy"
Cohesion: 0.67
Nodes (3): 5. Current Experimental Strategy, Important limitation, Stage A: Controlled complexity experiments

### Community 68 - "7. Canonical T-060 Validation"
Cohesion: 0.67
Nodes (3): 7. Canonical T-060 Validation, Configuration, Status

### Community 69 - "2. Core Thesis"
Cohesion: 0.67
Nodes (3): 2. Core Thesis, Do not sell quantum advantage. Build a platform that can test it., Working research hypothesis

### Community 70 - "3. Pilot Dataset: WDBC"
Cohesion: 0.67
Nodes (3): 3. Pilot Dataset: WDBC, Dataset specification, Important limitation

### Community 71 - "4. Proposed System Architecture"
Cohesion: 0.67
Nodes (3): 4. Proposed System Architecture, Expanded architecture, Primary pipeline

### Community 72 - "9. Data Preprocessing"
Cohesion: 0.67
Nodes (3): 9. Data Preprocessing, Data leakage rule, Required steps

### Community 73 - "19. Feasibility"
Cohesion: 0.67
Nodes (3): 19. Feasibility, Proposed feasibility constraints, Why the MVP is feasible

### Community 74 - "2. Core Thesis"
Cohesion: 0.67
Nodes (3): 2. Core Thesis, Do not sell quantum advantage. Build a platform that can test it., Working research hypothesis

### Community 75 - "3. Pilot Dataset: WDBC"
Cohesion: 0.67
Nodes (3): 3. Pilot Dataset: WDBC, Dataset specification, Important limitation

### Community 76 - "4. Proposed System Architecture"
Cohesion: 0.67
Nodes (3): 4. Proposed System Architecture, Expanded architecture, Primary pipeline

### Community 77 - "9. Data Preprocessing"
Cohesion: 0.67
Nodes (3): 9. Data Preprocessing, Data leakage rule, Required steps

### Community 78 - "Phase 0 — Workspace & Infrastructure"
Cohesion: 0.67
Nodes (3): Phase 0 — Workspace & Infrastructure, T-000: Agentic workspace setup, T-001: .gitignore + README.md

### Community 79 - "Phase 2 — Data & Preprocessing"
Cohesion: 0.67
Nodes (3): Phase 2 — Data & Preprocessing, T-020: DatasetManager — WDBC loader, T-021: PreprocessingEngine — leakage-safe scaler + PCA

### Community 80 - "Phase 6 — Experiment Runner + Results Store"
Cohesion: 0.67
Nodes (3): Phase 6 — Experiment Runner + Results Store, T-060: ExperimentRunner — orchestration, T-061A: ResultsStore — JSON persistence

## Knowledge Gaps
- **541 isolated node(s):** `12. Demo Flow`, `14. Known Limitations`, `15. Open Questions`, `16. Unsupported Claims — Must NOT Make`, `18. Persistent Project Knowledge (Current State)` (+536 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 582 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **7 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `TASKS.md — Task Registry` connect `TASKS.md — Task Registry` to `MILESTONE 04: Quantum Suitability & Complexity Benchmarking`, `AGENTS.md — Agentic Development Operating System`, `Phase 0 — Workspace & Infrastructure`, `Phase 2 — Data & Preprocessing`, `Phase 6 — Experiment Runner + Results Store`, `Phase 8 — Frontend Dashboard`, `Phase 10 — Quality & Documentation`, `Phase 1 — Environment & Dependencies`, `Phase 3 — Classical ML`, `Phase 4 — Quantum ML`, `Phase 9 — Integration & Demo`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `ExperimentRunner` (e.g. with `ExperimentConfig` and `DatasetManager`) actually correct?**
  _`ExperimentRunner` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `ExperimentConfig` (e.g. with `CVExperimentRunner` and `ExperimentRunner`) actually correct?**
  _`ExperimentConfig` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `12. Demo Flow`, `14. Known Limitations`, `15. Open Questions` to the rest of the system?**
  _541 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `experiment_runner.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06368011847463902 - nodes in this community are weakly interconnected._
- **Should `PROJECT_KNOWLEDGE.md` be split into smaller, more focused modules?**
  _Cohesion score 0.043478260869565216 - nodes in this community are weakly interconnected._
- **Should `EXPERIMENT_PROTOCOL.md` be split into smaller, more focused modules?**
  _Cohesion score 0.05128205128205128 - nodes in this community are weakly interconnected._