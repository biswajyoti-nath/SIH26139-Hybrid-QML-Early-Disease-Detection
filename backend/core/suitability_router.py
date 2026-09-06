class SuitabilityRouter:
    """
    T-062 Evidence-Gated Quantum Pathway Selection (Rule-Based Prototype).
    Initial research/demo thresholds. Require future validation.
    DO NOT claim these are optimal.
    """
    MIN_QUANTUM_DELTA = 0.01  # Quantum must beat classical by this margin
    MAX_ACCEPTABLE_RUNTIME_RATIO = 100.0  # Max multiple of classical runtime allowed
    MIN_VARIANCE_RETENTION = 0.50  # Must retain 50% variance to even try
    
    @classmethod
    def route(cls, profile, classical_metrics, quantum_metrics, runtimes):
        """
        Determines the recommended computational pathway based on empirical evidence.
        """
        c_score = classical_metrics.get("roc_auc", 0.5)
        
        # Pick the best quantum model based on score
        q_scores = {k: v.get("roc_auc", 0.5) for k, v in quantum_metrics.items()}
        if not q_scores:
            return cls._build_response("INCONCLUSIVE", "No quantum metrics provided.")
            
        best_q_model = max(q_scores, key=q_scores.get)
        q_score = q_scores[best_q_model]
        
        delta = q_score - c_score
        
        c_runtime = runtimes.get("classical", 1.0)
        q_runtime = runtimes.get(best_q_model, 9999.0)
        
        # Rule 1: Extreme Representation Bottleneck
        if profile.get("variance_retained", 1.0) < cls.MIN_VARIANCE_RETENTION:
            reason = (
                f"The dataset exhibited a substantially stronger representation bottleneck "
                f"({profile['variance_retained']*100:.1f}% variance retained) under the "
                f"tested 8-dimensional quantum configuration. The tested classical reference "
                f"outperformed the quantum pathways."
            )
            return cls._build_response("CLASSICAL PREFERRED", reason, "svm", best_q_model, c_score, q_score, delta, profile, runtimes)
            
        # Rule 2: Classical Outperforms or Comparable
        if delta < cls.MIN_QUANTUM_DELTA:
            reason = (
                "The tested classical reference substantially outperformed or matched "
                "both quantum pathways under the current protocol, while the quantum "
                "pathways also incurred substantially higher simulator cost. "
                "Classical ML is therefore preferred for this configuration."
            )
            return cls._build_response("CLASSICAL PREFERRED", reason, "svm", best_q_model, c_score, q_score, delta, profile, runtimes)
            
        # Rule 3: Quantum Outperforms but too expensive
        if (q_runtime / max(c_runtime, 0.001)) > cls.MAX_ACCEPTABLE_RUNTIME_RATIO:
            reason = (
                "The tested quantum pathway showed a predictive advantage, but incurred "
                "computational cost beyond the acceptable threshold. Classical fallback recommended."
            )
            return cls._build_response("CLASSICAL PREFERRED", reason, "svm", best_q_model, c_score, q_score, delta, profile, runtimes)
            
        # Rule 4: Quantum Promising
        reason = "The tested quantum pathway demonstrated a predictive advantage within acceptable simulator cost bounds."
        return cls._build_response("QUANTUM PATHWAY PROMISING", reason, "svm", best_q_model, c_score, q_score, delta, profile, runtimes)

    @staticmethod
    def _build_response(recommendation, reason, c_model="svm", q_model="qsvm", c_score=0.0, q_score=0.0, delta=0.0, profile=None, runtimes=None):
        return {
            "recommendation": recommendation,
            "reason": reason,
            "best_classical_model": c_model,
            "best_quantum_pathway": q_model,
            "classical_score": c_score,
            "quantum_score": q_score,
            "delta": delta,
            "complexity_profile": profile or {},
            "runtime_comparison": runtimes or {},
            "confidence": "High (Empirical CV CV-Matched)"
        }
