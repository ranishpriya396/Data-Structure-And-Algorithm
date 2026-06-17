def longestConsecutive( nums) :
    n = len(nums)
    max_count = 0 
    for i in range(0,n):
        num = nums[i]
        count  = 1 
        while num+1 in nums:
            count +=1
            num +=1
        max_count = max(max_count ,count )
    return max_count 
nums =[1,99,101,98,2,5,3,100]
result = longestConsecutive(nums)
print(result)

# optimal solution ::
my_set = set(nums)
print(my_set)
max_count = 0
n = len(my_set)
for num in range(0,n):
    if num-1 not in my_set :
        count = 1
        x = num
        while x+1 in nums:
            count +=1
            x = x+1
    max_count = max(max_count , count )          
print(max_count)
            