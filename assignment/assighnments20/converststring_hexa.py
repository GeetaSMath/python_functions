# Create a function that takes a string's characters as ASCII
# and returns each character's hexadecimal value as a string.
# Examples
# convert_to_hex("hello world") ➞ "68 65 6c 6c 6f 20 77 6f 72 6c 64"
# convert_to_hex("Big Boi") ➞ "42 69 67 20 42 6f 69"
# convert_to_hex("Marty Poppinson") ➞ "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"

def convert_to_hex(s):
    hexa_value = []
    for x in s:
        hexa_value.append((hex(ord(x)))[2:])
    return ''.join(hexa_value)


print(convert_to_hex("hello world"))
