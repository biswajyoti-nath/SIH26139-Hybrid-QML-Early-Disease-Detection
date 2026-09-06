import time
import os
import pennylane as qml
from pennylane import numpy as pnp
import numpy as np

# Suppress pennylane warnings for cleaner output
import warnings
warnings.filterwarnings("ignore")

def sanity_check():
    print("========================================")
    print("TASK 3: SMALL GPU SANITY BENCHMARK")
    print("========================================")
    
    n_qubits = 4
    
    try:
        dev_cpu = qml.device("lightning.qubit", wires=n_qubits)
        dev_gpu = qml.device("lightning.gpu", wires=n_qubits)
    except Exception as e:
        print(f"ERROR: Could not instantiate devices. {e}")
        exit(1)
        
    print(f"CPU Device: {dev_cpu.name}")
    print(f"GPU Device: {dev_gpu.name}")
    
    def circuit(weights, inputs):
        qml.AngleEmbedding(inputs, wires=range(n_qubits))
        qml.BasicEntanglerLayers(weights, wires=range(n_qubits))
        return qml.expval(qml.PauliZ(0))
        
    qnode_cpu = qml.QNode(circuit, dev_cpu, diff_method="adjoint")
    qnode_gpu = qml.QNode(circuit, dev_gpu, diff_method="adjoint")
    
    # Identical initialization
    np.random.seed(42)
    inputs = pnp.array(np.random.random(n_qubits), requires_grad=False)
    weights = pnp.array(np.random.random((2, n_qubits)), requires_grad=True)
    
    # CPU
    t0 = time.perf_counter()
    res_cpu = qnode_cpu(weights, inputs)
    t_cpu = time.perf_counter() - t0
    
    # GPU
    t0 = time.perf_counter()
    res_gpu = qnode_gpu(weights, inputs)
    t_gpu = time.perf_counter() - t0
    
    diff = np.abs(res_cpu - res_gpu)
    
    print(f"\nCPU Result: {res_cpu:.6f} ({t_cpu:.4f}s)")
    print(f"GPU Result: {res_gpu:.6f} ({t_gpu:.4f}s)")
    print(f"Numerical Difference: {diff:.6e}")
    
    if diff > 1e-5:
        print("ERROR: TASK 4: Numerical consistency failed!")
        exit(1)
    else:
        print("TASK 4: Numerical consistency verified.")
        
    return True

def benchmark_realistic_workload():
    print("\n========================================")
    print("TASK 5: REALISTIC VQC WORKLOAD BENCHMARK")
    print("========================================")
    
    n_qubits = 8
    n_layers = 3
    batch_size = 32
    iterations = 20
    learning_rate = 0.01
    
    print(f"Workload: {n_qubits} qubits, {n_layers} layers, {iterations} iterations, batch_size={batch_size}")
    
    dev_cpu = qml.device("lightning.qubit", wires=n_qubits)
    dev_gpu = qml.device("lightning.gpu", wires=n_qubits)
    
    def circuit(weights, inputs):
        qml.AngleEmbedding(inputs, wires=range(n_qubits))
        qml.StronglyEntanglingLayers(weights, wires=range(n_qubits))
        return qml.expval(qml.PauliZ(0))
        
    qnode_cpu = qml.QNode(circuit, dev_cpu, diff_method="adjoint")
    qnode_gpu = qml.QNode(circuit, dev_gpu, diff_method="adjoint")
    
    # Data
    np.random.seed(42)
    X_batch = pnp.array(np.random.random((batch_size, n_qubits)), requires_grad=False)
    y_batch = pnp.array(np.random.choice([-1, 1], size=batch_size), requires_grad=False)
    
    # Weights
    weights_shape = qml.StronglyEntanglingLayers.shape(n_layers=n_layers, n_wires=n_qubits)
    initial_weights = pnp.array(np.random.random(weights_shape), requires_grad=True)
    
    def run_training(qnode):
        def cost(weights):
            preds = [qnode(weights, x) for x in X_batch]
            return pnp.mean((pnp.array(preds) - y_batch)**2)
            
        opt = qml.AdamOptimizer(stepsize=learning_rate)
        weights = pnp.copy(initial_weights)
        
        t0 = time.perf_counter()
        for i in range(iterations):
            weights, loss = opt.step_and_cost(cost, weights)
        total_time = time.perf_counter() - t0
        return loss, total_time
        
    # Warmup
    print("Warming up GPU...")
    _ = run_training(qnode_gpu)
        
    print("\nRunning CPU...")
    loss_cpu, time_cpu = run_training(qnode_cpu)
    print(f"CPU Loss: {loss_cpu:.6f} | Time: {time_cpu:.2f}s")
    
    print("Running GPU...")
    loss_gpu, time_gpu = run_training(qnode_gpu)
    print(f"GPU Loss: {loss_gpu:.6f} | Time: {time_gpu:.2f}s")
    
    speedup = time_cpu / time_gpu if time_gpu > 0 else 0
    diff = np.abs(loss_cpu - loss_gpu)
    print(f"\nFinal Speedup: {speedup:.2f}x")
    print(f"Final Loss Difference: {diff:.6e}")
    
    with open("GPU_BENCHMARK_REPORT.md", "w") as f:
        f.write("# GPU Quantum Simulation Infrastructure Benchmark\n\n")
        f.write("## Environment\n")
        f.write(f"- PennyLane version: {qml.__version__}\n")
        f.write(f"- CPU Device: {dev_cpu.name}\n")
        f.write(f"- GPU Device: {dev_gpu.name}\n")
        f.write("\n## Realistic Workload Configuration\n")
        f.write(f"- Qubits: {n_qubits}\n")
        f.write(f"- Layers: {n_layers}\n")
        f.write(f"- Iterations: {iterations}\n")
        f.write(f"- Batch Size: {batch_size}\n")
        f.write("\n## Results\n")
        f.write(f"- CPU Runtime: {time_cpu:.2f} seconds\n")
        f.write(f"- GPU Runtime: {time_gpu:.2f} seconds\n")
        f.write(f"- Accelerated Speedup: **{speedup:.2f}x**\n")
        f.write(f"- Numerical Consistency Error: {diff:.6e}\n")
        f.write("\n*Note: GPU optimization strictly accelerates statevector simulation via cuQuantum. This is an engineering acceleration and does not change model accuracy or constitute a 'quantum advantage'.*\n")

if __name__ == "__main__":
    if sanity_check():
        benchmark_realistic_workload()
