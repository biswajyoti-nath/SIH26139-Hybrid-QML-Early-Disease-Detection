import numpy as np
from sklearn.datasets import load_breast_cancer
from dataclasses import dataclass

@dataclass
class Dataset:
    X: np.ndarray
    y: np.ndarray
    feature_names: list[str]
    target_names: list[str]
    provenance: str

class DatasetManager:
    """
    Manages loading and validation of the WDBC dataset.
    """
    
    @staticmethod
    def load_wdbc() -> Dataset:
        """
        Loads the WDBC dataset from sklearn, validates it against expected schema,
        and standardizes the target encoding so that Malignant = 1, Benign = 0.
        
        Provenance: sklearn.datasets.load_breast_cancer -> UCI ML Repository.
        """
        # Load raw data
        data = load_breast_cancer()
        X = data.data
        y = data.target  # By default in sklearn: 0 = malignant, 1 = benign
        feature_names = list(data.feature_names)
        target_names = list(data.target_names)
        
        # sklearn's breast cancer dataset encodes malignant as 0 and benign as 1.
        # We MUST ensure Malignant = 1 (positive class for clinical detection).
        if target_names[0] == 'malignant' and target_names[1] == 'benign':
            y = 1 - y  # Flip so malignant is 1, benign is 0
            target_names = ['benign', 'malignant'] # Now 0 is benign, 1 is malignant
            
        # Validation checks
        assert X.shape[0] == 569, f"Expected 569 samples, got {X.shape[0]}"
        assert X.shape[1] == 30, f"Expected 30 features, got {X.shape[1]}"
        assert not np.isnan(X).any(), "Dataset contains missing values in X"
        assert not np.isnan(y).any(), "Dataset contains missing values in y"
        
        unique_targets = np.unique(y)
        assert set(unique_targets) == {0, 1}, f"Targets must be binary {0, 1}, got {unique_targets}"
        
        return Dataset(
            X=X,
            y=y,
            feature_names=feature_names,
            target_names=target_names,
            provenance="sklearn.datasets.load_breast_cancer (UCI WDBC)"
        )
