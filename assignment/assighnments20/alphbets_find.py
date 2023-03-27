# Given a name, return the letter with the highest index in alphabetical order,
# with its corresponding index, in the form of a string. You are prohibited to use max() nor
# is reassigning a value to the alphabet list allowed.
#
# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
# "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# alphabet_index(alphabet, "Flavio") ➞ "22v"
# alphabet_index(alphabet, "Andrey") ➞ "25y"
# alphabet_index(alphabet, "Oscar") ➞ "19s

def alphabet_index(alphabet, val):
    high_index = 0
    for char in val.lower():
        index = alphabet.index(char)
        if index > high_index:
            high_index = index
    return str(high_index) + alphabet[high_index]


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabet_index(alphabet, "Flavio"))
