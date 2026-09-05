# SIH Judge Q&A: Quantum Machine Learning Validity

**Q: Why quantum?**
A: SIH PS 26139 explicitly requests a "Hybrid Quantum Machine Learning Platform." Our objective is not to retroactively justify quantum, but to rigorously test whether adding a Variational Quantum Circuit (VQC) to a classical pipeline actually provides value over optimized classical baselines. 

**Q: Why WDBC?**
A: The Wisconsin Diagnostic Breast Cancer (WDBC) dataset is the gold standard for tabular binary classification in oncology. It is mathematically well-understood, entirely reproducible, and allows us to test the information bottleneck of quantum feature encoding without confounding variables.

**Q: What does quantum actually add?**
A: In our current ablation study, it adds nothing to predictive power. It acts as an expensive non-linear kernel. By mapping data into a high-dimensional Hilbert space via `AngleEmbedding`, we hypothesized better separability. However, the experiments prove that for structured tabular data, classical SVMs resolve the hyperplanes far more efficiently.

**Q: Why did VQC perform worse?**
A: The VQC achieved ~62% ROC-AUC versus SVM's ~99%. This is caused by the *expressivity vs. trainability* trade-off (barren plateaus). We proved this experimentally: 8 qubits performed worse than 6 qubits. The continuous nature of tabular data is difficult to encode efficiently in NISQ-era gates compared to native classical float representations.

**Q: Did you tune fairly?**
A: Yes. We utilized a strict 20% holdout for an ablation study across dimensionality, depth, loss functions, and iterations. The winning configuration was then subjected to the exact same 5-fold stratified cross-validation split as the classical models. No data leaked. 

**Q: Are you cherry-picking?**
A: No. We are publishing the negative result. The VQC is 37% worse.

**Q: Where is the quantum advantage?**
A: There is none on this dataset. Claiming quantum advantage for a 569-sample tabular dataset via a statevector simulator would be scientific fraud. Our contribution is the rigorous framework that *proves* the lack of advantage, which is highly valuable to the MedTech community currently flooded with unverified QML hype.

**Q: Why should I believe your result?**
A: The experiment is entirely reproducible. The preprocessing pipeline mathematically prevents leakage, the data splits are seeded, and the quantum gradients are tracked transparently. 

**Q: Could the classical model simply be better for this data?**
A: Yes. WDBC is linearly separable (as shown by linear SVM hitting 99% ROC-AUC). A complex quantum neural network is the wrong tool for linearly separable tabular data.

**Q: The simulator is not a quantum computer. What exactly have you demonstrated?**
A: We demonstrated that even in a theoretically perfect, noiseless environment (statevector simulation), standard VQC architectures struggle to match classical solvers. Running on noisy real hardware would only degrade these results further.

**Q: The problem statement asks for hybrid QML. Where is the hybrid component?**
A: The architecture is genuinely hybrid. The classical CPU executes StandardScaler and PCA, extracting the principal components. These components are then injected as parameters into the VQC, which is optimized via classical Adam descent using gradients computed via the quantum parameter-shift rule.
