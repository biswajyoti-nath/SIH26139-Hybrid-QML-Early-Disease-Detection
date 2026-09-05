# SIH PS 26139: Knowledge Graph Root

This document serves as the structural root for the project's knowledge graph, mapping the conceptual components of our hybrid quantum machine learning platform.

## Research
- **Literature**: Managed via [RESEARCH_LOG.md](RESEARCH_LOG.md) and [RESEARCHER.md](../agents/RESEARCHER.md).
- **Dataset**: Pilot dataset (WDBC) details are in [PROJECT_KNOWLEDGE.md](PROJECT_KNOWLEDGE.md).
- **Hypotheses**: Core claims and boundaries are maintained in [CLAIMS_LEDGER.md](CLAIMS_LEDGER.md).

## Experiments
- **Classical**: Baseline implementations via [ClassicalModelEngine](SOFTWARE_ARCHITECTURE.md).
- **Quantum**: VQC implementations via [QuantumModelEngine](SOFTWARE_ARCHITECTURE.md) and [EXPERIMENTALIST.md](../agents/EXPERIMENTALIST.md).
- *Logging*: All experiment results are tracked in [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) and [EXPERIMENT_LOG.md](../EXPERIMENT_LOG.md).

## Software
- **Data**: Handled by `DatasetManager` (see [SOFTWARE_ARCHITECTURE.md](SOFTWARE_ARCHITECTURE.md)).
- **Preprocessing**: Handled by `PreprocessingEngine` (leakage-safe).
- **Models**: Both `ClassicalModelEngine` and `QuantumModelEngine`.
- **Evaluation**: Core metrics calculated by `EvaluationEngine`.
- **API**: FastAPI backend.
- **UI**: React dashboard.
- *Development*: Guided by [ENGINEER.md](../agents/ENGINEER.md) and [EVALUATOR.md](../agents/EVALUATOR.md).

## Demo
- **Experiment**: Live execution and cached results.
- **Results**: Honest metric comparison.
- **Presentation**: Defined in [DEMO_SPECIFICATION.md](DEMO_SPECIFICATION.md) and guided by [JUDGE.md](../agents/JUDGE.md).
