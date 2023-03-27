# 4 -> "Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise,
# two lines rhyme if the last word from each sentence contains the same vowels.
#
# Examples
# does_rhyme(""Sam I am!"", ""Green eggs and ham."") ➞ True
#
# does_rhyme(""Sam I am!"", ""Green eggs and HAM."") ➞ True
# # Capitalization and punctuation should not matter.
#
# does_rhyme(""You are off to the races"", ""a splendid day."") ➞ False
#
# does_rhyme(""and frequently do?"", ""you gotta move."") ➞ F

def does_rhyme(s1, s2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s1_words = s1.lower().split()
    s2_words = s2.lower().split()
    s1_last_word_vowels = [char for char in s1_words[-1] if char in vowels]
    s2_last_word_vowels = [char for char in s2_words[-1] if char in vowels]
    return s1_last_word_vowels == s2_last_word_vowels

print(does_rhyme("Sam I am!", "Green eggs and ham."))
print(does_rhyme("Sam I am!", "Green eggs and HAM."))






