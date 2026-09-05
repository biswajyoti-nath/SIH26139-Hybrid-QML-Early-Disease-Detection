import numpy as np
from backend.core.preprocessing import PreprocessingEngine
from backend.core.dataset import DatasetManager

def test_leakage_safety():
    """
    Test that the scaler and PCA do not leak information from the test set.
    We verify this by ensuring the scaler means strictly match the train set means,
    and NOT the full dataset means.
    """
    dataset = DatasetManager.load_wdbc()
    
    result = PreprocessingEngine.run_pipeline(
        dataset.X, dataset.y, 
        test_size=0.2, 
        random_seed=42, 
        n_pca_components=8
    )
    
    # Manually split to check scaler math
    from sklearn.model_selection import train_test_split
    X_train_raw, _, _, _ = train_test_split(
        dataset.X, dataset.y, 
        test_size=0.2, 
        random_state=42, 
        stratify=dataset.y
    )
    
    # The scaler mean MUST match the train set mean, not the full set mean
    train_mean = np.mean(X_train_raw, axis=0)
    full_mean = np.mean(dataset.X, axis=0)
    
    # Assert scaler fitted on train
    np.testing.assert_array_almost_equal(result.scaler.mean_, train_mean)
    
    # Assert scaler did NOT fit on full data (they should be different)
    with np.testing.assert_raises(AssertionError):
        np.testing.assert_array_almost_equal(result.scaler.mean_, full_mean)
        
    # Assert PCA outputs correct dimensions
    assert result.X_train.shape[1] == 8
    assert result.X_test.shape[1] == 8
