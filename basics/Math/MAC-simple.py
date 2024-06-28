'''
This script performs a Multiply-Accumulate (MAC) operation on two lists of numbers.
The MAC operation multiplies corresponding elements of the two lists and accumulates the result.
'''

# Lists of numbers
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]

# Initialize the accumulator
sum_of_products = 0

# Perform the MAC operation
for i in range(len(a)):
    sum_of_products += a[i] * b[i]

# Print the result
print("List a:", a)
print("List b:", b)
print("Sum of products:", sum_of_products)

'''
Expected outcome: 
List a: [1, 2, 3, 4, 5]
List b: [10, 20, 30, 40, 50]
Sum of products: 550
'''

