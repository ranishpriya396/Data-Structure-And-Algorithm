def check_sorted(arr):
    n = len(arr)
    for i in range(0, n ):
        if arr[i]>arr[i+1]:
            return "not sorted"
            break 
    else : 
        return "sorted"
arr = [2,45,67,889,456,876,6765]
print(check_sorted(arr))