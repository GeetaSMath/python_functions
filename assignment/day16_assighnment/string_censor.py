# Someone has attempted to censor my strings by replacing every vowel
# with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
# Given a censored string and a string of the censored vowels, return the original uncensored string.
# Example
# uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
# uncensor("abcd", "") ➞ "abcd"
# uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

def uncensor(censored_str, vowels):

    for vowel in vowels:
        censored_str = censored_str.replace('*', vowel, 1)

    return censored_str

censored_str1="Wh*r* d*d my v*w*ls g*?"
vowels1="eeioeo"
print(uncensor(censored_str1,vowels1))
