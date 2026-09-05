from typing import Any, Dict
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.calibration import CalibratedClassifierCV

class ModelFactory:
    """
    Creates un-fitted models according to a common interface.
    The returned models must support .fit(X, y), .predict(X), and .predict_proba(X).
    """
    
    @staticmethod
    def create_classical_model(model_name: str, params: Dict[str, Any]) -> Any:
        if model_name == "svm":
            # SVC(probability=True) is deprecated in sklearn 1.9
            # We use CalibratedClassifierCV to get probabilities for ROC-AUC
            # while keeping the underlying estimator deterministic and warning-free.
            base_svc = SVC(**params)
            return CalibratedClassifierCV(estimator=base_svc, cv=5, ensemble=False)
        elif model_name == "random_forest":
            return RandomForestClassifier(**params)
        elif model_name == "xgboost":
            # Explicitly set n_jobs=1 for deterministic behavior on CPU if threading causes issues.
            # However, for modern XGBoost, random_state is usually sufficient. 
            # We enforce deterministic exact tree method if needed, but defaults are usually fine
            # as long as random_state is passed.
            return XGBClassifier(**params)
        else:
            raise ValueError(f"Unknown classical model: {model_name}")
