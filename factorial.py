def prime_factors(n):
    factors = []

    # Check divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check divisibility by odd numbers
    i = 3
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    # If n is still greater than 2, it must be a prime factor
    if n > 2:
        factors.append(n)

    # Print the result
    print(f"The prime factors of {n} are: {factors}")
prime_factors(24)

