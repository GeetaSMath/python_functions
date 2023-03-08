# Create a function that finds the highest integer in the list using recursion.



def find_highest_int(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max = find_highest_int(numbers[1:])
        if numbers[0] > max:
            return numbers[0]
        else:
            return max

number=[6, 5, 7, 11, 3, 5, 10]
a=find_highest_int(number)
print(a)