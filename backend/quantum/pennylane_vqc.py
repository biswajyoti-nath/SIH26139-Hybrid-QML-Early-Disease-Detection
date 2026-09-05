import pennylane.numpy as np
import numpy as std_np
import pennylane as qml

class PennyLaneVQC:
    """
    A Variational Quantum Classifier (VQC) using PennyLane.
    Implements a standard scikit-learn compatible interface.
    """
    def __init__(
        self, 
        n_qubits: int = 8, 
        n_layers: int = 3, 
        learning_rate: float = 0.1, 
        iterations: int = 50,
        random_state: int = 42
    ):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.random_state = random_state
        
        np.random.seed(self.random_state)
        self.weights = np.random.uniform(
            0, 2 * np.pi, (self.n_layers, self.n_qubits), requires_grad=True
        )
        
        self.dev = qml.device("lightning.qubit", wires=self.n_qubits)
        
        @qml.qnode(self.dev, interface="autograd")
        def _circuit(weights, x):
            qml.AngleEmbedding(x, wires=range(self.n_qubits))
            qml.BasicEntanglerLayers(weights, wires=range(self.n_qubits))
            return qml.expval(qml.PauliZ(0))
            
        self.circuit = _circuit
        self.opt = qml.AdamOptimizer(stepsize=self.learning_rate)
        
    def _forward(self, weights, x):
        expval = self.circuit(weights, x)
        return (expval + 1.0) / 2.0
        
    def _cost(self, weights, X, Y):
        predictions = qml.math.stack([self._forward(weights, x) for x in X])
        return qml.math.mean((predictions - Y) ** 2)
        
    def fit(self, X, y):
        np.random.seed(self.random_state)
        
        X_ag = np.array(X, requires_grad=False)
        y_ag = np.array(y, requires_grad=False)
        
        def cost_wrapper(w):
            return self._cost(w, X_ag, y_ag)
            
        for it in range(self.iterations):
            # step() returns the updated weights. It is NOT a tuple when only 1 arg is passed.
            self.weights = self.opt.step(cost_wrapper, self.weights)
            
        return self
        
    def predict_proba(self, X) -> std_np.ndarray:
        probas = [self._forward(self.weights, np.array(x, requires_grad=False)) for x in X]
        probas = std_np.array([float(p) for p in probas])
        return std_np.vstack([1.0 - probas, probas]).T
        
    def predict(self, X) -> std_np.ndarray:
        probas = self.predict_proba(X)[:, 1]
        return (probas >= 0.5).astype(int)
