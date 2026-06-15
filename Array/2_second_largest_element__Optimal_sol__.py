def sec_largest(arr):
    n = len(arr)
    largest = float("-inf")
    sec_largest = float("-inf")
    for i in range(0,n):
        if arr[i] > largest:
            sec_largest = largest 
            largest = arr[i]
        elif arr[i] > sec_largest and arr[i]!=largest :
            sec_largest = arr[i]

    return sec_largest            


            
arr = [2,45,67,889,456,876,6765]
result = sec_largest(arr)
print(result)