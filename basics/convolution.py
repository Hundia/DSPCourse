def verbose_convolution(x, h):
    print(f"Input sequences:")
    print(f"x = {x}")
    print(f"h = {h}")
    print("\nConvolution process:")

    # Initialize the output sequence y
    y = [0] * (len(x) + len(h) - 1)
    
    # Iterate through each position in the output sequence
    for i in range(len(y)):
        print(f"\nCalculating y[{i}]:")
        
        # For each position, iterate through h
        for j in range(len(h)):
            # Check if the corresponding x element exists
            if 0 <= i-j < len(x):
                x_val = x[i-j]
                h_val = h[j]
                product = x_val * h_val
                y[i] += product
                print(f"  x[{i-j}] * h[{j}] = {x_val} * {h_val} = {product}")
            else:
                print(f"  (x[{i-j}] doesn't exist) * h[{j}] = 0")
        
        print(f"  y[{i}] = {y[i]}")
    
    print("\nFinal result:")
    print(f"y = {y}")
    return y

# Example usage
x = [1, 2, 3]
h = [0, 1, 0.5]

result = verbose_convolution(x, h)