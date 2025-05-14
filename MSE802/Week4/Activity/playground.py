# in python have to use j for imaginary any other characters gives
# compile errors

# matrix = np.array([[1, 2+3j, 3], [4j, 5, 6]])    - VALID
# matrix = np.array([[1, 2+3i, 3], [4i, 5, 6]])    - INVALID
#  j  is the built-in literal syntax for complex numbers
# Python only accepts complex literals in real + imaginary order  5j - 2   as   -2 + 5j


import numpy as np

def transpose(matrix):
    return np.transpose(matrix)

def conjugate_transpose(matrix):
    return np.conj(matrix.T)

def adjoint(matrix):
    return conjugate_transpose(matrix)

# Example usage:
matrix = np.array([[1, 2+3j, 3], [4j, 5, 6]])
print("Original Matrix:")
print(matrix)

print("\nTranspose:")
print(transpose(matrix))

print("\nConjugate Transpose (Hermitian Transpose):")
print(conjugate_transpose(matrix))

print("\nAdjoint:")
print(adjoint(matrix))