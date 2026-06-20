def search_index(nums,target):
    n = len(nums)
    lb = n 
    s = 0 
    e = n-1
    while s <= e:
        mid = (s+e)//2
        if nums[mid] >= target:
            lb = mid
            e = mid-1
        else :
            e = mid+1
    return lb 