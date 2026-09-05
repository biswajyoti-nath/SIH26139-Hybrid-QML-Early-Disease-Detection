# PROJECT_STATE.md
## SIH 26139 — Hybrid QML Platform for Early Disease Detection

> **Keep this file concise. A fresh agent must be able to read it in under 2 minutes.**  
> Update this file at the END of every work session.

---

## Current Phase

**Phase 0: Research Audit & Workspace Setup** ← ACTIVE  
(Phase 1: Environment + Classical Baseline is NEXT)

---

## Current Objective

Establish the agentic development workspace so future sessions can work autonomously and reproducibly. Research audit is complete.

---

## Completed Milestones

| Milestone | Date | Evidence |
|---|---|---|
| Research audit: read all project documents | 2026-09-05 | Session 1 |
| Literature verification via Tavily (9 papers) | 2026-09-05 | docs/RESEARCH_LOG.md |
| Environment inspection | 2026-09-05 | Python 3.14.4, Node 22, Docker 29 |
| docs/PROJECT_KNOWLEDGE.md created (17 sections) | 2026-09-05 | 413 lines |
| docs/RESEARCH_LOG.md created (9 entries) | 2026-09-05 | 321 lines |
| docs/CLAIMS_LEDGER.md created (5 categories) | 2026-09-05 | 175 lines |
| docs/TECH_STACK.md created | 2026-09-05 | 300 lines |
| docs/EXPERIMENT_PROTOCOL.md created | 2026-09-05 | 432 lines |
| docs/SOFTWARE_ARCHITECTURE.md created | 2026-09-05 | 506 lines |
| docs/DEMO_SPECIFICATION.md created | 2026-09-05 | 284 lines |
| docs/OPEN_QUESTIONS.md created | 2026-09-05 | 336 lines |
| Agentic workspace setup (AGENTS.md, agent files, etc.) | 2026-09-05 | This session |
| Git repository initialized | 2026-09-05 | git init |
| Initial commit (research docs) | 2026-09-05 | See git log |

---

## Active Task
 
**T-000: Agentic workspace setup** — ✅ ACCEPTED (this session)  
**T-001: .gitignore + README.md** — ✅ ACCEPTED (this session)  
**T-010: Python environment resolution (`uv` setup)** — ✅ ACCEPTED (this session)  
**Next active task: T-011 — Backend project skeleton**

---

## Blocked Tasks

| Task ID | Block reason | Unblocked by |
|---|---|---|
| T-010 (Environment setup) | Need to verify Python 3.14 quantum package compatibility | Manual action: `pip install pennylane` in Python 3.14, fallback to Python 3.12 |
| T-020 (DatasetManager) | Blocked by T-010 (environment must be healthy first) | T-010 verified |
| T-100 (VQC implementation) | Blocked by T-020, T-030, T-040 | Classical baseline must pass first |

---

## Latest Verified Result

**None yet.** No experiments have run. No code has been written. No models have been trained.

The latest verified artifacts are the documentation files in `docs/`.

---

## Known Problems / Risks

| Problem | Severity | Status |
|---|---|---|
| Python 3.14 may not be compatible with quantum packages | CRITICAL | UNRESOLVED — T-010 must address |
| Sammartino 2026 reference unverifiable | HIGH | Do not cite; remove from PPT if unresolved |
| Prajapati et al. year appears wrong (2023, not 2025) | HIGH | Verify before citing |
| VQC barren plateau risk | HIGH | Mitigated by shallow circuits; QSVM fallback ready |
| VQC training slow for demo | HIGH | Cache strategy defined in DEMO_SPECIFICATION.md |

---

## Next Recommended Action

**→ T-000-GIT: Create .gitignore and README.md, make initial commit.**  
**→ T-010: Resolve Python 3.12 vs 3.14 — create virtual environment.**

The very first implementation step is environment verification. See `TASKS.md`.

---

## Key Architecture Decisions Made

| Decision | Choice | Doc reference |
|---|---|---|
| Quantum framework | PennyLane (primary), Qiskit (secondary/fallback) | docs/TECH_STACK.md, DECISIONS.md |
| Python version | Python 3.12 (not 3.14) | docs/TECH_STACK.md |
| Pilot dataset | WDBC | docs/PROJECT_KNOWLEDGE.md §9 |
| VQC encoding (initial) | AngleEmbedding (Ry) | docs/OPEN_QUESTIONS.md Q3.1 |
| Ansatz (initial) | RealAmplitudes | docs/OPEN_QUESTIONS.md Q3.2 |
| Optimizer | Adam | docs/OPEN_QUESTIONS.md Q3.6 |
| Results storage | JSON files (MVP) | docs/OPEN_QUESTIONS.md Q1.3 |
| Backend | FastAPI + Uvicorn | docs/SOFTWARE_ARCHITECTURE.md |
| Frontend | React 18 + Vite + Tailwind | docs/SOFTWARE_ARCHITECTURE.md |

---

## Experimental Results Summary

| Experiment | Status | Best metric | File |
|---|---|---|---|
| (no experiments yet) | — | — | — |

---

## Last Session Handoff

**What was done:**
- Complete agentic workspace setup: AGENTS.md, PROJECT_STATE.md, TASKS.md, DECISIONS.md, EXPERIMENT_LOG.md.
- All 6 agent protocols: EVALUATOR.md, RESEARCHER.md, ENGINEER.md, EXPERIMENTALIST.md, JUDGE.md, SESSION_PROTOCOL.md.
- README.md, .gitignore, scripts/health_check.sh.
- experiments/ directory scaffold with gitkeep files.
- Git repository initialized; all 28 files committed (root commit cd2ddb9).
- Health check: 27 PASS, 5 WARN (expected), 0 FAIL.

**What was verified:**
- `bash scripts/health_check.sh` exits 0, 27 PASS, 0 FAIL.
- Git commit `cd2ddb9` recorded all 28 files.
- All mandatory docs exist and pass file-presence checks.

**What failed:** Nothing.

**What remains:** All implementation tasks (T-010 through T-103).

**Next recommended action:** T-010 — Python environment resolution.
- Try `pip install pennylane scikit-learn xgboost shap fastapi uvicorn` in Python 3.14.
- If quantum packages fail: `python3.12 -m venv .venv`.
- Install all packages; record versions in docs/TECH_STACK.md.
- Run `python -c "import pennylane; print(pennylane.__version__)"` to verify.
- Then proceed to T-011 (backend skeleton) and T-020 (DatasetManager).

