# SESSION_PROTOCOL.md — Session Start/End Checklist
## SIH 26139 · Hybrid QML Platform

> Copy and follow this checklist at the start and end of every work session.  
> A fresh agent must be able to continue from the end-of-session record without asking for context.

---

## SESSION START CHECKLIST

```
TIME: ________________
AGENT SESSION ID: ________________

ORIENTATION (mandatory reads):
[ ] Read AGENTS.md
[ ] Read PROJECT_STATE.md
[ ] Read TASKS.md — identify highest-priority PLANNED task
[ ] Read DECISIONS.md — check for relevant settled choices
[ ] git status — check for uncommitted changes
[ ] git log --oneline -10 — recent context
[ ] scripts/health_check.sh — environment healthy?

TASK SELECTION:
[ ] Selected task: _________________ (from TASKS.md)
[ ] Dependencies verified as VERIFIED: _________________
[ ] Task marked as IMPLEMENTING in TASKS.md

SPECIFIC CONTEXT (fill in):
[ ] Active module being worked on: _________________
[ ] Key file(s) being modified: _________________
[ ] Known issues to be aware of: _________________
```

---

## SESSION END CHECKLIST

```
TIME: ________________

WHAT WAS DONE:
(describe in 3-5 bullet points)
- 
- 
- 

WHAT WAS VERIFIED:
(list tasks that reached VERIFIED status with evidence)
- Task: ___ — Evidence: ___
- 

WHAT FAILED:
(list any failed attempts, errors encountered, and how they were resolved)
- 

EXPERIMENTS RUN:
(list any experiments, even if they failed — required for EXPERIMENT_LOG.md)
- 

WHAT REMAINS:
(list incomplete items for the next session)
- 

NEXT RECOMMENDED ACTION:
(specific: "Run T-020 DatasetManager implementation")
_________________

STATE UPDATES MADE:
[ ] PROJECT_STATE.md updated (active task, latest result, next action)
[ ] TASKS.md updated (status changes)
[ ] DECISIONS.md updated (if new decisions made): YES / NO
[ ] EXPERIMENT_LOG.md updated (if experiments ran): YES / NO
[ ] docs/ files updated (if architecture changed): YES / NO

GIT:
[ ] git add -A
[ ] git commit -m "<type>(<scope>): <description>"
[ ] git log --oneline -3 (verify commit recorded)

WORKSPACE STATE: RECOVERABLE / BROKEN (describe if broken)
```

---

## Handoff Template

At end of session, append to PROJECT_STATE.md under "Last Session Handoff":

```markdown
## Last Session Handoff — YYYY-MM-DD

**What was done:**
- Item 1
- Item 2

**What was verified (with evidence):**
- Task T-XXX: [evidence type + file/test reference]

**What failed:**
- Item (with diagnosis)

**What remains:**
- Item 1

**Next recommended action:**
T-XXX: <specific action>

**Experiments run this session:**
- EXP-NNN: [status] — see EXPERIMENT_LOG.md

**Broken state (if any):**
None / Description
```

---

## Environment Quick Reference

```bash
# Activate environment
source .venv/bin/activate

# Check health
./scripts/health_check.sh

# Run tests
pytest backend/tests/ -v

# Start API (development)
uvicorn backend.api.main:app --reload --port 8000

# Start frontend (development)
cd frontend && npm run dev

# Run full experiment (from backend/)
python -m backend.core.experiment_runner experiments/configs/exp_NNN.json

# Git checkpoint
git add -A && git commit -m "type(scope): description"
```

---

## Task ID Quick Reference

| Phase | ID Range | Topic |
|---|---|---|
| Infrastructure | T-000–T-001 | Workspace, git, README |
| Environment | T-010–T-012 | Python, backend, frontend skeletons |
| Data & Preprocessing | T-020–T-021 | DatasetManager, PreprocessingEngine |
| Classical ML | T-030–T-032 | ClassicalModelEngine, EvaluationEngine, first experiment |
| Quantum ML | T-040–T-042 | QuantumEngine, PennyLane VQC, VQC experiment |
| Explainability | T-050–T-051 | SHAP classical + VQC attribution |
| Runner + Store | T-060–T-061 | ExperimentRunner, ResultsStore |
| API | T-070 | FastAPI |
| Frontend | T-080–T-084 | React dashboard |
| Integration | T-090–T-092 | Docker, demo, cache |
| Quality | T-100–T-103 | Tests, multi-seed, QSVM fallback |
| Future | F-001–F-006 | Post-MVP |
