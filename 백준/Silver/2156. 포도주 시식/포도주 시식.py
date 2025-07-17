n = int(input())
dp = [0] * (n+1)
amount = [0] * (n+1)

for i in range(1,n+1):
    k = int(input())
    amount[i] = k

if n >= 1:
    dp[1] = amount[1]

if n >= 2:
    dp[2] = amount[1]+amount[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + amount[i], dp[i-3]+amount[i-1]+amount[i])

print(dp[n])
    
    