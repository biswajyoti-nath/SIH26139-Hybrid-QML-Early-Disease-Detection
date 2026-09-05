# EVALUATOR.md — Implementation Evaluator Protocol
## SIH 26139 · Hybrid QML Platform

> Invoke this agent after any significant implementation work, before marking a task VERIFIED.  
> The evaluator's job is to find problems, not to validate effort.

---

## Invocation Rule

Run the evaluator after:
- Any new module is written
- Any experiment is run
- Any claim is added to documentation
- Any integration between modules is added

Do NOT skip the evaluator merely because "it looked right when I wrote it."

---

## Evaluation Checklist

### 1. FUNCTIONALITY

```
[ ] Does the code actually run without error?
[ ] Does `python -c "from <module> import <class>"` succeed?
[ ] Does the feature work end-to-end, not just in isolation?
[ ] Are edge cases handled? (empty data, wrong shapes, bad config)
[ ] Are errors informative rather than cryptic?
[ ] Does the module match its spec in docs/SOFTWARE_ARCHITECTURE.md?
```

### 2. RESEARCH INTEGRITY

```
[ ] Is preprocessing leakage-free?
      → StandardScaler fitted ONLY on X_train?
      → PCA fitted ONLY on X_train?
      → X_test transformed using train-fitted parameters only?
[ ] Are all models using the SAME train/test split?
[ ] Are all models using the SAME random seed?
[ ] Are all models evaluated on the SAME held-out test set?
[ ] Is the positive class consistent? (malignant=1 throughout)
[ ] Is runtime measured with perf_counter, not time.time (for precision)?
```

### 3. REPRODUCIBILITY

```
[ ] Is the random seed recorded before any model trains?
[ ] Does re-running the same config produce the same results?
[ ] Is the experiment config saved BEFORE training starts?
[ ] Does the results file contain ALL required metadata fields?
      → See EXPERIMENT_PROTOCOL.md §8 for required schema
[ ] Are package versions recorded?
[ ] Can a fresh environment reproduce the results from the metadata alone?
```

### 4. SCIENTIFIC VALIDITY

```
[ ] Are published benchmark numbers separated from our results?
[ ] Is the sensitivity/specificity computed on the malignant (positive) class?
[ ] Is the ROC-AUC computed using predicted probabilities (not hard labels)?
[ ] Is the VerdictPanel honest? (not engineered to show quantum winning)
[ ] Is the SHAP disclaimer present for VQC explanations?
[ ] Is WDBC described as a research benchmark, NOT an early-detection dataset?
```

### 5. CLAIMS INTEGRITY

```
[ ] Does any output, log, or UI text contain a Category E claim? (see CLAIMS_LEDGER.md)
[ ] Is any metric presented without specifying experimental conditions?
[ ] Is any number from a cited paper presented as our result?
[ ] Does any text imply clinical validation or QPU testing that didn't happen?
[ ] Is "simulator execution" described as "quantum speedup"?
```

### 6. SIH ALIGNMENT

```
[ ] Does this implementation still address PS 26139?
[ ] Is the hybrid quantum-classical architecture maintained?
[ ] Does the implementation support fair classical vs quantum comparison?
[ ] Are explainability features progressing?
[ ] Are limitations honestly documented?
```

### 7. CODE QUALITY

```
[ ] Are there any hardcoded magic numbers that should be config parameters?
[ ] Are there any `except: pass` style silent error swallowers?
[ ] Are there any `global` variables that could cause test interference?
[ ] Are file paths constructed portably (pathlib, not string concatenation)?
[ ] Are temporary/debug prints removed or converted to proper logging?
```

---

## Evaluation Outcomes

### PASS
All critical checks pass. Mark task VERIFIED. Commit.

### CONDITIONAL PASS
Minor issues found that don't affect scientific validity. Document issues in TASKS.md as polish tasks (P3). Mark task VERIFIED with caveat. Commit.

### FAIL — BLOCK
Critical issue found:
- Data leakage detected
- Results not reproducible
- Category E claim present
- Module doesn't match architectural spec
- Results file missing required fields

→ Mark task IMPLEMENTING (revert). Fix the issue. Re-evaluate.

---

## Failure Response Protocol

```
IMPLEMENTATION (VERIFIED attempt)
        ↓
EVALUATION (this protocol)
        ↓
FAILURE detected
        ↓
Diagnose: what exactly is wrong?
        ↓
Make the SMALLEST change that fixes it
        ↓
Re-run the specific failing check
        ↓
Re-run full evaluation checklist
        ↓
If PASS: commit
If FAIL: diagnose again (do not guess repeatedly)
```

**Do NOT:** rewrite the module to solve a localized problem.  
**Do NOT:** mark VERIFIED while a known failure is unresolved.  
**Do NOT:** remove a failing test to make CI pass.

---

## Output Format

After evaluation, produce a brief structured report:

```
## Evaluation Report — <Task ID> — <date>

FUNCTIONALITY: PASS / FAIL
RESEARCH INTEGRITY: PASS / FAIL
REPRODUCIBILITY: PASS / FAIL
SCIENTIFIC VALIDITY: PASS / FAIL
CLAIMS INTEGRITY: PASS / FAIL
SIH ALIGNMENT: PASS / FAIL

Overall: PASS / CONDITIONAL PASS / FAIL — BLOCK

Issues found:
- [CRITICAL] Description
- [MINOR] Description

Recommended action: <specific fix or "commit">
```
