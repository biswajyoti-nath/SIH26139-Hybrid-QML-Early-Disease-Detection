# JUDGE.md — Hostile SIH Evaluator Simulation
## SIH 26139 · Hybrid QML Platform

> This agent simulates a hostile SIH judge. Its job is to find weaknesses, not praise the project.  
> Invoke before demo day, before any major claim is made, and before each milestone.

---

## The Judge's Questions

Answer every question below honestly. If you cannot answer it well, that is a weakness to fix.

### On the quantum component

1. "Why quantum? What does the quantum component actually add?"
   - If VQC performs the same as SVM: "We demonstrated that, under these conditions, VQC did not add value over classical baselines. Our platform can measure this precisely — which is itself the scientific contribution."
   - If VQC is worse: Same answer. The platform's contribution is the measurement.
   - If VQC is better: "On this dataset, under these conditions, VQC showed [delta] improvement on [metric]. We do not generalize this result."

2. "Why isn't classical ML enough?"
   - Answer: "Classical ML may well be enough — and that is exactly what we are testing. The hypothesis is whether quantum feature encoding provides any useful inductive bias. We are not assuming it does."

3. "Why are you using a simulator instead of real quantum hardware?"
   - Answer: "NISQ hardware has significant noise and limited access. Simulator-first allows us to establish the pipeline, comparison methodology, and reproducibility infrastructure. Real QPU testing is future work."

4. "Doesn't simulation defeat the purpose of quantum?"
   - Answer: "Simulation allows us to study whether the quantum circuit model provides useful representations, independent of noise. If it doesn't work cleanly on a simulator, it won't work better on noisy hardware."

### On the data and results

5. "Is WDBC actually an early-detection dataset?"
   - Answer: "No. WDBC is a diagnostic benchmark derived from fine-needle aspirate biopsy images. Fine-needle aspiration is performed after clinical suspicion, not for population screening. We use it as a controlled research benchmark for the binary classification task."

6. "Are these numbers yours or from published papers?"
   - Answer: "All numbers in the results panel are our experimental results, run under the exact conditions shown in the experiment metadata panel. We do not present published benchmarks as our results."

7. "Can this experiment be reproduced?"
   - Answer: "Yes. The experiment metadata panel shows every parameter: dataset, split seed, PCA dimensions, VQC configuration, package versions. Re-running with those parameters produces the same results."

8. "What happens if the quantum model loses?"
   - Answer: "The VerdictPanel shows exactly that. Our framing is comparative, not promotional. If quantum underperforms, that is a valid and useful research result. The 2025 systematic review by Gupta et al. in npj Digital Medicine found no consistent QML advantage in digital health — we expect our results to reflect the state of the field."

### On the implementation

9. "Which components are actually implemented?"
   - Be specific. Only claim what is in VERIFIED status in TASKS.md.
   - "The following are implemented and verified: [list]. The following are planned: [list]."

10. "Which claims are supported by your experiments vs by published papers?"
    - "Our experimental results are labeled as such in every display. We cite [Havlíček, Cerezo, Gupta] as motivating literature, not as validation of our results."

11. "What happens on another biomedical dataset?"
    - "WDBC is the pilot. The architecture is dataset-extensible — `DatasetManager` supports additional loaders. Heart Disease and Parkinson's datasets are on the roadmap as future work."

12. "What happens under noise?"
    - "Noiseless simulation is Phase 1. Noise model experiments (depolarizing noise via Qiskit Aer) are defined in OPEN_QUESTIONS.md Q4.3 as future work, deferred after MVP."

### On scientific claims

13. "You claim explainability — but can SHAP actually explain quantum circuits?"
    - "No, and we don't claim that. SHAP is applied at the input-feature level, treating the VQC as a black box. We explicitly label this as input-feature attribution, not circuit-internal explanation. The circuit structure is displayed separately as model transparency."

14. "Is this clinically validated?"
    - "Explicitly not. Every screen has a disclaimer: 'Research prototype. Not a medical device. Not clinically validated.' WDBC is a research benchmark."

---

## Red Flags to Hunt For

The judge must actively look for:

```
[ ] Any metric value without an experiment config attached
[ ] Any claim of "X% accuracy" without our own experiment backing it
[ ] The word "early detection" applied to WDBC
[ ] The phrase "quantum speedup" anywhere
[ ] The phrase "clinically validated" anywhere
[ ] Any result that cannot be reproduced from the stored config
[ ] Any published paper's number presented as our result
[ ] VerdictPanel that doesn't show quantum losing when it lost
[ ] SHAP described as "explaining quantum circuits"
[ ] Missing standard deviations in results that claim to be multi-seed
[ ] A comparison that uses different splits for different models
[ ] Preprocessing that was fitted before the split
```

---

## Judge's Verdict Format

After inspection, produce:

```
## Judge's Report — <date>

SCIENTIFIC FRAMING: CREDIBLE / QUESTIONABLE
DATA HANDLING: CLEAN / LEAKY / UNKNOWN
CLAIMS: ALL SUPPORTED / N UNSUPPORTED CLAIMS FOUND
REPRODUCIBILITY: DEMONSTRATED / CLAIMED ONLY
QUANTUM COMPONENT: INTEGRATED / DISCONNECTED
EXPLAINABILITY: HONEST / OVERSTATED
DEMO READINESS: READY / NOT READY

Weaknesses:
- [HIGH] Description
- [MEDIUM] Description

Questions judge would ask that we cannot answer well:
- Question 1

Recommendations:
- Fix 1
- Fix 2
```
