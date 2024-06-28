'''
This article will show you how to calculate the Pearson correlation coefficient between two signals in Python.

What is the Pearson Correlation Coefficient?

The Pearson correlation coefficient is a measure of the linear correlation between two variables. It ranges from -1 to 1, where:

'''
import numpy as np

# Define two signals
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

def pearson_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two signals.

    The Pearson correlation coefficient measures the linear correlation
    between two variables. It ranges from -1 to 1, where:
    - 1 indicates a perfect positive linear correlation
    - 0 indicates no linear correlation
    - -1 indicates a perfect negative linear correlation

    Parameters:
    x (array-like): First input signal
    y (array-like): Second input signal

    Returns:
    float: Pearson correlation coefficient

    Raises:
    ValueError: If the input arrays have different lengths

    Note:
    Both input signals should have the same length.
    """
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_sq = np.sum(x ** 2)
    sum_y_sq = np.sum(y ** 2)
    sum_xy = np.sum(x * y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2))
    
    return numerator / denominator

r = pearson_correlation(x, y)

# Print results
print(f"Signal x: {x}")
print(f"Signal y: {y}")
print(f"Pearson Correlation Coefficient: {r}")
