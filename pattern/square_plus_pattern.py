def square_plus_pattern(num):
    for i in range(num):
        for j in range(num):
            if i == num // 2 or j == num // 2:
                print('*', end='')
            else:
                print('', end=' ')
        print()


print(square_plus_pattern(5))
