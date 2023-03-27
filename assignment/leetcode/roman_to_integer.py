# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def romanToInt(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in s:
        curr_value = values[c]
        if curr_value > prev_value:
            result += curr_value - 2 * prev_value
        else:
            result += curr_value
        prev_value = curr_value
    return result
print(romanToInt("III")) # Output: 3
print(romanToInt("LVIII")) # Output: 58




















