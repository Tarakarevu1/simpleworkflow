def bubble_sort(arr):
    arr_copy = arr[:]
    n = len(arr_copy)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    print("Bubble_sort")
    return arr_copy
