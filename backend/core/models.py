from typing import Any, Dict
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

class ModelFactory:
    """
    Creates un-fitted models according to a common interface.
    The returned models must support .fit(X, y), .predict(X), and .predict_proba(X).
    """
    
    @staticmethod
    def create_classical_model(model_name: str, params: Dict[str, Any]) -> Any:
        if model_name == "svm":
            # Must set probability=True for ROC-AUC
            return SVC(probability=True, **params)
        elif model_name == "random_forest":
            return RandomForestClassifier(**params)
        elif model_name == "xgboost":
            return XGBClassifier(**params)
        else:
            raise ValueError(f"Unknown classical model: {model_name}")
