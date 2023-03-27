#
# Example
# 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example
# 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3.
# Example
# 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M               1000

# def roman_to_int(s: str)-> int:
#     sym_val={
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000
#     }
#     result= 0
#     for i in range(len(s)):
#         if i< len(s) -1 and sym_val[s[i]]<sym_val[s[i+1]]:
#             result -=sym_val[s[i]]
#         else:
#             result += sym_val[s[i]]
#     return result
# print(roman_to_int('IIIX'))

import functools as fn
import operator as op

class Solution:
    lookup_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    ops = {
        False: op.add,
        True: op.sub
    }
    def romanToInt(self, s: str) -> int:
        _, result = fn.reduce(
            lambda state, c:
                (lambda num, prev_num, result:
                    (num, self.ops[prev_num > num](result, num))
                )(self.lookup_table[c], *state),
            s[::-1],
            (0, 0)
        )
        return result

x=Solution()
print(x.romanToInt('XVI'))