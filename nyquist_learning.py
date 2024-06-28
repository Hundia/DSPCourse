import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
f_signal = 50  # Signal frequency in Hz
duration = 1.0  # Duration in seconds

# Generate time array for different sampling rates
t_high = np.linspace(0.0, duration, 5000, endpoint=False)  # High sampling rate
t_nyquist = np.linspace(0.0, duration, 100, endpoint=False)  # Nyquist rate
t_low = np.linspace(0.0, duration, 50, endpoint=False)  # Below Nyquist rate

# Generate sine wave signal
x_high = np.sin(2.0 * np.pi * f_signal * t_high)
x_nyquist = np.sin(2.0 * np.pi * f_signal * t_nyquist)
x_low = np.sin(2.0 * np.pi * f_signal * t_low)

# Plot the signals
plt.figure(figsize=(12, 8))

# High sampling rate plot
plt.subplot(3, 1, 1)
plt.plot(t_high, x_high, label='High Sampling Rate (5000 Hz)')
plt.title('High Sampling Rate (5000 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Nyquist rate plot
plt.subplot(3, 1, 2)
plt.plot(t_nyquist, x_nyquist, label='Nyquist Rate (100 Hz)', color='orange')
plt.title('Nyquist Rate (100 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

# Below Nyquist rate plot
plt.subplot(3, 1, 3)
plt.plot(t_low, x_low, label='Below Nyquist Rate (50 Hz)', color='red')
plt.title('Below Nyquist Rate (50 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
