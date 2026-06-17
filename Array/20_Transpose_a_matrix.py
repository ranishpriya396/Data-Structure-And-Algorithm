arr = [[1,2,3],[4,5,6]]
rows = len(arr)
col = len(arr[1])
result = [[0]*rows for i in range(0,col)]
print(result)
for i in range(0,rows):
    for j in range(0,col):
        result[j][i] = arr[i][j]
print(result)