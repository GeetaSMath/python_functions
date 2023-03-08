def swap_numbers(a, b):
    # Swap the values of a and b
    a, b = b, a
    return a, b
x = 5
y = 10
print(f"Before swapping: x = {x}, y = {y}")
x, y = swap_numbers(x, y)
print(f"After swapping: x = {x}, y = {y}")
