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
        learning_rate: float = 0.05, 
        iterations: int = 50,
        random_state: int = 42,
        loss_fn: str = "mse"
    ):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.random_state = random_state
        self.loss_fn = loss_fn.lower()
        self.history_ = []
        
        np.random.seed(self.random_state)
        self.weights = np.random.uniform(
            0, 2 * np.pi, (self.n_layers, self.n_qubits), requires_grad=True
        )
        
        self.dev = qml.device("lightning.qubit", wires=self.n_qubits)
        
        @qml.qnode(self.dev, interface="autograd")
        def _circuit(weights, x):
            # AngleEmbedding supports 2D arrays directly (batching)
            qml.AngleEmbedding(x, wires=range(self.n_qubits), rotation='X')
            qml.BasicEntanglerLayers(weights, wires=range(self.n_qubits), rotation=qml.RY)
            return qml.expval(qml.PauliZ(0))
            
        self.circuit = _circuit
        self.opt = qml.AdamOptimizer(stepsize=self.learning_rate)
        
    def _forward(self, weights, X):
        # By passing a 2D array, lightning.qubit processes the entire batch in C++
        expval = self.circuit(weights, X)
        return (expval + 1.0) / 2.0
        
    def _cost(self, weights, X, Y):
        predictions = self._forward(weights, X)
        if self.loss_fn == "mse":
            return qml.math.mean((predictions - Y) ** 2)
        elif self.loss_fn == "bce":
            eps = 1e-15
            p = qml.math.clip(predictions, eps, 1.0 - eps)
            return -qml.math.mean(Y * qml.math.log(p) + (1 - Y) * qml.math.log(1 - p))
        else:
            raise ValueError(f"Unknown loss function: {self.loss_fn}")
        
    def fit(self, X, y):
        np.random.seed(self.random_state)
        self.history_ = []
        
        X_ag = np.array(X, requires_grad=False)
        y_ag = np.array(y, requires_grad=False)
        
        def cost_wrapper(w):
            return self._cost(w, X_ag, y_ag)
            
        for it in range(self.iterations):
            self.weights = self.opt.step(cost_wrapper, self.weights)
            loss = float(self._cost(self.weights, X_ag, y_ag))
            self.history_.append(loss)
            
        return self
        
    def predict_proba(self, X) -> std_np.ndarray:
        probas = self._forward(self.weights, np.array(X, requires_grad=False))
        probas = std_np.array([float(p) for p in probas])
        probas = std_np.clip(probas, 0.0, 1.0)
        return std_np.vstack([1.0 - probas, probas]).T
        
    def predict(self, X) -> std_np.ndarray:
        probas = self.predict_proba(X)[:, 1]
        return (probas >= 0.5).astype(int)
