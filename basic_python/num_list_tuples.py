# 2. Write a Python program which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

def generate_list_and_tuple():
    numbers = input("Enter comma-separated numbers: ")
    # convert input into a list and a tuple
    numbers_list = numbers.split(",")
    numbers_tuple = tuple(numbers_list)
    print("List: ", numbers_list)
    print("Tuple: ", numbers_tuple)


print(generate_list_and_tuple())
