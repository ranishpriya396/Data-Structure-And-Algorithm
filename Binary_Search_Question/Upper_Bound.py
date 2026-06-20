def upper_bound(nums, target):
    n = len(nums)
    high = n-1
    low = 0
    up = -1
    while low<= high:
        mid = (low+high)//2
        if nums[mid] > target:
            up = mid
            high = mid -1 
        else:
            low  = mid+1
    return up
print()
nums = [5,7,7,8,8,10]
target = 7
print(upper_bound(nums,target))
