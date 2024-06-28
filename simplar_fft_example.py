import numpy as np
from scipy.fft import fft, fftfreq

# Example parameters
sampling_rate = 2  # 8 samples per second
duration = 1.0  # 1 second duration
t = np.linspace(0.0, duration, int(sampling_rate * duration), endpoint=False)

# Create a simple signal
x = np.sin(2.0 * np.pi * 2.0 * t)

# Perform Fourier Transform
yf = fft(x)
xf = fftfreq(sampling_rate, 1 / sampling_rate)  # Generate frequency bins

print("Time-domain signal:", x)
print("FFT of the signal:", yf)
print("Frequency bins:", xf)
print("Sliced frequency bins:", xf[:sampling_rate // 2])
