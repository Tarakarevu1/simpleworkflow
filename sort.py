def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
            
    return arr
