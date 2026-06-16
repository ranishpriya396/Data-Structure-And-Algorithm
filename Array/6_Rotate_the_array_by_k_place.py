# # best solution : 
# print("::: best solution :::")
# arr = [1,2,3,4,5,6,7]
# n = len(arr)
# r = 35# rotation
# k =  r%n 
# arr[:] = arr[n-k : ]+arr[: n-k]
# print(arr)

print("::: optimal solution :::")
arr = [1,2,3,4,5,6,7]
n = len(arr)
k =5 
def reverse(arr , l ,r):
    while l< r :
        arr[l],arr[r] = arr[r],arr[l]
        l+=1
        r-=1
reverse(arr , n-k, n-1)
print(arr)##reverse the last k element
reverse(arr,0,n-k-1)
print(arr) # reverse the remaining element 
reverse(arr, 0 , n-1) 
print(arr) # reverse the whole array 