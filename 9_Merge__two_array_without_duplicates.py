arr1= [1,1,1,2,2,3,4,5]
arr2 =  [1,2,3,4,4,5,5,6,7,8,9,10,10]
def merge_two_array(arr1,arr2,):
    n = len(arr1)
    m = len(arr2)
    result = []
    i = 0 
    j = 0 
    while i<n and j <m :
        if arr1[i] <= arr2[j] :
            if len(result) == 0 or result[-1] != arr1[i] :
                result.append(arr1[i])
                i=+1
            elif len(result) == 0 or result[-1] != arr2[j] :
                result.append(arr2[j])
                j +=1
    while i<n:
        if len(result)==0 or result[-1] != arr1[i]:
            result.append(arr1[i])
    while j<m : 
        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(i)
    return result 
r = merge_two_array(arr1, arr2)
print(r)