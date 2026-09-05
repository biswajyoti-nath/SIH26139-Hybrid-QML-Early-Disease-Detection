import pennylane.numpy as np
import pennylane as qml
import time

dev = qml.device("lightning.qubit", wires=4)

@qml.qnode(dev, interface="autograd")
def circuit(weights, x):
    qml.AngleEmbedding(x, wires=range(4), rotation='X')
    qml.BasicEntanglerLayers(weights, wires=range(4), rotation=qml.RY)
    return qml.expval(qml.PauliZ(0))

weights = np.random.uniform(0, 2*np.pi, (2, 4), requires_grad=True)
x_batch = np.random.uniform(0, 1, (100, 4), requires_grad=False)

t0 = time.time()
for _ in range(10):
    res = circuit(weights, x_batch)
t1 = time.time()
print(f"Batched time: {t1-t0}s. Shape: {res.shape}")

t0 = time.time()
for _ in range(10):
    res2 = np.array([circuit(weights, x) for x in x_batch])
t1 = time.time()
print(f"Sequential time: {t1-t0}s. Shape: {res2.shape}")
