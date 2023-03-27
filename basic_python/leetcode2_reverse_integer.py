# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x
# causes the value to go outside the
#
# signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
def reverse(x):
    if x == 0:
        return 0
    sign = x // abs(x)
    x = abs(x)
    digits = []
    while x > 0:
        digit = x % 10
        digits.append(digit)
        x //= 10
    reversed_x = 0
    for i, digit in enumerate(digits):
        reversed_x += digit * 10 ** (len(digits) - i - 1)
    reversed_x *= sign
    if reversed_x < -2 ** 31 or reversed_x > 2 ** 31 - 1:
        return 0
    return reversed_x


print(reverse(123))
print(reverse(-321))
