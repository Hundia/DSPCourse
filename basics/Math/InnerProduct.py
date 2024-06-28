'''
The inner product is a fundamental operation in linear algebra that takes two equal-length sequences of numbers and returns a single number. It's calculated by multiplying corresponding entries and then summing up those products.

For two vectors a = (a1, a2, ..., an) and b = (b1, b2, ..., bn), their inner product is defined as:

a · b = a1b1 + a2b2 + ... + an*bn

Key points about the inner product:
1.It's only defined for vectors of the same length.
2.The result is a scalar (a single number), not a vector.
3.It's commutative: a · b = b · a
4.It has geometric interpretations, including being related to vector lengths and angles between vectors.
'''
def inner_product(a, b):
    """
    Calculate the inner product of two vectors.
    
    Args:
    a (list): First vector
    b (list): Second vector
    
    Returns:
    float: The inner product of vectors a and b
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    
    return sum(x * y for x, y in zip(a, b))

# Example usage:
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

result = inner_product(a, b)
print(f"The inner product of {a} and {b} is: {result}")

# You can also use it with different vectors:
c = [0.5, 1.5, 2.5]
d = [2, 3, 4]
print(f"The inner product of {c} and {d} is: {inner_product(c, d)}")