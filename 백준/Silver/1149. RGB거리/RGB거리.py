n = int(input())
min_price = 0
price = []
for i in range(n):
    row = list(map(int,input().split()))
    price.append(row)

dp = [[0]*3 for _ in range(n)]
def min_price(price,n):
    global min_price
    dp[0][0] = price[0][0]
    dp[0][1] = price[0][1]
    dp[0][2] = price[0][2]

    for i in range(1,n):
        dp[i][0] = price[i][0] + min(dp[i-1][1],dp[i-1][2])
        dp[i][1] = price[i][1] + min(dp[i-1][2],dp[i-1][0])
        dp[i][2] = price[i][2] + min(dp[i-1][0],dp[i-1][1])

    min_price = min(dp[n-1][0], dp[n-1][1],dp[n-1][2])
    
    return min_price

print(min_price(price,n))