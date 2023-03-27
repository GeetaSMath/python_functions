# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# , determine if the input string is valid
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example
# 1:
#
# Input: s = "()"
# Output: true
# Example
# 2:
#
# Input: s = "()[]{}"
# Output: true
#
# def isvalid(s: str) -> bool:
#     while any(x in s for x in ["()", "[]", "{}"]):
#         s = s.replace("()", "").replace("[]", "").replace("{}", "")
#     return s == ""
#
# val2="()[]{"
# val = "()[]{}"
# print(isvalid(val))
# print(isvalid(val2))

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i == "(" or i == "[" or i == "{"):
                stack.append(i)
            else:
                if not stack:
                    return False
                ele = stack.pop()
                if i == ")":
                    if (ele != "("):
                        return False
                elif (i == "]"):
                    if (ele != "["):
                        return False
                else:
                    if (ele != "{"):
                        return False
        if stack:
            return False
        return True


x = Solution()
print(x.isValid("()[]{}"))
