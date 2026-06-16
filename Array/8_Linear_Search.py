arr = [1,0,4,0,0,6,9,0,8,0]
target = 9
n = len(arr)
for i in range(0,n):
    if arr[i] == target:
        print(i)
    