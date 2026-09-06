# Graph Report - core-program  (2026-09-06)

## Corpus Check
- 37 files · ~53,551 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 889 nodes · 1437 edges · 66 communities (53 shown, 4 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 60
- Community 61
- Community 63

## God Nodes (most connected - your core abstractions)
1. `SIH 2026 PS 26139: Current Research & Implementation Approach` - 26 edges
2. `DatasetManager` - 17 edges
3. `PennyLaneVQC` - 16 edges
4. `TASKS.md — Task Registry` - 15 edges
5. `ExperimentRunner` - 14 edges
6. `DECISIONS.md — Architecture & Research Decision Log` - 13 edges
7. `MILESTONE 04: Research Direction Pivot` - 12 edges
8. `Approved Language Examples` - 12 edges
9. `1. Demo Flow (11 Steps)` - 12 edges
10. `AGENTS.md — Agentic Development Operating System` - 11 edges

## Surprising Connections (you probably didn't know these)
- `run_benchmark()` --uses--> `ComplexityProfiler`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/complexity_profiler.py
- `run_benchmark()` --uses--> `EvaluationEngine`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/evaluation.py
- `run_benchmark()` --uses--> `PreprocessingEngine`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/preprocessing.py
- `run_benchmark()` --uses--> `SyntheticGenerator`  [INFERRED]
  scripts/run_complexity_benchmark.py → backend/core/synthetic_generator.py
- `run_benchmark()` --uses--> `DatasetManager`  [INFERRED]
  scripts/run_t061_benchmark.py → backend/core/dataset.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Breast Cancer QML Benchmarking Literature** — docs_research_log_mpofu_2025, docs_research_log_kundu_2025, docs_research_log_pushpanjali_2025, wdbc_dataset [EXTRACTED 0.90]
- **QML Theoretical Foundations and Challenges** — docs_research_log_havlicek_2019, docs_research_log_cerezo_2021, docs_research_log_gupta_2025 [EXTRACTED 0.95]
- **Scientific Integrity Framework** — docs_claims_ledger, docs_experiment_protocol, decisions [EXTRACTED 1.00]

## Communities (66 total, 4 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.05
Nodes (50): ComplexityProfiler, ndarray, Computes observable statistical descriptors of a dataset. These are purely…, ExperimentConfig, CVExperimentRunner, Dataset, DatasetManager, Manages loading and validation of datasets. (+42 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (64): 10. Classical Baseline, 11. Quantum Baseline, 12. WDBC Experimental Results, 13. Quantum Ablation Strategy, 14. Complexity Profiler, 15. Planned System Architecture, 16. Planned Platform Modules, 17. Evidence-Driven Quantum Routing (+56 more)

### Community 2 - "Community 2"
Cohesion: 0.06
Nodes (56): Active Task, Blocked Tasks, Session Handoff (Next Agent Instructions), SIH 26139 — Hybrid QML Platform, Deferred / Future Work, MILESTONE 04: Quantum Suitability & Complexity Benchmarking, Phase 0 — Workspace & Infrastructure, Phase 10 — Quality & Documentation (+48 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (45): 10. Explainability Strategy, 11. Software Architecture, 12. Demo Flow, 13. Research Evidence, 14. Known Limitations, 15. Open Questions, 16. Unsupported Claims — Must NOT Make, 17. Implementation Roadmap (+37 more)

### Community 4 - "Community 4"
Cohesion: 0.06
Nodes (31): PennyLaneVQC, ndarray, A Variational Quantum Classifier (VQC) using PennyLane. Implements a standard…, circuit(), patch, test_benchmark_runner(), test_sanity_check_mocked(), test_vqc_bce_loss() (+23 more)

### Community 5 - "Community 5"
Cohesion: 0.05
Nodes (38): 10. Verdict Logic, 11. Experiment Flow Diagram, 12. Dataset Provenance Decision, 13. FAIR COMPARISON & SELECTION BIAS RULE, 1. Dataset, 2. Preprocessing Pipeline, 3. Data Split, 4. Reproducibility Parameters (+30 more)

### Community 6 - "Community 6"
Cohesion: 0.08
Nodes (37): 11. Quantum Feature Encoding, 12. Variational Quantum Circuit, 15. Explainability, 17. MVP, 18. Ideal Demo Flow, 1. Problem Statement and Requirements, 20. Risks and Mitigations, 21. Research Positioning (+29 more)

### Community 7 - "Community 7"
Cohesion: 0.08
Nodes (36): 11. Quantum Feature Encoding, 12. Variational Quantum Circuit, 15. Explainability, 17. MVP, 18. Ideal Demo Flow, 19. Feasibility, 1. Problem Statement and Requirements, 20. Risks and Mitigations (+28 more)

### Community 8 - "Community 8"
Cohesion: 0.06
Nodes (29): ENGINEER AGENT PROTOCOL, EVALUATOR AGENT PROTOCOL, EXPERIMENTALIST AGENT PROTOCOL, JUDGE AGENT PROTOCOL, RESEARCHER AGENT PROTOCOL, Demo, Experiments, Research (+21 more)

### Community 9 - "Community 9"
Cohesion: 0.11
Nodes (30): Category 1 — Environment and Infrastructure, Category 2 — Quantum Framework, Category 3 — Quantum Circuit Design, Category 4 — Experimental Design, Category 5 — Explainability, Category 6 — Strategic Questions, Priority Levels, Q1.1 — Python 3.14 Package Compatibility (+22 more)

### Community 10 - "Community 10"
Cohesion: 0.11
Nodes (26): Approved Language Examples, CLAIM_002: Classical Baselines are Extremely Strong on WDBC, CLAIM_003: VQC Core Engine is Functional, CLAIM_004: VQC Performance and Advantage (FIREWALL), CLAIM_005: Untuned VQC Underperforms Strong Classical Baselines, CLAIM_006: Optimized VQC Underperforms Classical ML on WDBC, CLAIM_007: VQC Dimensionality Trade-off (Barren Plateaus), CLAIM_008: Dataset-Dependent Hybrid Quantum Performance (+18 more)

### Community 11 - "Community 11"
Cohesion: 0.08
Nodes (25): Backend, Classical ML Stack, Compatibility Concerns Summary, Complete Recommended Requirements, Dependencies (via `uv`), Deployment, Docker (installed), Environment Management Strategy: `uv` (+17 more)

### Community 12 - "Community 12"
Cohesion: 0.14
Nodes (24): 1. Demo Flow (11 Steps), 2. Judge Q&A Preparation, 3. What Must Be True Before Demo Day, 4. Demo Script (2-Minute Version), Core Principle, Q: "Can this system be used for actual cancer diagnosis?", Q: "Can you scale this to larger datasets?", Q: "How do you ensure the comparison is fair?" (+16 more)

### Community 13 - "Community 13"
Cohesion: 0.12
Nodes (18): 1. Regime Table & Dataset Statistics, 2. Classical Results (Mean ROC-AUC), 3. VQC Results & Variability (Mean ROC-AUC across 3 seeds), 4. Runtime Comparison, 5. Observations, 6. Alternative Explanations, 7. Limitations, 8. Conclusion & Limitations (+10 more)

### Community 14 - "Community 14"
Cohesion: 0.17
Nodes (15): Add new dependency, Check health, Environment Quick Reference, Handoff Template, Last Session Handoff — YYYY-MM-DD, Run full experiment (from backend/), Run tests, SESSION END CHECKLIST (+7 more)

### Community 15 - "Community 15"
Cohesion: 0.24
Nodes (14): 1. Read the operating system, 2. Set up environment, 3. Check health, 4. Run tests, Core Architecture (Proposed), Directory Structure, Disclaimer, Ensure uv is installed, then run: (+6 more)

### Community 16 - "Community 16"
Cohesion: 0.29
Nodes (12): 10. Risks of Scientific Leakage / Biased Evaluation, 11. Exact Next Implementation Milestone, 1. Current Architecture, 2. Current Experiments, 3. Current Authoritative Results, 4. Current Scientific Claims, 5. Current Limitations, 6. What Must Remain Unchanged (+4 more)

### Community 17 - "Community 17"
Cohesion: 0.15
Nodes (13): 0–30 minutes, 115–140 minutes, 140–165 minutes, 165–180 minutes, 27. Three-Hour Execution Plan, 30–75 minutes, 75–115 minutes, Build / revise Slides 1–3 (+5 more)

### Community 18 - "Community 18"
Cohesion: 0.15
Nodes (13): 0–30 minutes, 115–140 minutes, 140–165 minutes, 165–180 minutes, 27. Three-Hour Execution Plan, 30–75 minutes, 75–115 minutes, Build / revise Slides 1–3 (+5 more)

### Community 19 - "Community 19"
Cohesion: 0.17
Nodes (12): 0. Project Identity (30-second brief), 0. STRATEGIC OBJECTIVE & WINNING FILTER, 1. Mandatory Session Protocol, 2. Task Lifecycle State Machine, 3. Git Commit Convention, 4. Directory Layout, 5. Specialized Agent Invocation, 6. Critical Scientific Rules (Non-Negotiable) (+4 more)

### Community 20 - "Community 20"
Cohesion: 0.32
Nodes (11): 10. What remains unresolved?, 1. Does VQC outperform SVM on WDBC?, 2. Does VQC approach classical performance?, 3. Which variables affect VQC performance?, 4. Does increased circuit depth help?, 5. Does increased qubit count help?, 6. Does BCE improve training compared with MSE?, 7. What is the computational cost? (+3 more)

### Community 21 - "Community 21"
Cohesion: 0.18
Nodes (11): 14. Evaluation Metrics, Accuracy, Computational efficiency, Confusion matrix, F1-score, Generalization, Precision, Primary metrics (+3 more)

### Community 22 - "Community 22"
Cohesion: 0.18
Nodes (11): 14. Evaluation Metrics, Accuracy, Computational efficiency, Confusion matrix, F1-score, Generalization, Precision, Primary metrics (+3 more)

### Community 23 - "Community 23"
Cohesion: 0.38
Nodes (9): 1. Dimensionality Reduction, 2. Feature Encoding (Quantum Data Loader), 3. Ansatz (Parameterized Variational Circuit), 4. Measurement & Classification, 5. Training Protocol, Architecture, Common Interface Integration, Research Objective (+1 more)

### Community 24 - "Community 24"
Cohesion: 0.42
Nodes (8): Objective, Quantum Ablation Protocol, Selection Rule, Stage A: PCA / Qubit Dimension, Stage B: Circuit Depth, Stage C: Loss Function, Stage D: Training Budget, Stage E: Classical Comparison

### Community 25 - "Community 25"
Cohesion: 0.22
Nodes (9): 13. Experimental Design, Fair comparison rules, Rule 1: Same data, Rule 2: Same split, Rule 3: Same preprocessing, Rule 4: No leakage, Rule 5: Record configurations, Rule 6: Multiple seeds (+1 more)

### Community 26 - "Community 26"
Cohesion: 0.22
Nodes (9): 13. Experimental Design, Fair comparison rules, Rule 1: Same data, Rule 2: Same split, Rule 3: Same preprocessing, Rule 4: No leakage, Rule 5: Record configurations, Rule 6: Multiple seeds (+1 more)

### Community 27 - "Community 27"
Cohesion: 0.46
Nodes (7): Advantages of PennyLane, Alternative Considered: Qiskit, Evidence, Framework: PennyLane, Limitations, Quantum Stack Decision, Why Selected

### Community 28 - "Community 28"
Cohesion: 0.25
Nodes (8): 16. Software Architecture, Architectural separation, Backend, Classical ML, Deployment, Explainability, Proposed stack, Quantum

### Community 29 - "Community 29"
Cohesion: 0.25
Nodes (8): 23. PPT Source of Truth, Constraints, Mitigations, Roadmap, Slide 1 — Team Details & Problem Statement, Slide 2 — Proposed Solution, Slide 3 — Technical Approach, Slide 4 — Feasibility & Viability

### Community 30 - "Community 30"
Cohesion: 0.25
Nodes (8): 16. Software Architecture, Architectural separation, Backend, Classical ML, Deployment, Explainability, Proposed stack, Quantum

### Community 31 - "Community 31"
Cohesion: 0.25
Nodes (8): 23. PPT Source of Truth, Constraints, Mitigations, Roadmap, Slide 1 — Team Details & Problem Statement, Slide 2 — Proposed Solution, Slide 3 — Technical Approach, Slide 4 — Feasibility & Viability

### Community 32 - "Community 32"
Cohesion: 0.52
Nodes (6): 1. Environment Specifications, 2. Dataset & Preprocessing, 3. VQC Architecture, 4. Training Hyperparameters, 5. Noise and Hardware (Future Variables), Canonical Quantum Baseline Configuration

### Community 33 - "Community 33"
Cohesion: 0.33
Nodes (6): 24. Slide 5 — Impact & Benefits, Clinicians, Healthcare AI teams, Measurable outcomes, Patients, Researchers

### Community 34 - "Community 34"
Cohesion: 0.33
Nodes (6): 25. Slide 6 — Research & References, Cerezo et al. 2021, Core references, Gupta et al. 2025, Havlíček et al. 2019, WDBC Dataset

### Community 35 - "Community 35"
Cohesion: 0.33
Nodes (6): 5. Classical Baseline Architecture, Baseline models, Optional QSVM / Quantum Kernel, Random Forest, SVM, XGBoost

### Community 36 - "Community 36"
Cohesion: 0.33
Nodes (6): 24. Slide 5 — Impact & Benefits, Clinicians, Healthcare AI teams, Measurable outcomes, Patients, Researchers

### Community 37 - "Community 37"
Cohesion: 0.33
Nodes (6): 25. Slide 6 — Research & References, Cerezo et al. 2021, Core references, Gupta et al. 2025, Havlíček et al. 2019, WDBC Dataset

### Community 38 - "Community 38"
Cohesion: 0.33
Nodes (6): 5. Classical Baseline Architecture, Baseline models, Optional QSVM / Quantum Kernel, Random Forest, SVM, XGBoost

### Community 39 - "Community 39"
Cohesion: 0.60
Nodes (5): fail(), header(), pass(), health_check.sh script, warn()

### Community 40 - "Community 40"
Cohesion: 0.40
Nodes (5): Cerezo et al. 2021, Gupta et al. 2025, Havlíček et al. 2019, Variational Quantum Classifier (VQC), ZZFeatureMap

### Community 41 - "Community 41"
Cohesion: 0.40
Nodes (5): 10. Dimensionality Reduction, Candidate methods, Feature selection, PCA, Working approach

### Community 42 - "Community 42"
Cohesion: 0.40
Nodes (5): 10. Dimensionality Reduction, Candidate methods, Feature selection, PCA, Working approach

### Community 43 - "Community 43"
Cohesion: 0.40
Nodes (4): Environment, GPU Quantum Simulation Infrastructure Benchmark, Realistic Workload Configuration, Results

### Community 44 - "Community 44"
Cohesion: 0.50
Nodes (4): Kundu, Muhuri & Kumar 2025, Mpofu & Mthunzi-Kufa 2025, Prajapati et al. 2025, WDBC Dataset

### Community 45 - "Community 45"
Cohesion: 0.50
Nodes (4): 0. Purpose of This Document, Evidence rule, Research & Working Specification, SIH 2026 — PS 26139

### Community 46 - "Community 46"
Cohesion: 0.50
Nodes (4): 8. Proposed Quantum Component, Candidate approach, Candidate pipeline, Proposed operating range

### Community 47 - "Community 47"
Cohesion: 0.50
Nodes (4): 0. Purpose of This Document, Evidence rule, Research & Working Specification, SIH 2026 — PS 26139

### Community 48 - "Community 48"
Cohesion: 0.50
Nodes (4): 8. Proposed Quantum Component, Candidate approach, Candidate pipeline, Proposed operating range

### Community 49 - "Community 49"
Cohesion: 0.67
Nodes (3): 3. Pilot Dataset: WDBC, Dataset specification, Important limitation

### Community 50 - "Community 50"
Cohesion: 0.67
Nodes (3): 4. Proposed System Architecture, Expanded architecture, Primary pipeline

### Community 51 - "Community 51"
Cohesion: 0.67
Nodes (3): 19. Feasibility, Proposed feasibility constraints, Why the MVP is feasible

### Community 52 - "Community 52"
Cohesion: 0.67
Nodes (3): 2. Core Thesis, Do not sell quantum advantage. Build a platform that can test it., Working research hypothesis

## Knowledge Gaps
- **215 isolated node(s):** `12. Demo Flow`, `14. Known Limitations`, `15. Open Questions`, `16. Unsupported Claims — Must NOT Make`, `18. Persistent Project Knowledge (Current State)` (+210 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 253 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Team Chai.EXE · Barak Valley Engineering College` connect `Community 10` to `Community 9`, `Community 12`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `SIH 26139 · Hybrid QML Platform` connect `Community 2` to `Community 13`, `Community 14`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `T-061: Real PS-Relevant Biomedical Complexity Benchmark` connect `Community 2` to `Community 13`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **Are the 6 inferred relationships involving `DatasetManager` (e.g. with `CVExperimentRunner` and `ExperimentRunner`) actually correct?**
  _`DatasetManager` has 6 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `ExperimentRunner` (e.g. with `ExperimentConfig` and `DatasetManager`) actually correct?**
  _`ExperimentRunner` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `12. Demo Flow`, `14. Known Limitations`, `15. Open Questions` to the rest of the system?**
  _215 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.05322128851540616 - nodes in this community are weakly interconnected._