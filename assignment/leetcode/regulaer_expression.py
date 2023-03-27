# Given an input string s and a pattern p,
# implement regular expression matching with support for '.' and '*' where:
# Matches any  single     characte
# '*' Matches zero or more of the preceding element.
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
import re


def isMatch(s: str, p: str) -> bool:
    pattern = re.compile(p)
    return bool(pattern.fullmatch(s))


print(isMatch(s="aa", p="a"))
