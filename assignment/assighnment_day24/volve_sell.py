# The volume of a spherical shell is the difference between the
# enclosed volume of the outer sphere and the enclosed volume of the inner sphere:
# V=(4/3) * pi(R^3 - r^3)
# Create a function that takes r1 and r2 as arguments and returns
# the volume of a spherical shell rounded to the nearest thousandth.
# Examples
# vol_shell(3, 3) ➞ 0
# vol_shell(7, 2) ➞ 1403.245
# vol_shell(3, 800) ➞ 2144660471.753

def vol_shell(r1, r2):
    pi = 3.1415926535
    volume = (4 / 3) * pi * ((r2 ** 3) - (r1 ** 3))
    return round(volume, 3)


print(vol_shell(3, 3))
print(vol_shell(7, 2))
print(vol_shell(3, 800))


def dict_val(dict_val):
    print(dict_val)
    return list(dict_val.values())


age = {
    "a": 10,
    "b": 20,
    "c": 30
}
print(dict_val(age))

from math import pi

r = float(input("Input the radius of the circle : "))
print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))
num = int(input("Enter an integer: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    print(rev,"rev num")
    num = num // 10
    print(num, "num is")

print("The reversed integer is:", rev)
