n = 13 
k = 2  #(kis place pe check karni hai bit)

def check_bit_set(nums, k ):
    if n&(1<<k) !=0:
        return True
    return False
nums = 13
k = 2
r = check_bit_set(nums,k)
print(r)


# using right shift:
def check_bit_set_using_right_shift(nums,k):
    if (n>>k)&1==1:
        return True
    return False
nums = 13
k = 2
r = check_bit_set_using_right_shift(nums,k)
print(r)