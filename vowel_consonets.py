# Check whether an alphabet is a vowel or a consonant

def is_vowel_or_consonant(alphabet):
    try:
        vowels = "aeiou"
        return f"{alphabet} is a vowel" if alphabet.lower() in vowels else f"{alphabet} is a consonant"
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    alphabet = input("Enter the user alphabets")
    result = is_vowel_or_consonant(alphabet)
    print(result)
