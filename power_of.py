def print_powers_of_two(n):
    """
    This function takes a positive integer n and prints a table of the powers of 2
    that are less than or equal to 2^n.
    """
    if n < 0 or n >= 31:
        print("Error: N should be between 0 and 30.")
        return
    power = 1
    while power <= pow(2, n):
        print(power)
        power *= 2

# Take input from the user
n = int(input("Enter the power value N: "))

# Call the print_powers_of_two function
print_powers_of_two(n)
