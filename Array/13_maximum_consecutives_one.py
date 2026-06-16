arr = [1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,]
count = 0 
max_count = 0 
n = len(arr)
for i in range(0,n):
    if arr[i] == 1 :
        count +=1
        max_count = max(count , max_count)
    else :
        # max_count = max(count , max_count)
        count = 0 
        
print(max_count)