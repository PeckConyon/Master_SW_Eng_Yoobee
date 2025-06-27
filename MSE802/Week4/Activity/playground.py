from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_bloch_vector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# 1. Initial state |0>
qc1 = QuantumCircuit(1)
state1 = Statevector.from_instruction(qc1)
bloch_vector1 = state1.data[:2]  # Extract the qubit's amplitudes
plot_bloch_vector(state1.to_dict()['bloch'], title="Before Hadamard (|0⟩)")
plt.show()

# 2. Apply Hadamard to qubit
qc2 = QuantumCircuit(1)
qc2.h(0)
state2 = Statevector.from_instruction(qc2)
plot_bloch_vector(state2.to_dict()['bloch'], title="After Hadamard (Superposition)")
plt.show()
