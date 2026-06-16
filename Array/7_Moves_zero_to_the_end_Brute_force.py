arr = [1,0,4,0,0,6,9,0,8,0]
n = len(arr)
temp = []
for i in range(0,n):
    if arr[i] !=0 :
        temp.append(arr[i])
nt = len(temp)
for i in range(0,nt):
    arr[i] = temp[i]
for j in range(nt , n ):
    arr[j]= 0 

print(arr)