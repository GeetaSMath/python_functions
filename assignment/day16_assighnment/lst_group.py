# Create a function that groups a list of numbers based on a size parameter.
# The size represents the maximum length of each sub-list.
# [1, 2, 3, 4, 5, 6], 3
# [[1, 3, 5], [2, 4, 6]]
# # Divide list into groups of size 3.
# [1, 2, 3, 4, 5, 6], 2
# [[1, 4], [2, 5], [3, 6]]
# # Divide list into groups of size 2.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
# # "Leftover" lists are okay.
# Examples
# group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]
# group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]
# group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]
# group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]

def groups(lst, size):
    return [lst[i::size] for i in range(size)]

lst1 = [1, 2, 3, 4, 5, 6]
size1 = 5
print(groups(lst1,size1))