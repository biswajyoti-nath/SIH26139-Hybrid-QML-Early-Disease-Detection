from typing import Any, Dict
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.calibration import CalibratedClassifierCV
from backend.quantum.pennylane_vqc import PennyLaneVQC

class ModelFactory:
    """
    Creates un-fitted models according to a common interface.
    The returned models must support .fit(X, y), .predict(X), and .predict_proba(X).
    """
    
    @staticmethod
    def create_classical_model(model_name: str, params: Dict[str, Any]) -> Any:
        if model_name == "svm":
            base_svc = SVC(**params)
            return CalibratedClassifierCV(estimator=base_svc, cv=5, ensemble=False)
        elif model_name == "random_forest":
            return RandomForestClassifier(**params)
        elif model_name == "xgboost":
            return XGBClassifier(**params)
        elif model_name == "vqc":
            return PennyLaneVQC(**params)
        else:
            raise ValueError(f"Unknown model: {model_name}")
