import numpy as np

# Define matrices A and B
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

# Perform matrix multiplication
C = np.dot(A, B)

# Print the matrices and the result
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix C (Result of A * B):")
print(C)
