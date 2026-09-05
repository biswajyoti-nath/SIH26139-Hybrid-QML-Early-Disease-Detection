import numpy as np
from sklearn.datasets import make_classification, make_moons, make_circles

class SyntheticGenerator:
    """
    Generates controlled synthetic datasets for complexity-regime benchmarking.
    """
    
    @staticmethod
    def generate(regime: str, n_samples: int = 500, random_state: int = 42) -> tuple:
        """
        Generates (X, y) based on the predefined regime identifier.
        """
        if regime == "R1_SIMPLE":
            # Linear boundary, low noise, low correlation
            return make_classification(
                n_samples=n_samples, n_features=10, n_informative=5, n_redundant=0,
                n_clusters_per_class=1, flip_y=0.01, class_sep=2.0, random_state=random_state
            )
            
        elif regime == "R2_NONLINEAR":
            # Highly non-linear (Moons) embedded in higher dimensions with some noise
            X, y = make_moons(n_samples=n_samples, noise=0.15, random_state=random_state)
            # Pad with random noise features to reach 10 dimensions to match baseline dims
            np.random.seed(random_state)
            noise_features = np.random.randn(n_samples, 8)
            X = np.hstack((X, noise_features))
            return X, y
            
        elif regime == "R3_CORRELATED":
            # High correlation/redundancy
            return make_classification(
                n_samples=n_samples, n_features=10, n_informative=3, n_redundant=7,
                n_clusters_per_class=2, flip_y=0.05, class_sep=1.0, random_state=random_state
            )
            
        elif regime == "R4_NOISY":
            # High label noise and overlapping classes
            return make_classification(
                n_samples=n_samples, n_features=10, n_informative=5, n_redundant=2,
                n_clusters_per_class=2, flip_y=0.25, class_sep=0.5, random_state=random_state
            )
            
        elif regime == "R5_HIGH_DIMENSIONAL":
            # Many features, few informative
            return make_classification(
                n_samples=n_samples, n_features=100, n_informative=5, n_redundant=10,
                n_clusters_per_class=2, flip_y=0.05, class_sep=1.0, random_state=random_state
            )
            
        else:
            raise ValueError(f"Unknown synthetic regime: {regime}")
