# for loop
for letter in 'Flexiple':
    if letter == 'x':
        pass
    print('Letters: ', letter)

#example
employee_list = [('geeta', 1), ('Anu', 2)]
for i in employee_list:
    print(i)

# example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# while loop
num = [5, 6, 7, 8]
squ = []
val=0
for nums in num:
    val = nums ** 2
    squ.append(val)
    print("square value for given number", val)

# example
i = 0
while i < 6:
  i += 1
  if i == 3:
    # break
    continue
  print(i)
