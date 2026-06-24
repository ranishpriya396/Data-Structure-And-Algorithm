def decimal_to_binary(nums):
    n = nums
    res = ""
    while n > 0:
        if n % 2 == 1:       # Fixed variable name logic
            res = res + '1'
        else:
            res = res + '0'
        n = n // 2          # Added assignment operator to prevent infinite loop
    return res[::-1]

nums = 9
r = decimal_to_binary(nums)
print(r)
