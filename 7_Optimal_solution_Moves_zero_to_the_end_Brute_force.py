arr = [1,0,2,4,3,0,0,3,5,1]
if len(arr) == 1: 
    print(arr)
n= len(arr) 
i = 0 
while i <n : 
    if arr[i] == 0 :
        break 
    i+=1
if i == len(arr) : 
    print(arr)
j = i +1
while j <n :
    if arr[j] != 0 :
        arr[j] ,arr[i] = arr[i], arr[j]
        i +=1
    j =j+1
print(arr)
