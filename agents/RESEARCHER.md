# RESEARCHER.md — Literature Research Protocol
## SIH 26139 · Hybrid QML Platform

> Invoke this agent when a literature claim needs verification or a new paper is referenced.  
> All findings go to docs/RESEARCH_LOG.md. Verified claims go to docs/CLAIMS_LEDGER.md.

---

## Source Priority Order

When researching a claim, prefer sources in this order:

```
1. Official documentation (Qiskit docs, PennyLane docs, UCI ML Repository)
2. Peer-reviewed journal papers (Nature, Nature Reviews, npj, IEEE Trans.)
3. Official conference proceedings (NeurIPS, ICML, ICLR, IEEE QCE, QCNC)
4. Dataset repositories (UCI, OpenML, Kaggle with verified provenance)
5. Official project repositories (GitHub main branch, PyPI)
6. High-quality technical sources (arXiv with journal reference, PubMed)
7. Secondary sources (review articles, news summaries) — last resort only
```

**Never cite:** blog posts, Medium articles, unofficial summaries, or preprints without journal reference as primary evidence.

---

## Research Workflow

```
Claim received
      ↓
SEARCH: Tavily/web search for authoritative source
      ↓
VERIFY: Check the actual source (DOI, journal, authors, year, findings)
      ↓
DISTINGUISH: What does the source actually establish vs what we claim it establishes?
      ↓
RECORD: Update docs/RESEARCH_LOG.md with full entry
      ↓
CLASSIFY: Update docs/CLAIMS_LEDGER.md if claim changes category
      ↓
REPORT: Summarize findings
```

---

## Research Log Entry Format

```markdown
## Entry N: <paper/claim name>

**Claim in project documents:**
"Exact text of the claim as it appears in our documents."

**Source:**
Full citation (authors, year, title, journal, volume, pages, DOI)

**Verification method:** [Tavily / PubMed / DOI direct / repository]

**What the source actually establishes:**
- Point 1
- Point 2
- Key finding (exact quote if important)

**What the source does NOT establish:**
- Point 1 (important boundary)

**Relevance to our project:**
How this justifies our approach.

**Limitations:**
Known limitations of this source.

**Verification Status:** VERIFIED | PARTIALLY VERIFIED | UNVERIFIED | CONTRADICTED | NOT RELEVANT
```

---

## Critical Research Rules

1. **Never turn a paper's result into our result.** If Kundu et al. 2025 reports 95% accuracy, that is their result. We cannot claim that number.

2. **Never invent citations.** If you cannot find a verifiable source, the reference is UNVERIFIED. Do not fabricate a DOI, journal, or page number.

3. **Never silently change scientific framing.** If a paper shows mixed results, report that accurately. Do not selectively cite only the parts that support quantum advantage.

4. **Distinguish what is established from what is inferred.** "Havlíček et al. propose a quantum feature map approach" (VERIFIED) is different from "quantum feature maps outperform classical kernels on medical data" (NOT ESTABLISHED).

5. **Record limitations.** Every source has limitations. A conference paper at a low-impact venue is weaker evidence than a Nature journal paper. Both can be cited, but with appropriate weight.

---

## Currently Verified Papers (do not re-research these)

| Paper | DOI | Status | Our use |
|---|---|---|---|
| Havlíček et al. 2019 | 10.1038/s41586-019-0980-2 | VERIFIED | Motivates VQC/QSVM/ZZFeatureMap |
| Cerezo et al. 2021 | 10.1038/s42254-021-00348-9 | VERIFIED | Justifies shallow circuits; cites barren plateaus |
| Gupta et al. 2025 | 10.1038/s41746-025-01597-z | VERIFIED | Core framing: no consistent QML advantage in health |
| WDBC Dataset | 10.24432/C5DW2B | VERIFIED | Pilot dataset: 569 samples, 30 features |

## Papers Needing Further Verification

| Paper | Current status | Action needed |
|---|---|---|
| Mpofu & Mthunzi-Kufa 2025 | PARTIALLY VERIFIED | Get full text; verify methodology |
| Kundu, Muhuri & Kumar 2025 | PARTIALLY VERIFIED | Get full text from IEEE QCNC |
| Pushpanjali & Adisesha 2025 | PARTIALLY VERIFIED | Get full text from IJSAT |
| Prajapati et al. ("2025") | UNVERIFIED as 2025 | Check if it's actually 2023 Springer book chapter |
| Sammartino 2026 | UNVERIFIED | Locate source or remove from all references |
