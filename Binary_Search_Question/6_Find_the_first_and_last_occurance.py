def first_last_occurance(nums, target):
    first = first_occurancee(nums,target)
    last = last_occurancee(nums , target)
    if first == -1 or last == -1 : 
        return [-1,-1]
    else : 
        return [first , last-1]

def first_occurancee(nums , target): # --> lower bound 
    n = len(nums)
    low = 0 
    high = n-1
    lb = -1
    while low <= high :
        mid = (low+high)//2
        if nums[mid] == target:
            lb = mid
        elif nums[mid]> target :
            high = mid-1    
        else :
            low = mid +1
            
    return lb

def last_occurancee(nums , target): # --> upper bound 
    n = len(nums)
    low = 0 
    high = n-1
    up  = -1
    while low <= high :
        mid = (low+high)//2
        if nums[mid] >  target:
            up  = mid
            high = mid-1
        else :
            low = mid +1
    return up
nums = [5,7,7,8,8,10]
target = 6
ans = first_last_occurance(nums, target)
print(ans)