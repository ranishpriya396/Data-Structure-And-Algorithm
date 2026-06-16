nums = [-2,1,-3,4,-1,2,1,-5,4]
maxi = float("-inf")
n =len(nums)
total = 0 
for i in range(0, n):
    total = total + nums[i]
    maxi = max(total , maxi)
    if total < 0 :
        total = 0 
print(maxi)