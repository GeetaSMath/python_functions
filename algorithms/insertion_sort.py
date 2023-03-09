def inseration_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


arr = [8, 9, 1, 3, 4, 5, 6]
inseration_sort(arr)
print(arr)
