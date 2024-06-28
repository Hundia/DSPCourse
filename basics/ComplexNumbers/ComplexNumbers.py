import numpy as np

"""
This script demonstrates operations with complex numbers in Python,
including conversion between rectangular and polar forms.
"""


# Define a complex number in rectangular form
z = 3 + 4j

# Get real and imaginary parts
a = z.real
b = z.imag

# Convert to polar form
r = np.abs(z)
theta = np.angle(z)

print(f"Complex number (rectangular): {z}")
print(f"Real part: {a}")
print(f"Imaginary part: {b}")
print(f"Polar form: r = {r}, theta = {theta} radians")
# Convert to exponential form
z_exp = r * np.exp(1j * theta)
print(f"Exponential form: {z_exp}")
# Convert back to rectangular form
z_rectangular = r * (np.cos(theta) + 1j * np.sin(theta))
print(f"Converted back to rectangular form: {z_rectangular}")

# Conjugate a complex number
# Define a complex number
z = 3 + 4j

# Compute the conjugate
z_conjugate = np.conj(z)

print(f"Complex number: {z}")
print(f"Conjugate: {z_conjugate}")

# Multiplying a complex number by its conjugate
product = z * z_conjugate
print(f"Product of z and its conjugate: {product}")

# Inner Product of Complex Vectors - Notice the np.conj() function used in the inner product
# Define two complex vectors
a = np.array([1+2j, 3+4j, 5+6j])
b = np.array([7+8j, 9+10j, 11+12j])

# Compute the inner product
inner_product = np.dot(a, np.conj(b))

print(f"Vector a: {a}")
print(f"Vector b: {b}")
print(f"Inner product of a and b: {inner_product}")
