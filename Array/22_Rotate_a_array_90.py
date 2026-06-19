matrix = [[1,2,3],[4,5,6],[7,8,9]]
r = len(matrix)
c =len(matrix)
result = [[0]*r for i in range(0,c)]

for i in range(0,r):
    for j in range(0,c):
        result[j][i] = matrix[i][j]
for i in range(0,r):
    result[i].reverse()
matrix = result 
print(matrix)
