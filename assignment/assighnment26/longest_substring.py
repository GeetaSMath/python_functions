# Given a string s, find the length of the longest
# substring
#  without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def substring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        r = 1
        cnt = 1
        tmp = s[0]
        while r < len(s):
            if s[r] not in tmp:
                tmp += s[r]
                cnt = max(len(tmp), cnt)
                r += 1
            else:
                tmp = tmp[1:]
        return cnt


x = Solution()
res = x.substring("abcabcbb")
print(res)
