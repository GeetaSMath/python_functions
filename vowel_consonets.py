def is_vowel_or_consonant(alphabet):
    # Check whether an alphabet is a vowel or a consonant
    vowels = ['a', 'e', 'i', 'o', 'u']

    if alphabet.lower() in vowels:
        return f"{alphabet} is a vowel"
    else:
        return f"{alphabet} is a consonant"
alphabet = 'a'
result = is_vowel_or_consonant(alphabet)
print(result)
