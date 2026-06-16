"""
prices = [7,2,1,5,6,4,8]
max_profit = 0 
n = len(prices)
for i in range(0,n):
    for j in range(i,n):
        if prices[j] > prices[i]:
            p = prices[j] - prices[i]
            max_profit = max(max_profit, p )
print(max_profit )
"""
# optimal soluton :
p = [7,2,1,5,6,4,8]
n = len(p)
min_price = float('inf')
max_profit = 0
for i in range(0,n):
    min_price = min(p[i],min_price)
    max_profit = max(p[i]-min_price, max_profit)
print(max_profit) 


