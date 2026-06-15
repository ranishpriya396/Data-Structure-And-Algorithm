arr = [1,1,2,2,3,3,3,4,10,9,2,4,5,5,6,6,1,1,2,2,3,3,7,7,8,8,9,10,1]
n =len(arr)
f ={}
for i in range(0,n):
    f[arr[i]] = 0 
j = 0 
for k in f :
    arr[j] = k 
    j+=1
arr = arr[:j]
print(arr)