arr = [1,2,3,4,6,7,8,9]
n = len(arr)
# using sciling 
print("  ::  Method-1  ::  ")
arr[:] = [arr[n-1]] + arr[:n-1]
print(arr)
#using without loop
print("  :: Method-2  :: ")
temp = arr[n-1]
for i in range(n-2,-1,-1):
    arr[i+1] = arr[i]
arr[0] = temp
print(arr)
