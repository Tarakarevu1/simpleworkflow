def bubble_sort(arr):
    arr_copy = arr[:]
    n = len(arr_copy)
    for i in range(n):
        for j in range(i+1,n):
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap the elements
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy
