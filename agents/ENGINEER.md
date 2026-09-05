# ENGINEER.md — Coding Agent Protocol
## SIH 26139 · Hybrid QML Platform

> This is the default role for implementation sessions.  
> Read AGENTS.md and PROJECT_STATE.md first. Then follow this protocol.

---

## Before Touching Any Code

```
[ ] Read AGENTS.md (already done this session)
[ ] Read PROJECT_STATE.md (already done this session)
[ ] Identify the single task to work on from TASKS.md
[ ] Inspect existing files in the target module (do not assume they're empty)
[ ] Read the module spec in docs/SOFTWARE_ARCHITECTURE.md
[ ] Check DECISIONS.md for any relevant settled choices
[ ] Verify environment: scripts/health_check.sh
```

**If you skip the inspect step and overwrite working code, that is a bug you introduced.**

---

## Implementation Rules

### Make Small, Testable Changes

- One module at a time.
- One function at a time when possible.
- Test after each logical unit is complete.
- Do NOT write 500 lines and then test.

### Prefer Existing Architecture

- Do NOT redesign the architecture to solve a localized problem.
- If `docs/SOFTWARE_ARCHITECTURE.md` specifies a module interface, implement exactly that interface.
- If you need to deviate, record it in DECISIONS.md first.

### No Unnecessary Dependencies

- Use stdlib when sufficient.
- Do NOT add a new package to `requirements.txt` without documenting why in DECISIONS.md.
- Check that the new package is compatible with Python 3.12 and other installed packages.

### Loose Coupling

- Each module should be independently importable.
- `backend/core/` modules should NOT import from `backend/api/`.
- The quantum layer (backend/quantum/) is swappable — never hard-code the framework in core/.
- Tests should mock heavy dependencies (quantum circuits, SHAP computation) when testing logic.

### Reproducibility Always

- All random operations must be seeded.
- Seed is passed as a parameter, not set globally in module scope.
- See EXPERIMENT_PROTOCOL.md §4 for the full seeding policy.

---

## When Blocked

```
1. DIAGNOSE: Read the exact error message carefully. Do not skip the traceback.
2. INSPECT: Check the actual state of the relevant file/module.
3. SEARCH: Look in official documentation for the API being used.
      → PennyLane: https://docs.pennylane.ai
      → Qiskit: https://docs.quantum.ibm.com
      → sklearn: https://scikit-learn.org/stable/api
      → FastAPI: https://fastapi.tiangolo.com
4. MAKE THE SMALLEST CHANGE: Do not rewrite the module to solve a misplaced import.
5. TEST AGAIN: Confirm the specific issue is resolved.
6. If still blocked after 3 iterations: document the blocker in TASKS.md and move to another task.
```

**Do NOT:** guess repeatedly with different random approaches. Read the docs.

---

## File and Path Conventions

```python
from pathlib import Path

# Use pathlib, not string concatenation
EXPERIMENTS_DIR = Path(__file__).parent.parent.parent / "experiments"
CONFIG_DIR = EXPERIMENTS_DIR / "configs"
RESULTS_DIR = EXPERIMENTS_DIR / "results"

# Never use hardcoded absolute paths in committed code
```

---

## Error Handling Policy

```python
# Informative errors with context
class PreprocessingNotFittedError(RuntimeError):
    """Raised when PreprocessingEngine.transform() called before fit()."""
    pass

class DatasetValidationError(ValueError):
    """Raised when dataset fails schema validation."""
    pass

# Do NOT use bare except
# Do NOT use except: pass (silent swallowing)
# DO use specific exception types
# DO include context in error messages
```

---

## After Implementation

```
[ ] Run unit tests for the changed module
[ ] Run integration test (if module integrates with another)
[ ] Run scripts/health_check.sh
[ ] Apply EVALUATOR.md checklist
[ ] Update TASKS.md status
[ ] If architecture changed: update docs/SOFTWARE_ARCHITECTURE.md
[ ] Commit: git add -A && git commit -m "<type>(<scope>): <description>"
[ ] Update PROJECT_STATE.md
```

---

## Module Implementation Order

Follow the dependency order in TASKS.md:

```
T-010 (env) → T-011 (backend skeleton)
            → T-020 (DatasetManager)
            → T-021 (PreprocessingEngine)
            → T-030 (ClassicalModelEngine)
            → T-031 (EvaluationEngine)
            → T-032 (first experiment)
            → T-040 (QuantumEngine ABC)
            → T-041 (PennyLane VQC)
            → T-042 (VQC experiment)
            → T-050, T-051 (Explainability)
            → T-060, T-061 (Runner + Store)
            → T-070 (FastAPI)
            → T-080–T-084 (Frontend)
            → T-090–T-092 (Integration + Demo)
```

A task should not begin until all its listed dependencies are in VERIFIED state.
