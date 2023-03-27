# "Create a function that takes a list lst and a number n and returns
# a list of two integers whose product is that of the number n.
#
# Examples
# two_product([1, 2, 3, 4, 13, 5], 39) ➞ [3, 13]
#
# two_product([11, 2, 7, 3, 5, 0], 55) ➞ [5, 11]
#
# two_product([100, 12, 4, 1, 2], 15) ➞ None"

def product(lst, n):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] == n:
                return [lst[i], lst[j]]
    return

print(product([1, 2, 3, 4, 13, 5], 39))
print(product([11, 2, 7, 3, 5, 0], 55))