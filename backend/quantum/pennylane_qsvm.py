import pennylane as qml
import pennylane.numpy as np
import numpy as std_np
from sklearn.svm import SVC
from sklearn.calibration import CalibratedClassifierCV

class PennyLaneQSVM:
    def __init__(self, n_qubits: int = 8, random_state: int = 42, C: float = 1.0):
        self.n_qubits = n_qubits
        self.random_state = random_state
        self.C = C
        
        try:
            self.dev = qml.device("lightning.gpu", wires=self.n_qubits)
        except Exception:
            self.dev = qml.device("lightning.qubit", wires=self.n_qubits)
            
        def feature_map(x):
            qml.AngleEmbedding(x, wires=range(self.n_qubits), rotation='X')
            
        @qml.qnode(self.dev, interface="autograd")
        def _kernel_circuit(x1, x2):
            feature_map(x1)
            qml.adjoint(feature_map)(x2)
            return qml.probs(wires=range(self.n_qubits))
            
        self.kernel_circuit = _kernel_circuit
        
        base_svc = SVC(kernel="precomputed", C=self.C, random_state=self.random_state)
        self.svm = CalibratedClassifierCV(estimator=base_svc, cv=5, ensemble=False)
        
    def kernel_matrix(self, X1, X2):
        N = len(X1)
        M = len(X2)
        gram = std_np.zeros((N, M))
        
        for i in range(N):
            x1_tiled = std_np.tile(X1[i], (M, 1))
            probs = self.kernel_circuit(x1_tiled, X2)
            if M == 1:
                gram[i, :] = float(probs[0])
            else:
                gram[i, :] = std_np.array(probs[:, 0])
                
        is_symmetric = (X1 is X2) or (std_np.array_equal(X1, X2))
        if is_symmetric:
            std_np.fill_diagonal(gram, 1.0)
            
        return gram
        
    def fit(self, X, y):
        self.X_train = std_np.array(X)
        self.y_train = std_np.array(y)
        K_train = self.kernel_matrix(self.X_train, self.X_train)
        self.svm.fit(K_train, self.y_train)
        return self
        
    def predict_proba(self, X):
        X = std_np.array(X)
        K_test = self.kernel_matrix(X, self.X_train)
        return self.svm.predict_proba(K_test)
        
    def predict(self, X):
        X = std_np.array(X)
        K_test = self.kernel_matrix(X, self.X_train)
        return self.svm.predict(K_test)
