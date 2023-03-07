def swap_numbers(a, b):
    # Swap the values of a and b
    a, b = b, a
    return a, b
# Initialize two numbers
x = 5
y = 10
# Print the original values
print(f"Before swapping: x = {x}, y = {y}")
# Swap the values using the function
x, y = swap_numbers(x, y)
# Print the new values
print(f"After swapping: x = {x}, y = {y}")
