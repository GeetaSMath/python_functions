def print_powers_of_two(n):
    if n < 0 or n >= 31:
        print("Error: N should be between 0 and 30.")
        return
    power = 1
    while power <= pow(2, n):
        print(power)
        power *= 2
n = int(input("Enter the power value N: "))
print_powers_of_two(n)
