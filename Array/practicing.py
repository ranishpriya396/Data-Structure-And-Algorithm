# merger two problem array without adding duplicates  and these array are sorted array :

nums1 = [1,1,1,2,3,3,6,7,7,8,9,10]
nums2 = [1,2,3,4,5,6,7,8,9,10,11,12]
result = []
m = len(nums1)
n = len(nums2)
i = 0 
j = 0 
while i < m and j <n :
    
    if nums1[i] <= nums2[j] :
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i +=1
    else : 
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
            j +=1
while i < n :
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
        i+=1
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
        j = j+1
print(result)