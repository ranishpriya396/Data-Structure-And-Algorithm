def singleNumber( nums) -> int:
    f  = {}
    n = len(nums)
    for i in range(0,n):
        if nums[i] in f :
            f[nums[i]] +=1
        else :
            f[nums[i]] = 1 
            
    for key , value in f.items() :
        if value == 1  :
            return key
    
nums= [4,1,2,1,2]
r = singleNumber(nums)
print(r)