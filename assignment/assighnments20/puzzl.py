# Write a Python program to find a list of integers with exactly two occurrences of nineteen
# at least three occurrences of five. Return True otherwise False

# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False

def has_two_19s_and_three_5s(lst):
    count_19 = 0
    count_5 = 0
    for num in lst:
        if num == 19:
            count_19 += 1
        elif num == 5:
            count_5 += 1
    return count_19 == 2 and count_5 >= 3

lst1 = [19, 19, 15, 5, 3, 5, 5, 2]
lst2 = [19, 15, 15, 5, 3, 3, 5, 2]

print(has_two_19s_and_three_5s(lst1))
print(has_two_19s_and_three_5s(lst2))



