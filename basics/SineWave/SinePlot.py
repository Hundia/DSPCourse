import numpy as np
import matplotlib.pyplot as plt

# Function to plot sine wave
def plot_sine_wave(amplitude, frequency, phase, duration, label, color):
    t = np.linspace(0, duration, 1000)
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    plt.plot(t, x, label=label, color=color)

# Parameters for sine waves
parameters = [
    (1, 1, 0, 'Amplitude=1, Frequency=1Hz, Phase=0', 'blue'),
    (2, 1, 0, 'Amplitude=2, Frequency=1Hz, Phase=0', 'green'),
    (1, 2, 0, 'Amplitude=1, Frequency=2Hz, Phase=0', 'red'),
    (1, 1, np.pi/4, 'Amplitude=1, Frequency=1Hz, Phase=π/4', 'purple'),
    (1, 1, np.pi/2, 'Amplitude=1, Frequency=1Hz, Phase=π/2', 'orange')
]

# Plot settings
plt.figure(figsize=(10, 6))
plt.title('Sine Waves with Different Parameters')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot each sine wave with different parameters
for amplitude, frequency, phase, label, color in parameters:
    plot_sine_wave(amplitude, frequency, phase, 2, label, color)

# Add legend to the plot
plt.legend()
plt.show()
