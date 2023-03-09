def parlell_bar_pattern(num):
    for i in range(num):
        for j in range(num):
            if (j == 0 or j == num - 1):
                print("*", end='')
            else:
                print('', end=' ')
        print()


print(parlell_bar_pattern(5))
