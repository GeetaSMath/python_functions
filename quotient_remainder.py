def quotient_remainder(a, b):
    # Compute the quotient and remainder
    # // division operator
    # %  quotient
    q = a // b
    r = a % b

    # Print the result
    print(f"The quotient of {a} divided by {b} is {q}")
    print(f"The remainder of {a} divided by {b} is {r}")
quotient_remainder(17, 5)