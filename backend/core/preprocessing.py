import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class PreprocessingResult:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    scaler: StandardScaler
    pca: Optional[PCA]

class PreprocessingEngine:
    """
    Leakage-safe preprocessing engine.
    Ensures all transformations are fitted ONLY on the training data.
    """
    
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
        
        # 2. Scale (fit on train ONLY)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # 3. PCA (fit on train ONLY)
        pca = None
        if n_pca_components is not None:
            pca = PCA(n_components=n_pca_components, random_state=random_seed)
            X_train_final = pca.fit_transform(X_train_scaled)
            X_test_final = pca.transform(X_test_scaled)
        else:
            X_train_final = X_train_scaled
            X_test_final = X_test_scaled
            
        return PreprocessingResult(
            X_train=X_train_final,
            X_test=X_test_final,
            y_train=y_train,
            y_test=y_test,
            scaler=scaler,
            pca=pca
        )
