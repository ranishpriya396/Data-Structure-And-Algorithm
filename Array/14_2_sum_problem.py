arr = [5,9,1,2,4,15,6,3]
n = len(arr)
target = 8 
# Create dictionary: list items as keys, index as values
f = {}
for i in range(0,n):
    remaining = target - arr[i]
    if remaining in f :
        print([f[remaining], i ])
    f[arr[i]] = i 