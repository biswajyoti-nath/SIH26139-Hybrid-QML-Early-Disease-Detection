import numpy as np
from sklearn.decomposition import PCA
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
import warnings

def profile_dataset(X, y=None, n_components=8):
    """
    Computes descriptive complexity variables for the dataset.
    DO NOT CLAIM THESE ARE VALIDATED PREDICTORS OF QUANTUM SUITABILITY.
    """
    n_samples, n_features = X.shape
    
    # R_k and L_k (PCA retention & loss)
    from sklearn.preprocessing import StandardScaler
    X_scaled = StandardScaler().fit_transform(X)
    pca = PCA(n_components=min(n_components, n_features))
    pca.fit(X)
    pca.fit(X_scaled)
    variance_retained = float(np.sum(pca.explained_variance_ratio_))
    information_loss = 1.0 - variance_retained
    
    # C (Compression ratio)
    compression_ratio = float(n_features) / n_components
    
    # rho (Mean absolute pairwise Pearson correlation)
    # Ignore warnings for zero variance columns
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        corr = np.corrcoef(X, rowvar=False)
        # Handle nan if any column had 0 variance
        corr = np.nan_to_num(corr, nan=0.0)
        # Extract upper triangle without diagonal
        upper_tri = corr[np.triu_indices_from(corr, k=1)]
        mean_abs_correlation = float(np.mean(np.abs(upper_tri))) if len(upper_tri) > 0 else 0.0

    # S (Linear separability proxy)
    # Uses a fast LinearSVC. Must be careful of leakage in real implementation.
    separability_proxy = 0.0
    if y is not None:
        clf = LinearSVC(random_state=42, max_iter=1000, dual="auto")
        try:
            scores = cross_val_score(clf, X, y, cv=3, scoring='roc_auc')
            separability_proxy = float(np.mean(scores))
        except Exception:
            separability_proxy = 0.5 # Default / inconclusive
            
    return {
        "raw_dimensions": n_features,
        "reduced_dimensions": n_components,
        "variance_retained": variance_retained,
        "information_loss": information_loss,
        "compression_ratio": compression_ratio,
        "separability_proxy": separability_proxy,
        "mean_abs_correlation": mean_abs_correlation
    }
