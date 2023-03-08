def square(size):
    for i in range(size):
        for j in range(size):
            print("$", end=" ")
        print()
size = int(input("Enter the user value: "))
square(size)
