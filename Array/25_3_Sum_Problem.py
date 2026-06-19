nums = [-1,0,1,2,-1,-4]
temp = []
n = len(nums)
nums.sort()
for i in range(0,len(nums)):
    if i !=0 and nums[i] == nums[i-1]:
        continue
    
    j = i+1
    k = n-1
    while j < k :
        total_sum = nums[i]+nums[j]+nums[k] 
        if total_sum <0 :
            j= j+1
        elif total_sum > 0:
            k = k-1
        else :
            temp.append([nums[i], nums[j],nums[k]])
            j = j+1
            k = k-1
            while j < k and nums[j] == nums[j-1]:
                j +=1
            while k < n and  nums[k] == nums[k+1]:
                k -=1
                
                
                
                
print(temp)


