import numpy as np

# Define two vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Initialize the accumulator
inner_product = 0

# Perform the MAC operation to compute the inner product
for i in range(len(a)):
    inner_product += a[i] * b[i]

# Alternatively, using np.dot for comparison
inner_product_np = np.dot(a, b)

# Print the results
print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Inner Product (using explicit MAC): {inner_product}")
print(f"Inner Product (using np.dot): {inner_product_np}")
