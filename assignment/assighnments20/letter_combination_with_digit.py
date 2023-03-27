# Given a string containing digits from 2-9 inclusive, return all possible letter combinations
# that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]Example 2:
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"] in python
def letter_combinations(digits):
    if not digits:
        return []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    n = len(digits)
    result = [""]
    for i in range(n):
        letters = mapping[digits[i]]
        m = len(result)
        for j in range(m):
            prefix = result[j]
            for letter in letters:
                result.append(prefix + letter)
        result = result[m:]
    return result


digits = "23"
combinations = letter_combinations(digits)
print(combinations)
