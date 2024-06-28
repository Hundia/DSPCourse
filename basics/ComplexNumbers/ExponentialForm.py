import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1  # Amplitude
f = 1  # Frequency in Hz
omega = 2 * np.pi * f  # Angular frequency
phi = np.pi / 4  # Phase offset in radians
t = np.linspace(0, 1, 1000)  # Time array for 1 second, 1000 samples

# Phase theta
theta = omega * t + phi

# Original sine wave
x_t = A * np.sin(theta)

# Exponential form
z_t = A * np.exp(1j * theta)

# Real and imaginary parts
real_part = z_t.real
imag_part = z_t.imag

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, x_t, label='Sine wave: $\\sin(2\\pi ft + \\phi)$')
plt.title('Original Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, real_part, label='Real part: $\\cos(2\\pi ft + \\phi)$', linestyle='dashed')
plt.title('Real Part of the Complex Exponential')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, imag_part, label='Imaginary part: $\\sin(2\\pi ft + \\phi)$', linestyle='dashed')
plt.title('Imaginary Part of the Complex Exponential')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
