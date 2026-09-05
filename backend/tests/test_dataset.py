from backend.core.dataset import DatasetManager
import numpy as np

def test_wdbc_load_and_validate():
    dataset = DatasetManager.load_wdbc()
    
    # Assert shape
    assert dataset.X.shape == (569, 30)
    assert dataset.y.shape == (569,)
    
    # Assert positive class is malignant (1)
    assert dataset.target_names[1] == 'malignant'
    assert dataset.target_names[0] == 'benign'
    
    # Check binary constraints
    assert set(np.unique(dataset.y)) == {0, 1}
    
    # Check for NaNs
    assert not np.isnan(dataset.X).any()
