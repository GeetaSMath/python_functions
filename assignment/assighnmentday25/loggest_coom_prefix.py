# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def logset_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        for val in strs[1:]:
            if i >= len(val) or val[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]


strs = ["dog", "racecar", "car"]
print(logset_common_prefix(str))

# class Solution:
#     def longestCommonPrefix(self, m):
#         if not m: return ''
#         s1 = min(m)
#         s2 = max(m)
#
#         for i, c in enumerate(s1):
#             if c != s2[i]:
#                 return s1[:i]
#         return s1
# x=Solution()
# print(x.longestCommonPrefix()
