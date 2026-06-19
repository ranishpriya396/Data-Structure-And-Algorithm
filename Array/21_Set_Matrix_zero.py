matrix = [
[4, 9, 8],
[1, 0, 1],
[8, 4, 1],
[2, 3, 0]
]
def make_infinity(matrix, row, col):
    r = len(matrix)
    c =len(matrix[0])
    for i in range(0, r):  # --> column constant 
        if matrix[i][col] != 0 :
            matrix[i][col] = float("inf")
    for j in range(0,c) :
        if matrix[row][j] != 0 :
            matrix[row][j] = float("inf")
def set_zero(matrix):
    r = len(matrix)
    c =len(matrix[0])
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == 0:
                make_infinity(matrix, i , j )
    for i in range(0,r):
        for j in range(0,c):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0 
    return matrix        
r = set_zero(matrix)
print(r)           
            