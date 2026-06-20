def lower_bound(nums, target):
    n = len(nums)
    high = n-1
    low = 0
    lb = n
    while low<= high:
        mid = (low+high)//2
        if nums[mid] >= target:
            lb = mid
            high = mid -1 
        else:
            low  = mid+1
    return lb
print()
nums = [5,7,7,8,8,10]
target = 7
print(lower_bound(nums,target))
