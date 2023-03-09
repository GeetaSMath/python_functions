def hallow_decreasing_pattern(num):
    for i in range(num):
        for j in range(i, num):
            if i==0 or j==i or j==num-1:
                print('*', end='')
            else:
                print('', end=' ')
        print()
print(hallow_decreasing_pattern(5))