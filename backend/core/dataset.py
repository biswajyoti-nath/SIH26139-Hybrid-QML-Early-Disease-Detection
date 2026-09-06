import numpy as np
from sklearn.datasets import load_breast_cancer
from dataclasses import dataclass
from typing import Optional
import openml

@dataclass
class Dataset:
    X: np.ndarray
    y: np.ndarray
    feature_names: list[str]
    target_names: list[str]
    provenance: str
    groups: Optional[np.ndarray] = None

class DatasetManager:
    """
    Manages loading and validation of datasets.
    """
    
    @staticmethod
    def load_wdbc() -> Dataset:
        """
        Loads the WDBC dataset from sklearn.
        """
        data = load_breast_cancer()
        X = data.data
        y = data.target  # 0 = malignant, 1 = benign
        feature_names = list(data.feature_names)
        target_names = list(data.target_names)
        
        if target_names[0] == 'malignant' and target_names[1] == 'benign':
            y = 1 - y  # Flip so malignant is 1, benign is 0
            target_names = ['benign', 'malignant']
            
        assert X.shape[0] == 569
        assert X.shape[1] == 30
        assert not np.isnan(X).any()
        assert not np.isnan(y).any()
        unique_targets = np.unique(y)
        assert set(unique_targets) == {0, 1}
        
        return Dataset(
            X=X, y=y,
            feature_names=feature_names,
            target_names=target_names,
            provenance="sklearn.datasets.load_breast_cancer (UCI WDBC)",
            groups=None
        )

    @staticmethod
    def load_parkinsons() -> Dataset:
        """
        Loads the UCI Parkinson's Disease Classification dataset (ID 42176 on OpenML).
        """
        dataset = openml.datasets.get_dataset(42176)
        X_df, y_series, _, attribute_names = dataset.get_data(
            dataset_format='dataframe', 
            target=dataset.default_target_attribute
        )
        
        X = X_df.to_numpy()
        y_raw = y_series.to_numpy()
        
        # Targets are 1 (PD) and 0 (Healthy)
        y = np.array([1 if str(val) == '1' else 0 for val in y_raw])
        
        assert X.shape[0] == 756, f"Expected 756 samples, got {X.shape[0]}"
        assert X.shape[1] == 753, f"Expected 753 predictive features, got {X.shape[1]}"
        assert not np.isnan(X).any(), "Dataset contains missing values in X"
        assert not np.isnan(y).any(), "Dataset contains missing values in y"
        unique_targets = np.unique(y)
        assert set(unique_targets) == {0, 1}, f"Targets must be binary {0, 1}, got {unique_targets}"
        
        # Group generation based on provenance (Sakar 2018): 252 subjects, 3 consecutive recordings each
        groups = np.repeat(np.arange(252), 3)
        
        # Validate grouping assumption
        unique_groups, counts = np.unique(groups, return_counts=True)
        assert len(unique_groups) == 252, f"Expected 252 groups, got {len(unique_groups)}"
        assert all(c == 3 for c in counts), "Groups do not have exactly 3 recordings"
        assert len(groups) == X.shape[0], "Group length does not match sample count"
        
        # Verify target consistency within groups
        for g in unique_groups:
            idx = np.where(groups == g)[0]
            if len(np.unique(y[idx])) > 1:
                raise ValueError(f"Patient {g} has inconsistent targets across recordings")

        return Dataset(
            X=X, y=y,
            feature_names=list(X_df.columns),
            target_names=['Healthy', 'Parkinsons'],
            provenance="OpenML 42176 (Sakar 2018: 756 instances, 753 predictive features, binary classification)",
            groups=groups
        )
