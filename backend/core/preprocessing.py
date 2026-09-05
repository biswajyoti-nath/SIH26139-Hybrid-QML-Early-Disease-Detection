import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from typing import Tuple, Optional, Any

@dataclass
class PreprocessingResult:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    pipeline: Pipeline

class PreprocessingEngine:
    """
    Leakage-safe preprocessing engine.
    Ensures all transformations are fitted ONLY on the training data via sklearn Pipeline.
    """
    
    @staticmethod
    def build_pipeline(n_pca_components: Optional[int] = None, random_seed: int = 42) -> Pipeline:
        steps = [('scaler', StandardScaler())]
        if n_pca_components is not None:
            steps.append(('pca', PCA(n_components=n_pca_components, random_state=random_seed)))
        return Pipeline(steps)
    
    @staticmethod
    def run_pipeline(
        X: np.ndarray, 
        y: np.ndarray, 
        test_size: float = 0.2, 
        random_seed: int = 42,
        n_pca_components: Optional[int] = None
    ) -> PreprocessingResult:
        """
        Executes the full pipeline: Split -> Scale -> PCA.
        """
        # 1. Split (stratified)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=test_size, 
            random_state=random_seed, 
            stratify=y
        )
        
        # 2. Build & Fit Pipeline on train ONLY
        pipeline = PreprocessingEngine.build_pipeline(n_pca_components, random_seed)
        X_train_final = pipeline.fit_transform(X_train)
        X_test_final = pipeline.transform(X_test)
            
        return PreprocessingResult(
            X_train=X_train_final,
            X_test=X_test_final,
            y_train=y_train,
            y_test=y_test,
            pipeline=pipeline
        )
