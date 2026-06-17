arr = [[1,2,3],[4,5,6],[8,9,0]]
n = len(arr)
print("Diagonal elements : ")
print("\n\n")
for i in range(0,n):
    for j in range(0,n):
        if i == j :
            print(arr[i][j],end = " ")
        else :
            print("*",end =" ")
    print()
    
print("upper right traiange :")
print("\n\n")
for i in range(0,n):
    for j in range(0,n):
        if j>=i :
            print(arr[i][j],end = " ")
        else : 
            print("*", end = " ")
    print()

print("upper left triange :")
print("\n\n")
for i in range(0,n):
    for j in range(i,n):
        print(arr[i][j],end = " ")
    print()

print("Lower left triangle : ")
for i in range(0,n):
    for j in range(0,i+1):
        print(arr[i][j],end = " ")
    print()


print("\n\n")
for i in range(0,n):
    for j in range(0,n):
        if j<=i :
            print(arr[i][j],end = " ")
        else : 
            print("*", end = " ")
    print()
    
# print this : 
"""

   * * 3
   * 5 *
   7 * * 
nhi hua 
"""
for i in range(0,n):
    for j in range(n-i-1,-1,-1):
        print(arr[i][j],end = "")
    print("")
        