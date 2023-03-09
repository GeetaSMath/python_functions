def hallow_increasing_triangle(num):
    for i in range(num):
        for j in range(i+1):
            if i==num-1 or j==0 or j==i:
                print('*', end='')
            else:
                print('', end=' ')
        print()

print(hallow_increasing_triangle(5))