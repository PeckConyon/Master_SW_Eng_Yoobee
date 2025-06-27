from qiskit import QuantumCircuit

qc = QuantumCircuit(1)
qc.i(0)  # Apply Identity gate to qubit 0
qc.draw('text')