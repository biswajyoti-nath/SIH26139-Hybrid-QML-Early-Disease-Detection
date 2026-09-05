import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

class ComplexityProfiler:
    """
    Computes observable statistical descriptors of a dataset.
    These are purely descriptive and do NOT yet define 'quantum suitability'.
    """
    
    @staticmethod
    def profile(X: np.ndarray, y: np.ndarray, random_state: int = 42) -> dict:
        n_samples, n_features = X.shape
        class_balance = float(np.mean(y == 1))
        
        # Feature correlation (mean absolute off-diagonal Pearson correlation)
        corr_matrix = np.corrcoef(X.T)
        if n_features > 1:
            np.fill_diagonal(corr_matrix, 0)
            mean_abs_corr = float(np.mean(np.abs(corr_matrix)))
        else:
            mean_abs_corr = 0.0
            
        # Linear Separability (Logistic Regression CV Accuracy)
        # If this is very high, the dataset has a simple linear boundary.
        lr = LogisticRegression(random_state=random_state, max_iter=1000)
        try:
            linear_separability = float(np.mean(cross_val_score(lr, X, y, cv=5, scoring='accuracy')))
        except Exception:
            linear_separability = 0.0
            
        return {
            "n_samples": n_samples,
            "n_features": n_features,
            "class_balance_pos_ratio": class_balance,
            "mean_abs_feature_correlation": mean_abs_corr,
            "linear_separability_score": linear_separability
        }
