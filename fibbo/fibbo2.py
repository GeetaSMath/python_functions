
def fibo(n):
    a = 0
    b = 1

    # Checking n is less than 0
    if n < 0:
        print("Incorrect input")

    # Checking n is equal to 0
    elif n == 0:
        return 0

    # Checking if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
print(fibo(8))