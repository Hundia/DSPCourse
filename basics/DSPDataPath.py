
import numpy as np

# Simulate 16-bit memory
memory_x = np.array([0x1234, 0x5678], dtype=np.int16)
memory_y = np.array([0x9ABC, 0xDEF0], dtype=np.int16)

# Fetch 16-bit values from memory
x = memory_x[0]
y = memory_y[0]

print(f"x (16-bit): {x:#06x}")
print(f"y (16-bit): {y:#06x}")

# Multiply 16-bit values to get a 32-bit result
product = np.int32(x) * np.int32(y)

print(f"Product (32-bit): {product:#010x}")

def sign_extend_32_to_40(value):
    """
    Sign extend a 32-bit integer to 40 bits.

    This function takes a 32-bit integer and extends its sign to 40 bits.
    If the input value is negative (i.e., the 31st bit is set),
    it sets the upper 8 bits to 1 to preserve the sign.

    Args:
        value (int): A 32-bit integer to be sign-extended.

    Returns:
        int: The sign-extended 40-bit integer.
    """
    value = int(value)  # Convert to a regular Python integer

    if value & 0x80000000:  # Check if the sign bit (31st bit) is set
        value |= 0xFFFFFF0000000000  # Set the higher bits to 1 for sign extension
    return value

# Sign extend the 32-bit product to 40 bits
product_40bit = sign_extend_32_to_40(product)

print(f"Product (40-bit, sign extended): {product_40bit:#014x}")

# Initialize 40-bit accumulator
accumulator = 0x0000000000

# Accumulate the 40-bit product
accumulator += product_40bit

print(f"Accumulator (40-bit): {accumulator:#014x}")

def quantize_to_16bit(value):
    """
    Quantize a 40-bit value to 16-bit using truncation.

    This function takes a 40-bit integer value and truncates it to fit into 16 bits.
    It simply retains the least significant 16 bits of the input value.

    Args:
        value (int): A 40-bit integer to be quantized.

    Returns:
        np.int16: The quantized 16-bit value as a numpy int16 type.
    """
    # Truncate the value to fit into 16 bits
    quantized_value = value & 0xFFFF
    return np.int16(quantized_value)

# Quantize the accumulator value to 16 bits
quantized_result = quantize_to_16bit(accumulator)

print(f"Quantized Result (16-bit): {quantized_result:#06x}")

# Store the quantized result back to memory
memory_y[0] = quantized_result

print(f"Updated memory_y[0] (16-bit): {memory_y[0]:#06x}")