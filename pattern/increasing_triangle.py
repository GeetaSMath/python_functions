def inc_triangle(size):
    for i in range(size):
        for j in range(i + 1):
            print('*', end=' ')
        print()

size = int(input("Enter the user value: "))
inc_triangle(size)

def dec_triangle(size):
    for i in range(size):
        for j in range(i,size):
            print('*', end='')
        print()

size = int(input("Enter the user value: "))
dec_triangle(size)
