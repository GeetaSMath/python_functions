# Given a string s, return the longest  palindromic substring
#  in s.
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer. in python

def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s
    longest = ""
    for i in range(n):
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if len(longest) < r - l - 1:
            longest = s[l + 1:r]
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        if len(longest) < r - l - 1:
            longest = s[l + 1:r]
    return longest


s = "babad"
longest = longest_palindrome(s)
print(longest)
