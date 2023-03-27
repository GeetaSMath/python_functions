# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100


def pow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        return 1.0 / pow(x, -n)
    elif n % 2 == 0:
        return pow(x * x, n // 2)
    else:
        return x * pow(x, n - 1)


print(pow(x=2.00000, n=10))
