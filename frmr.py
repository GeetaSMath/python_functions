# Q1. A farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
#
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.


CHICKENS_LEGS = 2
COWS_LEGS = 4
PIGS_LEGS = 4

def total_legs(chiken, cows, pigs):
    chi_leg=chiken * CHICKENS_LEGS
    cows_leg = cows*COWS_LEGS
    pigs_leg = pigs*PIGS_LEGS
    total = chi_leg+cows_leg+pigs_leg
    return total


a=total_legs(chiken=16, cows = 4, pigs = 6)
print(a)
