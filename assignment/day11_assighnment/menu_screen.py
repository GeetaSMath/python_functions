# "Create a class that imitates a select screen. For simplicity, the cursor can only move right!
#
# In the display method, return a string representation of the list,
# but with square brackets around the currently selected element. Also,
# create the method to_the_right, which moves the cursor one element to the right.
# The cursor should start at index 0.
# Examples
# menu = Menu([1, 2, 3])
# menu.display() ➞ "[[1], 2, 3]"
# menu.to_the_right()
# menu.display() ➞ "[1, [2], 3]"
#
# menu.to_the_right()
# menu.display() ➞ "[1, 2, [3]]"
# menu.to_the_right()
# menu.display() ➞ "[[1], 2, 3]"

class Menu:
    def __init__(self, option):
        self.option = option
        self.cursor = 0

    def display(self):
        pass

    def to_the_right(self):
        self.cursor = (self.cursor + 1) % len(self.option)

menu = Menu([1, 2, 3])
menu.to_the_right()
print(menu.to_the_right())