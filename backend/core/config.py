from pydantic import BaseModel
from typing import Dict, Any, Optional

class ExperimentConfig(BaseModel):
    experiment_id: str
    dataset_name: str
    split_strategy: str
    test_size: float
    random_seed: int
    n_pca_components: Optional[int]
    models: Dict[str, Dict[str, Any]]
    
    @classmethod
    def load_from_json(cls, json_path: str):
        with open(json_path, 'r') as f:
            return cls.model_validate_json(f.read())
