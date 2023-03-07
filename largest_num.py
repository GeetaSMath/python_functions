def find_largest(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest
largest_num = find_largest(10, 5, 20)
print(largest_num)
