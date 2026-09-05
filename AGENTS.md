# AGENTS.md — Agentic Development Operating System
## SIH 26139 · Hybrid QML Platform for Early Disease Detection
### Team Chai.EXE · Barak Valley Engineering College · Egreen Quanta

> This file is the **permanent instruction manual** for every agent session working on this repository.  
> A fresh agent must read this file FIRST, then follow the session protocol exactly.  
> Do NOT rely on conversation history. The repository IS the persistent memory.

---

## 0. Project Identity (30-second brief)

- **Problem:** SIH 2026 PS 26139 — Hybrid Quantum ML Platform for Early Disease Detection.
- **Core claim we make:** We are building a platform that can *test* whether quantum ML adds value over classical ML — not one that *assumes* it does.
- **Pilot dataset:** WDBC (569 samples, 30 features, binary: benign/malignant).
- **Central hypothesis:** Can a hybrid QML platform discover WHEN a quantum pathway is scientifically justified for biomedical prediction?
- **Core Outcome:** The platform should be capable of concluding whether quantum is useful, not useful, inconclusive, or if classical ML is preferable.
- **Scientific anchor:** Gupta et al. 2025 (npj Dig. Med.) reviewed 4,915 QML papers and found *no consistent evidence* of QML advantage in digital health. Our rigorous benchmarking is itself the contribution.
- **What we must NEVER claim:** quantum speedup, early detection, clinical validation, fabricated metrics.

**Read these next:**
1. `PROJECT_STATE.md` — current phase, active task, next action
2. `TASKS.md` — prioritized task list with statuses
3. `docs/PROJECT_KNOWLEDGE.md` — full technical knowledge model
4. `docs/EXPERIMENT_PROTOCOL.md` — non-negotiable experimental rules
5. `docs/CLAIMS_LEDGER.md` — what may and may not be claimed

---

## 1. Mandatory Session Protocol

Every agent session MUST follow this sequence:

```
START OF SESSION
│
├─ 1. Read AGENTS.md (this file) ─────────────── orientation
├─ 2. Read PROJECT_STATE.md ──────────────────── current status
├─ 3. Read TASKS.md ──────────────────────────── task queue
├─ 4. Read DECISIONS.md ──────────────────────── settled choices
├─ 5. git status ─────────────────────────────── untracked/uncommitted work
├─ 6. git log --oneline -10 ──────────────────── recent commits
├─ 7. Identify highest-priority PLANNED task ─── what to work on
├─ 8. Verify environment health ──────────────── scripts/health_check.sh
│
├─ WORK LOOP
│   ├─ Mark task IMPLEMENTING in TASKS.md
│   ├─ Do ONE coherent task
│   ├─ Test the result (unit + integration)
│   ├─ Evaluate against agents/EVALUATOR.md criteria
│   ├─ Update docs if architecture changed
│   └─ Mark task VERIFIED or return to IMPLEMENTING
│
└─ END OF SESSION
    ├─ Update PROJECT_STATE.md
    ├─ Update TASKS.md (statuses)
    ├─ Update DECISIONS.md if decisions were made
    ├─ Update EXPERIMENT_LOG.md if experiments ran
    ├─ git add -A && git commit -m "<type>(<scope>): <description>"
    └─ Leave workspace in recoverable state
```

**Non-negotiable rules:**
- NEVER assume previous conversation context exists.
- NEVER skip the session-start reads.
- NEVER mark a task VERIFIED without evidence.
- NEVER make a claim that isn't in VERIFIED FACT or OUR EXPERIMENT categories.
- NEVER fabricate experimental numbers.
- NEVER redo work that is already committed.

---

## 2. Task Lifecycle State Machine

```
DISCOVERED ──► PLANNED ──► IMPLEMENTING ──► IMPLEMENTED ──► TESTING ──► VERIFIED ──► ACCEPTED
                                │                                           │
                                │                                           ▼
                                └────────────────────────────────────── FAILED (log and diagnose)
```

**VERIFIED requires evidence, not just code:**

| Task type | Evidence required for VERIFIED |
|---|---|
| Software module | Implementation exists + imports cleanly + unit tests pass + integration works |
| Experiment | Protocol followed + config recorded + results file exists + metrics stored |
| Research claim | Source identified + claim checked + evidence recorded + limitations noted |
| Bug fix | Failing test added → test now passes |

---

## 3. Git Commit Convention

```
<type>(<scope>): <description>

Types: feat, fix, test, docs, refactor, chore, experiment
Scopes: dataset, preproc, classical, quantum, eval, explain, api, ui, infra, docs, agents
```

Examples:
```
feat(dataset): implement WDBC DatasetManager with validation
feat(preproc): add leakage-safe PreprocessingEngine (scaler + PCA)
feat(classical): add SVM, RF, XGBoost ClassicalModelEngine
test(classical): verify all classical baselines on WDBC
feat(quantum): add PennyLane VQC QuantumModelEngine
experiment(vqc): first WDBC benchmark — seed=42, n_qubits=8, n_layers=3
feat(eval): add EvaluationEngine (all 8 metrics + verdict)
feat(api): add FastAPI experiment endpoints
feat(ui): add React dashboard with comparison table
docs(research): verify QML literature claims via Tavily
```

**Never commit:** API keys, .env files, large binary files (>.5MB), generated/cached data, __pycache__, node_modules, .venv.

---

## 4. Directory Layout

```
core-program/
│
├── AGENTS.md                   ← YOU ARE HERE. Read first every session.
├── PROJECT_STATE.md            ← Current phase, active task, next action
├── TASKS.md                    ← Full task list with priorities and statuses
├── DECISIONS.md                ← Architecture/research decisions log
├── EXPERIMENT_LOG.md           ← Record of every experiment run
│
├── agents/                     ← Specialized agent protocols
│   ├── EVALUATOR.md            ← Challenge implementation completeness
│   ├── RESEARCHER.md           ← Literature research protocol
│   ├── ENGINEER.md             ← Coding agent rules
│   ├── EXPERIMENTALIST.md      ← Experiment execution protocol
│   ├── JUDGE.md                ← Hostile SIH evaluator simulation
│   └── SESSION_PROTOCOL.md     ← Session start/end checklist
│
├── docs/                       ← Research + architecture (READ-MOSTLY)
│   ├── PROJECT_KNOWLEDGE.md    ← Full knowledge model (17 sections)
│   ├── RESEARCH_LOG.md         ← Literature verification log
│   ├── CLAIMS_LEDGER.md        ← Claims classification (A-E)
│   ├── TECH_STACK.md           ← Package versions + compatibility
│   ├── EXPERIMENT_PROTOCOL.md  ← Non-negotiable experimental rules
│   ├── SOFTWARE_ARCHITECTURE.md← Module specs and data flow
│   ├── DEMO_SPECIFICATION.md   ← 11-step demo + judge Q&A
│   ├── OPEN_QUESTIONS.md       ← Unresolved decisions
│   ├── SIH_26139_Research_Work_Document.md  ← Primary project spec
│   └── SIH_26139_ULTRA_DETAILED_ACTION_PLAN.md ← Execution plan
│
├── experiments/                ← Experiment artifacts
│   ├── configs/                ← Experiment configuration JSON files
│   ├── results/                ← Experiment result JSON files
│   ├── logs/                   ← Training logs
│   └── artifacts/              ← Saved models, plots
│
├── scripts/                    ← Utility scripts
│   └── health_check.sh         ← Quick environment health check
│
├── backend/                    ← [NOT YET CREATED] FastAPI + ML core
├── frontend/                   ← [NOT YET CREATED] React dashboard
│
├── .gitignore
└── README.md
```

---

## 5. Specialized Agent Invocation

Invoke specialized agents only when their perspective adds real value.

| Agent | When to invoke |
|---|---|
| `EVALUATOR` | After any significant implementation — before marking VERIFIED |
| `RESEARCHER` | When a literature claim needs checking or a new paper is referenced |
| `ENGINEER` | Default for all coding tasks |
| `EXPERIMENTALIST` | When designing or running an ML/QML experiment |
| `JUDGE` | Before demo, before any public claim, before major milestone |

The typical workflow is:
```
PRIMARY AGENT → ONE TASK → TEST → EVALUATOR → (pass) → COMMIT → NEXT TASK
                                              → (fail) → FIX → RE-TEST
```

---

## 6. Critical Scientific Rules (Non-Negotiable)

**SCIENTIFIC LANGUAGE RULES:**
Replace strong causal language with evidence-based wording. E.g., BAD: '8 qubits degraded performance because of barren plateaus.' GOOD: '8 qubits produced lower performance under this configuration. Possible explanations include trainability effects.'


These rules are permanent regardless of what phase we are in:

1. **Data leakage is a bug.** StandardScaler and PCA must be fitted on train data only.
2. **Same conditions for all models.** Same split, same seed, same preprocessing.
3. **Record before you run.** Experiment config must be saved before training starts.
4. **Never overwrite results.** Every experiment run creates a new timestamped file.
5. **Published numbers ≠ our results.** Never present Havlíček/Cerezo/any cited paper's numbers as our results.
6. **Quantum simulator ≠ speedup.** Never claim quantum is faster based on simulator results.
7. **WDBC ≠ early detection.** WDBC is a diagnostic benchmark. Never call it an early-detection dataset.
8. **VQC training is slow.** Pre-train and cache results for demo day.
9. **UI must show real results.** VerdictPanel must show quantum losing if it lost.
10. **No fabrication.** If the experiment hasn't run, the number doesn't exist.

---

## 7. Environment Rules

- **Use Python 3.12** (managed by `uv`).
- **Use `uv`** as the canonical package and environment manager.
- **Do not use pip directly.** Do not commit `.venv`.
- Install dependencies: `uv add <package>` (or `uv add --dev <package>`).
- Sync environment: `uv sync`
- Run project scripts: `uv run <script>` (e.g., `uv run pytest`, `uv run uvicorn backend.api.main:app`).
- Check environment: `uv run scripts/health_check.sh`
- The environment is reproducible via `pyproject.toml` and `uv.lock`.
