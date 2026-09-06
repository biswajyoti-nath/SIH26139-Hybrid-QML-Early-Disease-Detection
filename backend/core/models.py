from typing import Any, Dict
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.calibration import CalibratedClassifierCV
from backend.quantum.pennylane_vqc import PennyLaneVQC
from backend.quantum.pennylane_qsvm import PennyLaneQSVM

class ModelFactory:
    """
    Creates un-fitted models according to a common interface.
    The returned models must support .fit(X, y), .predict(X), and .predict_proba(X).
    """
    
    @staticmethod
    def create_classical_model(model_name: str, params: Dict[str, Any]) -> Any:
        base_name = model_name.split('_')[0] if '_' in model_name else model_name
        
        if base_name == "svm":
            base_svc = SVC(**params)
            return CalibratedClassifierCV(estimator=base_svc, cv=5, ensemble=False)
        elif base_name == "random" and model_name.startswith("random_forest"):
            return RandomForestClassifier(**params)
        elif base_name == "xgboost":
            return XGBClassifier(**params)
        elif base_name == "qsvm":
            return PennyLaneQSVM(**params)
        elif base_name == "vqc":
            return PennyLaneVQC(**params)
        else:
            raise ValueError(f"Unknown model: {model_name}")
