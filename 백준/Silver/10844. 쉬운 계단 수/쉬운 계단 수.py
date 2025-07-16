n = int(input())

dp = [[0]*10 for _ in range(101)]
sum_value = 0

if n >= 1:
    for i in range(0,10):
        if(i == 0):
            dp[1][i] = 0
        else:
            dp[1][i] = 1

if n >= 2:
    for i in range(0,10):
        if i in (0,1,9):
            dp[2][i] = 1
        else:
            dp[2][i] = 2


for i in range(3,n+1):
    for j in range(0,10):
        if (j == 0):
            dp[i][j] = dp[i-1][j+1]
        elif (j == 9):
            dp[i][j] = dp[i-1][j-1]   
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
for i in range(0,10):
    sum_value += dp[n][i]

print(sum_value%1000000000)

    