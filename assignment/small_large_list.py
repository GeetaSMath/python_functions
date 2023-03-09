# "In mathematics, interval is the difference between the largest number and the smallest number in a list.ew3
# To illustrate:
# A = (3, 5, 7, 23, 11, 42, 80)
# Interval of A = 80 - 3 = 77
# Examole
# face_interval([1, 2, 5, 8, 3, 9]) ➞ "":)""
# # List interval is equal to one of the other elements.
# face_interval([5, 2, 8, 3, 11]) ➞ "":(""
# # List interval is not among the other elements.
# face_interval(""bruh"") ➞ "":/""
# # ""bruh"" is not a list. It's string."

def face_intrvl(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i -1):
            if lst[j] > lst[j +1]:
                a = lst[j]
    if not isinstance(lst, list):
        if len(lst) >= 1:
            interval = max(lst) - min(lst)
            if interval in lst:
                return ""
            else:
                return interval

print(face_intrvl([1, 2, 5, 8, 3, 9]))
