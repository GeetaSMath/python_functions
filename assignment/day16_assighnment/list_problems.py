# Create a function that takes a list of lists and return the length of the missing list.
#
# Examples
# find_missing([[1], [1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]) ➞ 3

# find_missing([[5, 6, 7, 8, 9], [1, 2], [4, 5, 1, 1], [1]]) ➞ 3
# find_missing([[4, 4, 4, 4], [1], [3, 3, 3]]) ➞ 2

def find_lst(lst):
    x = len(lst) +1
    for i in range(1, x+1):
        if i not in [len(sublst) for sublst in lst]:
            return i

lst1 = [[1, 2], [4, 5, 1, 1], [5, 6, 7, 8, 9]]
print(find_lst(lst1))



