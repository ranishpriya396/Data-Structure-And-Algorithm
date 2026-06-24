def swapping(a , b ):
    a = (a^b)
    b = (a^b)
    a = (a^b)
    return a,b 

a = 3
b = 4
print("Before swapping : a = ",a ,"b = ",b)
print("after swapping : a , b")
res = swapping(a,b)
print(res)