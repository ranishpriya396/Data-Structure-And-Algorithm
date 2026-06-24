def binary_to_decimal(nums):
    res = 0
    n = nums
    for index , value in enumerate(n[::-1]):
        if value == '1':   
            res = res+2**index

    return res
n = '1001'
r = binary_to_decimal(n)
print(r)