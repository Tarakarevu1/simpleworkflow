def search_ele(arr,k):
    n=len(arr)
    for i in range(n):
        if(arr[i]==k):
            return i
    return -1
    
