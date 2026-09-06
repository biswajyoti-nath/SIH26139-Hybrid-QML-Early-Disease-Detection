import pennylane as qml
import numpy as np

dev = qml.device("lightning.gpu", wires=8)
# Fallback to qubit if gpu fails
try:
    dev = qml.device("lightning.gpu", wires=8)
except:
    dev = qml.device("lightning.qubit", wires=8)

@qml.qnode(dev)
def kernel_batch(x1, x2):
    qml.IQPEmbedding(x1, wires=range(8))
    qml.adjoint(qml.IQPEmbedding)(x2, wires=range(8))
    return qml.probs(wires=range(8))

x1 = np.random.random(8)
x2 = np.random.random((10, 8))
x1_tiled = np.tile(x1, (10, 1))

try:
    res = kernel_batch(x1_tiled, x2)
    print("Shape:", res.shape)
except Exception as e:
    print("Error:", e)
