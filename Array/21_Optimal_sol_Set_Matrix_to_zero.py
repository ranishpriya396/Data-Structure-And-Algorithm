matrix = [
[4, 9, 8],
[1, 0, 1],
[8, 4, 1],
[2, 3, 0]
]
def set_zero(matrix):
    r = len(matrix)
    c = len(matrix[0])
    row_trace = [0 for _ in range(0,r)]
    col_trace = [0 for _ in range(0,c)]
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                row_trace[i] = -1
                col_trace[j] = -1
    for i in range(0,r):
        for j in range(0,c):
            if row_trace[i] == -1 or col_trace[j] == -1 :
                matrix[i][j] = 0
                
    return matrix        
res = set_zero(matrix)
print(res)
            
            