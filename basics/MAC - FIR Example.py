'''
The Multiply-Accumulate (MAC) operation is a fundamental building block in digital signal processing (DSP). 
It is used extensively in various algorithms and applications, such as filtering, convolution, and Fast Fourier Transform (FFT). 
Understanding MAC is crucial for grasping how DSP operations are implemented efficiently.

In this article, we will explore the Multiply-Accumulate (MAC) operation and its implementation in Python.

What is the Multiply-Accumulate (MAC) Operation?

The Multiply-Accumulate (MAC) operation is a fundamental building block in digital signal processing (DSP).

It is used extensively in various algorithms and applications, such as filtering, convolution, and Fast Fourier Transform (FFT).

Understanding MAC is crucial for grasping how DSP operations are implemented efficiently.

The Multiply-Accumulate (MAC) operation is defined as:

y[n] = x[n] * h[n] + y[n - 1]

where x[n] is the input signal, h[n] is the filter coefficients, and y[n] is the output signal.


'''
import numpy as np

# Example input signal (e.g., a step signal)
x = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

# FIR filter coefficients (e.g., a simple moving average filter)
h = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Number of coefficients
N = len(h)

# Output signal (initialize to zero)
y = np.zeros(len(x))

# Perform FIR filtering using MAC operations
for n in range(len(x)):
    # Initialize the accumulator for the current output sample
    acc = 0
    for k in range(N):
        if n - k >= 0:
            acc += h[k] * x[n - k]
    y[n] = acc

print("Input Signal:", x)
print("Filter Coefficients:", h)
print("Filtered Output Signal:", y)
