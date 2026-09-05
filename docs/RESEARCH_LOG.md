# RESEARCH_LOG.md
## SIH 26139 — Literature Verification Log
### Team Chai.EXE · Barak Valley Engineering College

> **Last Updated:** 2026-09-05  
> **Purpose:** Record every external claim, its source, what it actually establishes, and its verification status.  
> **Methodology:** Tavily web search + direct DOI/URL verification against authoritative sources.

---

## Verification Status Codes

| Code | Meaning |
|---|---|
| VERIFIED | Confirmed from authoritative source (journal/conference/official repo) |
| PARTIALLY VERIFIED | Paper/claim exists but full text not accessed; details unconfirmed |
| UNVERIFIED | Cannot locate a verifiable source |
| CONTRADICTED | Evidence found that contradicts the claim |
| NOT RELEVANT | Source exists but does not support the specific claim made |

---

## Entry 1: Havlíček et al. 2019

**Claim in project documents:**  
"Havlíček et al. established a foundational supervised-learning approach using quantum-enhanced feature spaces and a variational quantum classifier."

**Source:**  
Havlíček, V., Córcoles, A. D., Temme, K., Harrow, A. W., Kandala, A., Chow, J. M., & Gambetta, J. M. (2019). Supervised learning with quantum-enhanced feature spaces. *Nature*, 567(7747), 209–212.

**DOI:** 10.1038/s41586-019-0980-2  
**arXiv:** 1804.11326  
**PubMed:** PMID 30867609

**Verification Method:** Tavily search + PubMed + arXiv + IDEAS/RePEC.

**What the source actually establishes:**
- Two approaches to supervised classification using quantum computers: quantum SVMs (QSVMs) with quantum kernels and a variational quantum classifier (VQC).
- Demonstrated that quantum circuits can generate classically intractable feature maps.
- The ZZFeatureMap was introduced in this work.
- Experiments were run on IBM real quantum hardware (2 qubits) and simulators.
- Cited 4,043 times (PubMed, as of search date).
- The paper does NOT demonstrate scalable quantum advantage over classical SVMs on general datasets.

**Relevance to our project:**
- Directly motivates QSVM and VQC as candidate quantum model choices.
- ZZFeatureMap from this paper is a candidate encoding for our implementation.
- Provides the theoretical grounding for quantum feature spaces.

**Limitations:**
- 2-qubit experiments; very small-scale.
- Quantum advantage shown on specially constructed datasets, not real biomedical datasets.
- 7 years old; the quantum ML landscape has evolved significantly.

**Verification Status:** **VERIFIED**

---

## Entry 2: Cerezo et al. 2021

**Claim in project documents:**  
"Cerezo et al. identify trainability, accuracy, and efficiency as important challenges for variational quantum algorithms."

**Source:**  
Cerezo, M., Arrasmith, A., Babbush, R., et al. (2021). Variational quantum algorithms. *Nature Reviews Physics*, 3(9), 625–644.

**DOI:** 10.1038/s42254-021-00348-9  
**Citations:** 3,727+ (Nature Reviews Physics)

**Verification Method:** Tavily search confirmed via Nature.com, ResearchGate, and multiple citing papers.

**What the source actually establishes:**
- Comprehensive review of variational quantum algorithms (VQAs) — the family of algorithms that includes VQC.
- Identifies three core challenges: **trainability** (barren plateaus), **accuracy**, and **efficiency**.
- Barren plateau problem: gradients of parameterized circuits vanish exponentially with qubit count, making training extremely difficult at scale.
- Describes the NISQ (Noisy Intermediate-Scale Quantum) context in which VQAs operate.
- Does NOT claim VQAs are superior to classical methods for practical tasks.

**Relevance to our project:**
- Directly justifies why we keep circuit depth shallow (3-5 layers) and qubit count small (5-10).
- The barren plateau challenge explains why VQC trainability is a known risk and must be monitored during experiments.
- Validates the hybrid quantum-classical pattern as the appropriate NISQ-era approach.

**Limitations:**
- Review paper — describes challenges, not solutions.
- The challenge of barren plateaus has not been fully resolved as of 2025.

**Verification Status:** **VERIFIED**

---

## Entry 3: Gupta et al. 2025

**Claim in project documents:**  
"A 2025 systematic review of QML for digital health found no consistent empirical trend supporting quantum utility over classical methods and highlighted weaknesses in many published comparisons."

**Source:**  
Gupta, R. S., Wood, C. E., Engstrom, T., Pole, J. D., & Shrapnel, S. (2025). A systematic review of quantum machine learning for digital health. *npj Digital Medicine*, 8, Article 237.

**DOI:** 10.1038/s41746-025-01597-z  
**Published:** 02 May 2025 (received 03 October 2024, accepted 29 March 2025)

**Verification Method:** Tavily search confirmed via Nature.com (official publisher), phys.org news article, UQ researcher profile, AIQRC newsletter.

**What the source actually establishes:**
- Systematic review of **4,915 papers** published 2015–2024.
- Only **16 papers** met final criteria for examining realistic operating environments (quantum hardware or noisy simulations).
- **Conclusion (exact, from phys.org): "Despite exponential growth in research claiming quantum benefits for health care, our analysis shows no consistent evidence that quantum algorithms outperform classical methods for clinical decision-making or health service delivery."**
- Performance differences showed **no consistent trend supporting empirical quantum utility** in digital health.
- Identified critical gaps in current research approaches.

**Relevance to our project:**
- This is the primary external justification for our core thesis: **rigorous benchmarking itself is the contribution**, not claiming quantum advantage.
- Directly supports our positioning: "We are building a platform to test whether quantum provides value, not to assume it does."
- The negative result of this review makes our honest comparative approach even more scientifically credible.

**Limitations:**
- Reflects the state of the field as of mid-2024 (review period).
- The authors remain optimistic about future quantum health applications.
- Does not apply to every possible dataset or problem class.

**Verification Status:** **VERIFIED**

---

## Entry 4: WDBC Dataset

**Claim in project documents:**  
"UCI lists: 569 instances, 30 real-valued features, Binary target: benign / malignant."

**Source:**  
Wolberg, W., Mangasarian, O., Street, N., & Street, W. (1993). Breast Cancer Wisconsin (Diagnostic). UCI Machine Learning Repository.

**DOI:** 10.24432/C5DW2B

**Verification Method:** Available directly in scikit-learn (`sklearn.datasets.load_breast_cancer`), UCI ML Repository page.

**What the source actually establishes:**
- Dataset: 569 instances, 30 features, binary target.
- Features computed from digitized FNA (fine-needle aspirate) images of breast masses.
- 357 benign (B), 212 malignant (M) — class ratio approximately 62.7% / 37.3%.
- 10 nuclear features computed per cell, 3 statistics (mean, SE, worst/largest) = 30 total features.
- No missing values in the standard version.
- Research/diagnostic benchmark — NOT a prospective early-detection study.

**Relevance to our project:**
- Pilot dataset for all experiments.
- Small enough for rapid quantum simulation experiments.
- Well-established benchmark that allows comparison of our results against published baselines.

**Limitations:**
- Single-institution, retrospective data.
- FNA is a diagnostic procedure, not a screening tool — calling this "early detection" is misleading.
- Does not generalize to other cancer types or imaging modalities.
- Class imbalance must be addressed in reporting (do not rely on accuracy alone).

**Verification Status:** **VERIFIED**

---

## Entry 5: Mpofu & Mthunzi-Kufa 2025

**Claim in project documents:**  
Listed as "Mpofu & Mthunzi-Kufa 2025" in the reference list, without specific claim.

**Source (found):**  
Mpofu, K., & Mthunzi-Kufa, P. (2025). Comparing artificial neural networks with variational quantum circuits for biomedical data classification. *MATEC Web of Conferences*, 417, 02001. EDP Sciences.

Additionally found:
- A preprint "Comparative Analysis of Classical and Quantum Machine Learning Algorithms in Breast Cancer Classification" (EuropePMC, PPR1188463).
- "Challenges and opportunities in quantum machine learning" (ResearchGate, September 2022) — different paper.

**Verification Method:** Tavily search (ResearchGate, IntechOpen, EuropePMC, SPIE).

**What the source actually establishes:**
- Compares ANNs vs VQCs for biomedical data classification (reported to use Wisconsin Breast Cancer Diagnostic dataset).
- Published in MATEC Web of Conferences (a conference proceedings venue).
- Uses WDBC as the test dataset — directly relevant to our setup.
- Low-impact venue; results should not be treated as high-confidence benchmarks.

**Relevance to our project:**
- Provides a precedent for our comparative approach (classical vs quantum on WDBC).
- We should cite this as "motivating our comparative approach" but NOT use any numerical results as our benchmark.

**Limitations:**
- Conference proceedings, not peer-reviewed journal.
- Full text not verified; reported methodology and results not confirmed.
- We cannot reproduce their specific experimental conditions without the full paper.

**Verification Status:** **PARTIALLY VERIFIED**  
*(Paper and authors confirmed to exist; full results and methodology not verified)*

---

## Entry 6: Kundu, Muhuri & Kumar 2025

**Claim in project documents:**  
"Kundu et al. 2025" listed in the reference list without specific claim.

**Source (found):**  
Kundu, A., Muhuri, S., & Kumar, R. (2025). Harnessing quantum-classical techniques for improved breast cancer prediction. In *Proceedings of IEEE QCNC 2025* (IEEE International Conference on Quantum Computing and Networking Communications).

Also found:  
Kundu, A., et al. (2025). A Quantum-Enhanced Model for Accurate Breast Cancer Classification and Early Diagnosis. (ResearchGate publication, published July 18, 2025.)

**Verification Method:** Tavily search (xlescience.org, ResearchGate, Semantic Scholar).

**What the source actually establishes:**
- Studies quantum-classical hybrid techniques for breast cancer prediction/classification.
- Uses WDBC (Wisconsin Breast Cancer Diagnostic) as the benchmark.
- IEEE QCNC is a legitimate IEEE conference.

**Relevance to our project:**
- Directly comparable research: quantum-classical methods + WDBC.
- Motivates our research direction.
- We should cite as "related work motivating our experimental approach," not use their specific numbers.

**Limitations:**
- Conference paper (not journal); full methodology and reproducibility details unknown.
- "Improved breast cancer prediction" — we cannot assess the strength of this claim without the full text.
- Numbers from this paper must NOT be cited as our experimental results.

**Verification Status:** **PARTIALLY VERIFIED**  
*(Paper confirmed to exist via multiple sources; full text and results not independently verified)*

---

## Entry 7: Prajapati et al. "2025"

**Claim in project documents:**  
"Prajapati et al. 2025" listed in reference list.

**Source (found):**  
Prajapati, J. B., Paliwal, H., Prajapati, B. G., Saikia, S., & Pandey, R. Quantum machine learning in prediction of breast cancer. In *Quantum Computing: A Shift from Bits to Qubits*. Springer, Singapore (2023), pp. 351–382.

**Verification Method:** Tavily search (MDPI Algorithms journal citing it as a 2023 Springer book chapter).

**What the source actually establishes:**
- Book chapter on QML for breast cancer prediction.
- Published as part of a 2023 Springer edited volume, NOT a 2025 paper.

**Relevance to our project:**
- Provides QML-for-breast-cancer context.
- The 2025 date in the project documents appears to be an error.

**Limitations:**
- **Publication year discrepancy** — project documents list 2025 but the source appears to be a 2023 Springer book chapter.
- Book chapters have less rigorous peer review than journal papers.
- Full content not independently verified.

**Verification Status:** **UNVERIFIED as a 2025 paper**  
*(Appears to be a 2023 Springer book chapter listed with wrong year; do not cite as a 2025 primary source until verified)*

> ⚠️ **ACTION REQUIRED:** Verify the exact publication year of this reference before citing it.

---

## Entry 8: Pushpanjali & Adisesha 2025

**Claim in project documents:**  
"Pushpanjali & Adisesha 2025" listed in reference list.

**Source (found):**  
Pushpanjali, P., & Adisesha, K. (2025). The Future of Breast Cancer Diagnosis: Benchmarking Quantum Machine Learning Models against Classical Techniques. *International Journal of Science and Applied Technology (IJSAT)*, 16(3) (July–September 2025).

**Verification Method:** Tavily search confirmed via IJSAT publication archive and ResearchGate.

**What the source actually establishes:**
- Benchmark comparison of quantum and classical ML for breast cancer diagnosis.
- Published in IJSAT — a lower-impact open-access journal.
- Directly comparable topic to our project.

**Relevance to our project:**
- Supports our comparative approach.
- We should cite as "related work" only.
- Do NOT use any numbers from this paper as our experimental results.

**Limitations:**
- IJSAT is not a high-impact indexed journal; results should be treated cautiously.
- Full text and methodology not independently verified.
- "Future of Breast Cancer Diagnosis" — title implies a stronger claim than is likely supportable.

**Verification Status:** **PARTIALLY VERIFIED**  
*(Paper exists; venue and topic confirmed; results and methodology not verified)*

---

## Entry 9: Sammartino 2026

**Claim in project documents:**  
"Sammartino 2026" listed in reference list.

**Source:** No verifiable publication found.

**Verification Method:** Tavily search returned no results for this reference.

**What the source actually establishes:** Unknown.

**Relevance to our project:** Unknown.

**Limitations:** Cannot assess relevance without identifying the source.

**Verification Status:** **UNVERIFIED**

> ⚠️ **ACTION REQUIRED:** Locate the full citation for Sammartino 2026 before including it in any submission. If not verifiable, remove from reference list.

---

## Summary Table

| Reference | Status | Safe to Cite? |
|---|---|---|
| Havlíček et al. 2019 | VERIFIED | Yes — for quantum feature maps and VQC motivation |
| Cerezo et al. 2021 | VERIFIED | Yes — for VQA challenges and hybrid architecture justification |
| Gupta et al. 2025 | VERIFIED | Yes — for systematic review findings; core justification for our approach |
| WDBC Dataset | VERIFIED | Yes — for dataset statistics |
| Mpofu & Mthunzi-Kufa 2025 | PARTIALLY VERIFIED | Yes, as related work; not for specific numbers |
| Kundu, Muhuri & Kumar 2025 | PARTIALLY VERIFIED | Yes, as related work; not for specific numbers |
| Prajapati et al. "2025" | UNVERIFIED as 2025 | ⚠️ Verify year before citing; appears to be 2023 |
| Pushpanjali & Adisesha 2025 | PARTIALLY VERIFIED | Cautiously, as related work only |
| Sammartino 2026 | UNVERIFIED | ❌ Do NOT cite until source is found |
