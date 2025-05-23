import numpy as np

# Define Pauli-X gate (NOT gate)
X = np.array([[0, 1],
              [1, 0]])

# Initial state vector for |00>
initial_state = np.array([1, 0, 0, 0])  # |00> in 2-qubit system

# Apply X gate to both qubits in parallel (tensor product)
X_tensor = np.kron(X, X)

# Final state after applying both X gates - in sequence
final_state = np.dot(X_tensor, initial_state)

print("Initial state |00>:", initial_state)
print("Final state after apply two X gates:", final_state)
