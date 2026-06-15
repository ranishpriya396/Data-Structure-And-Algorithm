# arr = [2,45,67,889,456,876,6765]
# largest = float("-inf")
# n = len(arr)
# for i in range(0,n):
#     if arr[i]>largest:
#         largest = arr[i]
# print(largest)

def largest(arr):
    largest = float("-inf")
    n = len(arr)
    for i in range(0,n):
        largest = max(largest, arr[i])
    return largest
arr = [2,45,67,889,456,876,6765]
result = largest(arr)
print(result)