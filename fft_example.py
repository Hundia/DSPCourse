import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from scipy.fft import fft, fftfreq

# Set this variable to True to use Plotly, or False to use Matplotlib
use_plotly = True

# Generate a time array 't'
sampling_rate = 1000  # 1000 samples per second
duration = 1.0  # 1 second duration
t = np.linspace(0.0, duration, int(sampling_rate * duration), endpoint=False)

# Create a composite signal 'x' which is a sum of two sine waves
# First sine wave: amplitude = 0.5, frequency = 50 Hz
# Second sine wave: amplitude = 0.25, frequency = 80 Hz
x = 0.5 * np.sin(2.0 * np.pi * 50.0 * t) + 0.25 * np.sin(2.0 * np.pi * 80.0 * t)

# Perform Fourier Transform to get the frequency domain representation
yf = fft(x)  # Compute the FFT

"""
Understanding fftfreq
The fftfreq function from the scipy.fft module generates the frequency bins for the discrete Fourier Transform (DFT) output. To understand this, we need to consider what happens when we perform a Fourier Transform on a signal.

Frequency Bins
When you apply the Fourier Transform to a time-domain signal, the result is a series of complex numbers representing the amplitude and phase of different frequency components. The fftfreq function helps to map each of these components to their corresponding frequencies.

Parameters
n (first parameter): This is the length of the DFT. In the context of our code, it is the number of samples in the time-domain signal, which is sampling_rate (1000 samples in this case).

d (second parameter): This is the sample spacing, which is the inverse of the sampling rate. Since sampling_rate is the number of samples per second, d is 1 / sampling_rate.

Output
The fftfreq function returns an array of frequency bins, which correspond to the frequencies for each component in the FFT result.

Example
For a signal sampled at 1000 Hz over 1 second, we have 1000 samples. The frequency bins will range from 0 to the Nyquist frequency (half the sampling rate) and then from negative Nyquist back to just below 0. The Nyquist frequency for this example is 500 Hz.

Slicing the Frequency Bins
The slicing [:sampling_rate // 2] is used because the FFT result is symmetric. For a real-valued time-domain signal, the negative frequency components are just the complex conjugates of the positive frequency components. Therefore, we typically only need to consider the first half of the frequency bins for practical purposes.

Detailed Example
Let's say sampling_rate = 1000 Hz and duration = 1 second, so we have 1000 samples. The fftfreq function call would generate an array of 1000 elements corresponding to the frequencies for each FFT component.

For the first half ([:sampling_rate // 2]), this would range from 0 to 499 Hz.
For the second half, it would range from -500 to -1 Hz.
"""
xf = fftfreq(sampling_rate, 1 / sampling_rate)[:sampling_rate // 2]  # Generate frequency bins

# Plotting with Plotly or Matplotlib
if use_plotly:
    # Plot using Plotly
    fig = make_subplots(rows=2, cols=1)

    # Time domain plot
    fig.add_trace(go.Scatter(x=t, y=x, mode='lines', name='Composite Signal (Time Domain)'), row=1, col=1)

    # Frequency domain plot
    fig.add_trace(go.Scatter(x=xf, y=2.0/sampling_rate * np.abs(yf[:sampling_rate//2]), mode='lines', name='Composite Signal (Frequency Domain)'), row=2, col=1)

    fig.update_layout(
        title='Composite Signal in Time and Frequency Domains',
        height=800,
        width=900
    )
    fig.update_xaxes(title_text='Time [s]', row=1, col=1)
    fig.update_yaxes(title_text='Amplitude', row=1, col=1)
    fig.update_xaxes(title_text='Frequency [Hz]', row=2, col=1)
    fig.update_yaxes(title_text='Magnitude', row=2, col=1)

    fig.show()
else:
    # Plot using Matplotlib
    plt.figure(figsize=(12, 8))

    # Time domain plot
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.title('Composite Signal (Time Domain)')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)

    # Frequency domain plot
    plt.subplot(2, 1, 2)
    plt.plot(xf, 2.0/sampling_rate * np.abs(yf[:sampling_rate//2]))
    plt.title('Composite Signal (Frequency Domain)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

"""
Explanation
Fourier Transform (fft)
The Fourier Transform is used to convert the signal from the time domain to the frequency domain. The fft function from the scipy.fft module computes the Fast Fourier Transform of the signal.

Frequency Bins (fftfreq)
The fftfreq function generates the frequency bins corresponding to the FFT output. Only the first half of the frequency bins are used because the FFT output is symmetric.

Magnitude Calculation
The FFT output is complex, so the magnitude is computed using np.abs. Only the first half of the FFT output is used because it is symmetric.

Scaling the FFT Output
The FFT output is scaled by 2.0/sampling_rate to match the amplitude of the time-domain signal. This ensures that the amplitude of the frequency components is correctly represented.
"""