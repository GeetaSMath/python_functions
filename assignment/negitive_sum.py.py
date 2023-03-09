# "Create a function that takes a string containing integers as well
# as other characters and return the sum of the negative integers only.
# Examples
# negative_sum(""-12 13%14&-11"") ➞ -23
# # -12 + -11 = -23
# negative_sum(""22 13%14&-11-22 13 12"") ➞ -33
# # -11 + -22 = -33"
import re

def negative_add(n):
    values = re.findall(r'-\d+',n)
    return sum(int,values)
if __name__ == '__main__':
    print(negative_add("-12 13%14&-11"))

