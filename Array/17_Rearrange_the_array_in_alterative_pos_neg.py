nums = [5,10,-3,-1,-10,6]
pos = []
neg = []
for i in range(0,len(nums)):
    if nums[i]<0:
        neg.append(nums[i])
    else :
        pos.append(nums[i])
for i in range(0,len(pos)):
    nums[2*i] = pos[i]
    nums[(2*i)+1] = neg[i]
print(nums)

# Optimal solution :
n = len(nums)
pos = 0 
neg = 1
result = [0]*n
for i in range(0,n):
    if nums[i]>0 :
        result[pos] = nums[i]
        pos = pos+2
    else :
        result[neg] = nums[i]
        neg = neg+2
print(result)